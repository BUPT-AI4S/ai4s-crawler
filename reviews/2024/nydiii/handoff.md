# 南耀笛：论文采集复核与AI4S精筛进度

更新：2026-11-09。负责人：南耀笛（nydiii）。本次按主分支 `990d642d8cb137db0db9873f16d4b004079869e5` 的分工、快照、候选文件及反馈规范汇总；提交前复核至 `f6e323c2b8ec728a0d2815546e92f74a4da1f015`，2024/2026相关数据未变，补充新公布的2025分工与快照。仅新增本人阶段反馈和成果归档；已有论文JSON、共享刊会表、原始数据和他人文件不变。

## 大屏入口与提交

- [2024逐来源标准反馈](../feedback/nydiii.json)：51个当前分工来源。
- [2025逐来源标准反馈](../../2025/feedback/nydiii.json)：51个当前分工来源，明确本人尚未开展。
- [2026逐来源标准反馈](../../2026/feedback/nydiii.json)：51个当前分工来源，明确本人尚未开展。
- [结构化进度与候选覆盖](progress.json)：版本、计数、分工变化、历史提交链接。
- [本人逐篇论文交付](../nydiii.json)：远端已存在，SHA256 `61b48b65efca8115f69f308131e9bbb7529690f7b3ef9ee007b8c02f33909c6c`；本次未重写。

## 已完成工作

1. **刊会核验55来源**：50建议纳入、5按当时范围排除，已于11月5日合并。历史行见[原核验记录](history/venue-review-55.json)，现行分工以最新source-assignments为准。
2. **最初537条类型筛查与AI4S精筛**：类型阶段305保留研究候选、230排除、2类型待核；随后按来源范围逐篇判断AI4S，类型筛查数量不能当作最终AI4S数量。两篇待定已补读并更新，详情见history。
3. **综述补审57篇**：46纳入、10排除、1待定；期刊537条最终321纳入、215排除、1待定、0未审。此前脑反馈综述后续纳入，Molecular Plant Spotlight仍排除。
4. **AAAI371条候选**：132纳入、239排除、0待定/未审。与期刊合并后历史交付**908条＝453纳入、454排除、1待定、0未审**。原字段保持，纳入附证据标签和已核查元数据；未核实链接留空。
5. **49刊全量书目核查**：覆盖固定快照25,346条；按逐刊声明口径48刊已核、ACA1刊未完成。42刊一致，3刊确证缺项，3刊存在已解释的目录外记录/登记问题。[精简证据JSON](raw-completeness-2024.json) · [口径说明](raw-completeness-note.txt) · [展示Excel](raw-completeness.xlsx)。卷期年与在线年区分，不能泛称所有刊的首次在线年全集均已独立核完。
6. **16条确认缺项逐项复核**：Nature13、Nature Medicine1、Annals of Oncology2；均为里程碑、简报、研究亮点或勘误，全部排除，0纳入。见[缺项证据](missing-record-recheck.json)与[说明](missing-record-recheck.md)。独立存档，不追加到原908条，不把非研究缺项数说成漏掉16篇研究论文；尚未补入原始元数据。
7. **49刊原生文章类型表**：885条分层规则，逐刊列原标签、含义、处理建议、官方证据和例文。[表与规则](article-types/README.md)。这是已整理的规则，尚未运行过滤或回填未知类型。

## 最新分工与数字口径

2024、2025和2026当前各51来源＝49期刊＋AAAI/BIBM。较原49刊＋AAAI新增BIBM、Engineering Applications of Artificial Intelligence、Neurocomputing；The Lancet转乔徐阳，Progress in Energy and Combustion Science转陈晨。旧记录保留用于交接，不覆盖新负责人数据。

2024当前候选**1,576条**；本人历史交付覆盖其中**885条＝449纳入、435排除、1待定、0未审**。历史文件另23条已不在当前分工，所以908不是当前任务的完成分母。

新分配来源691条尚未进入本人交付：BIBM548、EAAI100、Neurocomputing43。Neurocomputing原负责人已有32条结果（11纳入/21排除），30条匹配当前候选、2条在候选外；当前候选另外13条无该文件同ID结果。需交接后接续，不将他人成果直接记成本人已完成。

## 还需继续做的工作

