# 当前候选清理（2026-11-09）

按陈晨明确要求，将剩余5条无独立文字摘要、已确认exclude的非研究类型记录移出年度及4个分源ai4s.json候选文件。最新48源当前候选由1471变为1466，候选缺摘要由5变为0。采集快照仍是历史初筛数量，不改写；“候选移出”是精筛后清理，不声称历史初筛从未命中。

全量papers.json保留这5条原始书目，个人审核JSON也保留exclude和证据；最终include集合不含它们。被移出的完整候选对象及对应全量书目哈希保存在`excluded-candidate-removal-20261109.json`。以下旧统计属于相应历史时点。

# 剩余6条摘要的处理（2026-11-09）

按陈晨“把能补的补了，其余的直接不纳入”的要求，从用户提供的正式PDF第1页S56右栏500.29恢复JACC完整会议摘要，补入审核verified_metadata.abstract，并回填年度及分刊ai4s.json。该条因仅为会议补刊摘要继续排除。其余5条无独立文字摘要的评论、观点、社论、勘误、新闻记录已明确排除，保留证据和负责人决定；不把正文或生成文字冒充摘要。

本轮没有改变任何include/exclude判定，历史合计仍为5304条（include 2059、exclude 3245）。当前48源候选缺摘要从6降至5，剩余5条均是已排除记录，不是待审核论文。详情见`remaining-abstract-resolution-20261109.json`与`remaining-abstract-validation-20261109.json`。以下前轮6条缺失清单及验证均为历史快照，以本段及本轮处理清单为最新状态。

# 候选摘要回填（2026-11-09）

按陈晨明确要求，将已核实补回的130条摘要写入`metadata/2024/ai4s.json`的`abstract`，并同步22个已有分刊候选文件中的127条；MM的3条没有对应分源候选文件，仅更新年度汇总。不改变候选成员、顺序、其他字段或审核判定。个人审核JSON及其中原始字段保持不变，补录来源仍保留在verified_metadata。

当前48源的1471条候选缺文字摘要数由136降至6。剩余6条均已排除，不用图形摘要、评论正文或生成文字填充；具体条目与出处见`candidate-abstract-sync-20261109.json`，标准阶段反馈见`../feedback/chenchen052512.json`。这只更新候选摘要字段，不代表全库查漏或原43源全量审核完成；下方早期统计为各自时点的历史记录。

# 当前合并交付（2026-11-08）

负责人陈晨（chenchen052512）。本次按用户授权上传现有工作，主交付`../chenchen052512.json`共5304条：原43源2100条（纳入1594、排除506）与新增8源3204条（纳入465、排除2739）合并；历史合计51源，纳入2059、排除3245、pending 0、unreviewed 0。其中1条为负责人明确决定的暂行纳入。

最新分工48源对应5017条（纳入1793、排除3224）；原Chemical Engineering Journal、JAAD、iScience的287条作为历史成果保留，不混称最新分工。原刊会核验行及他人审核不修改。

**这是现有成果的提交，不代表原43源全年40900条全量审核完成。** 旧快照仍缺22737条文字摘要，3470条定位记录尚未完成摘要审核，二者不能相加。纳入论文仅2条缺文字摘要，均有全文依据。新增8源的38条无完整摘要记录当前均排除，其中2篇正式综述仅有摘要节选，需后续补齐复核；人工势场规划的AI边界也需复查。明确事项在`new-eight/followup-items.json`，不声称已经补验完成。

- `overall-progress.md`与`overall-progress.json`：全部工作及最新分工口径。
- `new-eight/handoff.md`、`new-eight/statistics.json`：新增8源的范围、结果与证据边界。
- `new-eight/abstract-followup.md`：用户补充摘要及1条暂行纳入的依据。
- `new-eight/new-tags.json`：29条新增标签；同步并入共享词表，保留最新远程已有条目。
- `upload-validation.json`：本次合并、原字段保留、去重、标签及摘要统计的验证。
- 原`coverage.json`、`validation.json`、`fulltext-review.json`、`abstract-supplements.json`和`recall-audit.json`仍对应下方历史43源批次，不作为5304条新合计统计。

## 以下为原2100条交付的历史说明

# 陈晨：2024年 AI4S 论文审核与全文补查

当前交付 2100 条：纳入 1594，排除 506。在前一摘要轮2077条的基础上，本轮从103条补查疑点中确认22篇AI4S论文补入；全文轮64篇排除，17篇当时待核实。按用户随后要求，仅依据摘要继续判断，其中16篇排除，最后用户提供生姜论文正式PDF，核实后纳入。当前103条累计纳入23、排除80、待核实0。原交付对象和原始字段全部保留。

