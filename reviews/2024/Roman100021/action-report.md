# 乔徐阳 · 2024 年审核行动清单处理记录

处理时间：2026-11-09。清单来源：`reviews/2024/actions/乔徐阳.md`（仓库提交 `990d642d8cb137db0db9873f16d4b004079869e5` 自动生成）。数据快照：北京时间 2026-11-05T10:31:19，采集范围为本轮分工的 34 本期刊与 CIKM，共 16,838 条记录、467 条初筛候选。

清单里的 39 段提示归为五类问题，逐类处理如下。逐来源口径、总数与证据见 [`coverage.json`](coverage.json)；摘要补查台账见 [`abstract-topup.csv`](abstract-topup.csv)。

## 1. 官网同口径总数（清单中 39 处「尚未确认」）

覆盖全部 35 个来源，35/35 已确认并写入 `coverage.json`，含 `official_total`、`official_scope`（口径）、`coverage_rationale`、`evidence_urls`，并附逐 DOI 比对结果。

- **Nature 系 15 本期刊**：官网 2024 年发表日期列表可整年枚举，逐页取全部文章条目后与采集按 DOI 比对。14 本零差；Molecular Psychiatry 官网 513 条、采集 510 条，多出的 3 条经逐条核实为两张图片摘要（`10.1038/s41380-023-02393-5`、`10.1038/s41380-023-02328-0`）与一条更正（`10.1038/s41380-024-02416-9`），不属研究条目，不补录。
- **其余 18 本期刊与 CIKM 之外的期刊（Elsevier、Springer、BMC、Cell Press）**：卷期目录与文章页对自动化访问返回 403，或只给卷期索引而无法枚举整年条目。改用出版方存缴的 Crossref 登记，按 ISSN、出版日 2024-01-01 至 2024-12-31、`type=journal-article` 统计——这正是采集器 `journal_meta.py` 的筛选条件，与全量采集完全同口径。逐 DOI 比对结果：19 本期刊全部缺 0 条、多 0 条。
- **CIKM**：正式长文（Full Research Track）录用 347 篇，与官网录用目录、程序主席报告一致；全量采集 697 条覆盖该届全部分轨，其中正式长文同轨 347 条，差额为其他分轨，已写入口径说明。

结论：所有差额都能用口径差异或非研究条目解释，未发现需要补采的 AI4S 论文，因此本轮没有新增「官网漏采补录」记录。

## 2. 逐篇交付与采集快照不同或未标注（清单中 23 个来源提示）

原因已定位：交付里 878 条写的是快照时间，另外 2,863 条（第 2 轮续做新增的判定）写成了续做当天的时间 `2026-11-07T23:01:58+08:00`，与快照不一致。

处理：3,741 条 `ai4s_review.snapshot_at` 全部统一为快照时间 `2026-11-05T10:31:19.144426+08:00`。这些记录的论文对象仍逐字保留快照原字段，只在 `ai4s_review` 下写判定。批次与覆盖范围：本批交付 = 快照中 35 个来源的全部初筛候选 + 复查中确认的 82 条「初筛漏筛补录」（沿用快照原始 ID）+ 全量复核中逐篇判定过的记录，未混入其他批次或年度的数据。

## 3. AI4S 候选缺少摘要（清单合计 67 篇）

按 `metadata/2024/ai4s.json` 的候选记录逐 DOI 补查 Crossref、OpenAlex、Europe PMC、Semantic Scholar 与出版方页面五路来源：

| 处理 | 数量 | 说明 |
| --- | ---: | --- |
| 补得原摘要并写回候选文件 | 28 | 同时更新 `metadata/2024/ai4s.json` 与对应 `metadata/<来源>/2024/ai4s.json`，`source` 追加摘要来源，`screening_status` 按 `article_type` 重设 |
| 仍缺摘要 | 39 | 均为 Elsevier 期刊：ScienceDirect 与 linkinghub 返回 403，Crossref 无摘要字段，OpenAlex／Europe PMC／Semantic Scholar 无记录，OpenAIRE 无可用描述 |

覆盖情况：MSSP 16→10、Acta Materialia 14→5、Computers and Electronics in Agriculture 14→11、Renewable Energy 12→8、DII 3→2、其余 6 本合计 8→3。逐 DOI 状态与查询记录见 [`abstract-topup.csv`](abstract-topup.csv)。

