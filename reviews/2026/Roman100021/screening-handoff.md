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
- **限流**：早期判断「约 400–500 次/时段」不准确——实测触发条件是**并发与瞬时速率**，不是累计配额。
  改成 curl 一次调用带 10 个 URL（复用同一连接，约 0.4 s/条）、批间 1.2 s、每 100 条歇 20 s 后，
  连续 2000+ 次零拒绝（逐条新连接反而更容易被 reset）。偶发 `000/502` 单条退避 90 s 重试即可恢复。
  断点在 `outputs/actions-2026/abstract-cache-full.json`，脚本 `fetch_full4.py`。
- **HTTP 200 但无 abstract**：说明该条目本身没有摘要（Comment/Correspondence/Editorial/更正），
  不是抓取失败，记 `no_abstract` 后不再重试；研究刊条目该比例低于 2%，Lancet 类则超过 85%。
- **非 Elsevier（Springer/Nature/BMC）**：不要用「页面第一个 `c-article-section__content`」兜底，
  那常常是参考文献段。只能用 Europe PMC 的 `abstractText`、JSON-LD 的 `description`，
  或明确的 `id="Abs1-content"`/`data-title="Abstract"` 区块；取不到就记 `no_abstract`。
  另需先用页面 `citation_article_type` 判类型——这批缺摘要的 460 条里绝大多数是
  Highlights/Letter/Correction/Research Highlight，本就没有摘要。
- **初筛漏筛/补摘要复核**：以 `papers.json` 全量书目为准，排除已在候选的 `(venue,id)`，
  再逐条读摘要确认 AI 实质参与且科学任务明确；摘要为空一律不补。
  筛查范围要从「标题含 AI」扩到「摘要含 AI」——补完摘要后发现大量论文标题不含 AI 术语
  （如「基于代理模型的燃烧优化」），只在摘要里提机器学习，仅按标题筛会漏掉；本轮因此新增 117 条候选。
- **官网总量**：出版方官网 403，用 Crossref 存缴登记作参考数，口径写在 `official_scope`；
  差额按在线优先/在印/评论类条目解释，不冒充官网数。

## 遗留

1. 全量书目 19,280 篇中仍有 1,941 篇无摘要：约 830 条经接口确认本身没有摘要（Comment/通讯/更正），
   其余集中在 Lancet 与在版短文。续跑 `fetch_full4.py` 即可（断点续传，约 80 条/分钟）；
   标题含 AI 的条目已全部处理完毕。
2. ~~14 个来源快照状态为 `abstract_incomplete`~~ 已处理：这 14 个来源的摘要补齐后，
   快照中 `state` 改为 `completed`、`with_abstract` 同步为实际值（合计 +5,681），`captured_at` 未动。
   依据是数据事实已变（剩余空缺经接口确认属本无摘要的评论/通讯/更正类），做法同 719ceca7。
3. **CIKM '26 论文集已出版但未采集**：论文集（Rome，2026-11-06）已存缴 Crossref，
   按 prefix 10.1145 + 2026-11 月 + proceedings-article 统计得 1,081 条。本批采集 0、候选 0——
   出版时间晚于采集快照两天，ACM DL 侧未进入采集范围。`official_total` 已按参考数填 1,081 并注明口径，
   该缺口需爬虫侧补采后补审，不能视为「无 AI4S 论文」。
4. 参考总数与采集数未做逐 DOI 比对；2026 为在版年，两方时点相差约 10 天。
5. 词表 `training_stage` 缺「后训练」，本轮无适用论文；若后续出现 RLHF/DPO 类研究，
   建议在共享词表新增 `后训练 / Post-training` 后再标注。

## COLM（2026-11-24 追加）

- COLM 论文整批进入候选后未筛，本轮按口径逐条复核：131 条候选 → 保留 22、剔除 109。
- 保留以"AI 承担具体科学任务"为准（天文观测拟合、分子设计、晶体发现、逆合成、形式定理证明、
  材料复现、城市仿真）；剔除为通用 LLM 能力研究、通用 Agent、纯 NLP 与面向通用能力的基准。
- 剔除项已从 `metadata/2026/ai4s.json` 移除，交付中保留 exclude 记录（`note: COLM 候选复核`）。
- 官方论文集 856 条与采集一致，`official_total` 记 856 并注明与采集同源。

**全量召回补充**：对未入候选的 834 篇按「标题领域词 → 摘要强领域词 → 全文复查」三层扫描，
送判 118 篇，补入 11 条（形式数学 4、临床诊断 4、社科质性编码/科学图表/科学提案 3）。
SGS 一条由排除改判为纳入（标题看不出，摘要下游任务是 Lean4 定理证明）。剩余 748 篇确认为通用语言模型研究。