**本轮完成的是87篇已取得全文的疑点复核（含用户提供1篇），不是全量论文查全。** 主交付JSON中的候选待定为0；此前1条缺文字摘要疑点已用用户PDF解决；103条结论保留在 `fulltext-review.json`、`recall-audit.json` 和Excel第三表。35个来源的同口径官网全年总量仍未核实。

## 范围与输入

- 负责人陈晨，GitHub chenchen052512，年份2024。
- 按已完成的刊会核验，只处理本人54个来源中保留的43个（41期刊、ICLR、ICML）；11个排除来源未进入精筛。不改他人结果或刊会核验行。
- 输入提交297469ea973ffa3fbc83e1277e8528c83222cf96；快照2026-11-05T10:31:19.144426+08:00。原候选1356条，旧补录13条。
- 已同步远程至 4b5a1a874a4f7a5d2f68647e63e6eb75ea200dbd，共享词表以该提交的73条规范名及定义为先；本次按用户授权提交原分工的2024年补查和标签成果；不纳入新分工8个来源。
- 原论文全部原字段、原值不变；查证后的补充放入 `ai4s_review.verified_metadata`。补录沿用原ID，理由标明“初筛漏筛补录”。

## 本轮全文复核

前轮全量补查待核实103条，实际获得65份PDF、21份出版方存档JATS全文XML，共86篇。PDF核验文件签名、页数和题名；PMLR论文按正式目录OpenReview ID和题名对应。XML按DOI/题名匹配并检查存在正文。Water Research综述取得的是作者接受稿，证据位置按该版本页码；ICML使用正式PMLR公开版本。

每篇根据疑点定向阅读方法、实验、结果和结论，记录实际阅读范围；不声称逐字通读全部证明与附录。完整获取记录在本地“待核实论文全文/核验结果.json”，复核结论与来源哈希在 `fulltext-review.json`。PDF和XML原文件只保存在本地输出目录，不加入仓库。

22篇纳入包含具体生物医学/植物/化学研究、科学参数反演、物理成像方法、工程约束设计及科学评测资源。64篇排除主要因为通用算法的领域演示不足以构成本轮AI4S研究，或实际只有常规统计、规则处理、传统计算及概念展望。这17篇随后按用户要求仅用摘要筛选：14篇按从严纳入口径排除，1篇重试补到GnRH原摘要后排除，1篇查明是更正公告排除；生姜论文索引虽只有Image 1.，现已通过用户下载的正式3页正文核实并纳入。

物理模拟可支持纳入，不统一要求湿实验或实物验证；模拟、回顾性队列和预测毒性不写成实物成功、临床效益或湿实验确认。已有AI工具如果实质支撑科学分析也可纳入，不虚构作者重新训练模型。

一篇Journal of Pharmaceutical Analysis简报（DOI 10.1016/j.jpha.2023.11.007）出版方仅提供图形摘要及Highlights，没有独立文字摘要。已核对简报正文及补充材料§1.7、§3.1的实际ADMETlab预测分析后纳入；verified_metadata.abstract保留null并标注graphical_abstract_only，未拿Highlights或模型生成文字冒充原摘要。

## 历史摘要轮与本轮衔接

前一轮从1369条扩至2077条，新增708条摘要确认漏筛；原纳入中5条按文献类型/研究实质改为排除，保留previous_review。对应JACC 500.29、JAAD 51749、JACC 500.22会议补刊摘要，以及Position: Mission Critical – Satellite Data is a Distinct Modality in Machine Learning、Engineering的Generative AI for Materials Discovery: Design Without Understanding（Views & Comments）。本轮这5条不变。

累计补录744条（旧13 + 摘要轮708 + 全文轮23）；旧补录中有1条现为排除，因此补录总记录数不等于当前纳入补录篇数。主交付纳入1594 = 历史868 + 708 − 5 + 23；主交付排除506。

历史原交付补回175条来源原摘要，并恢复1条CanDo截断摘要。同快照全量40900条原缺摘要28117，前轮按来源/DOI/题名补回5409条，该旧统计中有19条实际为Image 1.图形占位，本次移出可用文字摘要并补回1条GnRH原摘要，上传前另将11条更正/撤稿说明、获奖备注、学科分类或图注移出可用摘要计数，当前真正文字摘要补充5380条，全量仍缺22737条。旧登记5409包含原交付175，不重复相加。本轮另从已读JATS抽取17条真正文字摘要，存入摘要补充文件的独立字段，可能与5409重复，不作为新增篇数累加；Highlights和图形摘要不计文字摘要。

