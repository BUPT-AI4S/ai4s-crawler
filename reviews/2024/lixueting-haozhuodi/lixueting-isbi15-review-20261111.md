# 李雪婷：15条ISBI复核与2024年全部待定核对（2026-11-11）

15条均已有摘要。本轮按原文方法和实验确认 **8条纳入、0条排除、7条仍待定**；未新增作者摘要。此前这15条在历史交付中为pending、在全量台账中为exclude，本次按证据同步纠正。旧审核人及原结论完整留存在[逐篇审计](lixueting-isbi15-review-20261111.json)。

## 本轮逐篇结果

| 编号 | 论文 | 结论 | 核查重点 |
|---|---|---|---|
| 1 | Structural-Connectivity-Based Individual Parcellations Improve Regional Cortical Thickness Heritability Study. | 待定 | 脑结构连接与个体分区服务皮层厚度遗传率研究，但现有摘要不足以区分分区中的机器学习与固定几何/统计处理。定位到同篇 HAL 作者稿，下载返回访问验证页，未取得正文，撤回旧台账证据不足的直接排除。 |
| 2 | Deformable Image Registration with Stochastically Regularized Biomechanical Equilibrium. | 纳入 | 同题作者稿明确将生物力学平衡正则项用于隐式神经表示配准，神经网络从空间坐标预测位移，并在合成形变及肺部 DIRLab 4DCT 上验证。AI 实质参与医学影像配准，修正旧台账排除结论。 |
| 3 | Towards Multi-Perspective Panoramic Ultrasound Imaging Using Low-Cost 3D Printed Track And 1D Linear Probe. | 纳入 | 公开会议作者稿 §2.2.1 明确使用五层 U-Net 从手工分割腕部超声图像学习骨区域，随后进行配准融合；§3 在四名受试者的腕部成像上验证。AI 分割直接支撑全景医学影像重建，修正旧台账排除结论。 |
| 4 | Decoding Radiologists' Intentions: A Novel System for Accurate Region Identification in Chest X-Ray Image Analysis. | 纳入 | PMC 原文明确使用 ResNet/CLIP 视频表示和 T5 编解码器，预训练后在带眼动与报告的胸片数据上微调，预测放射科医师意图及时间定位，并关联影像区域。存在直接的医学影像理解任务与模型训练、实验，修正旧台账排除结论。 |
| 5 | Medical Image Segmentation Using the Equivariance Under Diffeomorphisms Framework. | 待定 | 论文针对结肠和肝血管分割，但摘要只说明微分同胚等变与最优传输，不能据此确定学习模型。正式页面及作者机构记录未提供可读的方法正文，撤回旧台账证据不足的直接排除。 |
| 6 | Interpretable Models for Detecting and Monitoring Elevated Intracranial Pressure. | 纳入 | 作者稿明确训练 YOLOv5 定位视神经及眼球，使用卷积稀疏编码分类器或 R2U-Net 分割测量视神经鞘，并用超声视频评估颅内压升高的代理指标。AI 参与医学测量和辅助判断，修正旧台账排除结论。 |
| 7 | Structure-Preserved Graph Embedding for Improved MRF Reconstruction. | 待定 | 目标 DOI 10635494 的摘要说明结构保持图嵌入用于 MR 指纹重建，但未明确学习模块。发现另有题名带 Deep、DOI 10635500 的同作者论文；不能把另一篇的深度学习证据用于本条。未取得目标原文，撤回旧台账证据不足的直接排除。 |
| 8 | A Moment-Based Weighted Block Sparse Bayesian Learning Approach for Simultaneous Dual-Layer Lung Electrical Impedance Tomography. | 纳入 | 原文 §3 和算法1明确给出加权块稀疏贝叶斯学习，用观测数据迭代学习块稀疏性、噪声和相关性参数；§4 以人体胸腔仿真及马肺实测数据评价双层电阻抗重建。属于贝叶斯学习直接用于医学成像，修正旧台账排除结论。 |
| 9 | Airways Measurement from Ct Images in Health and Asthma. | 待定 | CT 气道重塑测量有明确哮喘研究目标，但摘要未说明气道分割是否使用学习模型。作者所在机构记录说明未附文件，IEEE 正文未能读取；不能仅凭分割/形态测量判断 AI 作用，撤回旧台账直接排除。 |
| 10 | sqFibrosis: A Robust Liver Fibrosis Scoring System for Telepathology. | 待定 | 摘要描述把63项胶原结构与形态特征整合为肝纤维化评分，但未说明评分是否通过学习得到。出版方、作者发表清单及开放版本检索未提供同篇可读方法；早期同名工作不足以代替2024年原文，撤回旧台账直接排除。 |
| 11 | Blind Color Deconvolution and Classification of Histological Images Using the Hyperbolic Secant Prior. | 纳入 | 作者公开原文 §4.2 在 Camelyon-17 多中心乳腺病理数据上从头训练 VGG19，比较所提染色分离预处理对独立中心乳癌分类的影响。即使预处理是贝叶斯推断，完整研究仍有实质 AI 病理分类任务及实验，修正旧台账排除结论。 |
| 12 | Detecting Symmetry in Ascidian Embryo. | 待定 | 摘要及研究团队年度说明描述以细胞接触表面特征识别海鞘胚胎对称关系，但未取得同篇完整算法。HAL 原文链接返回访问验证页，不能确认其中是否只有规则匹配或存在学习过程，撤回旧台账证据不足的直接排除。 |
| 13 | Real-Time Video Enhancement for the Removal of Surgical Lighting Artifacts in Computer-Assisted Orthopedic Surgery. | 纳入 | 原文将手术照明伪影校正用于模拟舟骨固定手术视频，使用 MediaPipe 手部姿态检测作为明确下游任务，验证校正对医学导航相关检测成功率的影响。虽校正本身为物理建模，AI 姿态检测实质参与医疗工程评估，修正旧台账排除结论。 |
| 14 | Multiscale Neuroimaging Features for the Identification of Medication Class and Non-Responders in Mood Disorder Treatment. | 纳入 | 作者稿以静息态 fMRI 的多尺度独立成分和功能连接特征，训练核支持向量机并执行特征选择，预测心境障碍患者的用药类别及不响应情况，报告交叉验证实验。机器学习与治疗反应研究直接相关，修正旧台账排除结论。 |
| 15 | Wavelia #2: The Microwave Breast Surface Estimation Module. | 待定 | 短摘要只说明微波乳房表面估计模块及两例患者结果，尚不能确定是否使用 AI。作者发表清单确认了该会议文献，但没有公开同篇方法正文；未用后续系统论文替代本篇证据，撤回旧台账直接排除。 |

