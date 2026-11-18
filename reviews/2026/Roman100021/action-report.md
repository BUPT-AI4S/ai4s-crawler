# 2026 论文审核行动报告：乔徐阳（Roman100021）

- 采集快照：`2026-11-08T21:38:12.854071+08:00`（`metadata/2026/snapshot.json`）
- 交付批次：`2026-Roman100021-20261108T213812+0800`
- 来源：35 个（分工见 `reviews/source-assignments-2026.json`）
- 逐篇交付：1,148 条 —— 纳入 883、排除 265、待定 0、未审 0
- 候选：1,144 条（其中 121 条为本轮初筛漏筛补录），候选缺摘要 0

## 一、候选摘要补全

行动清单列出 128 条候选缺摘要，集中在 Elsevier 与 2 个 Springer Nature 刊。

- **125 条 Elsevier**：Crossref `alternative-id` 取 PII，再读 ScienceDirect 引用导出接口
  `sdfe/arp/cite?pii=<PII>&format=text/x-bibtex&withabstract=true`，返回的 BibTeX 含原摘要与作者关键词。
  逐条回填时同时补 `keywords`，未改写任何已有字段。成功 122 条。
- **2 条 BMC/Springer（Genome Biology）**：Europe PMC / Springer 页面元数据取原摘要。
- **4 条判为无摘要非研究型**：Lancet 通讯（pp.599–600）、DIII 社论（pp.131–132）、
  Science China Chem 的 Highlights 短文（pp.4762–4763）、Acta Materialia 更正公告。
  已在交付中按类型判 `exclude` 并保留记录，同时移出候选池（与 2024 批次同政策），
  故候选缺摘要归零，而不是留 4 条永久待补。

回填结果：`metadata/2026/ai4s.json` 与对应 `metadata/<code>/2026/ai4s.json` 共 124 条
`abstract`（及 `keywords`）更新，差异只落在这些记录上。

## 二、初筛漏筛补录

关键词初筛漏掉了一批 AI4S 论文。按「确有 AI 实质参与 + 明确科学/工程任务 + 有可核实原摘要」
逐条核实后补录 121 条，均标注「初筛漏筛补录」，写入候选文件并纳入逐篇交付：

| 来源 | 补录 | 来源 | 补录 |
|---|---|---|---|
| Computers and Electronics in Agriculture | 31 | npj Precision Oncology | 15 |
| Mechanical Systems and Signal Processing | 18 | npj Science of Food | 7 |
| Renewable Energy | 15 | Microsystems & Nanoengineering | 7 |
| Transportation Research Part E | 6 | Acta Materialia | 5 |
| Communications Earth & Environment | 5 | The Lancet | 3 |
| Diagnostic and Interventional Imaging | 3 | Leukemia | 3 |
| Transportation Research Part D | 2 | Composites Science and Technology | 1 |

跳过的主要类型：摘要为空（Elsevier 三刊合计约 300 条命中无摘要）、仅贝叶斯/统计推断、
运筹与业务优化、工具/平台类、文献计量综述、纯实验或器件研究、把 AI 当被测对象的评测。

## 三、官网同口径总量

- 34 个期刊：出版方官网对自动化访问返回 403，改用 Crossref 存缴登记作**参考数**
  （ISSN + 出版日 2026-01-01 至 2026-11-08 + `type=journal-article`）。
  合计参考数 18,672 条、采集 19,280 条；差额已在各来源 `coverage_status` 中逐条说明
  （在线优先、在印条目与评论类条目的口径差异），未冒充官网数。
- CIKM：2026 届论文集尚未出版，采集 0 条、候选 0，`official_total` 留 `null`。

## 四、逐篇精筛与标签

- 883 篇纳入，410 个不同标签，全部命中共享词表（`tag-vocabulary.json`，1,334 条）。
- 标签按 `domain` + `task` 为主，必要时补 `method` / `contribution`；证据位置统一「输入摘要」，
  标签理由优先取摘要中对应原句，取不到时回落到判定理由。
- 「自主实验室」用于 1 篇（LaAlO₃ 分子束外延的物理信息贝叶斯优化闭环实验，`10.1038/s41427-026-00668-1`）；
  「科学智能体」9 篇、「科学基础模型」1 篇、「综述」25 篇。
- 共享词表 `training_stage` 只有「预训练」「微调」，没有「后训练」。本轮 883 篇中没有一篇
  以后训练（RLHF/DPO/可验证奖励强化学习）为主要研究对象，故未新增词表条目，避免空标签。

## 五、遗留与限制

1. 14 个来源快照状态仍为 `abstract_incomplete`（Lancet、MSSP、Renewable Energy、Acta Materialia、
   Environment International、TR-D、TR-E、Computers and Electronics in Agriculture、Science China
   Chemistry、Science China Life Sciences、Composites Science and Technology、Leukemia、Oncogene、
   DIII）。这是爬虫侧全量采集状态，审核端无法清除；候选层摘要已补齐，不影响本轮判定。
2. CIKM 2026 论文集未出版，官网总数待论文集上线后补。
3. 参考数与采集数的差额未做逐 DOI 比对（2026 年为在版年，双方时点相差 10 天）。
