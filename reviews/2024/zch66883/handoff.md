# 朱长昊 2024 批次交接

本次独立重做，未使用朱长昊上一版判定。按用户确认保留乔徐阳的 ISCAS 工作，未改动该来源。

批次：2024-20261105-zch66883-independent-redo。采集快照：2026-11-05T10:31:19.144426+08:00。按仓库当前README仅执行2024，不宣称已完成2020—2026。

## 来源核验

53个来源：建议纳入30，不建议纳入7，待核实16。原始对应候选857、122、217；ISCAS另187条跳过。来源报告见source-review.pdf / source-review.md。期刊采用2025中科院升级版大类；B会议结合当届录取率和评审机制，缺证据不编造结论。

## 逐篇结果

原候选857条全部审核，另对快照全量书目内、经出版方证据核实的3条漏筛记录补审。交付860条：**纳入187、排除667、待定6、未审0**。

187篇纳入均核对Crossref DOI、正式题名及作者顺序；其中23篇确认可直接取得且题名/DOI匹配的公开PDF，56篇确认作者所述代码库可访问。其余公开PDF或辅助链接未确认时填null，不把论文页、付费下载页或HTTP 403冒充公开PDF。公开作者版/预印本与正式排版可能不同。

原始字段逐项保留，仅新增ai4s_review（schema_version=2）；原有ai4s_tags保持原样，最终标签读取ai4s_review.tags。非纳入标签为空。合并键为(venue,year,id)，860条无重复键。来源排除/待核实的论文不构造占位。

## 待定6条

- date / 10.23919/date58400.2024.10546587 / HDCircuit: Brain-Inspired HyperDimensional Computing for Circuit Recognition.：HDC用于电路识别有工程对象；该DATE记录为2页，需从正式节目确认论文类型。
- date / 10.23919/date58400.2024.10546502 / Microprocessor Design Space Exploration via Space Partitioning and Bayesian Optimization.：贝叶斯优化用于微处理器设计有工程对象；该DATE记录为2页，需确认Regular或扩展摘要类型。
- date / 10.23919/date58400.2024.10546835 / Trans-Net: Knowledge-Transferring Analog Circuit Optimizer with a Netlist-Based Circuit Representation.：Trans-Net跨工艺及电路迁移学习符合工程研究，但DATE记录为2页，须核实是否正式长文。
- date / 10.23919/date58400.2024.10546817 / Learning to Floorplan like Human Experts via Reinforcement Learning.：强化学习结合专家风格进行芯片规划符合工程研究，但DATE记录为2页，须核实是否正式长文。
- mm / 10.1145/3664647.3685647 / Utilizing Very High-resolution Optical RGB Satellite Imagery in Geo-information Extraction for Fine-scale Map-making.：卫星地理信息提取与GAN道路分割相关，但需核实该记录属于主会正式研究长文还是博士论坛等其他类型，暂不纳入。
- mm / 10.1145/3664647.3681364 / Improving Interaction Comfort in Authoring Task in AR-HRI through Dynamic Dual-Layer Interaction Adjustment.：生理信号驱动的人机交互舒适度预测可能相关，但摘要未明确预测模型是否采用AI学习，需方法证据。

DATE四条已取得官网对应PDF，但没有以2页篇幅单独推定Short/Extended，仍待正式类型证据；MM一条待论文类型，一条待AI方法证据。

## 补审与初筛覆盖缺口

- 10.1016/j.ipm.2024.103855：同快照内漏筛补审（非原始书目漏采）：该条目已在全量papers.json，未进入ai4s.json。正式出版方摘要说明将造影超声的灌注信息通过多视图解耦和双向蒸馏迁移至B模超声肝癌诊断。 [出版方证据](https://www.sciencedirect.com/science/article/pii/S0306457324002140)
- 10.1016/j.chemolab.2024.105131：同快照内漏筛补审（非原始书目漏采）：该条目已在全量papers.json，未进入ai4s.json。出版方说明将过程物理先验嵌入图学习软传感模型，并在青霉素分批补料发酵的不同情景验证。 [出版方证据](https://www.sciencedirect.com/science/article/pii/S0169743924000716)
- 10.1016/j.chemolab.2023.105059：同快照内漏筛补审（非原始书目漏采）：该条目已在全量papers.json，未进入ai4s.json。出版方和作者机构原始摘要说明以高光谱及优化K近邻预测鲑鱼储存天数、比较空间腐败非均匀性；正式出版卷245为2024，不能按DOI中的2023错分年份。 [出版方证据](https://www.sciencedirect.com/science/article/pii/S016974392300309X)

这3篇已在同快照全量书目中，属于漏筛，不是新发现书目漏采。它们不是全部漏筛的数量估计。IPM全量303条、TRB158条均无摘要；Chemolab163条有45条摘要。补齐摘要并重跑初筛后才能评估完整召回。

[UbiComp官网](https://www.ubicomp.org/ubicomp-iswc-2024/)将主技术论文列为IMWUT；当前19条候选全为Companion，均因非主研究长文排除。不能据此断言UbiComp没有AI4S论文。需按正式2024卷期与会议展示年对齐IMWUT，并协调分工后补采。

WWW官方主集432+Companion346=778，与快照全量778一致；66条原候选DOI均匹配SIGWEB目录。该一致性不替代778条逐条去重/完整性核查。其他来源的口径、官网数量和缺口详见coverage.csv（53来源）；未知总数明确留空。

## 文件与复核

- ../zch66883.json：唯一可合并论文数组。
- coverage.csv：53来源的全量、摘要、官方口径、候选、补审及判定数量。
- metadata-verification.csv：纳入/待定的DOI、公开PDF尝试及辅助链接验证记录。
- manifest.json：批次、数量、输入/输出SHA-256和限制。
- source-evidence.json：独立来源核验事实与证据。

合并时只读新增审核字段，不覆盖输入原字段。后续取得证据时更新6条pending和16个待核实来源；补采/重跑后新候选应按新快照另批交付。
