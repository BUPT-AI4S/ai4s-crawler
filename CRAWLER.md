# Academic 论文爬虫

按**会议/期刊 + 年份**采集论文。使用 `--metadata-only` 只生成 JSON，不下载 PDF；新增 CCF 会议与 Nature 期刊仅支持元数据模式。

在 `academic/` 目录下运行。

当前生产范围来自教师表的“建议结论=建议纳入”：541个来源（105个会议、436个期刊）。启用代码见 `approved_sources.py`；未纳入项保留为注释，运行入口也会过滤它们。完整名称、ISSN、建议理由与入口依据在 `teacher_sources.json`。教师确认栏仍为待确认，本次按用户指定的建议列执行。

2026-11-04服务器任务只补爬2024年：`-v teacher-approved -y 2024 --metadata-only --workers 64 --skip-completed`。已完成且仍在启用范围内的来源复用结果；旧来源数据保留，年度汇总仅包含本次选择。详情池为32路，各上游仍分别限速。新增期刊用已核实ISSN从Crossref枚举，OpenAlex及出版方公开页面补摘要，未承诺出版社目录和摘要全量覆盖。

## 安装

服务器续跑可使用 `--metadata-only --workers 16 --skip-completed`：按上一轮状态跳过已完成且结果文件齐全的来源，优先重试失败项，并交错安排会议与期刊。论文详情共用最多 16 路请求池，断点仍由各来源线程顺序写入，不会并行改写同一个结果文件。需要回补某个已完成来源时，对它单独运行且不带 `--skip-completed`。

请求复用线程独立的 HTTP 连接；不同上游分别限速。Crossref 公开池保持单请求并发，OpenAlex 最多两个请求并行；收到 429/503 时遵守 `Retry-After`，不会因为增加来源并发而同比提高同一接口的请求压力。

```bash
pip install requests beautifulsoup4 lxml loguru python-dotenv openreview-py
```

## 用法

```bash
cd academic

# ICLR / NeurIPS 等走 OpenReview
python academic.py -v iclr -y 2025 --metadata-only

# CVPR / ICCV / ECCV / WACV 走 TheCVF Open Access（不走 OpenReview）
python academic.py -v cvpr -y 2025 --metadata-only

# 先试 5 篇
python academic.py -v cvpr -y 2025 --metadata-only --limit 5 --metadata-dir metadata_trial

# 同一年多个会
python academic.py -v iclr,cvpr -y 2025 --metadata-only

# 只导出元数据，不下载 PDF。全量在 papers.json，AI4S 子集在 ai4s.json
python academic.py -v iclr,icml,neurips,cvpr,eccv,acl,naacl,emnlp,aaai,kdd -y 2026 --metadata-only

# 每个会先试 2 篇
python academic.py -v cvpr,eccv,aaai,kdd -y 2026 --metadata-only --limit 2

# 同时处理 4 个来源，优先安排已支持的 OpenReview 来源
python academic.py -v ccf-ab,wacv,nature-all -y 2024 --metadata-only --workers 4
```

输出：

- 下载 PDF 时：`pdfs/<venue>/<year>/*.pdf` 和 `pdfs/<venue>/<year>/papers.json`
- `--metadata-only` 时：`metadata/<venue>/<year>/papers.json`、`metadata/<venue>/<year>/ai4s.json`
- 同一年汇总：`metadata/<year>/papers.json`、`metadata/<year>/ai4s.json`

已存在的合法 PDF 会跳过。元数据模式按论文 id 断点续写，中断后可重跑。

`--workers` 默认 1，仅用于元数据模式。不同来源各写自己的断点，全部结束后统一汇总；并发状态保存在 `metadata/<year>/run-status.json`。Crossref、OpenAlex、DBLP SPARQL 的请求在进程内共享各自的速率门控，429/503 时遵守 `Retry-After`。OpenReview SDK 的共享客户端按串行方式访问，其公开页面回退不占用客户端锁。

