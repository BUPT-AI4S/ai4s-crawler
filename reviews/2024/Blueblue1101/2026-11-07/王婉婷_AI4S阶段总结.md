# 王婉婷｜AI4S 论文复核、漏筛补录与新增刊源审计阶段总结

负责人：王婉婷（GitHub：Blueblue1101）  
论文年份：2024；统计截至本地成果 2026 年 11 月 8 日  
核对版本：main `6de707f`；输入快照：2026-11-05 10:31（北京时间）

## 一、当前进度

**1,574 条初筛候选已全部复核；目前累计形成 11,933 条审核记录，纳入 2,365 篇。全量漏筛检查尚未完成，此前成果已上传，本轮增量随本次提交。** 本报告仅统计王婉婷的成果，不混入此前龙兆科的工作量。

| 指标 | 结果 |
|---|---|
| 工作范围 | 52个来源、30,468条原始记录 |
| 累计已审 | 11,933条（约39.2%） |
| 累计判定 | 纳入2,365篇；排除8,834条（主要因无AI实质参与、仅研究通用AI模型或常规业务应用，或属于评论、社论、勘误等非研究文种及不属本批年份/轨道的记录）；待定734条 |
| 初筛候选复核 | 1,574条全部处理：纳入1,151、排除314条（虽命中初筛关键词，但摘要显示仅研究通用AI模型、缺少具体科学/工程任务，或仅用传统算法与物理模拟；另有少量观点评论等非研究内容）、待定109 |
| 原有个人记录复核 | 1,383条全部复核，129条判定调整 |
| 从未命中关键词记录中确认漏筛并纳入 | 累计1,214篇 |
| 补齐并核验完整摘要 | 累计1,384条 |
| 官网确认的新增漏采论文 | 目前0篇；不表示所有来源均无漏采 |
| 仍未审 | 18,535条全量文章，并非18,535篇AI4S候选 |

这里的“已审”包含摘要判定、文献类型排除和证据不足的待定记录。按审核依据，9,612条归入摘要语义判断，2,046条归入文献类型判断，275条仅能完成缺失或错误摘要核查。**不能把11,933条都表述为“已读完完整摘要”。**

## 二、复核与精筛方法

1. **锁定范围并去重。** 使用新清单49个来源，加上原有成果中的3个历史来源；以`(venue, year, id)`识别记录，保留已完成成果，继续未审部分。
2. **先筛文种，再判断AI4S相关性。** 只考虑原创研究、正式会议研究论文和实质综述。评论、社论、新闻、宣传、勘误、撤稿通知、会议摘要等排除。来源质量合格并不代表整刊论文都纳入。
3. **只根据摘要作语义判断。** 同时检查“研究什么科学/工程问题”“AI实际做了什么”“二者关系是否明确”。通用模型基准、常规业务应用、传统仿真或仅提AI愿景不能自动纳入。证据不足列待定，未读取正文。
4. **查漏筛、补摘要。** 对全量记录与初筛候选作差集；关键词仅用于调整阅读顺序，不代替纳入/排除判断。缺摘要尝试从正式来源、Europe PMC、OpenAIRE及已保存仓库元数据补齐，并核对DOI、题名和内容。
5. **修复“有字段但没摘要”的情况。** 检查致谢、作者贡献、审稿修改说明、补充材料介绍、截断片段和错配摘要。能找到同篇完整摘要则补回；找不到的保留问题状态，不计为完整摘要补齐。
6. **按最新词表打标签。** 纳入论文按领域、任务、方法等有证据的维度选择中英文规范标签；其余状态标签为空。先查已有标签及同义词，再提出新词项。
7. **并行审核后统一校验。** 此前三个子代理分源处理；本轮由主模型批量处理，统一检查边界案例、元数据和标签。保留原始论文字段，只更新`ai4s_review`；既有成果不重复计量。