## 到底还剩多少待定

按最新2024年分工的51个来源，逐一核对全部顶层交付、李雪婷个人文件和29,289条全量台账。三种口径的待定标识集合完全一致：**280条**，其中267条缺摘要、13条已有摘要但缺足够方法证据。此次原文获取失败的7条均保留待定，没有用题名或相近论文替代原文判定。

此外存在 **47条历史交付判定冲突**（ISBI44条、iScience3条），与280条待定互不重叠。它们已有不同文件的纳入/排除/待定结论，需统一交付，网页规则将它们排除在待定统计之外。若把待定和需统一的冲突合计，则是 **327条尚有待处理事项的记录**；不能把“280条待定”解释为所有审核及数据一致性工作均只剩280条。

| 范围 | 纳入 | 排除 | 待定 | 冲突 | 总数 |
|---|---:|---:|---:|---:|---:|
| 李雪婷个人交付 | 2,317 | 1,976 | 280 | 不适用 | 4,573 |
| 李雪婷2024全量台账 | 2,317 | 26,692 | 280 | 不适用 | 29,289 |
| 全部交付合并后（网页口径） | 2,296 | 2,005 | 280 | 47 | 4,628 |

三者纳入、排除数的差异来自全量台账覆盖更多记录，以及网页合并了历史交付并暂不计入冲突。所有负责来源的已交付记录都能在全量台账找到，没有额外遗漏在台账外的pending。

- [280条完整待定清单](lixueting-isbi15-review-20261111-pending.json)：题名、DOI、摘要状态、逐篇缺少的证据。
- [47条冲突清单](lixueting-isbi15-review-20261111-conflicts.json)：各文件结论、理由和证据链接。
- [汇总与一致性核验](lixueting-isbi15-review-20261111-summary.json)。

上述数字仅指2024年当前采集快照 `2026-11-05T10:31:19.144426+08:00`。2025和2026年各51个来源目前仍无逐篇交付，不能把2024年的待定数当作跨年份全部未完成工作量。官网总量核验等来源层面事项也不包含在论文待定数内。

本轮只修改指定15条论文、相关来源反馈与必要汇总；47条其他冲突未擅自改判。原始论文字段、摘要和其他记录保留不变，未修改监控页面、脚本或工作流。原文核查区分作者稿、PMC原文及通过网页工具读取的PDF；访问验证页不记为已阅读全文。最新行动清单和词表读取自 `cfede5ca68d009dc46f3b131b7e9dfa9c15d2378`。
