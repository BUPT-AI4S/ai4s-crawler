# 陈晨：2024年AI4S论文精筛交付

原始候选 1356 条，已逐篇审核；补入经正式来源确认的缺摘要漏筛记录 13 条，共 1369 条。纳入 868，排除 501，待核实 0，未审 0。

范围：43个已通过刊会核验的来源；11个已排除来源未进入论文精筛。输入锁定仓库 297469ea973ffa3fbc83e1277e8528c83222cf96，候选文件SHA-256为 e3cada0c94bfe7482de596b9ac7464860de5bf2635d5cc8375ba7117f728503a。快照时间 2026-11-05T10:31:19.144426+08:00；审核跨2026-11-05至2026-11-06。

交付JSON保留原论文对象全部字段及原值，仅追加 ai4s_review；新增13条来自同一全量快照，属于漏筛补入，并非新发现官网漏采。结论为相关性与文种审核，不是对每篇论文质量的保证。

## 执行口径

- 不再使用AI4S数量或占比剔除来源。沿用已确认的刊会分区和学科决定。
- 保留有明确科学或工程任务且AI发挥实质作用的研究、方法、科学数据及实质性综述。排除管理、经济、社科、人文、新闻社论、仅展望AI，以及缺乏独立领域贡献的通用性能演示。
- 数学保留科学方程、数学研究与形式化定理证明。单纯教材或竞赛数学题准确率评测按本批严口径排除。
- 仿真、回顾性队列、离线蛋白评价均保持证据边界，不写成实验室发现或临床部署。
- 纳入包含3条会议补刊摘要（JACC 2条、JAAD 1条；其中1条综述摘要、2条原创研究摘要），已用conference_abstract单列，不计作完整期刊论文。

## 元数据与链接

原1356条均核对了出版方登记DOI或正式会议记录，并尝试访问论文页及可获得的公开PDF。纳入记录中 421 条具有通过文件头验证的公开直达PDF，其余未验证字段留空。Elsevier中转页HTTP200不算正文可读。未验证的原始链接仍按原值保存，不代表已核实。

多数结论依据完整标题摘要；对会影响判断的疑点定向补读正式全文、方法或实验，位置写在每条审核对象。训练阶段只在直接证据支持时填写。

## 官网覆盖及初筛风险

同快照43来源共采集40900条，28117条缺摘要；原候选1356条中170条缺摘要，已按证据补核或列待定。8个来源的官网目录记录集合已匹配，35个仍未核实同口径全年总量。

ICLR 2024官方目录2260条、ICML 2024正式PMLR目录2610条，与快照集合匹配；LaTeX/Unicode题名差异以稳定OpenReview标识对齐。Nature五刊及Carbon Neutrality目录集合亦已匹配。Archives of Computational Methods in Engineering的卷期年目录与在线发表年快照尚未对齐，不能直接把162对176的差值解释为漏采。其他官网访问受限的来源未用Crossref计数冒充官方总量。

每期刊从缺摘要且未命中的记录序列三分位抽取最多2条，共80条。抽查确证13条漏筛，48条排除，19条证据不足；这是定点抽样，不能外推全量漏筛率。期刊全量初筛应在补齐摘要后重跑；本交付完成了指定候选批次，不宣称完成全量文献覆盖。

## 用户补充PDF及JAAD浏览器摘要后的8条复核（2026-11-06）

按用户要求，能取得PDF的定向读原文，其余依据实际取得的摘要。用户随后打开了JAAD 51749正式页，已读到完整摘要并补判纳入。原8条待定最终改为6条纳入、2条排除、0条待核实。两份用户PDF原件未改动，已记录文件名、读取页码和SHA-256。