依据：[仓库精筛规则](https://github.com/BUPT-AI4S/ai4s-crawler/blob/6de707f7668f96506f0c58f27d9cccf642e5d5b3/skills/ai4s-paper-review/references/review-rules.md)。

### 原有1,383条记录的复核结果

| 状态 | 复核前 | 复核后 |
|---|---|---|
| 纳入 | 1026 | 1059 |
| 排除 | 241 | 237 |
| 待定 | 116 | 87 |

共调整129条判定，体现了补证后的纳入、排除及保守待定：

| 判定调整 | 篇数 |
|---|---|
| 排除 → 纳入 | 19 |
| 排除 → 待定 | 4 |
| 纳入 → 排除 | 13 |
| 纳入 → 待定 | 30 |
| 待定 → 排除 | 6 |
| 待定 → 纳入 | 57 |

## 三、新清单中新出现的刊源及水平

新清单49个来源中，38个与原有实际审核的41个来源重合，重合比例约77.6%；其余为**10本期刊和1个会议**。“新出现”指此前没有王婉婷的个人审核记录，**不等于仓库此前没有爬取**。

以下水平和建议复用仓库已保存的刊会核验记录，并非本报告重新独立认证。期刊采用**2025版中科院分区**，CVPR采用**CCF 2026年第七版**；均不冒称为2024年同期评级。10本期刊中9本一区、1本二区，仓库均登记“建议纳入”。

| 新增来源 | 来源编码 | 已记录水平 | 来源结论 | 本批文献处理 |
|---|---|---|---|---|
| [CVPR](https://www.ccf.org.cn/Academic_Evaluation/By_category/2026-03-31/870181.shtml) | cvpr | CCF A（2026年第七版） | 建议纳入 | 主会正式研究论文；Workshop、比赛及非研究条目另行排除 |
| [Advances in Applied Energy](https://api.crossref.org/journals/2666-7924) | j-5be82edc26 | 工程技术 1区 | 建议纳入 | 原创研究和实质综述逐篇审核；评论、社论等排除 |
| [The Lancet Healthy Longevity](https://www.thelancet.com/journals/lanhl/home) | j-1c0b582639 | 医学 1区 | 建议纳入 | 原创研究和实质综述逐篇审核；评论、社论等排除 |
| [The Lancet Haematology](https://www.thelancet.com/journals/lanhae/home) | j-b65bc153a0 | 医学 1区 | 建议纳入 | 原创研究和实质综述逐篇审核；评论、社论等排除 |
| [Pharmacological Reviews](https://api.crossref.org/journals/0031-6997) | j-6f25cc9655 | 医学 1区 | 建议纳入 | 综述为主；仅保留有实质AI4S内容的综述 |
| [Seminars in Cancer Biology](https://api.crossref.org/journals/1044-579X) | j-c2843d80b8 | 医学 2区 | 建议纳入 | 综述为主；仅保留有实质AI4S内容的综述 |
| [Trends in Cognitive Sciences](https://www.cell.com/trends/cognitive-sciences/home) | j-d562500035 | 心理学 1区 | 建议纳入 | 综述为主；仅保留有实质AI4S内容的综述 |
| [Trends in Endocrinology and Metabolism](https://www.cell.com/trends/endocrinology-metabolism/home) | j-216eba8f80 | 医学 1区 | 建议纳入 | 综述为主；仅保留有实质AI4S内容的综述 |
| [Trends in Microbiology](https://www.cell.com/trends/microbiology/home) | j-f457cf101a | 生物学 1区 | 建议纳入 | 综述为主；仅保留有实质AI4S内容的综述 |
| [Trends in Molecular Medicine](https://www.cell.com/trends/molecular-medicine/home) | j-72172ba21c | 医学 1区 | 建议纳入 | 综述为主；仅保留有实质AI4S内容的综述 |
| [Science Immunology](https://www.science.org/journal/sciimmunol) | j-3d73a601f6 | 医学 1区 | 建议纳入 | 原创研究和实质综述逐篇审核；评论、社论等排除 |

质量依据及局限：期刊按ISSN对照公开的2025分区表，并结合出版方信息及正式出版记录核验；综述刊作为综述来源使用。大多数JCR分区、具体盲审形式和完整编委名单未独立核实，因此本表不补写未经核实的影响因子或JCR等级。Advances in Applied Energy的专属审稿政策仍待补证。CVPR和Advances in Applied Energy在仓库分别登记于丁利军、乔徐阳名下，本次按用户清单补查，未改负责人登记。

依据：[source-quality-audit.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/source-quality-audit.json)；[分区公开材料入口](https://cce.ncepu.edu.cn/xzzx/yjsjx1/7632005045644e61a0d12c7bbeff6204.htm)。

### 11个新增来源的实际审核进度

表中“纳入”包含其初筛候选及后续漏筛补录；“补摘要”可包含最终排除的论文，不等于纳入篇数。所有数量均来自本地累计交付。

| 来源 | 原采集 | 已审 | 纳入 | 排除 | 待定 | 未审 | 补齐完整摘要 |
|---|---|---|---|---|---|---|---|
| CVPR | 2716 | 1748 | 254 | 1437 | 57 | 968 | 0 |
| Advances in Applied Energy | 41 | 40 | 11 | 26 | 3 | 1 | 40 |
| The Lancet Healthy Longevity | 145 | 114 | 1 | 72 | 41 | 31 | 26 |
| The Lancet Haematology | 206 | 4 | 0 | 1 | 3 | 202 | 0 |
| Pharmacological Reviews | 65 | 43 | 0 | 42 | 1 | 22 | 42 |
| Seminars in Cancer Biology | 53 | 5 | 0 | 5 | 0 | 48 | 5 |
| Trends in Cognitive Sciences | 152 | 108 | 9 | 82 | 17 | 44 | 96 |
| Trends in Endocrinology and Metabolism | 140 | 108 | 1 | 107 | 0 | 32 | 88 |
| Trends in Microbiology | 179 | 108 | 1 | 103 | 4 | 71 | 65 |
| Trends in Molecular Medicine | 156 | 114 | 1 | 111 | 2 | 42 | 85 |
| Science Immunology | 171 | 162 | 0 | 134 | 28 | 9 | 0 |
| **合计** | 4024 | 2554 | 278 | 2120 | 156 | 1470 | 447 |

## 四、新开展审计的方法与结果

| 审计事项 | 使用方法 | 当前结果与边界 |
|---|---|---|
| 来源资格 | 复用并核对main刊会清单、ISSN、分区、正式出版及文种依据 | 52个范围内来源登记为建议纳入；新增11源的评级和局限见上表 |
| 官网漏采 | 按年份与正式轨道比对年总量，再核DOI或题名成员 | 12个Nature系列来源、CVPR及ECAI已完成相应成员比对；已核验范围未确认具体漏采；其余不能宣称补漏完成 |
| 关键词漏筛 | 全量与候选作差集，批量读取摘要并逐条保存语义判定 | 累计补入1,214篇；是已采集论文中的漏筛，不是新爬1,214篇 |
| 摘要补录与真实性 | DOI/题名匹配后检查完整性，剔除致谢、修订说明及错配文本 | 累计1,384条完整摘要核验补齐；自动API返回数不直接计为完成量 |
| 文献类型 | 依据出版方类型及明确书目说明排除非研究条目 | 2,046条审核以文献类型为主要依据，其中900条为明确类型的程序化排除 |
| 元数据链接 | 检查失效或验证页链接，区分原值保留与重新核验 | 累计撤销605条异常PDF核验记录；上一轮另核实21个作者给出的公开代码/项目链接；尚未逐条重新核完所有纳入论文的DOI/PDF/代码 |
| 标签规范 | 对照最新中英文词表和别名，逐条校验标签与证据 | 共享词表757项（含此前累计贡献9项，本轮无新词项）；累计新增项此前已上传，本轮无新词项 |
| 跨审核人重复 | 按来源、年份和ID对照其他个人JSON | 发现890条同键重合，其中46条判定不同；本轮新增400条与他人文件同键重合为0；未覆盖他人结果 |
| 交付完整性 | 检查唯一键、原字段、候选覆盖、标签、总量闭合及压缩包校验和 | 校验通过；11,933已审＋18,535未审＝30,468；本轮交付随本次提交 |

### 官网与论文集核验明细

以下统计包含各来源范围内的多种文种，不能把官网条目数直接当成AI4S论文数。ECAI特别区分正式研究轨道、其他轨道及年份；ISBI区分出版社登记核验与官网完整目录核验。

| 来源 | 本地采集条目 | 官方/登记口径 | 结果 |
|---|---|---|---|
| Nature Computational Science | 167 | 167 | 逐条目录比对；未发现已核实漏项 |
| Nature Ecology & Evolution | 342 | 342 | 逐条目录比对；未发现已核实漏项 |
| Nature Human Behaviour | 300 | 300 | 逐条目录比对；未发现已核实漏项 |
| Cell Discovery | 126 | 126 | 逐条目录比对；未发现已核实漏项 |
| Nature Chemical Biology | 290 | 290 | 逐条目录比对；未发现已核实漏项 |
| Nature Neuroscience | 313 | 313 | 逐条目录比对；未发现已核实漏项 |
| Nature Geoscience | 257 | 257 | 逐条目录比对；未发现已核实漏项 |
| Nature Microbiology | 329 | 329 | 逐条目录比对；未发现已核实漏项 |
| Nature Physics | 418 | 418 | 逐条目录比对；未发现已核实漏项 |
| npj Digital Medicine | 385 | 385 | 逐条目录比对；未发现已核实漏项 |
| npj Science of Learning | 80 | 80 | 逐条目录比对；未发现已核实漏项 |
| Nature Protocols | 165 | 165 | 逐条目录比对；未发现已核实漏项 |
| CVPR | 2716 | 2716 | 主会正式论文题名逐条匹配 2,716 条；未发现已核实漏项 |
| ECAI | 675 | 579（主轨544＋PAIS 35） | 579篇正式研究均匹配；675条原采集含不同年份/轨道等，不能直接相减当漏采 |
| Nature Communications | 10926 | 10926 | 年总量一致；仅逐条核对41页、820条，尚未核完整成员 |
| ISBI | 800 | 官方总量未独立确认 | 出版社Crossref登记的800篇研究DOI全部匹配；官网程序题名774条匹配、26条变体待核 |

12个完成目录比对的Nature系列来源合计3,172条。Nature Communications虽年总量一致，仍只核了部分目录成员，不能据总数相同推断完全无漏项。访问受限的来源按效率优先要求暂缓。依据：[official-directory-audit.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/official-directory-audit.json)。

### 最近一轮续审结果

在已完成11,533条的基础上，最近一轮又完成400条，新增漏筛纳入5篇、补齐完整摘要91条：

| 处理组 | 本轮已审 | 纳入 | 排除 | 待定 |
|---|---|---|---|---|
| Nature Communications（系统组） | 52 | 0 | 49 | 3 |
| Nature Communications（补查） | 63 | 0 | 62 | 1 |
| 材料、能源及工程刊源 | 35 | 0 | 34 | 1 |
| 生物医学刊源 | 123 | 0 | 102 | 21 |
| CVPR / ECAI | 42 | 4 | 37 | 1 |
| Nature Communications | 85 | 1 | 80 | 4 |
| **合计** | 400 | 5 | 364 | 31 |

这轮不是重做此前记录；已完成结果与本轮新增按唯一键去重。原有判定均保留。本轮由主模型批量读取摘要、逐条保存语义判定，并重点复核可能纳入项和抽查排除项，已保存实际完成的结果和断点，未把计划量计入完成量。

本轮400条：纳入5篇；排除364条（5条明确非研究文种、359条摘要未显示AI4S实质关系）；待定31条（12条摘要问题、19条关系或类型证据不足）。补齐91条完整摘要。排除记录抽查20条；详见本轮批量续审汇报。

## 五、标签更新

已统一“梯度提升树”到现有“梯度提升”；“支持向量机”复用最新共享词表中的条目。累计贡献9个词项；本轮新增0项，均按现有词表查重后追加：

| 中文标签 | 英文标签 | 适用范围 |
|---|---|---|
| 食品来源鉴别 | Food provenance authentication | 使用AI分析食品组成、光谱或其他测量特征，鉴别其地理产地、生产方式或饲养/原料来源。 |
| 栖息地制图 | Habitat mapping | 利用AI从影像、传感或空间环境数据识别、分类和量化栖息地及其结构特征，并生成用于生态与保护研究的空间分布图。 |
| 能源基础设施选址 | Energy infrastructure siting | 在供能、可达性或环境约束下，确定充电站、加氢站、抽水蓄能电站等能源基础设施的位置及空间布局。 |
| 地基承载力预测 | Foundation bearing capacity prediction | 根据土体、地基几何及荷载条件预测地基承载能力，支持岩土工程设计与安全评估。 |
| 模糊推理 | Fuzzy inference | 通过模糊集合、规则与隶属度推理实现具有不确定性的预测或决策；单纯提及模糊性不足以使用本标签。 |
| 飞行燃油消耗预测 | Flight fuel consumption prediction | 根据航路、天气、机型或运行信息预测航班燃油消耗，支持航空能耗与排放评估及优化。 |
| DNA甲基化预测 | DNA methylation prediction | 利用学习或概率推断模型，从序列、片段组学或其他观测预测DNA甲基化状态或水平。 |
| 视觉同步定位与建图 | Visual simultaneous localization and mapping | 利用视觉数据与学习模型联合估计相机轨迹并构建或对齐物理环境地图。 |
| 自动驾驶场景重建 | Autonomous driving scene reconstruction | 从车辆传感数据重建道路环境与动态对象的三维场景，用于自动驾驶工程研究中的场景表示或视图合成。 |

标签均与对应纳入论文一起保存在本地JSON中。依据：[tag-additions.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/tag-additions.json)。

## 六、未完成事项与交付状态

- **继续精筛：** 全量尚余18,535条，其中6,965条仍缺可用摘要，11,570条已有摘要或待核描述但尚未完成审核。
- **补证与核对：** 734条待定需补完整摘要、明确AI方法或确认文种；46条跨审核人判定差异需在汇总时协调；未核完的来源目录和论文链接继续保留审计状态。
- **上传状态：** 此前成果已上传，本轮增量随本次提交；并行精筛仍受使用额度限制，主模型已恢复处理并保存断点。
- **恢复方式：** 从已保存断点过滤已审唯一键后续做；上传前再同步main及共享词表，不重跑覆盖已有成果。

本地个人交付文件：[Blueblue1101.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101.json)。统计与续审依据：[summary.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/summary.json)、[validation.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/validation.json)、[coverage.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/coverage.json)、[continuation-checkpoint.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation-checkpoint.json)。

## 七、漏筛纳入的具体论文（节选）

累计1,214篇漏筛纳入论文来自45个来源，均未进入原初筛候选。已按DOI及同来源规范化题名检查，与原候选没有重复。这是已采集论文中的漏筛补录，不是新增爬取数量；仅部分论文能进一步确认具体漏判原因。

| 方向 | 论文原题名／链接 | 来源 | 为什么纳入 |
|---|---|---|---|
| 材料发现 | [Synthesizability of materials stoichiometry using semi-supervised learning](https://doi.org/10.1016/j.matt.2024.05.002) | Matter | 半监督学习预测材料可合成性，指导实验发现新的无机材料相。 |
| 电池健康 | [State of health estimation for battery modules with parallel-connected cells under cell-to-cell variations](https://doi.org/10.1016/j.etran.2024.100346) | eTransportation | 特征选择＋相关向量回归估计并联电池模块健康状态；原摘要字段误存审稿修改说明，已修复。 |
| 综合能源 | [Probabilistic load forecasting for integrated energy systems using attentive quantile regression temporal convolutional network](https://doi.org/10.1016/j.adapen.2024.100165) | Advances in Applied Energy | 注意力与时序卷积网络联合预测电、热、冷负荷及不确定性。 |
| 遥感监测 | [COMIC: An unsupervised change detection method for heterogeneous remote sensing images based on copula mixtures and Cycle-Consistent Adversarial Networks](https://doi.org/10.1016/j.inffus.2024.102240) | Information Fusion | 用CycleGAN和统计建模检测异构遥感影像中的地表变化。 |
| 单细胞生物学 | [Semi-supervised integration of single-cell transcriptomics data](https://doi.org/10.1038/s41467-024-45240-z) | Nature Communications | 半监督整合单细胞转录组，校正批次差异并保留生物变异。 |
| 肿瘤生物学 | [Glioblastoma functional heterogeneity and enrichment of cancer stem cells with tumor recurrence](https://doi.org/10.1016/j.neuron.2024.10.012) | Neuron | 无监督单细胞分析识别胶质母细胞瘤状态，并与复发演化实验联系。 |
| 生态保护 | [Unlocking ground-based imagery for habitat mapping](https://doi.org/10.1016/j.tree.2023.11.005) | Trends in Ecology & Evolution | 利用地面影像与计算机视觉进行栖息地制图和物种分布预测。 |
| 疾病量化 | [TULIP: Multi-camera 3D Precision Assessment of Parkinson's Disease](https://openaccess.thecvf.com/content/CVPR2024/html/Kim_TULIP_Multi-camera_3D_Precision_Assessment_of_Parkinsons_Disease_CVPR_2024_paper.html) | CVPR | 机器学习从三维姿态预测帕金森运动症状评分。 |

其余论文的题名、来源、标签、DOI/论文页和摘要判定依据，见[全部1,214篇漏筛纳入详细清单](王婉婷_AI4S漏筛纳入详细清单.md)。

## 附录：全部52个来源的累计结果

“漏筛纳入”是纳入论文的子集；“补摘要”是元数据工作量，不能与已审或纳入相加。

| 来源 | 全量 | 纳入 | 排除 | 待定 | 未审 | 漏筛纳入 | 补摘要 |
|---|---|---|---|---|---|---|---|
| Nature Communications | 10926 | 691 | 2611 | 109 | 7515 | 207 | 3 |
| CVPR | 2716 | 254 | 1437 | 57 | 968 | 163 | 0 |
| Nano Energy | 1248 | 14 | 7 | 1 | 1226 | 8 | 15 |
| Applied Catalysis B Environment and Energy | 1198 | 3 | 120 | 4 | 1071 | 1 | 68 |
| Renewable and Sustainable Energy Reviews | 864 | 35 | 261 | 27 | 541 | 25 | 118 |
| ISBI | 800 | 648 | 96 | 56 | 0 | 363 | 0 |
| Energy Storage Materials | 798 | 14 | 5 | 8 | 771 | 1 | 12 |
| Journal of Materials Science & Technology | 790 | 1 | 2 | 0 | 787 | 0 | 2 |
| Journal of Energy Chemistry | 687 | 14 | 1 | 3 | 669 | 2 | 15 |
| ECAI | 675 | 127 | 502 | 46 | 0 | 93 | 1 |
| Clinical Gastroenterology and Hepatology | 527 | 10 | 19 | 38 | 460 | 8 | 14 |
| Information Fusion | 522 | 40 | 51 | 11 | 420 | 35 | 98 |
| Trends in Food Science & Technology | 462 | 4 | 5 | 18 | 435 | 2 | 5 |
| Molecular Cell | 418 | 8 | 122 | 4 | 284 | 7 | 30 |
| Nature Physics | 418 | 3 | 214 | 1 | 200 | 1 | 0 |
| Artificial Intelligence Review | 414 | 111 | 198 | 16 | 89 | 75 | 22 |
| npj Digital Medicine | 385 | 172 | 185 | 28 | 0 | 124 | 0 |
| Matter | 364 | 13 | 64 | 3 | 284 | 5 | 52 |
| Neuron | 346 | 11 | 311 | 19 | 5 | 7 | 232 |
| Nature Ecology & Evolution | 342 | 2 | 167 | 1 | 172 | 1 | 0 |
| The Lancet Regional Health - Europe | 333 | 3 | 56 | 51 | 223 | 2 | 1 |
| Nature Microbiology | 329 | 5 | 114 | 1 | 209 | 1 | 0 |
| Nature Neuroscience | 313 | 14 | 171 | 15 | 113 | 5 | 0 |
| Chem | 309 | 2 | 38 | 5 | 264 | 1 | 15 |
| Science Translational Medicine | 303 | 15 | 250 | 19 | 19 | 6 | 0 |
| Nature Human Behaviour | 300 | 15 | 149 | 5 | 131 | 3 | 0 |
| Nature Chemical Biology | 290 | 6 | 147 | 1 | 136 | 0 | 0 |
| Nature Geoscience | 257 | 8 | 114 | 0 | 135 | 2 | 0 |
| Journal of Advanced Research | 218 | 11 | 15 | 1 | 191 | 9 | 26 |
| The Lancet Haematology | 206 | 0 | 1 | 3 | 202 | 0 | 0 |
| Trends in Biotechnology | 179 | 2 | 139 | 3 | 35 | 1 | 119 |
| The Lancet Planetary Health | 179 | 2 | 19 | 35 | 123 | 1 | 0 |
| Trends in Microbiology | 179 | 1 | 103 | 4 | 71 | 1 | 65 |
| Science Immunology | 171 | 0 | 134 | 28 | 9 | 0 | 0 |
| Trends in Ecology & Evolution | 171 | 1 | 134 | 4 | 32 | 1 | 0 |
| Nature Computational Science | 167 | 36 | 120 | 11 | 0 | 6 | 0 |
| Nature Protocols | 165 | 7 | 28 | 0 | 130 | 2 | 0 |
| Trends in Molecular Medicine | 156 | 1 | 111 | 2 | 42 | 1 | 85 |
| Trends in Cognitive Sciences | 152 | 9 | 82 | 17 | 44 | 9 | 96 |
| The Lancet Healthy Longevity | 145 | 1 | 72 | 41 | 31 | 1 | 26 |
| Trends in Endocrinology and Metabolism | 140 | 1 | 107 | 0 | 32 | 1 | 88 |
| Trends in Neurosciences | 128 | 2 | 100 | 2 | 24 | 2 | 78 |
| International Journal of Mining Science and Technology | 126 | 8 | 7 | 0 | 111 | 5 | 0 |
| Cell Discovery | 126 | 6 | 11 | 15 | 94 | 1 | 0 |
| Molecular Neurodegeneration | 100 | 1 | 42 | 2 | 55 | 0 | 0 |
| eTransportation | 80 | 5 | 5 | 2 | 68 | 2 | 11 |
| npj Science of Learning | 80 | 5 | 66 | 9 | 0 | 2 | 0 |
| Pharmacological Reviews | 65 | 0 | 42 | 1 | 22 | 0 | 42 |
| Smart Learning Environments | 64 | 7 | 13 | 1 | 43 | 7 | 0 |
| Seminars in Cancer Biology | 53 | 0 | 5 | 0 | 48 | 0 | 5 |
| PhotoniX | 43 | 5 | 35 | 3 | 0 | 4 | 0 |
| Advances in Applied Energy | 41 | 11 | 26 | 3 | 1 | 10 | 40 |
| **合计** | 30468 | 2365 | 8834（无AI实质参与、通用AI/常规业务应用、非研究文种或不属本批范围） | 734 | 18535 | 1214 | 1384 |