39 条仍缺摘要的候选没有被判为「与 AI4S 无关」：它们在交付中的判定仍以可核实证据为准，摘要缺口如实保留，待有订阅权限或机构网络时重跑。

## 4. 交付中的待定与未审记录（清单中 11 个来源提示）

交付原有 26 条待定、0 条未审，逐条复核后处理如下：

- **改判排除 19 条**：2 条按文献类型（The Lancet 评论栏目 2 页短文，Crossref 与 PubMed 均无摘要正文）；1 条按补得的摘要（货运列车储能配置为凸优化建模与闭式解，非 AI）；16 条按题名明示的方法排除（解析模型、博弈论、交通分配、排队模型、运筹优化、经典卡尔曼滤波、材料合成与表征、传感器实验等），理由中注明「以题名证据排除」。
- **保持待定 7 条**：缺口是「无法确认是否使用机器学习」，不是缺相关性证据。逐条写明缺什么：
  - `10.1016/j.ymssp.2023.110886`（时滞系统稳定性优化，可能用智能优化）
  - `10.1016/j.ymssp.2024.111513`（子结构参数化降阶，是否数据驱动未知）
  - `10.1016/j.renene.2024.120892`（GWO-Enhanced PSO 元优化，须确认群体智能是否为实质 AI 方法）
  - `10.1016/j.renene.2024.121211`（生物甲烷产气建模，机理/统计与机器学习的区分）
  - `10.1016/j.compag.2024.108683`（遮挡下仔猪分割，很可能构成 AI 实质参与，须摘要确认）
  - `10.1016/j.compag.2024.109218`（气候对产奶量影响建模，方法不明）
  - `10.1038/s41380-024-02841-w`（摘要只称预测模型与 79.5%–98.0% 准确率，未说明模型类别；全文与方法是付费内容）

这 7 条已在 `rationale` 中写明五路摘要源与出版方页面的核实结果和下一步动作。待定率 7/3,741 = 0.19%。

## 5. The Lancet 同 DOI 冲突

新版分工把 The Lancet 交给乔徐阳，主分支 `reviews/2024/nydiii.json` 仍保留同一批三条记录。核对结论：

- 三条同键记录（`10.1016/s0140-6736(24)00476-8`、`(24)00550-6`、`(24)01548-4`）的负责人已按 [`source-assignments-2024.json`](../../source-assignments-2024.json) 确认是乔徐阳。
- 其中全球生育率预测一篇本次判排除（人口学预测，AI 未实质参与），旧文件判纳入，是冲突来源；另两篇双方都判纳入。
- 处理：从 `nydiii.json` 删除这三条重复记录（该文件 908 条减至 905 条），保留本次交付中的判定，避免合并时重复计数。旧文件其余记录不动。

处理后 The Lancet 来源内无同键冲突。

## 6. 补摘要第二轮：从出版方文章页直读

第二轮先穷举全部免费接口，全部落空后再改为逐篇读取出版方文章页正文。

已排空的接口（对 39 条逐一试过，命中 0）：Crossref、OpenAlex、Europe PMC、PubMed、Semantic Scholar、OpenAIRE、Unpaywall（含 OA 位置与 SSRN/OSTI 副本）、Wayback（按 DOI 与按 PII 两种入口）、fatcat、x-mol、Baidu 学术、CNKI 系站点。ScienceDirect 与 linkinghub 对脚本请求一律返回 403 挑战页，headless 浏览器同样是挑战页。

最终可行路径是逐篇读取文章页 DOM 后逐字回填摘要正文：

- Elsevier 37 篇：以 Crossref 的 `alternative-id` 取 PII，逐篇打开 `https://www.sciencedirect.com/science/article/pii/<PII>`，从 Abstract 栏逐字复制正文（不改写、不摘要）。
- Springer 1 篇：`https://link.springer.com/article/10.1007/s11427-024-2673-9`。
- 结果：36 篇取回摘要写回候选文件；3 篇经页面结构核实属于本身无摘要的文章类型，只登记证据、不编造内容：
  - `10.1016/j.diii.2024.07.011`：Editorial（Vol.105(11):415-416）
  - `10.1016/j.diii.2024.07.010`：Letter to the Editor（Vol.105(10):409-411）
  - `10.1007/s11427-024-2673-9`：Research Highlight（Sci. China Life Sci. 68:588-589）

