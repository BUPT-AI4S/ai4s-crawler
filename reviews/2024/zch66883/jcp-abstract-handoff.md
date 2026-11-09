# JCP 2024 年摘要补录交接

2026 年 11 月 9 日，朱长昊（`zch66883`）完成 BUPT-AI4S 2024 批次中 *Journal of Cleaner Production*（JCP，来源代码 `j-76f25ed87e`）的待定摘要处理。

## 本批结果

| 处置 | 条数 |
| --- | ---: |
| 从 Web of Science 补录原摘要 | 3,302 |
| 按文献类型无需摘要 | 5 |
| 用户确认无需补摘要 | 5 |
| 待补 | 0 |
| 原待定清单合计 | 3,312 |

无需补摘要的文献包括 3 条出版商通知、1 条评论和 1 条编辑说明。另 5 条研究或综述在 Web of Science 导出的摘要字段为空，朱长昊确认本批无需继续补录。两类处置分别记录在[结项对账表](jcp-abstract-remaining.csv)的 `final_disposition` 列，原始缺口原因也保留在 `reason` 列。

## 摘要获取步骤

1. 从[北邮 CARSI 资源入口](https://idp.bupt.edu.cn/idp/)进入 Web of Science，用北邮统一身份认证登录。在检索页选择 **Web of Science Core Collection**。
2. 在 **Advanced Search → Query Builder** 的查询框输入 `SO=(Journal of Cleaner Production) AND PY=(2024)`，当次返回 4,738 条。先选 **Export → Excel → Full Record** 导出首页 50 条，检查文件确实含 DOI 和 Abstract 两列。试导样本只用于验证。
3. 朱长昊在同一结果页选择 **Records from**，按 1–1000、1001–2000、2001–3000、3001–4000、4001–4738 分五批导出 **Full Record**，将五份 `.xls` 交给 Codex。各批实际为 1,000、1,000、1,000、1,000、738 条，合计 4,738 个不同的 Web of Science 记录号。试导样本未计入。
4. 在本地读取五份导出文件。从[期刊分诊表](venue-type-triage.csv)筛出 JCP 2024 年的 3,312 条 `pending`，对照该刊[采集书目](../../../metadata/j-76f25ed87e/2024/papers.json)、[既有精筛 JSON](../zch66883.json)和[历史摘要补录](abstract-backfill-20261107.csv)，以规范化 DOI 匹配导出记录，再核对题名。归属年份采用项目书目口径，实际补入的 3,302 条在导出中的出版年也均为 2024。DOI 尾部年份可能早于正式出版年。
5. 对 DOI `10.1016/j.jclepro.2024.143735` 单独核对。导出题名重复了一段，DOI、三位作者和文章号 143735 一致，因此采用其摘要。每条摘要保留 Web of Science 原文和含唯一记录号的出处链接。导出、匹配和回填均可用本地脚本完成，摘要正文无需逐条交给模型。

## 文件和后续合并

[摘要补录表](jcp-abstract-backfill.csv)沿用六列格式 `source_code,year,id,doi,abstract_source_url,abstract`。合并时按 `(source_code, year, id)` 对齐原书目，用 DOI 交叉核对。摘要记录共 3,302 条，合并键无重复。

本次提交包含摘要补录、结项处置及本交接。新补的摘要可供后续 AI4S 精筛。项目中的原始书目、分诊表和既有精筛决定作为对账基线保留。