|原候选序号（从1计）|论文|本轮结论|依据与限制|
|---:|---|---|---|
|65|Comprehensive gridded dataset of photosynthetically active radiation in the upper ocean from 1958 to 2022|不建议纳入|摘要明确最终海洋PAR数据由ESM及DINEOF重建，GRNN只用于对比。另核对ESM原始方法：以邻近已知环境串作距离加权估计，属于插值型生态统计重建；按本批严口径，不将这一重建流程及神经网络比较项视为实质AI贡献，因此排除。这不表示数据集质量差。 依据完整摘要及公开的ESM原始方法核对，未阅读本篇付费全文；采用本批保守的AI4S边界。|
|99|Development of a novel machine learning-based approach for brain function assessment and integrated software solution|建议纳入|完整摘要明确采集EEG与fNIRS，使用GCN融合神经电活动和血流动力学信息，并加入Granger因果及脑区邻接特征，比较运动想象任务的识别表现。AI实质处理神经生理信号，支持脑功能及康复研究，纳入。 按出版方摘要及贡献段判定；未核验全文实验细节，不将平台设想写成临床部署。|
|159|Sustainable management and valorization of antibiotic waste|不建议纳入|用户提供的正式PDF第16页第9节把VOSviewer和Bibliometrix称为机器学习工具，实际处理的是314篇文献的词云与共现图（第17页Fig.5—6），并非用AI预测、设计或优化抗生素废物处理过程。主体为废物资源化及可持续性综述，缺乏实质AI4S方法内容，排除。 定向阅读全文中与AI判定有关的章节和图示，未声称逐字通读全部23页。|
|180|Applicability analysis of transformer to wind speed forecasting by a novel deep learning framework with multiple atmospheric variables|建议纳入|作者机构完整摘要说明用VMD分解多气象变量、GNN提取变量依赖，再以Transformer等时序网络预测风速；另比较MLP、LSTM及GRU，结果GRU优于Transformer。AI直接预测风速物理量，属于气象及能源工程任务，纳入。 按作者机构提供的完整摘要判定，未阅读付费全文；未将题名中的Transformer写成最优模型。|
|251|A multidisciplinary approach to select wind turbines for power-hydrogen production: Energy, exergy, economic, environmental under uncertainty prediction by artificial intelligence|建议纳入|出版方完整摘要和Highlights明确：对八种风机的风电制氢系统作能量、㶲、经济与环境评价，AI预测系统性能，蒙特卡洛另用于项目成功概率及经济风险分析。科学工程对象及AI性能预测作用已有摘要直接支持，按本次允许摘要判定的要求纳入；不因附带经济评价排除。 摘要未披露AI具体架构、逐项预测目标及训练验证细节，方法仅标人工智能预测。所谓3000年是计算场景，不能理解为实测或真实长期预报；本次只判相关性。|
|339|500.29 Artificial Intelligence Based Optical Coherence Tomography Comparison of Plaque Characteristics and DNA Repair Activity in Patients with CAD|建议纳入|用户PDF第1页右栏500.29完整摘要：49名DECODE受试者使用OCTplus AI软件定量钙化、脂质、纤维等斑块成分，并与38人可用的DNA连接酶活性检测比较。AI实质提供冠心病机制研究的影像测量，纳入并单列会议摘要。组间差异未达显著，钙化趋势p=0.053，不能写成已证实关联。 采用现成AI软件；未声明新训练网络或临床部署。PDF文件名对应同页另一篇摘要，已按正文500.29及题名核实。|
|341|51749 Deep ensemble learning with demographic data may out-perform deep learning in skin lesion classification on demographic data|建议纳入|用户打开的JAAD正式页现可读完整摘要：以HAM10000的7771个病灶及PAD-UFES-20的127个病灶构建分类数据，训练人口学风险模型，再将最佳梯度提升模型的风险输出加入CNN。AI直接区分黑色素瘤与良性黑素细胞痣，属于实质医学诊断研究，纳入并单列会议补刊摘要。 页面明确ABSTRACT ONLY，属于会议补刊摘要而非完整期刊论文。使用两公开数据集；作者承认仅3个人口学变量且泛化限于所用数据。只按摘要判相关性，不据此认定临床有效性，也不套用题名不同的2023年论文。|
|366|Nonlinear elastic wave dispersions of solar cells strengthened by advanced functionally graded materials via both mathematical modeling and deep neural networks technique|建议纳入|出版方推荐文献区中题名完全匹配的摘要说明：解析求解3D功能梯度钙钛矿太阳能电池非线性PDE，生成相速度数据供DNN训练、测试与验证，再用DNN预测非线性相速度及其参数敏感性。属于用AI代理模型研究材料力学波传播，纳入；证据限于数值仿真。 本篇独立页面访问受限，摘要从出版方其他文章页内的推荐文献模块取得，按对应完整题名定位，未把页面主文摘要当成本篇，也未阅读付费全文或验证实物器件。|

## 待核实记录

|来源|论文|缺口|
|---|---|---|
|本批候选|无|指定批次待核实记录已清零；官网覆盖及全量缺摘要风险仍另列。|

## 各来源核验

