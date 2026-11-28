# 王梦冉2026候选原摘要补取

输入 main `5ed1b31923ec534eb877cdb0f91895e53ed65847`，48个本人来源，个人台账2233条；2026-11-17缺摘要401条。

本轮补取52条：官网citation-and-abstract BibTeX 47条，Springer正式落地页1条，OpenAlex连续位置原摘要索引3条，Europe PMC原摘要1条。17份官网导出均排除Editorial Board，按DOI和完整题名匹配；原文件、SHA256、卷期URL和逐篇匹配见abstract-recovery.json。

有效缺摘要401→349。所有原字段、决策和标签保留；新增内容精筛0，原始abstract字段仍保持原值，摘要仅放ai4s_review.verified_metadata.abstract。候选总集、源全量和历史快照未修改；总量对账完成状态保留。

全部401条执行Crossref（21批）、OpenAlex（11批）、Europe PMC（21批）查询并保存返回或错误。Crossref其中1批20条返回429，不能据此声称其登记库没有摘要。部分官网正文未能取得：ScienceDirect正常Chrome在Applied Soft Computing第199/198卷及Journal of Hydrology目录返回CPE00002，重试仍失败；第200卷导出未产生完整下载，不计入证据。Semantic Scholar返回429后未连续重试。SCIS MafAFP正式页为Letter且没有Abstract，不以引言替代。搜索结果中的摘要片段不计作完整摘要。

余下349条须官网恢复后继续逐DOI补取或人工提供citation-and-abstract原始导出；没有把访问失败当成无摘要或审核完成。EMNLP另有2702条源缺采不在本轮补摘要范围。

| 来源 | 本轮前缺摘要 | 本轮补得 | 剩余 |
|---|---:|---:|---:|
| Trends in Chemistry | 1 | 0 | 1 |
| Building and Environment | 23 | 0 | 23 |
| Transportation Research Part C Emerging Technologies | 4 | 0 | 4 |
| Sensors and Actuators B Chemical | 23 | 0 | 23 |
| Materials & Design | 2 | 2 | 0 |
| Science China Information Sciences | 2 | 1 | 1 |
| Energy and Buildings | 9 | 0 | 9 |
| Knowledge-Based Systems | 61 | 0 | 61 |
| Applied Soft Computing | 84 | 40 | 44 |
| Artificial Intelligence in Medicine | 1 | 0 | 1 |
| Current Biology | 1 | 1 | 0 |
| Computer Methods in Applied Mechanics and Engineering | 8 | 8 | 0 |
| Engineering Structures | 32 | 0 | 32 |
| Cell Systems | 1 | 0 | 1 |
| Journal of Hydrology | 84 | 0 | 84 |
| Cell Reports Physical Science | 1 | 0 | 1 |
| Agricultural and Forest Meteorology | 2 | 0 | 2 |
| International Journal of Heat and Mass Transfer | 29 | 0 | 29 |
| Information Sciences | 24 | 0 | 24 |
| International Journal of Medical Informatics | 1 | 0 | 1 |
| Computer Physics Communications | 8 | 0 | 8 |

逐条未补齐清单及尝试状态：`abstract-recovery.json` 的 `remaining_records`。已补摘要的内容判读将在独立审核中进行。
