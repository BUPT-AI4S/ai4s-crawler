# 龙兆科 2026 年候选审核与目录对账（2026-11-19）

本轮针对 main 行动清单的 9 个待处理期刊，沿用 2026-11-08T21:38:12.854071+08:00 采集快照。输入 main 为 1397d8b3d12cbb706afcdc0ea72b6ac8da6b97d4，词表与该提交一致，无新增标签。

## 已完成部分

- Machine Tools：ScienceDirect Volume 214–223 目录共53条，逐 PII 对应原52条；补存1条 Editorial Board，核实并纳入1篇热误差建模漏筛论文。保留此前负责人明确排除的原候选决定。
- Computer Science Review：官方 Volume 59–62 共193条，逐 PII 与 DOI 对账；原198条中的5条由出版社 Crossref 元数据证实已调整到2027年 Volume63，单列范围差异；取得3篇原摘要后复核纳入。
- Ecological Indicators、Food Chemistry、Environmental Research、Gastroenterology：当前候选摘要或文献类型证据已补齐，完成 Crossref 替代参考目录逐 DOI 对账。
- ESWA：263条当前候选逐一建档，104条已有原摘要完成模型精筛（72纳入、32排除），159条缺原摘要保留待定。
- JCP：新增13条原摘要补证及纳入判定，其中12条来自出版社页面，1条为 DOI/题名匹配的作者预印本。

## 目录统计口径与范围

出版社目录、文章页直接请求曾返回403，正常浏览器间歇返回CPE00002。负责人确认已完成人机验证，并明确要求“目录请用可靠替代来源核对”。因此，另外7刊使用 Crossref 出版社登记数据；`reference_check` 明确标为参考数，`official_total` 保持空值。

Crossref 以期刊 ISSN、journal-article 类型和2026出版年检索，完整游标分页后按 DOI 对账。每页查询链接、时间、数量及原响应字段保存在 `*-crossref-catalogue.json`。2027年份差异另有逐 DOI 元数据或2027参考目录证据。原始 papers.json 与采集快照全部保留。

本轮精筛范围为当前年度候选及取得原摘要的漏筛补录。目录核对新增的书目保存于各来源 `catalogue-additions.json`，明确标记 `bibliographic_addition_not_ai4s_screened`；不自动作 AI4S 纳入/排除，也不把目录核验宣称为全刊逐篇精筛。最终目录证据及差异分别写入各来源 `catalogue-reconciliation.json`，阶段反馈包含稀疏构建可读取的完整审计。

Gastroenterology 的30条会议摘要以 DOI、170(6)卷期及S页码核实为 DDW® 2026 Abstracts 增刊条目；文献类型依据出版社增刊归属，未声称取得摘要全文。其余来信、勘误与撤稿通知分别保留出版社页面或 PubMed 的类型证据。

## 仍待处理

原9个黄点中6个已满足当前候选批次的完成检查；仍有3刊254条候选缺原摘要或进一步类型证据：Pattern Recognition 76、ESWA 159、JCP 19。逐条清单在 `remaining-tasks.json`。

已尝试出版社直接请求、正常浏览器、OpenAlex（255个 DOI 中返回252条，均无原摘要）、Semantic Scholar（小批量取得1篇；后续查询与一次重试均429）。出版社页面间歇恢复后已补存成功取得的原摘要；不能将访问失败、题名推断或AI生成文字作为原摘要。

`validation.json` 记录原字段保留、候选与审核唯一键、纳入摘要、词表、原始全量数据和负责人既有决定的检查结果。监控由仓库现有工作流生成，未修改监控脚本、工作流或其他负责人的交付。