AI4S 关键词在 `ai4s_keywords.txt`。KDD 官方 AI for Sciences 分轨即使没命中关键词也会进入 `ai4s.json`。

## CCF A/B 会议

`ccf_conferences.json` 收录 2026 年第七版目录的全部 190 个 A/B 会议：A 类 58 个、B 类 132 个，覆盖 10 个领域。另保留原有 WACV，因此内置会议总数为 191 个。完整名称、领域、命令标识和覆盖注意事项见 [CCF_CONFERENCES.md](CCF_CONFERENCES.md)。目录版本和来源 URL 保存在配置中。

```bash
# 全部 A/B 会议，最终 AI4S 候选汇总到 metadata/2025/ai4s.json
python academic.py -v ccf-ab -y 2025 --metadata-only

# 只选择 A 类或 B 类
python academic.py -v ccf-a -y 2025 --metadata-only
python academic.py -v ccf-b -y 2025 --metadata-only

# 指定新增会议，少量试抓到独立目录
python academic.py -v ijcai,miccai,colt,uai,www,sc -y 2025 --metadata-only --limit 2 --metadata-dir metadata_trial_ccf

# 同时选择所有 A/B 会议和 Nature 期刊
python academic.py -v ccf-ab,nature-all -y 2025 --metadata-only
```

