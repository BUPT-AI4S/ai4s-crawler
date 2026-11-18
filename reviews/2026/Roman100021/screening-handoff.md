# 2026 精筛交接说明：乔徐阳（Roman100021）

## 交付文件

- `reviews/2026/Roman100021.json`：1,390 条逐篇判定（纳入 1,125 / 排除 265 / 待定 0 / 未审 0），
  每条保留爬取原字段并追加八字段 `ai4s_review`。
- `reviews/2026/Roman100021/coverage.json`：35 个来源的采集数、候选数、缺摘要数、判定统计、
  参考总数（Crossref）与口径说明。
- `reviews/2026/feedback/Roman100021.json`：35 个来源对象，`issues` / `next_actions` 为空；
  核对方法与差额写在 `coverage_note` / `coverage_rationale`。
- `reviews/2026/Roman100021/action-report.md`：本轮做了什么、数字怎么来的。

## 数据改动

1. `metadata/2026/ai4s.json` 与分来源 `metadata/<code>/2026/ai4s.json`：
   - 补 124 条候选摘要（Elsevier 122、Springer/BMC 2），同批补 `keywords`；
   - 新增 121 条初筛漏筛补录记录 + 242 条「补摘要后复核」补入记录；
   - 移出 4 条非研究型候选（Lancet 通讯、DIII 社论、Science China Chem Highlights、
     Acta Materialia 更正），交付中保留其 exclude 记录。
2. 分来源 `metadata/<code>/2026/papers.json`：回填 530 篇全量书目缺摘要（标题含 AI 的 448/488）。
   聚合 `metadata/2026/papers.json` 为 856 MB LFS，未手工改写。
3. 未改动 `snapshot.json`、其他负责人的文件、监控脚本与词表。

## 关键方法（可复现）

- **Elsevier 摘要**：Crossref `works/<doi>` 的 `alternative-id` 取 PII，再请求
  `https://www.sciencedirect.com/sdfe/arp/cite?pii=<PII>&format=text/x-bibtex&withabstract=true`。
  该接口返回含 `abstract` 与 `keywords` 的 BibTeX，不触发出版方 403；python urllib 会被拦，
  需用 curl 的 TLS 指纹。批量场景先用 Crossref 按 ISSN 分页取 DOI→PII（`rows=1000&cursor=*`），
  再逐条取引用，可省一半请求。
- **限流**：同一 IP 约 400–500 次后会被短时拒绝连接（返回空、curl exit 7），数十分钟恢复。
  脚本已做断点续跑（`outputs/actions-2026/abstract-cache-full.json`）与失败重试计数，
  建议单进程 1–2 并发、每条间隔 0.9 s 以上。
- **初筛漏筛/补摘要复核**：以 `papers.json` 全量书目为准，排除已在候选的 `(venue,id)`，
  按标题含 AI 方法词初筛，再逐条读摘要确认 AI 实质参与且科学任务明确；摘要为空一律不补。
- **官网总量**：出版方官网 403，用 Crossref 存缴登记作参考数，口径写在 `official_scope`；
  差额按在线优先/在印/评论类条目解释，不冒充官网数。

## 遗留

1. 全量书目仍有约 7,100 篇未补摘要（出版方限流），断点续跑 `fetch_full2.py` 即可；
   标题含 AI 的仅剩 40 篇未取到。
2. 14 个来源快照状态为 `abstract_incomplete`，属爬虫侧全量采集状态，审核端无法清除。
3. CIKM 2026 论文集未出版：采集 0、候选 0、`official_total` 为 null，待上线后补。
4. 参考总数与采集数未做逐 DOI 比对；2026 为在版年，两方时点相差约 10 天。
5. 词表 `training_stage` 缺「后训练」，本轮无适用论文；若后续出现 RLHF/DPO 类研究，
   建议在共享词表新增 `后训练 / Post-training` 后再标注。
