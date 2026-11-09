# 王婉婷｜AI4S 论文复核、漏筛补录与新增刊源审计阶段总结

负责人：王婉婷（GitHub：Blueblue1101）  
论文年份：2024；统计截至本地成果 2026 年 11 月 8 日  
核对版本：main `af22785`；输入快照：2026-11-05 10:31（北京时间）

## 一、当前进度

**1,574 条初筛候选已全部复核；目前累计形成 23,503 条审核记录，纳入 2,624 篇。全量漏筛检查尚未完成，此前成果已上传，本轮增量随本次提交。** 本报告仅统计王婉婷的成果，不混入此前龙兆科的工作量。

| 指标 | 结果 |
|---|---|
| 工作范围 | 52个来源、30,468条原始记录 |
| 累计已审 | 23,503条（约77.1%） |
| 累计判定 | 纳入2,624篇；排除19,549条（主要因无AI实质参与、仅研究通用AI模型或常规业务应用，或属于评论、社论、勘误等非研究文种及不属本批年份/轨道的记录）；待定1330条 |
| 初筛候选复核 | 1,574条全部处理：纳入1,151、排除314条（虽命中初筛关键词，但摘要显示仅研究通用AI模型、缺少具体科学/工程任务，或仅用传统算法与物理模拟；另有少量观点评论等非研究内容）、待定109 |
| 原有个人记录复核 | 1,383条全部复核，129条判定调整 |
| 从未命中关键词记录中确认漏筛并纳入 | 累计1,473篇 |
| 补齐并核验完整摘要 | 累计2,225条 |
| 官网确认的新增漏采论文 | 目前0篇；不表示所有来源均无漏采 |
| 仍未审 | 6,965条全量文章，并非6,965篇AI4S候选 |

这里的“已审”包含摘要判定、文献类型排除和证据不足的待定记录。按审核依据，21,066条归入摘要语义判断，2,122条归入文献类型判断，315条仅能完成缺失或错误摘要核查。**不能把23,503条都表述为“已读完完整摘要”。**

## 二、复核与精筛方法

1. **锁定范围并去重。** 使用新清单49个来源，加上原有成果中的3个历史来源；以`(venue, year, id)`识别记录，保留已完成成果，继续未审部分。
2. **先筛文种，再判断AI4S相关性。** 只考虑原创研究、正式会议研究论文和实质综述。评论、社论、新闻、宣传、勘误、撤稿通知、会议摘要等排除。来源质量合格并不代表整刊论文都纳入。
3. **只根据摘要作语义判断。** 同时检查“研究什么科学/工程问题”“AI实际做了什么”“二者关系是否明确”。通用模型基准、常规业务应用、传统仿真或仅提AI愿景不能自动纳入。证据不足列待定，未读取正文。
4. **查漏筛、补摘要。** 对全量记录与初筛候选作差集；关键词仅用于调整阅读顺序，不代替纳入/排除判断。缺摘要尝试从正式来源、Europe PMC、OpenAIRE及已保存仓库元数据补齐，并核对DOI、题名和内容。
5. **修复“有字段但没摘要”的情况。** 检查致谢、作者贡献、审稿修改说明、补充材料介绍、截断片段和错配摘要。能找到同篇完整摘要则补回；找不到的保留问题状态，不计为完整摘要补齐。
6. **按最新词表打标签。** 纳入论文按领域、任务、方法等有证据的维度选择中英文规范标签；其余状态标签为空。先查已有标签及同义词，再提出新词项。
7. **并行审核后统一校验。** 此前三个子代理分源处理；本轮由主模型批量处理，统一检查边界案例、元数据和标签。保留原始论文字段，只更新`ai4s_review`；既有成果不重复计量。