原有 12 个会议的专用采集路径继续保留。新增会议使用 [DBLP 官方 SPARQL API](https://blog.dblp.org/2024/09/09/introducing-our-public-sparql-query-service/)，先按会议 stream 和**出版年份**分页读取论文标识，再限定标识获取作者、DOI、页码及目录信息，避免大型作者关联聚合查询超时。随后用 Crossref 按 DOI 补摘要；仍缺摘要时尝试读取支持的出版社公开 HTML。直接 PDF 链接不请求，重定向后的 PDF 不读取正文，不下载期刊或会议 PDF，也不调用大模型。服务不可用会报错并保留断点，不能将失败解释成没有论文。

常用别名：`sigkdd` → `kdd`，`nips` → `neurips`，`ACM MM` / `acm-mm` → `mm`，`IEEE VIS` / `ieee-vis` → `vis`。重名 FSE 分开为软件工程 A 类 `fse`、密码学 B 类 `fse-crypto`。别名与分组重叠时只采一次。

记录新增 `conference_title`、`ccf_rank`、`ccf_field`、`ccf_catalog_version`、`ccf_paper_status`、`dblp_key`、`dblp_toc`、`booktitle`。等级说明来源在 2026 版目录中的分类，不回溯历史评级，也不认证单篇论文。一般记录的 `ccf_paper_status` 是 `unverified`；已识别的 short、Findings、Workshop、扩展摘要等标为 `excluded`，保留在 `papers.json`，不进入 `ai4s.json`。不能仅凭页数确认 Full/Regular paper。已有人工标签仍保留。

SIGGRAPH、VLDB、SIGMOD、CSCW、UbiComp、ISMB 等存在期刊承载主会论文的情况，会议 stream 可能不完整；配置和清单已标出，后续需对照官方各年目录核验。注册了全部 190 个会议不等于已完成逐会验证或全量采集。摘要缺失会标为 `needs_abstract`，影响关键词筛选召回率；规则筛选结果仍是候选集合。

## Nature 期刊

`nature_journals.json` 保存从 [Nature 官方目录](https://www.nature.com/siteindex) 提取的 2026-11-02 快照，共 179 本：Nature 1 本、Nature 学科研究刊 41 本、Nature Communications 1 本、Communications 11 本、npj 90 本、Reviews 27 本、Scientific 3 本、Progress 4 本及 Nature Protocols 1 本。地区新闻站和 Scientific American 不在此列表。目录中的新刊可能尚未发表或尚无 Crossref 记录，配置收录不等于已验证所有期刊可抓取。

每本刊使用官网路径作为 `-v` 标识，也支持完整英文刊名的连字符形式，例如 `nature-computational-science`。

| 标识/别名 | 期刊/期刊组 |
|---|---|
| `nature` | Nature 正刊 |
| `ncs` / `natcomputsci` | Nature Computational Science |
| `nmi` / `natmachintell` | Nature Machine Intelligence |
| `nc` / `natcomm` / `ncomms` | Nature Communications |
| `nmeth` | Nature Methods |
| `sdata` / `srep` / `scirev` | Scientific Data / Reports / Reviews |
| `npjcompumats` / `npjdigitalmed` | npj Computational Materials / Digital Medicine |
| `nature-core` | Nature、NC、NCS、NMI、Methods、Scientific Data 和上述两本 npj，共 8 本 |
| `nature-research` | 41 本 Nature 学科研究刊，含 NCS、NMI、Methods |
| `nature-npj` / `nature-communications` | 全部 npj / Communications 系列 |
| `nature-reviews` / `nature-scientific` / `nature-progress` | 对应系列 |
| `nature-all` | 注册表中的全部期刊；多个组或别名重叠时只抓一次 |

```bash
# 先在独立目录中试抓，每本最多 2 条，避免覆盖正式数据
python academic.py -v ncs,nmi,ncomms,npjcompumats -y 2025 --metadata-only --limit 2 --metadata-dir metadata_trial

# 核心组全量采集；去掉 --limit 后可断点续抓
python academic.py -v nature-core -y 2025 --metadata-only

# 全部 npj 或全部 Nature 来源
python academic.py -v nature-npj -y 2025 --metadata-only
python academic.py -v nature-all -y 2026 --metadata-only
```

本项目已建立本地 Windows 虚拟环境；如果 `python` 不在 PATH，可用 `.\.venv\Scripts\python.exe` 替换上述命令中的 `python`。

期刊先从官网主页解析 ISSN，再通过 [Crossref API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) 按 ISSN、发表年份分页获取元数据，官网论文页补充摘要、文章类型和学科关键词。优先采用在线发表年份，DOI 是去重和续抓标识。`papers.json` 包括所有抓到的记录（含新闻、更正等），`ai4s.json` 排除已识别的非研究内容，并要求同时有科学主题和 AI 方法证据；综述保留其原始 `article_type`，可按需另筛。

新增字段：`venue_type`、`journal_title`、`issn`、`article_type`、`screening_status`。没有摘要的记录保留在全量数据中并标为 `needs_abstract`；无法识别文章类型时保留 `unknown`，有摘要则标为 `needs_article_type`。这些记录需要补全或复核，不能用候选子集推断完整召回率。`pdf_url` 仅保存官网提供的链接，不自动下载期刊全文。

`--limit` 不允许覆盖已有 `papers.json`，再次试抓请换独立目录。批量采集遇到某一来源失败会保存断点、继续其他来源，最后以退出码 1 提示失败来源；完整成功返回 0。摘要补全失败会记录警告并保留基础元数据。

## AI4S 大类与细粒度关键词

`ai4s_taxonomy.json` 定义 12 个大类及其细粒度关键词/正则，可以直接维护配置。大类为两个可交叉的轴，不做互斥单选：

- 研究环节：科学数据、科学知识模型、科学基础模型、科学智能体、科学评测、自主实验室。
- 科学领域：AI for 数理科学、AI for 生命科学、AI for 物质科学、AI for 地球宇宙科学、AI for 信息科学、AI for 社会科学。

词库版本 `1.2` 包含 157 条大类下的主题/环节规则和 30 条通用方法规则，去重后共 184 个细粒度标签。覆盖蛋白质设计、ADMET、空间转录组、原子间势、逆合成、随机微分方程、湍流、降水临近预报、引力波、电子设计自动化、信道估计、公共政策等方向；通用方法包括图神经网络、自监督、预训练、扩散模型、流匹配、主动学习、贝叶斯优化等。

标签名称统一使用配置中的英文名称，中英文同义词、常见缩写与单复数可归并到同一标签。匹配前统一 Unicode 连字符、全角字符与字段内空白，保留标题/摘要/关键词之间的边界，避免跨字段误拼短语。通用方法词只有存在科学主题或明确科学语境时才输出，不会仅因出现 GNN、Transformer 等就归入 AI4S。此过程完全在本地运行，不调用模型 API。

`ai4s.json` 中新增：

- `ai4s_tags`：命中的大类，一篇论文可有多个。
- `ai4s_keywords`：归一化后的细粒度命中词，如 `protein`、`foundation model`、`neural operator`。
- `ai4s_tagging`：配置版本、匹配依据和证据；规则生成的标签统一标为 `needs_review`，没有匹配到类别则为 `unclassified`。规则不能替代语义复核。

`ai4s_tagging.evidence` 对应大类下的命中标签，`method_evidence` 记录额外的方法标签。例如蛋白质语言模型预训练论文可输出大类 `科学基础模型`、`AI for 生命科学`，细粒度词包括 `protein language model`、`pretraining`、`self-supervised learning`。对旧文件升级词库不会自动重写其已有标注；新采集和未标注输入使用新规则。

原始 `keywords` 保留来源关键词，`ai4s_hits` 保留原有召回关键词命中；三者含义不同。新流程不会覆盖输入记录已有的标签、关键词或标注元信息，也不会自动改写旧的人工整理数据。旧 JSON 中的“科研工具、工程科学”等额外标签尚未迁移到此 12 类口径。

会议仍保留原有关键词召回，并以新分类规则补充候选；期刊额外要求 AI 证据，以免普通蛋白质、分子论文全部进入 AI4S。研究环节标签需要科学语境，其中“科学数据”和“科学评测”优先检查标题及简述，避免仅因摘要提到使用数据集或做评测就贴标签。自定义召回词仍可加入 `ai4s_keywords.txt`，大类与细粒度标签规则在 `ai4s_taxonomy.json` 中维护。

## 验证

```bash
python -m unittest discover -s tests -v
```

回归测试覆盖 12 类、多标签与细粒度关键词、期刊 AI 证据筛选、非研究内容排除、原标签保留、分页去重、在线发表年份、断点写入、别名路由和批量失败退出码。真实网络验证仅对代表期刊少量试抓，不代表已完成全量抓取或语义标注审定。

## 数据源

| `-v` | 来源 |
|---|---|
| `iclr` / `neurips` / `icml` | OpenReview。接口被拦截时，ICML / NeurIPS 改用会议 virtual JSON，ICLR 再退到 proceedings.iclr.cc |
| `acl` / `emnlp` / `naacl` | 元数据模式先走 ACL Anthology，没有该年卷再走 OpenReview；下载 PDF 时走 OpenReview |
| `cvpr` / `iccv` / `wacv` | [openaccess.thecvf.com](https://openaccess.thecvf.com) |
| `eccv` | 下载 PDF 时走 Open Access，若无则 [ECVA](https://www.ecva.net/papers.php)。元数据模式走 ECCV 录用表，摘要用 Crossref 对标题 |
| `aaai` | 仅元数据。OJS 的 OAI-PMH，失败则抓 issue 页面 |
| `kdd` | 仅元数据。DBLP 书目，ACM 会议录分轨，OpenAlex 补摘要 |
| 其他 CCF A/B 会议 / `ccf-a` / `ccf-b` / `ccf-ab` | 仅元数据。DBLP 官方 SPARQL 按 stream/年份分页，Crossref DOI 和公开 HTML 补摘要 |
| Nature 单刊 / 期刊组 | 仅元数据。Crossref 按 ISSN 枚举；Nature 官网补摘要、类型与关键词 |

### OpenReview 登录

访问 ICLR 等会时需要。匿名容易被 challenge 拦住。在 `academic/.env` 写（不要提交）：

```bash
OPENREVIEW_USERNAME=you@example.com
OPENREVIEW_PASSWORD=your_password
```

也可以直接传 OpenReview venue id：

```bash
python academic.py -v ICLR.cc/2025/Conference -y 2025
```