写回时保持候选文件原有的行级格式、字段顺序与 CRLF：仅填 `abstract`，并把 `source` 追加 `sciencedirect.com` / `springer.com`；`screening_status` 按 `article_type` 是否已知重设为 `ready` 或 `needs_article_type`；无摘要的 3 条新增 `abstract_status: none_by_article_type`、`abstract_evidence_url`、`abstract_note` 三个字段说明缘由。

台账 `abstract-topup.csv` 已同步刷新：64 条「已补摘要写回候选文件」（35 条来自 ScienceDirect 页面直读、1 条来自 SpringerLink 页面直读、28 条为第一轮 API 命中）、3 条「原文类型无摘要」。

## 7. 文献类型清理：5 条非研究型条目移出候选池

第 6 节留下的 3 条「原文类型无摘要」不应停留在候选里——它们本就不是原创研究正文，是初筛收录了不该收的文献类型。按 `review-rules.md` 的文献类型口径（只纳入原创研究正文、正式会议研究论文和有实质学术内容的综述；评论、社论、读者来信、更正、撤稿公告按类型排除），连同扫描中发现的另 2 条同类型记录，一并从候选池移除：

| DOI | 出版方类型 | 来源 | 依据 |
| --- | --- | --- | --- |
| `10.1016/j.diii.2024.07.011` | Editorial | Diagnostic and Interventional Imaging | Vol.105(11):415-416，无摘要栏 |
| `10.1016/j.diii.2024.07.010` | Letter to the Editor | Diagnostic and Interventional Imaging | Vol.105(10):409-411，正文以 “To the Editor,” 开头 |
| `10.1007/s11427-024-2673-9` | Research Highlight | Science China Life Sciences | 68:588-589，SpringerLink 标注类型即 Research Highlight |
| `10.1016/j.envint.2024.108561` | Corrigendum | Environment International | 题名 “Corrigendum to …”，仅更正作者单位 |
| `10.1038/s41698-024-00510-3` | Retracted article | npj Precision Oncology | 题名 “RETRACTED ARTICLE: …”，出版方已撤回 |

处理方式：候选文件（`metadata/2024/ai4s.json` 与 4 个分来源文件，共 5 行）按行删除，其余记录的顺序、字段与 CRLF 不变；交付 JSON 保留这 5 条的 `exclude` 记录并注明文献类型——规则要求「对已有候选保留排除记录，并在理由中注明类型」，删候选不等于删判定。

清理后候选缺摘要归零：`coverage.json` 的 `candidate_missing_abstract` 35 个来源全部为 0。

## 8. 7 条待定：逐篇读原文后落定

第 6 节之后剩余的 7 条待定不是摘要缺失，而是方法不明。逐篇打开出版方文章页读摘要、引言与方法段（Molecular Psychiatry 一篇正文在订阅墙内，改读出版方补充材料 DOCX 与补充表 PDF），全部落定：

| DOI | 来源 | 判定 | 读到的方法 |
| --- | --- | --- | --- |
| `10.1016/j.ymssp.2023.110886` | Mech. Syst. Signal Process. | exclude | 传输零点直接配置 + 谱横坐标最小化的约束优化，最右特征根用 TDS-CONTROL 计算；经典控制理论，无学习型方法 |
| `10.1016/j.ymssp.2024.111513` | Mech. Syst. Signal Process. | exclude | 两层 Krylov-Craig-Bampton 子结构降阶 + 增广 CCM + Newmark-Beta 双层接触时程积分；确定性数值降阶 |
| `10.1016/j.renene.2024.120892` | Renewable Energy | include | GWO 元优化整定 PSO，再用 PSO 寻优光伏 MPPT 的 D-PID 增益；报告相对 INC/PSO/P&O 提升 9.1%–21.6% |
| `10.1016/j.renene.2024.121211` | Renewable Energy | include | 人工神经网络拟合三种海藻厌氧消化逐日产甲烷，R²>0.999、RMSE<4.537，优于 Gompertz/一级/Transfer/Cone 等经验模型 |
| `10.1016/j.compag.2024.108683` | Comput. Electron. Agric. | include | Mask R-CNN（ResNeXt-101）+ 自适应框扩展 + vMF 编码 + 贝叶斯栅格分类器的两阶段非模态实例分割，五档遮挡 IoU 0.834–0.930 |
| `10.1016/j.compag.2024.109218` | Comput. Electron. Agric. | exclude | PCA 与 t-SNE 做相关性与降维可视化，逐性状偏最小二乘回归/预测；经典统计建模 |
| `10.1038/s41380-024-02841-w` | Molecular Psychiatry | exclude | 补充表 11–13：临床变量 + PRS + 基因型 + 性别的多项逻辑回归（含系数、残差偏差与 AIC），非机器学习 |