1. **接续新增3来源**：BIBM548、EAAI100开展精筛；Neurocomputing交接32条旧结果并核查当前13条未被原负责人文件覆盖的候选及候选外2条。
2. **ACA补完22卷**：已核1307–1332共26卷614条，待核1285–1306；原始1106条中的492条尚未取得官网覆盖证据，绝不等同已确认漏爬492条。需要能正常读取目录的网络/访问支持。
3. **AAAI全量与AISI**：核最终正式论文集和第20期/Section覆盖。371候选完成不代表全会议AI4S召回完整。
4. **唯一待定**：FGFR-targeted therapeutics（DOI 10.1038/s41571-024-00869-z）。需合法取得全文AI相关段落再决定；摘要中未来展望不足以确认实质综述贡献。
5. **候选摘要补证与补存**：当前2024候选缺摘要149条，其中本人已审67条（29纳入、38排除）已有证据位置/链接，未补存verified_metadata.abstract；不能当作67条未审。另82条属于新增来源，其中4条Neurocomputing记录已有原负责人审核，交接时复用证据，其余在接续精筛时补证。只统计候选，不要求全量非候选摘要补齐。
6. **历史标签对齐**：现行规范要求中英文标签。历史453篇纳入的1817个标签尚缺label_en；其中当前分工449篇/1804标签。需复用当前共享词表逐项对齐，不靠无证据自动扩充标签。本次不改历史标签。
7. **类型规则接入**：原49刊15,949条unknown/缺失类型尚未回填，规则未执行。团队11月9日已明确接收有实质学术内容的综述，11月8日归档的暂挂标记需按现行政策对齐；不再将“是否要综述”列为尚待老师决策的问题。
8. **2026独立批次**：快照2026-11-08，当前51来源2012候选、410候选缺摘要，本人尚未开展；不得套用2024结果。当前BIBM无候选/采集状态按该年快照记录，不记为本人完成。

9. **2025独立批次**：整理期间新公布分工与快照，提交前已独立核验。当前51来源1,884候选、304候选缺摘要，本人尚未开展；采集器的completed/abstract_incomplete不代表本人审核完成。快照2026-11-09T10:51:18+08:00，已逐来源上报未开展状态。

## 需要协调或帮助

- 新旧负责人就The Lancet、Progress in Energy and Combustion Science、Neurocomputing完成成果交接和冲突归属确认。
- 合法获取唯一待定综述的全文AI相关段落，以及ACA余下22卷可用目录。
- 确认由谁把逐刊类型规则接入采集/过滤流程、修正Science两组错误DOI、补入16条非研究书目缺项。本次提供证据，不修改公共采集代码。
- 2024收尾、新分工来源与2025/2026新批次的优先顺序可由团队统筹；当前状态已分别上报。

## 当前2024逐来源覆盖

“本人未覆盖”是候选键未出现在本人交付，不等于团队完全无人审核；Neurocomputing见上方交接说明。