|来源编号|刊会|全量|缺摘要|原候选|补入|纳入|排除|待定|官网状态|
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
|j-c7fe39938d|Water Research|1573|1221|19|1|19|1|0|待核实：官网同口径总量未知|
|j-ef7cd14dbc|Remote Sensing of Environment|495|277|66|2|66|2|0|待核实：官网同口径总量未知|
|j-16256b0ce3|Earth-Science Reviews|282|190|4|0|4|0|0|待核实：官网同口径总量未知|
|j-b9e88c9085|Additive Manufacturing|666|481|7|0|7|0|0|待核实：官网同口径总量未知|
|j-8143dc670f|Advanced Engineering Informatics|668|623|11|2|13|0|0|待核实：官网同口径总量未知|
|j-da866ae444|Automation in Construction|639|494|6|0|5|1|0|待核实：官网同口径总量未知|
|j-c788b13dcd|International Journal of Mechanical Sciences|918|871|7|0|7|0|0|待核实：官网同口径总量未知|
|j-6097563751|Carbon|1043|920|5|0|4|1|0|待核实：官网同口径总量未知|
|j-8eff360546|Chemical Engineering Journal|10671|9858|44|0|39|5|0|待核实：官网同口径总量未知|
|j-6cf9b89ec2|Journal of Catalysis|588|575|3|0|3|0|0|待核实：官网同口径总量未知|
|j-31764e1eab|Physics of Life Reviews|147|126|1|0|0|1|0|待核实：官网同口径总量未知|
|j-0fe19b9e20|Robotics and Autonomous Systems|199|141|2|0|2|0|0|待核实：官网同口径总量未知|
|j-0cde8a3b99|Robotics and Computer-Integrated Manufacturing|170|135|2|1|3|0|0|待核实：官网同口径总量未知|
|j-3488061829|Applied Energy|2124|1759|67|1|54|14|0|待核实：官网同口径总量未知|
|j-b4ac12ae95|Energy Conversion and Management|1237|1052|13|1|12|2|0|待核实：官网同口径总量未知|
|j-800d438108|Plant Phenomics|92|92|1|1|2|0|0|待核实：官网同口径总量未知|
|j-e625b131f8|Agricultural Systems|294|294|3|0|3|0|0|待核实：官网同口径总量未知|
|npjbiofilms|npj Biofilms and Microbiomes|158|9|6|0|5|1|0|已核对：目录记录集合匹配|
|npjmgrav|npj Microgravity|115|4|2|0|2|0|0|已核对：目录记录集合匹配|
|nature-aps|Acta Pharmacologica Sinica|232|212|2|0|1|1|0|已核对：目录记录集合匹配|
|nature-laban|Lab Animal|186|168|1|0|1|0|0|已核对：目录记录集合匹配|
|nature-pcan|Prostate Cancer and Prostatic Diseases|156|111|1|0|1|0|0|已核对：目录记录集合匹配|
|j-283615fb03|Cell Host & Microbe|217|183|1|0|0|1|0|待核实：官网同口径总量未知|
|j-5514e73d4c|Trends in Genetics|135|100|1|0|1|0|0|待核实：官网同口径总量未知|
|j-32e2cb1c9f|Molecular Therapy|391|111|1|0|1|0|0|待核实：官网同口径总量未知|
|j-8f443c7880|EBioMedicine|572|78|39|1|35|5|0|待核实：官网同口径总量未知|
|j-8838d520aa|EClinicalMedicine|615|23|16|0|14|2|0|待核实：官网同口径总量未知|
|j-a2f9b41c54|Carbon Neutrality|39|0|3|0|1|2|0|已核对：目录记录集合匹配|
|j-00a21d67da|Ageing Research Reviews|382|300|1|0|1|0|0|待核实：官网同口径总量未知|
|j-ca8fb4629a|Cancer Letters|637|503|3|0|3|0|0|待核实：官网同口径总量未知|
|j-06b16d0494|JACC Cardiovascular Interventions|761|724|1|1|2|0|0|待核实：官网同口径总量未知|
|j-165d67ba72|Journal of Pharmaceutical Analysis|175|175|1|0|0|1|0|待核实：官网同口径总量未知|
|j-0f6b15d93b|Journal of the American Academy of Dermatology|2517|2278|1|0|1|0|0|待核实：官网同口径总量未知|
|j-e2678b0db0|Pharmacological Research|510|176|6|0|3|3|0|待核实：官网同口径总量未知|
|j-d6f749bf6c|Phytomedicine|1095|957|2|0|2|0|0|待核实：官网同口径总量未知|
|j-bdffac0a5c|Biosensors and Bioelectronics|814|769|4|0|3|1|0|待核实：官网同口径总量未知|
|j-4fc3d65983|Archives of Computational Methods in Engineering|176|148|10|1|10|1|0|待核实：卷期年与在线发表年尚未对齐|
|j-29686b6ead|Aerospace Science and Technology|885|856|12|0|12|0|0|待核实：官网同口径总量未知|
|iclr|International Conference on Learning Representations|2260|0|424|0|189|235|0|已核对：目录记录集合匹配|
|icml|International Conference on Machine Learning|2610|0|420|0|223|197|0|已核对：目录记录集合匹配|
|j-be601df25e|Research|269|8|15|0|10|5|0|待核实：官网同口径总量未知|
|j-4143d04801|Engineering|294|119|13|1|10|4|0|待核实：官网同口径总量未知|
|j-b6525f43da|iScience|2893|996|109|0|94|15|0|待核实：官网同口径总量未知|

## 仓库交付文件

- [论文审核 JSON](../chenchen052512.json)：1369条论文对象数组，保留原字段；每条新增 `ai4s_review`。
- [覆盖与摘要核验](coverage.json)：43个来源的官网核对状态、全量和候选缺摘要统计，以及80条缺摘要未命中记录的抽查证据。13条确证漏筛已补入论文JSON；19条抽样证据不足的记录仍保留未知，不计入本批候选待定数。
- [校验记录](validation.json)：原字段保留、唯一键、判定及标签、来源分工、Excel一致性与文件哈希检查。

负责人：陈晨（chenchen052512）。仅交付本人2024候选批次；Excel及用户下载的PDF保留本地。官网同口径总量未核实的35个来源，以及全量缺摘要导致的漏筛风险仍需后续补证，不声明全年全量审核完成。
