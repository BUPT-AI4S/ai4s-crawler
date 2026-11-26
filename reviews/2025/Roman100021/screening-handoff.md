# 2025 精筛交接说明：乔徐阳（Roman100021）

## 交付文件

- `reviews/2025/Roman100021.json`：1,429 条逐篇判定（纳入 933 / 排除 496 / 待定 0 / 未审 0），
  每条保留爬取原字段并追加八字段 `ai4s_review`。
- `reviews/2025/Roman100021/coverage.json`：36 个来源的采集数、候选数、缺摘要数、判定统计、
  参考总数（Crossref）与口径说明。
- `reviews/2025/feedback/Roman100021.json`：36 个来源对象，`issues` / `next_actions` 为空；
  核对方法与差额写在 `coverage_note` / `coverage_rationale`。
- `reviews/2025/Roman100021/action-report.md`：本轮做了什么、数字怎么来的。

## 数据改动

1. `metadata/2025/ai4s.json`（年度候选池）：追加 340 条全量召回补入记录；
   移出 5 条摘要在任何通道都取不到的候选（3 条 CIKM、2 条 Science China），
   交付中保留其 `exclude` 记录与理由。
2. 分来源 `metadata/<code>/2025/papers.json`：回填 5 千余篇缺摘要
   （Elsevier 4 千余、ACM 48、Nature/BMC 若干）。
   聚合 `metadata/2025/papers.json` 是数百 MB 的 LFS 对象，未手工改写，等爬虫侧重建。
3. `metadata/2025/snapshot.json`：18 个来源的 `state` 由 `abstract_incomplete` 改为 `completed`，
   `with_abstract` 同步为实际值，`captured_at` 未动。

## 关键方法（可复现）

- **Elsevier 摘要**：Crossref `works/<doi>` 的 `alternative-id` 取 PII，再请求
  `https://www.sciencedirect.com/sdfe/arp/cite?pii=<PII>&format=text%2Fx-bibtex&withabstract=true`。
  批量时用 curl 一次调用带 10 个 URL（复用连接，约 0.4 s/条），批间 1.2 s、每 100 条歇 20 s，
  可长时间不被封；两个进程并行时**必须写不同缓存文件**，否则互相覆盖。
- **PII 解析**：Crossref `filter=issn:...` 分页（`rows=1000&cursor=*`）取 `alternative-id`；
  仍缺的用 `curl -sI https://doi.org/<doi>` 看 `Location` 里的 PII。
- **Springer / Nature**：未登录页面含订阅墙，正文被截断，**不能**把第一个 `c-article-section__content`
  当摘要；Nature 并发 >2 会返回无 `Abs1-content` 的降级页，解析静默失败。
- **Semantic Scholar**：`/graph/v1/paper/DOI:<doi>?fields=title,abstract` 单条查询可用，
  批量接口 429 频繁；ACM 50 条里补到 48 条。
- **PubMed**：`esearch?term=<doi>[doi]` + `efetch?retmode=xml` 解析 `<AbstractText>`，
  约 1.5 s/条，是 Lancet 类临床刊最稳的通道；Europe PMC 的 `DOI:"..."` 查询必须 URL 编码，
  否则括号会破坏检索式（本轮踩过这个坑），且 core 返回偶尔 20 s 以上。
- **全量召回**：直接复用仓库 `ai4s_filter.select_ai4s` 重跑，与现有候选比对取差集，
  比自造关键词表更贴近采集口径。

## 判定口径

与 2024/2026 定稿一致：科学任务（自然/医学/工程建模推断生成、研究级数学、认知科学、
社科实证、科学任务基准）纳入；研究对象为 LLM 自身能力与机制、通用 Agent、纯 NLP、
模型治理、AI 自身社会行为、科学计量则排除。AI 仅一句带过、仅作基线、纯实验无 AI 的一律排除。
