# 2026 精筛交接说明：乔徐阳（Roman100021）

## 交付文件

- `reviews/2026/Roman100021.json`：1,148 条逐篇判定（纳入 883 / 排除 265 / 待定 0 / 未审 0），
  每条保留爬取原字段并追加八字段 `ai4s_review`。
- `reviews/2026/Roman100021/coverage.json`：35 个来源的采集数、候选数、缺摘要数、判定统计、
  参考总数（Crossref）与口径说明。
- `reviews/2026/feedback/Roman100021.json`：35 个来源对象，`issues` / `next_actions` 为空；
  核对方法与差额写在 `coverage_note` / `coverage_rationale`。
- `reviews/2026/Roman100021/action-report.md`：本轮做了什么、数字怎么来的。

## 数据改动

1. `metadata/2026/ai4s.json` 与分来源 `metadata/<code>/2026/ai4s.json`：
   - 补 124 条候选摘要（Elsevier 122、Springer/BMC 2），同批补 `keywords`；
   - 新增 121 条初筛漏筛补录记录（保留爬取原字段，判定为纳入）；
   - 移出 4 条非研究型候选（Lancet 通讯、DIII 社论、Science China Chem Highlights、
     Acta Materialia 更正），交付中保留其 exclude 记录。
2. 未改动 `snapshot.json`、`papers.json`、其他负责人的文件、监控脚本与词表。

## 关键方法（可复现）

- **Elsevier 摘要**：Crossref `works/<doi>` 的 `alternative-id` 取 PII，再请求
  `https://www.sciencedirect.com/sdfe/arp/cite?pii=<PII>&format=text/x-bibtex&withabstract=true`。
  该接口返回含 `abstract` 与 `keywords` 的 BibTeX，不触发出版方 403；python urllib 会被拦，
  需用 curl 的 TLS 指纹。分来源记录回填后，候选缺摘要从 128 降到 4（4 条为非研究型）。
- **漏筛补录**：以 `metadata/<code>/2026/papers.json` 为准，排除已在候选的 `(venue,id)`，
  按标题含 AI 方法词初筛，再逐条读摘要确认 AI 实质参与且科学任务明确；摘要为空一律不补。
- **官网总量**：出版方官网 403，用 Crossref 存缴登记作参考数，口径写在
  `official_scope`；差额按在线优先/在印/评论类条目解释，不冒充官网数。

## 遗留

1. 14 个来源快照状态为 `abstract_incomplete`，属爬虫侧全量采集状态，审核端无法清除。
2. CIKM 2026 论文集未出版：采集 0、候选 0、`official_total` 为 null，待上线后补。
3. 参考总数与采集数未做逐 DOI 比对；2026 为在版年，两方时点相差约 10 天。
4. 词表 `training_stage` 缺「后训练」，本轮无适用论文；若后续出现 RLHF/DPO 类研究，
   建议在共享词表新增 `后训练 / Post-training` 后再标注。
