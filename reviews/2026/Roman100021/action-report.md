# 2026 论文审核行动报告：乔徐阳（Roman100021）

- 采集快照：`2026-11-08T21:38:12.854071+08:00`（`metadata/2026/snapshot.json`）
- 交付批次：`2026-Roman100021-20261108T213812+0800`
- 来源：36 个（35 个原分工来源 + 2026-11-24 追加的 COLM，见 `reviews/source-assignments-2026.json`）
- 逐篇交付：2,155 条 —— 纳入 1,781、排除 374、待定 0、未审 0
- 候选：2,042 条（含 121 条初筛漏筛补录 + 876 条补摘要后复核补入 + COLM 复核保留 22 条），候选缺摘要 0

## 一、候选摘要补全（128 → 0）

行动清单曾列出 128 条候选缺摘要。

- **125 条 Elsevier**：Crossref `alternative-id` 取 PII，再读 ScienceDirect 引用导出接口
  `sdfe/arp/cite?pii=<PII>&format=text/x-bibtex&withabstract=true`，返回的 BibTeX 含原摘要与关键词。
- **2 条 Genome Biology**：Europe PMC / Springer 页面元数据。
- **4 条无摘要非研究型**：Lancet 通讯、DIII 社论、Science China Chem 的 Highlights、Acta Materialia 更正。
  交付中按类型判 `exclude` 并保留记录，同时移出候选池，故候选缺摘要归零。

## 二、全量书目缺摘要补全（7,641 → 1,941）

35 个来源共 19,280 篇，原有 **7,641 篇缺摘要**（Elsevier 7,181）。按 DOI → PII → BibTeX 回填，
累计补上 **5,700 篇**，现存 1,941 篇空缺。

- **限流的真实原因**：早期判断「约 400–500 次/时段配额」不准确。实测触发条件是**并发与瞬时速率**：
  逐条新连接、2 并发时约 400 次后被 reset；改为 curl 一次调用带 10 个 URL（复用同一连接，
  约 0.4 s/条）、批间 1.2 s、每 100 条歇 20 s 后，连续 9,600 次仅 2 次失败，零长时间封禁。
- **200 但无 abstract 字段**：说明该条目本身没有摘要（Comment/Correspondence/Editorial/更正），
  不是抓取失败。全部 9,633 条目标里这类有 829 条（8.6%），集中在 Lancet（该刊该批 85% 以上无摘要）。
- **非 Elsevier（Springer/Nature/BMC）460 条**：先用页面 `citation_article_type` 定类型，
  其中绝大多数是 Highlights/Letter/Correction/Research Highlight，本就没有摘要；
  仅 98 条研究型重抓，补到 11 条。注意不能拿「页面第一个正文块」当摘要——那常常是 References 段。
- 本轮只改分来源 `metadata/<code>/2026/papers.json`；聚合 `metadata/2026/papers.json` 是
  856 MB 的 LFS 对象，未手工改写，等爬虫侧重建。

## 三、补摘要后重新判断候选（新增 876 条）

补上摘要后分六轮复核，范围从「标题含 AI 术语」扩到「摘要含 AI」——很多论文标题不含 AI 术语
（如「基于代理模型的燃烧优化」），只在摘要里提机器学习，只按标题筛会漏。

| 轮次 | 复核 | 补入 | 主要来源 |
|---|---|---|---|
| 1 | 448 | 242 | compag 81、Renewable 70、MSSP 38、Acta 21 |
| 2 | 122 | 66 | compag 30、MSSP 12、TR-E 8、Env Int 4 |
| 3 | 408 | 184 | compag 145、MSSP 25、Acta 6、CST 6 |
| 4 | 251 | 36 | Env Int 7、TR-D 7、TR-E 6、compag 6 |
| 5 | 285 | 46 | Renewable 31、compag 14、CST 1 |
| 6 | 614 | 185 | MSSP 92、Renewable 58、compag 14、TR-E 11、TR-D 9 |

纳入率从首轮 54% 降到末轮 30% 以下（第三轮后降至 14%），边际收益明显收敛。