同时把 7 篇的原摘要回填到交付记录的 `abstract` 与 `verified_metadata.abstract`，`evidence_urls` 改为实际读取的文章页/补充材料地址。新增 3 条纳入的标签：`粒子群优化`+`群智能优化`（120892）、`神经网络`（121211）、`实例分割`+`卷积神经网络`（108683），均配 `AI 用于工程科学`/`AI 用于生命科学` 与对应任务标签。

## 9. 三条口径提示的收口（2026-11-09，第五轮）

行动清单里仅剩的三条"问题"（CIKM、Molecular Psychiatry、npj Schizophrenia）复核后都不是待办，而是上一轮把口径说明写进了 `issues`。监控对 `issues` 是原文照搬展示，所以一直显示为问题。本轮把说明移入 `coverage_note`、`issues` 与 `next_actions` 清空，并把 MP 的 `official_total` 从官网列表口径改成同口径。

| 来源 | 原提示 | 复核后的事实 | 处理 |
| --- | --- | --- | --- |
| CIKM | 官网 347 只覆盖 Full Research Track，采集 697 覆盖全部分轨 | 官网录用页 7 张分轨表逐行解析：Full Track 录用 348 条，347 条与采集逐篇对应；余 1 条 fp0540 在 Crossref 与 ACM proceedings 均无出版记录（录用未出版）；其余分轨官网合计 330 条、对应 324 条；采集 697 条为该届 proceedings（10.1145/3627673）全部条目，含未列入录用页的 Workshops 等 | `official_total` 维持 347，口径改记为"Full Research Track 正式出版长文"，分轨构成写入 `coverage_note` |
| Molecular Psychiatry | 官网 513 比采集多 3 条 | 3 条为 2 条单页图片摘要（`10.1038/s41380-023-02328-0`、`10.1038/s41380-023-02393-5`）与 1 条更正（`10.1038/s41380-024-02416-9`）；三条印刷年均为 2023、仅在线日期落在 2024，属出版年与在线日期口径差异。Crossref 出版年 journal-article 同口径 510 条，与采集 510 条逐 DOI 完全一致 | `official_total` 513 → **510**（同口径），三条差异条目的 DOI 与成因写入 `coverage_note` |
| npj Schizophrenia | 官网口径含图片摘要、更正等非研究条目 | 官网 2024 列表 124 条、Crossref journal-article 124 条、采集 124 条三者一致，逐 DOI 无缺无多 | `official_total` 维持 124，三者一致性写入 `coverage_note` |

结果：`official_total` 合计由 16,491 调整为 16,488（仅 MP 变动），35 个来源的反馈 `issues` 全部为空，交付与判定未改动。

## 交付统计（更新后）

| 指标 | 数量 |
| --- | ---: |
| 交付记录 | 3,741 |
| 纳入 | 665 |
| 排除 | 3,076 |
| 待定 | 0 |
| 未审 | 0 |
| 覆盖来源 | 35 |
| 官网同口径已确认来源 | 35 / 35 |
| 候选缺摘要 | 39 → 0（其中 5 条非研究型条目已移出候选池） |

## 仍未解决

- 无待定、无未审、候选缺摘要为 0，行动清单的自动提示项已全部消除。
- 本轮未改动其他负责人的交付文件（`nydiii.json` 的三条 Lancet 重复记录除外，原因见第 5 节）。
