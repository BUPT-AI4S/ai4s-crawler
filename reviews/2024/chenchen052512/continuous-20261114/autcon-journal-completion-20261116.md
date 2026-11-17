# Automation in Construction 2024整刊筛查

全刊639条已逐条筛查；本轮新增550条：254纳入、261排除、35待补证。累计294纳入、310排除、35待补证，0未筛选。既有89条判定及原始字段保持。

## 官网与参考对账

官网第157—168卷全部13个目录已核，168卷包含A、B两部分。538条研究、86条综述、13条编委名单、2条更正，共639条，与快照同文种口径。文章编号和PII均639个唯一值；全部集合指纹、逐卷归属与Crossref的639个DOI一致，未见漏采或额外记录。

[官网年度目录](https://www.sciencedirect.com/journal/automation-in-construction/issues) · [Crossref可复现查询](https://api.crossref.org/journals/0926-5805/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31&rows=1000)。

## 阅读范围

新增550条独立语义筛查，535条非通知记录已核原作者摘要的相关句段，其中107篇另读完整摘要。10篇补读可见引言/方法节选，1篇另读开放方法正文；非535篇完整摘要或全文通读。图形摘要与原作者文本摘要已区分。

补证后5篇从本轮初步待定转为纳入：105227（YOLOv8m）、105337（预训练检测引导扫描）、105327（ANN/CNN人体方向和活动）、105356（训练姿态分类器）、105389（YOLOv8工序感知）。这些不是对既有89条的更正。

随后在105429正文补核遇到CPE00002，部分其他论文仅提供机构/购买权限下的节选。全年官网目录对账已在此之前完成；35条剩余疑点均已有原摘要，缺的是具体AI实现或AI与工程研究贡献关系，不记作缺摘要。沿用会话中负责人当前不能人工核验的说明，没有新增人工核验。

输入年候选与来源候选均6条，缺输入摘要均0；保留原候选文件。新发现纳入与待定另记；不以全量非候选缺摘要统计冒充候选指标。

## 待补证清单

| DOI | 论文 | 缺证 |
|---|---|---|
|10.1016/j.autcon.2023.105196|Human-robot collaboration for modular construction manufacturing: Review of academic research|综述78篇模块化制造人机协作，摘要未明确所综述AI方法及其工程任务关系，需正文确认。|
|10.1016/j.autcon.2023.105235|Unsupervised video object segmentation for enhanced SLAM-based localization in dynamic construction environments|原摘要已读，物体掩码与运动显著性融合改善SLAM；尚需方法确认掩码生成及传播是否实际使用AI模型。|
|10.1016/j.autcon.2024.105287|Mixed reality-based active Hazard prevention system for heavy machinery operators|原摘要已读，混合现实监测眼头手行为预防机械风险，但分类器与AI实现不明，需查方法。|
|10.1016/j.autcon.2024.105291|Autonomous view planning methods for 3D scanning|原摘要已读，自动视角规划综述未明确AI方法与工程任务覆盖，需核正文方法分类。|
|10.1016/j.autcon.2024.105307|Measuring and identifying pre-service fatigue due to hypoxic exposure|原摘要报告缺氧认知实验与EEG疲劳识别，但未说明识别模型，需确认AI步骤。|
|10.1016/j.autcon.2024.105326|Enhancing digital twin efficiency in indoor environments: Virtual sensor-driven optimization of physical sensor combinations|原摘要已读，虚拟传感器性能驱动传感器组合选择，但预测模型与AI算法未说明，需补方法。|
|10.1016/j.autcon.2024.105344|Review of simultaneous localization and mapping (SLAM) for construction robotics applications|原摘要已读，为施工SLAM综述与评测，但未明确AI方法占实质贡献，需核算法清单。|
|10.1016/j.autcon.2024.105429|Tower crane safety technologies: A synthesis of academic research and industry insights|原摘要已读，塔吊监测、防撞与稳定性技术综述未明确AI方法覆盖，需正文确认。|
|10.1016/j.autcon.2024.105472|Stereoscopic monitoring of transportation infrastructure|原摘要已读，多平台交通基础设施监测综述未明确AI方法的实质覆盖，需核正文。|
|10.1016/j.autcon.2024.105480|Applications and challenges of digital twin intelligent sensing technologies for asphalt pavements|原摘要已读，沥青路面数字孪生智能传感综述，尚缺AI方法与监测任务对应关系。|
|10.1016/j.autcon.2024.105456|Crane safety operations in modular integrated construction|原摘要已读，模块建筑吊装安全系统综述未明确AI方法分类，需补正文证据。|
|10.1016/j.autcon.2024.105504|Generalized vision-based framework for construction productivity analysis using a standard classification system|原摘要已读，视觉工人活动和生产状态分析框架未交代学习模型，需核方法以确认AI和工程感知贡献。|
|10.1016/j.autcon.2024.105555|Monitoring and evaluating the status and behaviour of construction workers using wearable sensing technologies|原摘要已读，工人穿戴传感状态评估综述未明确AI方法覆盖，需核数据分析章节。|
|10.1016/j.autcon.2024.105576|4D point cloud-based spatial-temporal semantic registration for monitoring mobile crane construction activities|原摘要已读，四维点云语义配准识别吊装活动，具体AI模型与规则几何步骤边界仍需方法确认。|
|10.1016/j.autcon.2024.105566|Optimizing MEP design in early AEC projects through generative design|原摘要已读，MEP生成设计与蒙特卡洛稳健性验证未交代AI或演化算法，需核生成方法。|
|10.1016/j.autcon.2024.105577|Hybrid knowledge and data driven approach for prioritizing sewer sediment cleaning|原摘要已读，知识与数据混合评估污水管沉积清理优先级，但AI学习或推理实现缺证，需查方法。|
|10.1016/j.autcon.2024.105608|Effect of human emotional responses on human-robot team pty in construction|原摘要已读，EEG研究机器人参数与情绪响应关联，需确认情绪识别是否使用AI模型。|
|10.1016/j.autcon.2024.105610|Visual flow-based programming plugin for brain–computer Interface in computer-aided design|原摘要已读，为建筑设计脑机接口插件，需确认神经数据解码AI及其科学评估任务。|
|10.1016/j.autcon.2024.105630|Constructability-based design approach for steel structures: From truss beams to real-world inspired industrial buildings|原摘要已读，钢桁架可建造性惩罚优化未交代具体AI或演化求解算法，需补方法。|
|10.1016/j.autcon.2024.105619|Automated vision-based multi-plane bridge displacement monitoring|原摘要已读，编码标记与智能算法多平面测位移，但算法是否为AI未明，需核方法。|
|10.1016/j.autcon.2024.105674|Understanding construction workers’ cognitive processes under risky scenarios through electroencephalography|原摘要已读，EEG施工危险认知综述未明确AI信号解码方法覆盖，需核数据处理章节。|
|10.1016/j.autcon.2024.105676|Updating simulation model parameters using stochastic gradient descent|原摘要已读，SGD在线更新隧道仿真参数，但AI模型与传统参数校准边界不清，需核模型。|
|10.1016/j.autcon.2024.105692|Automating modular open-plan office layouts with performance-based generative design|原摘要已读，模块库和性能驱动生成办公室布局，但具体生成算法是否AI不明，需查方法。|
|10.1016/j.autcon.2024.105690|Virtual reality-based site layout planning for building design|原摘要已读，VR与多目标场地布局优化结合，未说明优化算法是否实质AI，需方法证据。|
|10.1016/j.autcon.2024.105713|Digital twin for smart metro service platform: Evaluating long-term tunnel structural performance|原摘要已读，地铁数字孪生长期结构性能平台未说明预测算法，需确认AI角色。|
|10.1016/j.autcon.2024.105722|Advanced fire emergency management based on potential fire risk assessment with informative digital twins|原摘要已读，知识型数字孪生评估动态火灾危险与疏散，但具体AI识别推理方法缺证，需正文。|
|10.1016/j.autcon.2024.105731|Automated safety and practicality enhancement of lift plans in modular construction|原摘要已读，多起重机吊装规划集成系统未明确AI求解与推理步骤，需核方法。|
|10.1016/j.autcon.2024.105767|Recent advances on inspection, monitoring, and assessment of bridge cables|原摘要已读，桥梁缆索检测监测评估综述未明确AI方法覆盖，需核正文。|
|10.1016/j.autcon.2024.105781|Automatic geometric digital twin of box girder bridge using a laser-scanned point cloud|原摘要已读，点云自动箱梁桥几何建模未交代AI模型，需核分割识别方法。|
|10.1016/j.autcon.2024.105788|Human-centered intelligent construction for sustainable cities|原摘要已读，以人为中心智能施工综述的具体AI工程贡献不明确，需正文证据。|
|10.1016/j.autcon.2024.105808|Energy-efficient configuration and scheduling framework for electric construction machinery collaboration systems|原摘要已读，电动工程机械能效配置调度未明确AI优化算法，需核求解方法。|
|10.1016/j.autcon.2024.105807|Fast 3D site reconstruction using multichannel dynamic and static object separation|原摘要已读，单目动态静态对象分离加速现场三维重建，具体识别模型AI角色未说明。|
|10.1016/j.autcon.2024.105823|Virtual in-situ modeling between digital twin and BIM for advanced building operations and maintenance|原摘要已读，建筑虚拟在位建模改善温度与故障估计，但具体AI模型未说明，需查建模与融合方法。|
|10.1016/j.autcon.2024.105837|Performance evaluation of struck-by-accident alert systems for road work zone safety|原摘要已读，道路作业区碰撞警报系统评测综述未明确AI方法和评测对象，需核正文。|
|10.1016/j.autcon.2024.105864|Terrain-adaptive motion planner for articulated construction vehicles in unstructured environments|原摘要已读，地形和车体动力学的运动规划器未说明AI搜索优化方法，需核方法。|

## 后续断点

陈晨名下尚有11,465条未筛选，分布在8本期刊和2个会议；另482条已经筛过但待补证，不与未筛选混计。下一本Applied Energy剩余2,003条。

本轮结果已保存为本地交付。此前自动审批拒绝推送的状态继续保留，本轮未推送或创建PR。
