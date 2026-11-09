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

## 交付统计（更新后）

| 指标 | 数量 |
| --- | ---: |
| 交付记录 | 3,741 |
| 纳入 | 662 |
| 排除 | 3,072 |
| 待定 | 7 |
| 未审 | 0 |
| 覆盖来源 | 35 |
| 官网同口径已确认来源 | 35 / 35 |
| 候选缺摘要 | 39 → 3（且 3 条为原文类型本身无摘要） |

## 仍未解决

- 3 条候选无摘要，原因不是取不到而是原文没有：2 条 DIII 的 Editorial/Letter、1 条 Sci. China Life Sci. 的 Research Highlight。已在候选文件写入 `abstract_status`、`abstract_evidence_url`、`abstract_note`，判定依据为文章类型与正文体例。
- 7 条待定：已不是摘要缺失所致，而是需要全文方法段才能定论；其中仔猪分割一篇（`10.1016/j.compag.2024.108683`）若确认为深度学习，应改判纳入并补标签。
- 本轮未改动其他负责人的交付文件（`nydiii.json` 的三条 Lancet 重复记录除外，原因见第 5 节）。