依据：[仓库精筛规则](https://github.com/BUPT-AI4S/ai4s-crawler/blob/af2278581bc87fa599cf971680c9ced8624c3c1c/skills/ai4s-paper-review/references/review-rules.md)。

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
| CVPR | 2716 | 2716 | 391 | 2220 | 105 | 0 | 0 |
| Advances in Applied Energy | 41 | 40 | 11 | 26 | 3 | 1 | 40 |
| The Lancet Healthy Longevity | 145 | 114 | 1 | 72 | 41 | 31 | 26 |
| The Lancet Haematology | 206 | 74 | 0 | 70 | 4 | 132 | 54 |
| Pharmacological Reviews | 65 | 43 | 0 | 42 | 1 | 22 | 42 |
| Seminars in Cancer Biology | 53 | 39 | 0 | 39 | 0 | 14 | 39 |
| Trends in Cognitive Sciences | 152 | 114 | 9 | 85 | 20 | 38 | 101 |
| Trends in Endocrinology and Metabolism | 140 | 108 | 1 | 107 | 0 | 32 | 88 |
| Trends in Microbiology | 179 | 143 | 1 | 137 | 5 | 36 | 98 |
| Trends in Molecular Medicine | 156 | 114 | 1 | 111 | 2 | 42 | 85 |
| Science Immunology | 171 | 162 | 0 | 134 | 28 | 9 | 0 |
| **合计** | 4024 | 3667 | 415 | 3043 | 209 | 357 | 573 |

## 四、新开展审计的方法与结果

| 审计事项 | 使用方法 | 当前结果与边界 |
|---|---|---|
| 来源资格 | 复用并核对main刊会清单、ISSN、分区、正式出版及文种依据 | 52个范围内来源登记为建议纳入；新增11源的评级和局限见上表 |
| 官网漏采 | 按年份与正式轨道比对年总量，再核DOI或题名成员 | 12个Nature系列来源、CVPR及ECAI已完成相应成员比对；已核验范围未确认具体漏采；其余不能宣称补漏完成 |
| 关键词漏筛 | 全量与候选作差集，批量读取摘要并逐条保存语义判定 | 累计补入1,473篇；是已采集论文中的漏筛，不是新爬1,473篇 |
| 摘要补录与真实性 | DOI/题名匹配后检查完整性，剔除致谢、修订说明及错配文本 | 累计2,225条完整摘要核验补齐；自动API返回数不直接计为完成量 |
| 文献类型 | 依据出版方类型及明确书目说明排除非研究条目 | 2,122条审核以文献类型为主要依据，其中900条为明确类型的程序化排除 |
| 元数据链接 | 检查失效或验证页链接，区分原值保留与重新核验 | 累计撤销605条异常PDF核验记录；此前批次曾核实21个作者给出的公开代码/项目链接，本轮另有7个作者声明的代码／项目链接通过HEAD端点检查；尚未逐条重新核完所有纳入论文的DOI/PDF/代码 |
| 标签规范 | 对照最新中英文词表和别名，逐条校验标签与证据 | 共享词表771项＋本轮新增6项＝777项；新增词项随所属批次提交 |
| 跨审核人重复 | 按来源、年份和ID对照其他个人JSON | 发现890条同键重合，其中46条判定不同；本轮新增3,170条与他人文件同键重合为0；未覆盖他人结果 |
| 交付完整性 | 检查唯一键、原字段、候选覆盖、标签、总量闭合及压缩包校验和 | 校验通过；23,503已审＋6,965未审＝30,468；本轮交付随本次提交 |

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

在已完成20,333条的基础上，最近一轮又完成3,170条，新增漏筛纳入90篇、补齐完整摘要513条：

| 处理组 | 本轮已审 | 纳入 | 排除 | 待定 |
|---|---|---|---|---|
| CVPR / ECAI | 352 | 58 | 265 | 29 |
| Nature Communications | 515 | 8 | 497 | 10 |
| Nature Communications（系统组） | 323 | 2 | 307 | 14 |
| Nature Communications（补查） | 465 | 4 | 445 | 16 |
| 材料、能源及工程刊源 | 419 | 5 | 406 | 8 |
| 生物医学刊源 | 1096 | 13 | 1021 | 62 |
| **合计** | 3170 | 90 | 2941 | 139 |

这轮不是重做此前记录；已完成结果与本轮新增按唯一键去重。原有判定均保留。本轮由主模型批量读取摘要、逐条保存语义判定，并重点复核可能纳入项和抽查排除项，已保存实际完成的结果和断点，未把计划量计入完成量。

本轮3170条：纳入90篇；排除2941条（45条明确非研究文种、2896条摘要未显示AI4S实质关系）；待定139条（19条摘要问题、120条关系或类型证据不足）。补齐513条完整摘要。排除记录抽查30条；详见本轮批量续审汇报。

## 五、标签更新

已统一“梯度提升树”到现有“梯度提升”；“支持向量机”复用最新共享词表中的条目。累计贡献29个词项；本轮新增6项，均按现有词表查重后追加：

| 中文标签 | 英文标签 | 适用范围 |
|---|---|---|
| 食品来源鉴别 | Food provenance authentication | 使用AI分析食品组成、光谱或其他测量特征，鉴别其地理产地、生产方式或饲养/原料来源。 |
| 主成分分析 | Principal component analysis | 通过正交线性投影提取最大方差方向，用于科学观测的降维、结构识别或特征表示。 |
| 非负矩阵分解 | Non-negative matrix factorization | 将非负观测分解为非负因子，用于信号解混、潜在组分发现或科学数据表示。 |
| 水下图像增强 | Underwater image enhancement | 针对水下光传播造成的色偏、散射和对比度退化，增强水下图像或视频的可用质量。 |
| 野生动物识别 | Wildlife identification | 从自然环境观测或航空影像中检测、定位并识别野生动物物种，支持种群调查和生态保护。 |
| 量子态性质学习 | Quantum state property learning | 由量子测量样本学习量子态参数或可观测量期望值，包括基态和热态性质；不要求学习算法在量子硬件上运行。 |
| 独立成分分析 | Independent component analysis | 将多变量观测分解为统计独立成分，用于生物信号或科学数据结构识别。 |
| 降维 | Dimensionality reduction | 从高维科学数据提取低维结构或表示，适用于未明确具体算法的降维贡献。 |
| 建筑属性制图 | Building attribute mapping | 利用遥感及地面观测推断建筑属性并生成空间分布图。 |
| 视觉注视轨迹预测 | Visual scanpath prediction | 根据个体和任务信息预测人类视觉注视位置及其序列。 |
| 高精道路地图构建 | High-definition road map construction | 从传感数据构建车道、道路边界等矢量化高精度地图。 |
| 交通参与者轨迹预测 | Traffic participant trajectory prediction | 预测车辆、行人等道路交通参与者的未来运动轨迹。 |
| 微震声发射源定位 | Microseismic and acoustic emission source localization | 从监测信号估计微震或声发射事件空间位置，服务岩土工程及结构安全监测。 |
| 细胞图像批次校正 | Cell image batch correction | 校正细胞成像表型数据跨批次、设备或实验室的系统性差异。 |
| 手物接触估计 | Hand-object contact estimation | 从观测数据重建手与物体的抓握接触区域，服务操作测量与接触行为研究。 |
| 储备池计算 | Reservoir computing | 利用动态储备池将输入转换为丰富的状态表示，并训练读出层完成时序预测或识别。 |
| 医疗操作技能评估 | Medical procedure skill assessment | 从操作过程观测识别医疗操作错误或评价技能质量。 |
| 考古器物使用痕迹分析 | Archaeological artifact use-wear analysis | 根据器物表面显微磨损等证据推断考古器物的使用方式及加工材料。 |
| 科研概念网络分析 | Scientific concept network analysis | 从科学文献提取概念并分析概念网络结构、演化及其与知识创新的关系。 |
| 文化遗产视觉阐释 | Visual interpretation of cultural heritage | 结合文化遗产图像和语义知识生成或评估辅助理解的视觉解释。 |
| 在线仇恨网络分析 | Online hate network analysis | 利用在线文本与交互网络分析仇恨言论的群体、传播结构及社会情境。 |
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

- **继续精筛：** 全量尚余6,965条，其中6,965条仍缺可用摘要，已有摘要／待核描述队列已处理完成。
- **补证与核对：** 1330条待定需补完整摘要、明确AI方法或确认文种；46条跨审核人判定差异需在汇总时协调；未核完的来源目录和论文链接继续保留审计状态。
- **上传状态：** 此前成果已上传，本轮增量随本次提交；已有摘要队列已处理完成。
- **恢复方式：** 后续仅补充缺摘要、待定证据和未完成的官网核验；已有摘要队列无剩余，不重复审核。

本地个人交付文件：[Blueblue1101.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101.json)。统计与续审依据：[summary.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/summary.json)、[validation.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/validation.json)、[coverage.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/coverage.json)、[continuation-checkpoint.json](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation-checkpoint.json)。

## 七、漏筛纳入的具体论文（节选）

累计1,473篇漏筛纳入论文来自45个来源，均未进入原初筛候选。已按DOI及同来源规范化题名检查，与原候选没有重复。这是已采集论文中的漏筛补录，不是新增爬取数量；仅部分论文能进一步确认具体漏判原因。

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

其余论文的题名、来源、标签、DOI/论文页和摘要判定依据，见[全部1,473篇漏筛纳入详细清单](王婉婷_AI4S漏筛纳入详细清单.md)。

## 附录：全部52个来源的累计结果

“漏筛纳入”是纳入论文的子集；“补摘要”是元数据工作量，不能与已审或纳入相加。

| 来源 | 全量 | 纳入 | 排除 | 待定 | 未审 | 漏筛纳入 | 补摘要 |
|---|---|---|---|---|---|---|---|
| Nature Communications | 10926 | 778 | 9654 | 494 | 0 | 294 | 3 |
| CVPR | 2716 | 391 | 2220 | 105 | 0 | 300 | 0 |
| Nano Energy | 1248 | 15 | 137 | 4 | 1092 | 9 | 84 |
| Applied Catalysis B Environment and Energy | 1198 | 3 | 120 | 4 | 1071 | 1 | 68 |
| Renewable and Sustainable Energy Reviews | 864 | 35 | 261 | 27 | 541 | 25 | 118 |
| ISBI | 800 | 648 | 96 | 56 | 0 | 363 | 0 |
| Energy Storage Materials | 798 | 14 | 103 | 9 | 672 | 1 | 15 |
| Journal of Materials Science & Technology | 790 | 1 | 49 | 0 | 740 | 0 | 47 |
| Journal of Energy Chemistry | 687 | 14 | 53 | 3 | 617 | 2 | 47 |
| ECAI | 675 | 127 | 502 | 46 | 0 | 93 | 1 |
| Clinical Gastroenterology and Hepatology | 527 | 14 | 190 | 60 | 263 | 12 | 140 |
| Information Fusion | 522 | 45 | 77 | 17 | 383 | 40 | 135 |
| Trends in Food Science & Technology | 462 | 4 | 97 | 26 | 335 | 2 | 44 |
| Molecular Cell | 418 | 8 | 381 | 9 | 20 | 7 | 177 |
| Nature Physics | 418 | 4 | 412 | 2 | 0 | 2 | 0 |
| Artificial Intelligence Review | 414 | 111 | 198 | 16 | 89 | 75 | 22 |
| npj Digital Medicine | 385 | 172 | 185 | 28 | 0 | 124 | 0 |
| Matter | 364 | 13 | 64 | 3 | 284 | 5 | 52 |
| Neuron | 346 | 11 | 311 | 19 | 5 | 7 | 232 |
| Nature Ecology & Evolution | 342 | 3 | 329 | 10 | 0 | 2 | 0 |
| The Lancet Regional Health - Europe | 333 | 5 | 225 | 59 | 44 | 4 | 11 |
| Nature Microbiology | 329 | 6 | 315 | 8 | 0 | 2 | 0 |
| Nature Neuroscience | 313 | 20 | 264 | 28 | 1 | 11 | 0 |
| Chem | 309 | 2 | 89 | 8 | 210 | 1 | 44 |
| Science Translational Medicine | 303 | 15 | 250 | 19 | 19 | 6 | 0 |
| Nature Human Behaviour | 300 | 21 | 262 | 17 | 0 | 9 | 0 |
| Nature Chemical Biology | 290 | 6 | 271 | 13 | 0 | 0 | 0 |
| Nature Geoscience | 257 | 9 | 247 | 1 | 0 | 3 | 0 |
| Journal of Advanced Research | 218 | 12 | 183 | 9 | 14 | 10 | 203 |
| The Lancet Haematology | 206 | 0 | 70 | 4 | 132 | 0 | 54 |
| Trends in Biotechnology | 179 | 2 | 139 | 3 | 35 | 1 | 119 |
| The Lancet Planetary Health | 179 | 4 | 124 | 37 | 14 | 3 | 0 |
| Trends in Microbiology | 179 | 1 | 137 | 5 | 36 | 1 | 98 |
| Science Immunology | 171 | 0 | 134 | 28 | 9 | 0 | 0 |
| Trends in Ecology & Evolution | 171 | 1 | 134 | 4 | 32 | 1 | 0 |
| Nature Computational Science | 167 | 36 | 120 | 11 | 0 | 6 | 0 |
| Nature Protocols | 165 | 9 | 148 | 8 | 0 | 4 | 0 |
| Trends in Molecular Medicine | 156 | 1 | 111 | 2 | 42 | 1 | 85 |
| Trends in Cognitive Sciences | 152 | 9 | 85 | 20 | 38 | 9 | 101 |
| The Lancet Healthy Longevity | 145 | 1 | 72 | 41 | 31 | 1 | 26 |
| Trends in Endocrinology and Metabolism | 140 | 1 | 107 | 0 | 32 | 1 | 88 |
| Trends in Neurosciences | 128 | 2 | 100 | 2 | 24 | 2 | 78 |
| International Journal of Mining Science and Technology | 126 | 9 | 104 | 0 | 13 | 6 | 0 |
| Cell Discovery | 126 | 7 | 77 | 34 | 8 | 2 | 1 |
| Molecular Neurodegeneration | 100 | 1 | 80 | 5 | 14 | 0 | 0 |
| eTransportation | 80 | 5 | 5 | 2 | 68 | 2 | 11 |
| npj Science of Learning | 80 | 5 | 66 | 9 | 0 | 2 | 0 |
| Pharmacological Reviews | 65 | 0 | 42 | 1 | 22 | 0 | 42 |
| Smart Learning Environments | 64 | 7 | 49 | 8 | 0 | 7 | 0 |
| Seminars in Cancer Biology | 53 | 0 | 39 | 0 | 14 | 0 | 39 |
| PhotoniX | 43 | 5 | 35 | 3 | 0 | 4 | 0 |
| Advances in Applied Energy | 41 | 11 | 26 | 3 | 1 | 10 | 40 |
| **合计** | 30468 | 2624 | 19549（无AI实质参与、通用AI/常规业务应用、非研究文种或不属本批范围） | 1330 | 6965 | 1473 | 2225 |
