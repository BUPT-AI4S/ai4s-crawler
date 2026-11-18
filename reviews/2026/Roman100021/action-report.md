# 2026 论文审核行动报告：乔徐阳（Roman100021）

- 采集快照：`2026-11-08T21:38:12.854071+08:00`（`metadata/2026/snapshot.json`）
- 交付批次：`2026-Roman100021-20261108T213812+0800`
- 来源：35 个（分工见 `reviews/source-assignments-2026.json`）
- 逐篇交付：1,390 条 —— 纳入 1,125、排除 265、待定 0、未审 0
- 候选：1,386 条（含 121 条初筛漏筛补录 + 242 条补摘要后复核补入），候选缺摘要 0

## 一、候选摘要补全（128 → 0）

行动清单列出 128 条候选缺摘要。

- **125 条 Elsevier**：Crossref `alternative-id` 取 PII，再读 ScienceDirect 引用导出接口
  `sdfe/arp/cite?pii=<PII>&format=text/x-bibtex&withabstract=true`，返回的 BibTeX 含原摘要与关键词，
  成功 122 条；同批补 `keywords`，未改写已有字段。
- **2 条 Genome Biology**：Europe PMC / Springer 页面元数据。
- **4 条无摘要非研究型**：Lancet 通讯（pp.599–600）、DIII 社论（pp.131–132）、
  Science China Chem 的 Highlights（pp.4762–4763）、Acta Materialia 更正公告。
  交付中按类型判 `exclude` 并保留记录，同时移出候选池，故候选缺摘要归零。

## 二、全量书目缺摘要补全（进行中）

全量 `papers.json`（35 个来源共 19,280 篇）原有 **7,641 篇缺摘要**，集中在 Elsevier 期刊
（7,181 条）。用同一接口按 DOI → PII → BibTeX 回填：

- 已回填 **530 篇**，其中标题含 AI 术语的 488 篇里补上 448 篇（92%）。
- 出版方对高频请求会短时限流（约 400–500 次后连接被拒，数十分钟恢复），故本轮未能一次跑完；
  抓取脚本按 DOI 断点续跑，缓存在 `outputs/actions-2026/abstract-cache-full.json`。
- 部分“缺摘要”并非采集失败，而是本身无摘要的条目（Lancet 的 Comment、Nature 的 Letter 等），
  这类不做补写。
- 本轮只更新分来源 `metadata/<code>/2026/papers.json`；聚合 `metadata/2026/papers.json` 是
  856 MB 的 LFS 对象，未手工改写，等爬虫侧重建。

## 三、补摘要后重新判断候选（新增 242 条）

对「补上摘要 + 标题含 AI 术语 + 尚未进入候选」的 448 篇重新逐条判断，按「AI 实质参与 + 明确科学/工程任务」
补入候选 242 条：

| 来源 | 补入 | 来源 | 补入 |
|---|---|---|---|
| Computers and Electronics in Agriculture | 81 | Renewable Energy | 70 |
| Mechanical Systems and Signal Processing | 38 | Acta Materialia | 21 |
| Composites Science and Technology | 14 | Transportation Research Part E | 9 |
| Transportation Research Part D | 9 | | |

跳过的主要类型：常规故障分类网络改进（换骨干/加注意力/调参）、器件与传感主导、信号预处理工具、
物流与供应链运筹、政策与行为分析、仅用 ML 拟合经验公式、愿景型综述。

## 四、初筛漏筛补录（121 条）

用各刊 `papers.json` 比对候选，按「AI 实质参与 + 科学任务明确 + 有原摘要」补入 121 条
（Computers and Electronics in Agriculture 31、MSSP 18、Renewable Energy 15、npj Precision Oncology 15 等），
均标注「初筛漏筛补录」。

## 五、官网同口径总量

- 34 个期刊：出版方官网对自动化访问返回 403，改用 Crossref 存缴登记作**参考数**
  （ISSN + 出版日 2026-01-01 至 2026-11-08 + `type=journal-article`），合计 18,672 条，
  与采集 19,280 条的差额在各来源 `coverage_status` 中逐条说明，未冒充官网数。
- CIKM：2026 届论文集尚未出版，采集 0、候选 0，`official_total` 留 `null`。

## 六、标签

- 1,125 篇纳入均有标签，全部命中共享词表；按 `domain` + `task` 为主，必要时补 `method`/`contribution`。
- 「自主实验室」1 篇（LaAlO₃ 分子束外延的物理信息贝叶斯优化闭环实验），
  「科学智能体」9 篇，「科学基础模型」1 篇，「综述」25 篇。
- 词表 `training_stage` 只有「预训练」「微调」，没有「后训练」；本轮无以后训练为主要研究对象的论文，
  未新增条目，避免空标签。

## 七、遗留

1. 全量书目仍有约 7,100 篇未补摘要（出版方限流），可断点续跑
   `outputs/actions-2026/fetch_full2.py`；其中标题含 AI 的仅剩 40 篇。
2. 14 个来源快照状态为 `abstract_incomplete`，属爬虫侧全量采集状态，审核端无法清除。
3. CIKM 2026 论文集未出版，官网总数待补。
4. 参考总数与采集数未做逐 DOI 比对（2026 为在版年，两方时点相差约 10 天）。