| 来源编号 | 刊会 | 当前候选 | 候选缺摘要 | 本人已交付 | 本人未覆盖候选 |
|---|---|---:|---:|---:|---:|
| bibm | IEEE International Conference on Bioinformatics and Biomedicine | 548 | 2 | 0 | 548 |
| nrm | Nature Reviews Molecular Cell Biology | 4 | 0 | 4 | 0 |
| nrmicro | Nature Reviews Microbiology | 1 | 0 | 1 | 0 |
| nrclinonc | Nature Reviews Clinical Oncology | 1 | 0 | 1 | 0 |
| nrd | Nature Reviews Drug Discovery | 2 | 0 | 2 | 0 |
| natrevmats | Nature Reviews Materials | 4 | 0 | 4 | 0 |
| j-35fc948b7d | Annals of Oncology | 20 | 17 | 20 | 0 |
| nenergy | Nature Energy | 5 | 0 | 5 | 0 |
| nrc | Nature Reviews Cancer | 4 | 0 | 4 | 0 |
| nrgastro | Nature Reviews Gastroenterology & Hepatology | 3 | 0 | 3 | 0 |
| j-1e4b0859b5 | Cancer Cell | 3 | 1 | 3 | 0 |
| nature | Nature | 122 | 1 | 122 | 0 |
| nrmp | Nature Reviews Methods Primers | 3 | 0 | 3 | 0 |
| nm | Nature Medicine | 34 | 1 | 34 | 0 |
| nrg | Nature Reviews Genetics | 5 | 0 | 5 | 0 |
| natrevchem | Nature Reviews Chemistry | 1 | 0 | 1 | 0 |
| natcatal | Nature Catalysis | 3 | 0 | 3 | 0 |
| j-1dc21a94b1 | Journal of Hematology & Oncology | 1 | 0 | 1 | 0 |
| j-d2d0663714 | Science | 38 | 0 | 38 | 0 |
| natrevphys | Nature Reviews Physics | 7 | 0 | 7 | 0 |
| j-4607bc7c42 | Cell | 16 | 3 | 16 | 0 |
| nbt | Nature Biotechnology | 29 | 0 | 29 | 0 |
| j-9ff3577364 | Progress in Materials Science | 2 | 0 | 2 | 0 |
| natelectron | Nature Electronics | 8 | 0 | 8 | 0 |
| j-e040f3f32c | Molecular Cancer | 5 | 1 | 5 | 0 |
| j-c34b87cb15 | Journal of Hepatology | 15 | 12 | 15 | 0 |
| j-9c7c2ba906 | The Innovation | 15 | 3 | 15 | 0 |
| j-41efefd652 | International Journal of Educational Technology in Higher Education | 2 | 0 | 2 | 0 |
| j-c68f7da396 | Nano-Micro Letters | 11 | 0 | 11 | 0 |
| nphoton | Nature Photonics | 6 | 0 | 6 | 0 |
| nmat | Nature Materials | 4 | 0 | 4 | 0 |
| nnano | Nature Nanotechnology | 5 | 0 | 5 | 0 |
| j-972e72b183 | Joule | 2 | 2 | 2 | 0 |
| j-71921095d2 | The Lancet Respiratory Medicine | 1 | 0 | 1 | 0 |
| j-d921a7e606 | The Lancet Oncology | 3 | 1 | 3 | 0 |
| j-825e995b88 | Progress in Polymer Science | 3 | 1 | 3 | 0 |
| j-0d5068779d | Molecular Plant | 2 | 2 | 2 | 0 |
| natsustain | Nature Sustainability | 7 | 0 | 7 | 0 |
| nature-cr | Cell Research | 4 | 1 | 4 | 0 |
| j-614c0898b2 | BMC Medicine | 16 | 1 | 16 | 0 |
| j-01c665c7a1 | Space Science & Technology | 2 | 0 | 2 | 0 |
| j-472852446c | Analytica Chimica Acta | 4 | 1 | 4 | 0 |
| j-57011f11e4 | Computers & Structures | 6 | 5 | 6 | 0 |
| j-b2a795c62c | Science China Earth Sciences | 18 | 0 | 18 | 0 |
| j-3d69adb6cc | Environmental Modelling & Software | 25 | 9 | 25 | 0 |
| j-0d7b7f9cca | Science China Technological Sciences | 12 | 1 | 12 | 0 |
| j-b86929fb5a | Computational Mechanics | 10 | 4 | 10 | 0 |
| npjsba | npj Systems Biology and Applications | 20 | 0 | 20 | 0 |
| aaai | AAAI Conference on Artificial Intelligence | 371 | 0 | 371 | 0 |
| j-5d396d92fa | Engineering Applications of Artificial Intelligence | 100 | 63 | 0 | 100 |
| j-f26b06f4ee | Neurocomputing | 43 | 17 | 0 | 43 |

## 版本说明

2024采集快照：2026-11-05T10:31:19.144426+08:00；2025采集快照：2026-11-09T10:51:18+08:00；2026采集快照：2026-11-08T21:38:12.854071+08:00。当前候选文件与快照可能更新于不同时点，版本和SHA256均在progress.json记录。

history目录为有日期的历史工作凭据，早期全量摘要统计、旧覆盖限制与旧类型范围不是当前待办口径；以后更新以本说明和标准反馈为准。文章类型计数跨层可重叠，885是规则记录数，不是论文篇数。自动actions由仓库工作流生成，本次不手工编辑；GitHub Pages刷新可能滞后于提交。