原交付外共5551条定位/补查记录；截至本次实际研究摘要阅读2053条，其中期刊1497、会议556（补1条GnRH摘要，另将1条勘误从摘要阅读改记文种核验）。标题定位未继续阅读摘要的记录明确未审，不伪称已完成摘要排除。本轮只跟进103条历史疑点，未扩大为全部5551条阅读全文。

## 官网目录与覆盖边界

8个来源已匹配目录集合：ICLR 2024正式目录2260条、ICML 2024 PMLR论文集2610条、Nature五刊及Carbon Neutrality。未给无DOI会议论文虚构DOI。

35个来源同口径全年总量仍未知。Archives of Computational Methods in Engineering卷期年与在线年不能直接相减。前轮发现的1668个索引首次上线条目经年份核对未确认为2024卷期漏采；这不证明其他来源完整。未审记录、未补全摘要和官网目录缺口仍需继续处理。

## 标签与元数据

最新远程73条共享词条的规范中英文和定义全部保留。将历史词表与本轮实际需要的概念合并后共 710 条；同义名归并，例如医学图像配准/医学影像配准、进化优化/演化优化、域适应/领域适应、生存预测/生存结局预测。宽窄不同的概念不硬合并。

全部纳入标签均有维度、中英文名、证据位置和理由，并与共享词表一致。排除与待核实记录标签为空。新22条有正式论文集或出版方存档来源，65份PDF的身份已核验；作者顺序、代码/项目/数据链接未逐项全部重核，未查到的值不编造。

## 各来源结果

“补查待核实”与主交付待定分开；“仍缺摘要”为前轮同快照补回后的历史统计。

|来源编号|刊会|交付纳入|交付排除|本轮全文补入|全文实审|补查待核实|仍缺摘要|官网同口径|
|---|---|---:|---:|---:|---:|---:|---:|---|
|j-c7fe39938d|Water Research|89|1|0|1|0|113|待核实：官网同口径总量未知|
|j-ef7cd14dbc|Remote Sensing of Environment|90|2|0|0|0|260|待核实：官网同口径总量未知|
|j-16256b0ce3|Earth-Science Reviews|7|0|0|0|0|187|待核实：官网同口径总量未知|
|j-b9e88c9085|Additive Manufacturing|21|0|0|0|0|481|待核实：官网同口径总量未知|
|j-8143dc670f|Advanced Engineering Informatics|25|0|0|0|0|613|待核实：官网同口径总量未知|
|j-da866ae444|Automation in Construction|40|1|0|0|0|491|待核实：官网同口径总量未知|
|j-c788b13dcd|International Journal of Mechanical Sciences|8|0|0|0|0|864|待核实：官网同口径总量未知|
|j-6097563751|Carbon|5|1|0|0|0|916|待核实：官网同口径总量未知|
|j-8eff360546|Chemical Engineering Journal|46|5|0|0|0|9832|待核实：官网同口径总量未知|
|j-6cf9b89ec2|Journal of Catalysis|3|0|0|0|0|572|待核实：官网同口径总量未知|
|j-31764e1eab|Physics of Life Reviews|1|1|0|0|0|109|待核实：官网同口径总量未知|
|j-0fe19b9e20|Robotics and Autonomous Systems|17|0|0|0|0|141|待核实：官网同口径总量未知|
|j-0cde8a3b99|Robotics and Computer-Integrated Manufacturing|14|0|0|0|0|133|待核实：官网同口径总量未知|
|j-3488061829|Applied Energy|81|14|0|0|0|1720|待核实：官网同口径总量未知|
|j-b4ac12ae95|Energy Conversion and Management|22|2|0|0|0|1043|待核实：官网同口径总量未知|
|j-800d438108|Plant Phenomics|66|0|3|4|0|9|待核实：官网同口径总量未知|
|j-e625b131f8|Agricultural Systems|3|0|0|0|0|288|待核实：官网同口径总量未知|
|npjbiofilms|npj Biofilms and Microbiomes|6|1|0|0|0|9|已核对：目录记录集合匹配|
|npjmgrav|npj Microgravity|4|0|0|0|0|4|已核对：目录记录集合匹配|
|nature-aps|Acta Pharmacologica Sinica|3|1|0|0|0|33|已核对：目录记录集合匹配|
|nature-laban|Lab Animal|1|0|0|0|0|156|已核对：目录记录集合匹配|
|nature-pcan|Prostate Cancer and Prostatic Diseases|1|0|0|0|0|39|已核对：目录记录集合匹配|
|j-283615fb03|Cell Host & Microbe|2|1|0|0|0|3|待核实：官网同口径总量未知|
|j-5514e73d4c|Trends in Genetics|2|0|0|0|0|26|待核实：官网同口径总量未知|
|j-32e2cb1c9f|Molecular Therapy|1|0|0|0|0|65|待核实：官网同口径总量未知|
|j-8f443c7880|EBioMedicine|62|5|0|1|0|22|待核实：官网同口径总量未知|
|j-8838d520aa|EClinicalMedicine|41|2|0|0|0|9|待核实：官网同口径总量未知|
|j-a2f9b41c54|Carbon Neutrality|2|2|0|0|0|0|已核对：目录记录集合匹配|
|j-00a21d67da|Ageing Research Reviews|10|0|0|0|0|14|待核实：官网同口径总量未知|
|j-ca8fb4629a|Cancer Letters|9|0|0|0|0|110|待核实：官网同口径总量未知|
|j-06b16d0494|JACC Cardiovascular Interventions|1|2|0|0|0|654|待核实：官网同口径总量未知|
|j-165d67ba72|Journal of Pharmaceutical Analysis|5|1|2|5|0|63|待核实：官网同口径总量未知|
|j-0f6b15d93b|Journal of the American Academy of Dermatology|0|1|0|0|0|2278|待核实：官网同口径总量未知|
|j-e2678b0db0|Pharmacological Research|6|3|0|0|0|90|待核实：官网同口径总量未知|
|j-d6f749bf6c|Phytomedicine|9|0|0|0|0|33|待核实：官网同口径总量未知|
|j-bdffac0a5c|Biosensors and Bioelectronics|47|1|0|0|0|93|待核实：官网同口径总量未知|
|j-4fc3d65983|Archives of Computational Methods in Engineering|17|1|0|0|0|141|待核实：卷期年与在线发表年尚未对齐|
|j-29686b6ead|Aerospace Science and Technology|15|0|0|0|0|845|待核实：官网同口径总量未知|
|iclr|International Conference on Learning Representations|250|235|0|0|0|0|已核对：目录记录集合匹配|
|icml|International Conference on Machine Learning|298|198|14|64|0|0|已核对：目录记录集合匹配|
|j-be601df25e|Research|23|5|2|3|0|6|待核实：官网同口径总量未知|
|j-4143d04801|Engineering|21|5|0|0|0|115|待核实：官网同口径总量未知|
|j-b6525f43da|iScience|220|15|2|9|0|146|待核实：官网同口径总量未知|