跳过的主要类型：常规故障分类网络改进（换骨干/加注意力/调参）、器件与传感主导、信号预处理工具、
物流与供应链运筹、政策与行为分析、仅用 ML 拟合经验公式、愿景型综述、AI 只在方法末尾一句带过。

## 四、初筛漏筛补录（121 条）

用各刊 `papers.json` 比对候选，按「AI 实质参与 + 科学任务明确 + 有原摘要」补入 121 条
（Computers and Electronics in Agriculture 31、MSSP 18、Renewable Energy 15、npj Precision Oncology 15 等），
均标注「初筛漏筛补录」。

## 五、官网同口径总量

- 34 个期刊：出版方官网对自动化访问返回 403，改用 Crossref 存缴登记作**参考数**
  （ISSN + 出版日 2026-01-01 至 2026-11-08 + `type=journal-article`），合计 18,672 条，
  与采集 19,280 条的差额在各来源 `coverage_status` 中逐条说明，未冒充官网数。
- CIKM：论文集 2026-11-06 出版，Crossref 登记 1,081 条；本批采集 0、候选 0，
  `official_total` 按参考数填 1,081，差额 -1,081 已注明需补采。

## 六、标签

- 1,759 篇纳入全部有标签，共 479 个标签，全部命中共享词表；按 `domain` + `task` 为主，
  必要时补 `method`/`contribution`。
- 「自主实验室」2 篇（LaAlO₃ 分子束外延的物理信息贝叶斯优化闭环；中锰钢的高斯过程 + 帕累托主动学习
  迭代合成），「科学智能体」15 篇，「科学基础模型」2 篇，「预训练」3 篇、「微调」2 篇，「综述」30 篇。
- 词表 `training_stage` 只有「预训练」「微调」，没有「后训练」；本轮无以后训练为主要研究对象的论文，
  未新增条目，避免空标签。

## 七、遗留

1. 全量书目仍有 1,941 篇无摘要，其中约 830 条经接口确认本身没有摘要（评论、通讯、更正类），
   其余集中在 Lancet 与部分在版短文；续跑 `outputs/actions-2026/fetch_full4.py` 即可。
2. 14 个来源原先的 `abstract_incomplete` 状态已在摘要补齐后更新为 `completed`，
   `with_abstract` 同步为实际值（+5,681），`captured_at` 未动。
3. CIKM '26 论文集已于 2026-11-06 出版（Crossref 登记 1,081 条），但本批采集为 0，
   需爬虫侧补采后补审；`official_total` 已按参考数填 1,081 并注明口径。
4. 参考总数与采集数未做逐 DOI 比对（2026 为在版年，两方时点相差约 10 天）。

## 八、COLM 追加与复核（2026-11-24）

COLM（Conference on Language Modeling）经用户指定追加到分工，采集 856 篇（官方论文集
proceedings.colm.cc，摘要覆盖 100%），初筛给出 131 条候选。这批候选未经人工筛选，按口径逐条判定：

- **保留 22 条**：AI 承担具体科学任务的条目，如 Stargazer（系外行星视向速度拟合环境）、
  MolDesignBench（LLM 调用化学工具做多约束分子设计）、CrystalSTAR（约束晶体发现）、
  RetroAgent（逆合成路线规划）、DreamProver / MechMath / VeriSoftBench（形式定理证明）、
  AutoMat（计算材料复现）、UrbanLLMind（城市出行仿真）。
- **剔除 109 条**：通用语言模型能力研究（记忆、偏见、对齐、RL 训练、解码、效率、上下文长度）、
  通用 Agent 与工具调用、纯 NLP 任务、以 AI 研究能力为对象的基准（如 ResearcherBench）。
- 剔除记录从候选池移出，但以 exclude 记录保留在交付中，理由逐条可查（`note: COLM 候选复核`）。
- 覆盖口径：官方论文集 856 条与采集一致，`official_total` 记 856 并注明与采集同源；
  官网无年度目录接口，OpenReview 与 DBLP 对自动化访问有人机校验，未做独立二次计数。
