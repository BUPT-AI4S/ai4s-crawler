# 2025 论文审核行动报告：乔徐阳（Roman100021）

- 采集快照：`2026-11-09T10:51:18+08:00`（`metadata/2025/snapshot.json`）
- 交付批次：`2025-Roman100021-20261126T120000+0800`
- 来源：36 个（见 `reviews/source-assignments-2025.json`）
- 逐篇交付：1,429 条 —— 纳入 933、排除 496、待定 0、未审 0
- 候选：1,330 条（初筛 995 + 全量召回补入 340 − 5 条无摘要移出），候选缺摘要 0

## 一、候选摘要补全（83 → 0）

行动清单曾列出 83 条候选缺摘要，全部为 Elsevier。

- Crossref `works/<doi>` 的 `alternative-id` 取 PII（新增 5,929 条映射，覆盖 99.6%），
  再读 ScienceDirect 引用导出接口
  `sdfe/arp/cite?pii=<PII>&format=text/x-bibtex&withabstract=true`，返回 BibTeX 含原摘要。
- 5 条确实取不到：3 条 CIKM（ACM DL 反爬）、2 条 Science China（订阅墙），
  交付中按证据不足 `exclude` 并保留理由，同时移出候选池，故候选缺摘要归零。

## 二、全量书目缺摘要补全（7,766 → 2,042）

36 个来源共 20,544 篇，原有 **7,766 篇缺摘要**（Elsevier 7,220），本轮补上 **5,724 篇**，
现存 2,042 篇。四通道：

| 通道 | 目标 | 补到 | 说明 |
|---|---|---|---|
| Elsevier（ScienceDirect cite） | 6,008 | 5,666 | DOI→PII→BibTeX，curl 单连接带 10 个 URL，双进程写不同缓存 |
| Springer / Nature / ACM / BMC（Semantic Scholar） | 546 | 58 | ACM 48/50，Nature 9，BMC 1；Springer 多为订阅墙 |
| PubMed（Lancet 等临床刊补漏） | 380 | 7 | `esearch` 按 DOI + `efetch` XML 解析 `AbstractText`，约 1.5 s/条 |
| 页面抓取 | — | 0 | Springer 预览页无正文、Nature 并发限流，放弃 |

现存 2,042 篇空缺构成：Elsevier 1,554（其中 1,515 条接口明确返回无 `abstract` 字段）、
Springer 256、Nature 207、BMC 23、ACM 2。

关键经验：

- **不能拿「页面第一个正文块」当摘要**：Springer 未登录时正文被截断，Nature 高并发会返回
  无 `Abs1-content` 的降级页，解析会静默失败（首次全量抓取 0 命中就是这个原因）。
- **OpenAlex 当日免费额度用尽**（`Insufficient budget`），批量 `filter=doi:` 全部失败，
  改用 Semantic Scholar 单条查询 + 429 退避。
- Elsevier 接口返回 200 但没有 `abstract` 字段的，说明条目本身没有摘要（Editorial、
  Corrigendum、Obituary、会议摘要），不是抓取失败；Lancet 与部分在版短文集中在此类。
- 只改分来源 `metadata/<code>/2025/papers.json`；聚合 `metadata/2025/papers.json` 是
  数百 MB 的 LFS 对象，未手工改写，等爬虫侧重建。

## 三、首轮精筛（995 条候选）

候选按来源分 5 组并行判定，共 909 条有摘要的候选：

| 组 | 来源 | 候选 | 纳入 | 排除 |
|---|---|---|---|---|
| a | Comput Electron Agric、Renewable Energy、Comms Earth Env | 167 | 132 | 35 |
| b | CIKM 2025、COLM 2025 | 149 | 33 | 116 |
| c | npj 系与 Nature 系刊 | 246 | 153 | 93 |
| d | MSSP、Acta Mater、CST、TR-E/D、Dev Cell | 95 | 68 | 27 |
| e | Env Int、ES&T、Lancet 系、Science China 系等 | 252 | 126 | 126 |

合计纳入 512、排除 397。补齐摘要后另有 78 条候选补判（纳入 71、排除 7）。

## 四、全量召回（初筛漏检检查）

缺摘要的论文在初筛时只能靠标题判断，必然漏。摘要补齐后用仓库自带 `ai4s_filter.select_ai4s`
对 36 个来源的 20,544 篇重跑一遍，与现有候选比对：

- 规则新命中 **435 条**（未在候选池内），逐条判定后 **补入 338 条、排除 97 条**。
- 集中在 Computers and Electronics in Agriculture（193）、MSSP（86）、Renewable Energy（69）、
  Acta Materialia（28）、TR-E（18）。
- 补入后纳入率 78%，远高于首轮的 56%——说明规则命中的多为标题即含 AI 术语的工程类论文，
  缺摘要时被整体漏掉。

## 五、COLM 2025 复核

COLM 2025 采集 418 篇，初筛给出 52 条候选。这批论文研究对象多为语言模型自身，
按统一口径（与 2024/2026 一致）复核：

- 45 条原有排除项 + 5 条初筛未命中的疑似漏检一并送判，最终 **纳入 10、排除 40**。
- 保留集中在形式数学（Lean 证明、数学推理基准）、科学智能体、科学评测。
- 剔除为通用 LLM 能力研究（架构、训练、解码、压缩、偏好建模、社交仿真）、通用 Agent、
  纯 NLP 与科学计量类。

## 六、官网同口径总量

- 34 个期刊：以 Crossref 存缴登记作**参考数**（ISSN + 出版日 2025-01-01 至 2025-12-31 +
  `type=journal-article`），逐来源写入 `official_total`，并在 `coverage_status` 注明
  「与采集同源，不构成独立核验」——采集本身即按 Crossref 登记口径分页拉取，
  两者相等是必然结果，不等于二次核验。
- CIKM '25：ACM DL 采集 852 条，Crossref 未存缴该论文集，按采集计数记录并注明同源。
- COLM '25：官方论文集 418 条与采集一致，官网无年度目录接口，未做独立二次计数。

## 七、标签

- 931 篇纳入全部有标签，全部命中共享词表 `tag-vocabulary.json`；
  按 `domain` + `task` 为主，必要时补 `method` / `contribution`。

## 八、遗留

1. 全量书目仍有 2,042 篇无摘要，其中绝大多数经接口确认本身无摘要（Editorial、Corrigendum、
   会议摘要、Letter），其余为 Springer 订阅墙与 Nature 降级页。
2. 18 个来源的采集状态原为 `abstract_incomplete`，摘要补齐后同步为 `completed`，
   `with_abstract` 改为实际值，`captured_at` 未动。
3. 参考总数与采集数未做逐 DOI 比对（2025 为在版年，两方时点不同）。