## 交付与检查

- `../chenchen052512.json`：2100条保留原字段的论文对象，纳入1594、排除506。
- `coverage.json`：43来源统计与官网核对边界。
- `fulltext-review.json`：本轮103条结论、此前判断、全文来源/哈希和实际阅读范围，103条均有结论。
- `recall-audit.json`：5551条原定位与补查记录，103条原判断保留并更新当前结论。
- `abstract-supplements.json`：5380条可用来源原摘要、19条单列图形占位、11条单列非摘要说明、既有截断更正及本轮JATS原摘要；独立字段间可能重复，不能相加当新增数。
- `validation.json`：原字段、去重、分工范围、中英文词表和工作簿逐格检查结果。

Excel保留“论文明细”“来源覆盖”“缺摘要抽样”三表，第三表前80条为历史抽样，后103条更新本轮结论，不重复追加另一批103。原历史样本与后103条可能重合，不能用其简单估计漏筛率。本次按仓库要求提交论文JSON、审计记录和共享词表；辅助Excel与原始PDF保留本地。

## 后续摘要判断

按用户要求，余17条不再要求正文补证。15条依据原摘要排除、1条按更正类型排除、1条缺文字摘要待核实；摘要不满足纳入证据标准时从严排除，不表示已经证明全文没有AI。补回的GnRH摘要以DOI和去标记后的题名核对；更正公告保留原题名，只在verified_metadata记录Erratum题名及2022原文DOI。辅助表格与审计记录已同步；本次通过Git提交交付。

## 最后一篇用户PDF核实

已核实生姜论文DOI、正式2024卷期、作者顺序和Short communication类型，读取3页正文及表1。科学任务为中药炮制质量鉴别，使用实测GC-IMS的9个指标成分训练SVM、随机森林、XGBoost等，纳入原创研究并复用既有标签，无新增词条。表1显示SVM-L测试准确率0.9412；验证限随机8:2划分，未读另附补充材料，不声称外部独立验证。该正式简报确无独立文字摘要，保留abstract=null及说明，与另一篇简报合计2条正文补证例外。

当前103条疑点：纳入23、排除80、待核实0；主交付2100条，纳入1594、排除506。全量覆盖仍有缺口；本次提交仅对应原分工，未变更新分工及刊会核验行。
