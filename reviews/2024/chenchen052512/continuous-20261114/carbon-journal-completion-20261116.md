# Carbon 2024整刊初筛与候选核查

第216—230卷含分页1043条，官网文章号集合与快照完全一致。

本轮新增1032条：纳入5、排除1025、待定2。累计1043条：纳入10、排除1031、待定2、未审0。旧11条审核保持。

## 阅读与对账范围

1043条逐条检查题名、书目信息及正式文种；21篇另读完整原摘要，8个正式论文页核验元数据或公开方法。非全量摘要精读或全文通读。149条正式非研究条目排除，其中96条为会议摘要，不能因题名含机器学习而视作研究正文。

正式文种：859研究、35综述、30编委、14勘误、96会议摘要、2个人纪念、1出版方说明、5通信、1社论。

初筛年候选5条，缺输入摘要0；来源候选5条，缺0。5篇漏筛纳入及2条待定另记，原字段与候选文件保持。

## 本轮补录纳入5篇

|文章号|论文|AI科学作用|
|---|---|---|
|119201|[Multi-directional strain sensor based on carbon nanotube array for human motion monitoring and gesture recognition](https://www.sciencedirect.com/science/article/pii/S0008622324004202)|原摘要明确将神经网络与三单元CNT阵列传感器结合，同时预测应变幅度与方向，准确率超过98%；AI实质参与物理量测量，不仅是手势识别演示。未核清具体神经网络架构，使用监督学习规范标签。|
|119231|[Dual-indicators machine learning assisted processing high-quality laser-induced fluorine-doped graphene and its application on droplet velocity monitoring sensor](https://www.sciencedirect.com/science/article/pii/S0008622324004500)|原摘要明确以高斯过程回归构建双指标预测模型，寻找兼具超疏水性和导电性的激光诱导氟掺杂石墨烯工艺参数，并报告测试误差和实物验证；科学贡献为材料加工优化。|
|119356|[Improved understanding of carbon nanotube growth via autonomous jump regression targeting of catalyst activity](https://www.sciencedirect.com/science/article/pii/S000862232400575X)|原摘要及公开Methods、Results and discussion片段确认ARES系统执行CNT生长实验，以原位Raman反馈给jump regression主动学习规划器选择下一实验，定位催化剂氧化还原相变附近高产率区域，形成实验执行与反馈闭环。|
|119533|[Thermal and electronic properties of borophene in two-dimensional lateral graphene-borophene heterostructures empowered by machine-learning approach](https://www.sciencedirect.com/science/article/pii/S0008622324007528)|原摘要、引言及结论明确用机器学习原子间势驱动分子模拟，研究石墨烯—硼烯横向异质结构的晶格热导与电荷转移；没有将普通DFT本身视作AI，未核清势函数架构，细分方法标签省略。|
|119573|[Concentration division for adsorption coefficient prediction using machine learning with Abraham descriptors: Data-splitting approach comparison and critical factors identification](https://www.sciencedirect.com/science/article/pii/S0008622324007929)|原摘要明确按平衡浓度划分数据训练ML吸附系数预测模型，并用Shapley值解释Abraham描述符与比表面积贡献，支持碳吸附剂设计；模型家族未在已读摘要明确，不猜具体网络。|

## 待定与易误判项

- 119488：正式Research article，正文栏目Perspectives，目录与论文页均无原摘要。Introduction有AI碳科学专节，但尚需原摘要和实质案例。
- 118765：呼吸感知器件原摘要和引言已读，本文训练/权重学习/判别流程仍需核查；不把引言引用的其他论文算法算作本文方法。
- 119643：Introduction及Methods确认TersoffHP经验势与LAMMPS，排除。
- 118603：原摘要的decision trees并未体现机器学习模型，实质为三元纳米润滑涂层，排除。
- 119161、118665：通用手写数字识别用于神经形态器件演示，未体现AI参与科学任务，排除。

## 剩余工作

陈晨2024锁定快照当前未筛选12,770条，分布在10本期刊和2个会议。另有444条已筛选待补证，单独计数。

|未筛选来源|剩余条数|
|---|---:|
|JACC Cardiovascular Interventions|755|
|Automation in Construction|550|
|Applied Energy|2003|
|Biosensors and Bioelectronics|733|
|Energy Conversion and Management|1210|
|Advanced Engineering Informatics|632|
|International Journal of Mechanical Sciences|909|
|Additive Manufacturing|631|
|Phytomedicine|1008|
|Aerospace Science and Technology|869|
|International Conference on Learning Representations|1557|
|International Conference on Machine Learning|1913|

## 访问与核验限制

纳入5篇正式页的DOI和PII已核，页面均有Purchase PDF；119356另显示View Open Manuscript入口，未打开手稿。公开PDF正文和代码未全面核实。GitHub命令行DNS仍失败，已用正常浏览器核对最新规则、词表及个人行动清单；本地结果尚未推送。
