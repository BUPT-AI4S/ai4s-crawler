# 王婉婷｜AI4S论文摘要批量审核工作汇报

2026年11月8日 · 2024年论文 · Blueblue1101 · continuation13

**本轮完成3,000条：纳入77篇、排除2,782条、待定141条；核验补齐完整摘要92条。** 覆盖29个来源，旧17,333条完整记录保持不变。

新增纳入均来自已经采集、未进入关键词初筛候选的记录，属于**漏筛补录**。本轮新爬0篇，未扩大官网漏采核验。缺摘要或抓取异常项按要求暂缓。

## 审核方法

按仓库main `cf3f0bf` 当前skill复核，从762项共享词表中查找已有标签。分批读取完整摘要，截断内容另行重读，逐条保存结论、理由、摘要哈希和队列位置。判断依据是明确的科学／工程任务、AI实质作用及二者关系，未以关键词命中替代语义判断，未读取正文或PDF。

80篇拟纳入全部重读，最终保留77篇并打标；边界调整记录在审计中。固定随机种子抽查30条排除记录（27条相关性排除、3条文种排除），重读后维持原结论。抽查不能代表全量准确率。证据不足或摘要异常的141条保留待定，未强行判为纳入。

## 本轮结果及原因

| 结果 | 条数 | 原因 |
|---|---|---|
| 纳入 | 77 | 摘要支持AI用于明确科学或工程研究任务 |
| 相关性排除 | 2768 | 摘要未显示AI实质参与，或仅有通用模型／基准而缺少实质科学研究任务 |
| 文种排除 | 14 | Viewpoint、Perspective、Commentary、Matters Arising、共识／意见及会议新闻等非本批研究文种 |
| 待定 | 141 | AI作用或领域贡献证据不足，以及摘要片段／无效描述，保留后续查证 |

## 各来源本轮工作量

“补摘要”指已取得的书目摘要经语义核验后写入元数据，不代表本轮新爬论文；已包含在已审记录中，不与纳入篇数相加。

| 来源 | 本轮已审 | 新爬 | 纳入 | 排除 | 待定 | 核验补齐摘要 |
|---|---|---|---|---|---|---|
| Nature Communications | 2073 | 0 | 17 | 1958 | 98 | 0 |
| CVPR | 382 | 0 | 53 | 319 | 10 | 0 |
| Nature Physics | 85 | 0 | 0 | 84 | 1 | 0 |
| Nature Ecology & Evolution | 46 | 0 | 0 | 40 | 6 | 0 |
| Nature Microbiology | 39 | 0 | 0 | 37 | 2 | 0 |
| Nano Energy | 38 | 0 | 0 | 37 | 1 | 17 |
| Nature Geoscience | 38 | 0 | 0 | 38 | 0 | 0 |
| Energy Storage Materials | 36 | 0 | 0 | 35 | 1 | 0 |
| Cell Discovery | 24 | 0 | 0 | 18 | 6 | 0 |
| International Journal of Mining Science and Technology | 21 | 0 | 1 | 20 | 0 | 0 |
| Nature Human Behaviour | 20 | 0 | 2 | 17 | 1 | 0 |
| Molecular Cell | 18 | 0 | 0 | 18 | 0 | 11 |
| Nature Chemical Biology | 17 | 0 | 0 | 16 | 1 | 0 |
| Nature Protocols | 17 | 0 | 2 | 13 | 2 | 0 |
| Nature Neuroscience | 16 | 0 | 1 | 14 | 1 | 0 |
| Journal of Energy Chemistry | 15 | 0 | 0 | 15 | 0 | 9 |
| Trends in Food Science & Technology | 13 | 0 | 0 | 13 | 0 | 3 |
| Information Fusion | 12 | 0 | 1 | 10 | 1 | 12 |
| The Lancet Planetary Health | 11 | 0 | 0 | 11 | 0 | 0 |
| Smart Learning Environments | 11 | 0 | 0 | 9 | 2 | 0 |
| Trends in Microbiology | 11 | 0 | 0 | 11 | 0 | 10 |
| Clinical Gastroenterology and Hepatology | 10 | 0 | 0 | 3 | 7 | 1 |
| The Lancet Regional Health - Europe | 9 | 0 | 0 | 8 | 1 | 0 |
| Seminars in Cancer Biology | 8 | 0 | 0 | 8 | 0 | 8 |
| Journal of Advanced Research | 8 | 0 | 0 | 8 | 0 | 8 |
| The Lancet Haematology | 7 | 0 | 0 | 7 | 0 | 3 |
| Journal of Materials Science & Technology | 7 | 0 | 0 | 7 | 0 | 7 |
| Molecular Neurodegeneration | 5 | 0 | 0 | 5 | 0 | 0 |
| Chem | 3 | 0 | 0 | 3 | 0 | 3 |
| **合计** | 3000 | 0 | 77 | 2782 | 141 | 92 |

## 新增漏筛纳入论文与标签

| 来源 | 论文 | 摘要依据 | 标签 |
|---|---|---|---|
| CVPR | [UnO: Unsupervised Occupancy Fields for Perception and Forecasting](https://openaccess.thecvf.com/content/CVPR2024/html/Agro_UnO_Unsupervised_Occupancy_Fields_for_Perception_and_Forecasting_CVPR_2024_paper.html) | 初筛漏筛补录。用激光雷达自监督学习四维占据世界模型，预测自动驾驶道路几何与目标状态并验证低标注迁移。 | AI 用于工程科学、自动驾驶感知、自监督学习、微调 |
| CVPR | [Instance-level Expert Knowledge and Aggregate Discriminative Attention for Radiology Report Generation](https://openaccess.thecvf.com/content/CVPR2024/html/Bu_Instance-level_Expert_Knowledge_and_Aggregate_Discriminative_Attention_for_Radiology_Report_CVPR_2024_paper.html) | 初筛漏筛补录。将疾病专家知识检索、弱监督判别注意力和自蒸馏用于胸部影像报告生成，在IU X-Ray和MIMIC-CXR进行医学评测。 | AI 用于生命科学、医学报告生成、检索增强学习、弱监督学习、知识蒸馏 |
| CVPR | [Smart Help: Strategic Opponent Modeling for Proactive and Adaptive Robot Assistance in Households](https://openaccess.thecvf.com/content/CVPR2024/html/Cao_Smart_Help_Strategic_Opponent_Modeling_for_Proactive_and_Adaptive_Robot_CVPR_2024_paper.html) | 初筛漏筛补录。针对不同能力和残障需求建立辅助机器人任务，使用对手建模推断能力与目标并优化协助策略，证据限于家庭仿真环境。 | AI 用于工程科学、机器人任务规划、策略学习 |
| CVPR | [Towards HDR and HFR Video from Rolling-Mixed-Bit Spikings](https://openaccess.thecvf.com/content/CVPR2024/html/Chang_Towards_HDR_and_HFR_Video_from_Rolling-Mixed-Bit_Spikings_CVPR_2024_paper.html) | 初筛漏筛补录。联合脉冲相机混合位深读出与跨位跨时注意力网络，在有限传输量下重建高动态范围高帧率视频。 | AI 用于工程科学、工程传感数据重建、注意力机制 |
| CVPR | [Beyond Average: Individualized Visual Scanpath Prediction](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Beyond_Average_Individualized_Visual_Scanpath_Prediction_CVPR_2024_paper.html) | 初筛漏筛补录。学习个体观察者特征以预测人类视觉注意扫描路径，直接建模注意行为个体差异，并在多视觉任务数据上验证。 | AI 用于生命科学、视觉注视轨迹预测、注意力机制 |
| CVPR | [Mind Marginal Non-Crack Regions: Clustering-Inspired Representation Learning for Crack Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Mind_Marginal_Non-Crack_Regions_Clustering-Inspired_Representation_Learning_for_Crack_Segmentation_CVPR_2024_paper.html) | 初筛漏筛补录。通过歧义感知损失和聚类表征改善裂纹检测分割，构建裂纹数据集并验证，直接服务工程缺陷识别。 | AI 用于工程科学、结构健康监测、语义分割、聚类 |
| CVPR | [Unsupervised Deep Unrolling Networks for Phase Unwrapping](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Unsupervised_Deep_Unrolling_Networks_for_Phase_Unwrapping_CVPR_2024_paper.html) | 初筛漏筛补录。以相位包裹物理模型构造深度展开网络，用自监督损失恢复科学成像相位，在三类相位数据上验证。 | AI 用于工程科学、图像重建、物理信息学习、无监督学习、知识蒸馏 |
| CVPR | [Versatile Medical Image Segmentation Learned from Multi-Source Datasets via Model Self-Disambiguation](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Versatile_Medical_Image_Segmentation_Learned_from_Multi-Source_Datasets_via_Model_CVPR_2024_paper.html) | 初筛漏筛补录。多源部分及稀疏标注学习用于多模态腹部结构分割，解决设备协议差异与标签不一致带来的医学成像问题。 | AI 用于生命科学、医学影像分割、弱监督学习、知识引导学习 |
| CVPR | [Weakly Misalignment-free Adaptive Feature Alignment for UAVs-based Multimodal Object Detection](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Weakly_Misalignment-free_Adaptive_Feature_Alignment_for_UAVs-based_Multimodal_Object_Detection_CVPR_2024_paper.html) | 初筛漏筛补录。针对无人机可见光和红外传感器错位设计自适应特征对齐网络，并验证目标感知对传感器失配的鲁棒性，直接服务无人机多传感器感知。 | AI 用于工程科学、目标检测、多模态学习、注意力机制 |
| CVPR | [Adaptive Fusion of Single-View and Multi-View Depth for Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2024/html/Cheng_Adaptive_Fusion_of_Single-View_and_Multi-View_Depth_for_Autonomous_Driving_CVPR_2024_paper.html) | 初筛漏筛补录。针对自动驾驶中相机位姿噪声与标定误差，用自适应学习融合单多视图深度，在鲁棒性场景中验证。 | AI 用于工程科学、自动驾驶感知、多模态学习、深度学习 |
| CVPR | [Adaptive Bidirectional Displacement for Semi-Supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Chi_Adaptive_Bidirectional_Displacement_for_Semi-Supervised_Medical_Image_Segmentation_CVPR_2024_paper.html) | 初筛漏筛补录。为医学图像分割提出基于置信度的半监督双向位移和一致性学习方法，直接改善医学图像标注稀缺条件下的分割。 | AI 用于生命科学、医学影像分割、半监督学习、数据增强 |
| CVPR | [Clustering Propagation for Universal Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Ding_Clustering_Propagation_for_Universal_Medical_Image_Segmentation_CVPR_2024_paper.html) | 初筛漏筛补录。以跨切片聚类传播统一自动及交互医学体积分割，在三套医学影像基准验证。 | AI 用于生命科学、医学影像分割、聚类、神经网络 |
| CVPR | [DualAD: Disentangling the Dynamic and Static World for End-to-End Driving](https://openaccess.thecvf.com/content/CVPR2024/html/Doll_DualAD_Disentangling_the_Dynamic_and_Static_World_for_End-to-End_Driving_CVPR_2024_paper.html) | 初筛漏筛补录。将交通动态参与者与静态结构分流建模，通过运动补偿和交叉注意力提升端到端驾驶感知与规划。 | AI 用于工程科学、自动驾驶感知、自动驾驶决策、注意力机制 |
| CVPR | [Evidential Active Recognition: Intelligent and Prudent Open-World Embodied Perception](https://openaccess.thecvf.com/content/CVPR2024/html/Fan_Evidential_Active_Recognition_Intelligent_and_Prudent_Open-World_Embodied_Perception_CVPR_2024_paper.html) | 初筛漏筛补录。将不确定性证据累积和奖励设计用于机器人主动识别策略，在遮挡、距离变化等模拟机器人环境中验证感知可靠性，直接服务机器人自主感知。 | AI 用于工程科学、目标检测、策略学习、不确定性量化 |
| CVPR | [Event-based Visible and Infrared Fusion via Multi-task Collaboration](https://openaccess.thecvf.com/content/CVPR2024/html/Geng_Event-based_Visible_and_Infrared_Fusion_via_Multi-task_Collaboration_CVPR_2024_paper.html) | 初筛漏筛补录。事件相机与红外传感器联合成像，通过多任务学习重建纹理、去模糊与融合，合成及真实数据验证极端照明和动态场景成像性能。 | AI 用于工程科学、工程传感数据重建、多任务学习、互信息学习 |
| CVPR | [Time-Efficient Light-Field Acquisition Using Coded Aperture and Events](https://openaccess.thecvf.com/content/CVPR2024/html/Habuchi_Time-Efficient_Light-Field_Acquisition_Using_Coded_Aperture_and_Events_CVPR_2024_paper.html) | 初筛漏筛补录。联合编码孔径和事件相机，以端到端可训练深度光学重建光场，并用真实相机原型验证单曝光成像。 | AI 用于工程科学、工程传感数据重建、深度学习 |
| CVPR | [Motion Blur Decomposition with Cross-shutter Guidance](https://openaccess.thecvf.com/content/CVPR2024/html/Ji_Motion_Blur_Decomposition_with_Cross-shutter_Guidance_CVPR_2024_paper.html) | 初筛漏筛补录。利用全局与滚动快门的互补曝光物理构建真实成像装置和网络，将运动模糊分解为时间一致清晰帧。 | AI 用于工程科学、工程传感数据重建、神经网络 |
| CVPR | [3DSFLabelling: Boosting 3D Scene Flow Estimation by Pseudo Auto-labelling](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_3DSFLabelling_Boosting_3D_Scene_Flow_Estimation_by_Pseudo_Auto-labelling_CVPR_2024_paper.html) | 初筛漏筛补录。利用自动驾驶场景刚体运动假设生成真实稀疏LiDAR场景流伪标签并训练模型，降低实测点云三维运动估计误差。 | AI 用于工程科学、自动驾驶感知、科学训练数据生成、数据增强 |
| CVPR | [Complementing Event Streams and RGB Frames for Hand Mesh Reconstruction](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_Complementing_Event_Streams_and_RGB_Frames_for_Hand_Mesh_Reconstruction_CVPR_2024_paper.html) | 初筛漏筛补录。融合事件与RGB传感器并设计退化训练策略，实测验证快速运动及复杂照明下手部三维测量。 | AI 用于工程科学、人体姿态识别、多模态学习、深度学习 |
| CVPR | [EVS-assisted Joint Deblurring Rolling-Shutter Correction and Video Frame Interpolation through Sensor Inverse Modeling](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_EVS-assisted_Joint_Deblurring_Rolling-Shutter_Correction_and_Video_Frame_Interpolation_through_CVPR_2024_paper.html) | 初筛漏筛补录。把事件传感器像素延迟和读出误差纳入逆模型并结合细化网络，以真实混合传感器数据验证高速视频重建，直接解决成像仪器误差。 | AI 用于工程科学、工程传感数据重建、物理与数据融合建模、神经网络 |
| CVPR | [Traffic Scene Parsing through the TSP6K Dataset](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_Traffic_Scene_Parsing_through_the_TSP6K_Dataset_CVPR_2024_paper.html) | 初筛漏筛补录。建立拥挤交通监控场景数据集并用细节解码网络改善交通参与者分割，针对实际道路监控领域问题。 | AI 用于工程科学、交通场景建模、语义分割、科学数据、科学评测 |
| CVPR | [ZePT: Zero-Shot Pan-Tumor Segmentation via Query-Disentangling and Self-Prompting](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_ZePT_Zero-Shot_Pan-Tumor_Segmentation_via_Query-Disentangling_and_Self-Prompting_CVPR_2024_paper.html) | 初筛漏筛补录。通过查询解耦、自提示及知识对齐实现未见肿瘤类别的零样本医学图像分割。 | AI 用于生命科学、医学影像分割、零样本学习、知识引导学习 |
| CVPR | [Accurate Training Data for Occupancy Map Prediction in Automated Driving Using Evidence Theory](https://openaccess.thecvf.com/content/CVPR2024/html/Kalble_Accurate_Training_Data_for_Occupancy_Map_Prediction_in_Automated_Driving_CVPR_2024_paper.html) | 初筛漏筛补录。基于证据理论构造更准确的自动驾驶占据图训练数据并训练预测模型，在道路场景中显著改善几何预测误差，直接服务自动驾驶感知。 | AI 用于工程科学、自动驾驶感知、科学训练数据生成、不确定性量化 |
| CVPR | [CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention](https://openaccess.thecvf.com/content/CVPR2024/html/Khan_CAD-SIGNet_CAD_Language_Inference_from_Point_Clouds_using_Layer-wise_Sketch_CVPR_2024_paper.html) | 初筛漏筛补录。面向CAD逆向工程，从实物点云自回归恢复草图—拉伸设计历史，以层间跨注意力和草图实例引导实现设计重建及交互补全。 | AI 用于工程科学、参数化CAD生成、自回归建模、注意力机制 |
| CVPR | [Flow-Guided Online Stereo Rectification for Wide Baseline Stereo](https://openaccess.thecvf.com/content/CVPR2024/html/Kumar_Flow-Guided_Online_Stereo_Rectification_for_Wide_Baseline_Stereo_CVPR_2024_paper.html) | 初筛漏筛补录。针对车辆和机器人振动引起的宽基线相机失准，学习实时立体校正并用实测数据验证下游深度改善。 | AI 用于工程科学、传感器校准、注意力机制、深度学习 |
| CVPR | [JRDB-PanoTrack: An Open-world Panoptic Segmentation and Tracking Robotic Dataset in Crowded Human Environments](https://openaccess.thecvf.com/content/CVPR2024/html/Le_JRDB-PanoTrack_An_Open-world_Panoptic_Segmentation_and_Tracking_Robotic_Dataset_in_CVPR_2024_paper.html) | 初筛漏筛补录。构建机器人在真实拥挤环境中的多模态全景分割与跟踪数据集并评估学习方法，直接支持机器人环境感知研究。 | AI 用于工程科学、科学数据、科学评测、语义分割 |
| CVPR | [Rapid Motor Adaptation for Robotic Manipulator Arms](https://openaccess.thecvf.com/content/CVPR2024/html/Liang_Rapid_Motor_Adaptation_for_Robotic_Manipulator_Arms_CVPR_2024_paper.html) | 初筛漏筛补录。以深度感知和动作／本体感觉历史估计隐变量，训练机械臂快速运动适应策略，在Maniskill2仿真抓取、插销及把手任务验证；摘要未报告真实机械臂实验。 | AI 用于工程科学、机器人操作控制、策略学习 |
| CVPR | [MGMap: Mask-Guided Learning for Online Vectorized HD Map Construction](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_MGMap_Mask-Guided_Learning_for_Online_Vectorized_HD_Map_Construction_CVPR_2024_paper.html) | 初筛漏筛补录。利用掩码引导BEV表示和点位置细化实现在线道路高精地图构建，直接解决道路结构定位与几何细节丢失问题。 | AI 用于工程科学、高精道路地图构建、表示学习 |
| CVPR | [Seeing Motion at Nighttime with an Event Camera](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Seeing_Motion_at_Nighttime_with_an_Event_Camera_CVPR_2024_paper.html) | 初筛漏筛补录。针对夜间事件传感器拖尾与非平稳照明，设计时间戳校准和照明感知重建网络，并以同轴硬件采集真实配对数据验证动态成像。 | AI 用于工程科学、工程传感数据重建、神经网络、科学数据 |
| CVPR | [Generalizing 6-DoF Grasp Detection via Domain Prior Knowledge](https://openaccess.thecvf.com/content/CVPR2024/html/Ma_Generalizing_6-DoF_Grasp_Detection_via_Domain_Prior_Knowledge_CVPR_2024_paper.html) | 初筛漏筛补录。将抓取物理约束引入学习模型并优化接触姿态，通过真实机器人抓取实验验证新物体泛化，直接服务机器人操作。 | AI 用于工程科学、机器人抓取、约束学习、深度学习 |
| CVPR | [iToF-flow-based High Frame Rate Depth Imaging](https://openaccess.thecvf.com/content/CVPR2024/html/Meng_iToF-flow-based_High_Frame_Rate_Depth_Imaging_CVPR_2024_paper.html) | 初筛漏筛补录。结合飞行时间传感器物理成像过程构建流模型与深度提取网络，通过真实实验改善动态场景深度成像帧率和精度，直接服务成像测量。 | AI 用于工程科学、工程传感数据重建、物理与数据融合建模、神经网络 |
| CVPR | [EventEgo3D: 3D Human Motion Capture from Egocentric Event Streams](https://openaccess.thecvf.com/content/CVPR2024/html/Millerdurai_EventEgo3D_3D_Human_Motion_Capture_from_Egocentric_Event_Streams_CVPR_2024_paper.html) | 初筛漏筛补录。为头戴事件传感器设计人体动作捕捉网络并制作真实设备和标注数据，验证低照度高速运动条件下测量重建。 | AI 用于工程科学、人体姿态识别、工程传感数据重建、深度学习、科学数据 |
| CVPR | [T4P: Test-Time Training of Trajectory Prediction via Masked Autoencoder and Actor-specific Token Memory](https://openaccess.thecvf.com/content/CVPR2024/html/Park_T4P_Test-Time_Training_of_Trajectory_Prediction_via_Masked_Autoencoder_and_CVPR_2024_paper.html) | 初筛漏筛补录。以掩码自编码和个体车辆记忆适应驾驶场景分布变化，在多套驾驶数据中验证交通参与者轨迹预测。 | AI 用于工程科学、交通参与者轨迹预测、掩码建模、自编码器、在线学习 |
| CVPR | [LaneCPP: Continuous 3D Lane Detection using Physical Priors](https://openaccess.thecvf.com/content/CVPR2024/html/Pittner_LaneCPP_Continuous_3D_Lane_Detection_using_Physical_Priors_CVPR_2024_paper.html) | 初筛漏筛补录。将道路几何物理先验与解析正则化融入单目三维车道神经网络，改善自动驾驶道路曲线检测的几何误差和稳健性。 | AI 用于工程科学、自动驾驶感知、物理信息学习、神经网络 |
| CVPR | [MANUS: Markerless Grasp Capture using Articulated 3D Gaussians](https://openaccess.thecvf.com/content/CVPR2024/html/Pokhariya_MANUS_Markerless_Grasp_Capture_using_Articulated_3D_Gaussians_CVPR_2024_paper.html) | 初筛漏筛补录。学习可关节化高斯表示，从多相机捕捉手物接触，利用涂料转移实测验证抓握接触测量精度。 | AI 用于工程科学、手物接触估计、神经渲染、科学数据 |
| CVPR | [CaDeT: a Causal Disentanglement Approach for Robust Trajectory Prediction in Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2024/html/Pourkeshavarz_CaDeT_a_Causal_Disentanglement_Approach_for_Robust_Trajectory_Prediction_in_CVPR_2024_paper.html) | 初筛漏筛补录。针对自动驾驶轨迹预测的分布偏移，使用因果解耦和潜空间干预学习不变表示，在两套驾驶数据上检验鲁棒性。 | AI 用于工程科学、交通参与者轨迹预测、不变表示学习、因果推断 |
| CVPR | [EMCAD: Efficient Multi-scale Convolutional Attention Decoding for Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Rahman_EMCAD_Efficient_Multi-scale_Convolutional_Attention_Decoding_for_Medical_Image_Segmentation_CVPR_2024_paper.html) | 初筛漏筛补录。高效多尺度注意力解码用于医学影像分割，在12个数据集六类医学任务验证。 | AI 用于生命科学、医学影像分割、卷积神经网络、注意力机制 |
| CVPR | [Collaborative Semantic Occupancy Prediction with Hybrid Feature Fusion in Connected Automated Vehicles](https://openaccess.thecvf.com/content/CVPR2024/html/Song_Collaborative_Semantic_Occupancy_Prediction_with_Hybrid_Feature_Fusion_in_Connected_CVPR_2024_paper.html) | 初筛漏筛补录。学习车辆间语义与占据特征融合，预测联网自动驾驶的三维道路占据，针对协同感知通信与感知精度问题验证。 | AI 用于工程科学、自动驾驶感知、注意力机制、科学数据 |
| CVPR | [Revisiting Spatial-Frequency Information Integration from a Hierarchical Perspective for Panchromatic and Multi-Spectral Image Fusion](https://openaccess.thecvf.com/content/CVPR2024/html/Tan_Revisiting_Spatial-Frequency_Information_Integration_from_a_Hierarchical_Perspective_for_Panchromatic_CVPR_2024_paper.html) | 初筛漏筛补录。分层频域网络融合全色与多光谱观测，提高遥感多光谱空间分辨率并验证真实场景泛化。 | AI 用于地球宇宙科学、图像超分辨率、多模态学习、神经网络 |
| CVPR | [Learning to Remove Wrinkled Transparent Film with Polarized Prior](https://openaccess.thecvf.com/content/CVPR2024/html/Tang_Learning_to_Remove_Wrinkled_Transparent_Film_with_Polarized_Prior_CVPR_2024_paper.html) | 初筛漏筛补录。基于偏振成像物理建立透明薄膜去除数据集，用角度估计和重建网络消除工业检测中的薄膜反光退化。 | AI 用于工程科学、图像重建、物理与数据融合建模、神经网络 |
| CVPR | [BEVSpread: Spread Voxel Pooling for Bird's-Eye-View Representation in Vision-based Roadside 3D Object Detection](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_BEVSpread_Spread_Voxel_Pooling_for_Birds-Eye-View_Representation_in_Vision-based_Roadside_CVPR_2024_paper.html) | 初筛漏筛补录。针对路侧感知视锥到鸟瞰映射误差设计自适应体素传播，在两套路侧交通数据验证车辆行人骑行者检测。 | AI 用于工程科学、自动驾驶感知、目标检测、表示学习 |
| CVPR | [GenH2R: Learning Generalizable Human-to-Robot Handover via Scalable Simulation Demonstration and Imitation](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_GenH2R_Learning_Generalizable_Human-to-Robot_Handover_via_Scalable_Simulation_Demonstration_and_CVPR_2024_paper.html) | 初筛漏筛补录。通过仿真示范生成与四维模仿学习获得人机物品交接策略，并在实体机器人实验验证抓取交接成功率，直接支持机器人控制工程。 | AI 用于工程科学、机器人操作控制、模仿学习、科学训练数据生成 |
| CVPR | [Incremental Nuclei Segmentation from Histopathological Images via Future-class Awareness and Compatibility-inspired Distillation](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Incremental_Nuclei_Segmentation_from_Histopathological_Images_via_Future-class_Awareness_and_CVPR_2024_paper.html) | 初筛漏筛补录。为病理图像细胞核增量分割提出未来类别感知与兼容蒸馏，直接支持计算病理诊断中的新增核类别学习。 | AI 用于生命科学、细胞图像分割、知识蒸馏 |
| CVPR | [Density-Adaptive Model Based on Motif Matrix for Multi-Agent Trajectory Prediction](https://openaccess.thecvf.com/content/CVPR2024/html/Wen_Density-Adaptive_Model_Based_on_Motif_Matrix_for_Multi-Agent_Trajectory_Prediction_CVPR_2024_paper.html) | 初筛漏筛补录。针对交通密度变化，用高阶交互图和自适应网络预测多交通参与者轨迹，在自动驾驶数据上验证。 | AI 用于工程科学、交通参与者轨迹预测、表示学习 |
| CVPR | [E-GPS: Explainable Geometry Problem Solving via Top-Down Solver and Bottom-Up Generator](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_E-GPS_Explainable_Geometry_Problem_Solving_via_Top-Down_Solver_and_Bottom-Up_CVPR_2024_paper.html) | 初筛漏筛补录。针对几何问题求解，将图文转换为形式语言并结合定理预测器、自顶向下求解与自底向上题目生成，实现可解释的数学推理。 | AI 用于数理科学、科学问题推理、数学实例生成、搜索与规划、监督学习 |
| CVPR | [One-Prompt to Segment All Medical Images](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_One-Prompt_to_Segment_All_Medical_Images_CVPR_2024_paper.html) | 初筛漏筛补录。提出一次提示的通用医学影像分割模型，在多模态医学数据及临床人员标注提示上训练并检验未见任务，直接贡献医学成像分析。 | AI 用于生命科学、医学影像分割、小样本学习、科学数据 |
| CVPR | [Tri-Perspective View Decomposition for Geometry-Aware Depth Completion](https://openaccess.thecvf.com/content/CVPR2024/html/Yan_Tri-Perspective_View_Decomposition_for_Geometry-Aware_Depth_Completion_CVPR_2024_paper.html) | 初筛漏筛补录。结合三视角几何表示和图传播网络补全深度，并以手机TOF真实传感数据验证测量重建。 | AI 用于工程科学、自动驾驶感知、工程传感数据重建、几何深度学习、科学数据 |
| CVPR | [Visual Point Cloud Forecasting enables Scalable Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Visual_Point_Cloud_Forecasting_enables_Scalable_Autonomous_Driving_CVPR_2024_paper.html) | 初筛漏筛补录。用视觉历史预测未来三维点云进行预训练，直接服务自动驾驶的感知、运动预测和规划，报告规划碰撞率改善。 | AI 用于工程科学、自动驾驶感知、自动驾驶决策、预训练、表示学习 |
| CVPR | [SG-BEV: Satellite-Guided BEV Fusion for Cross-View Semantic Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Ye_SG-BEV_Satellite-Guided_BEV_Fusion_for_Cross-View_Semantic_Segmentation_CVPR_2024_paper.html) | 初筛漏筛补录。融合卫星与街景学习城市建筑属性分割，在多城市数据上验证细粒度地理建筑信息提取，直接支持城市遥感研究。 | AI 用于地球宇宙科学、建筑属性制图、多模态学习、语义分割 |
| CVPR | [OOSTraj: Out-of-Sight Trajectory Prediction With Vision-Positioning Denoising](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_OOSTraj_Out-of-Sight_Trajectory_Prediction_With_Vision-Positioning_Denoising_CVPR_2024_paper.html) | 初筛漏筛补录。通过无监督视觉定位去噪预测视野外行人轨迹，在机器人/多传感数据集验证遮挡安全感知。 | AI 用于工程科学、行人轨迹预测、传感信号去噪、无监督学习 |
| CVPR | [Spike-guided Motion Deblurring with Unknown Modal Spatiotemporal Alignment](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Spike-guided_Motion_Deblurring_with_Unknown_Modal_Spatiotemporal_Alignment_CVPR_2024_paper.html) | 初筛漏筛补录。针对帧相机和脉冲相机实际时空失配，学习双向对齐与融合以恢复高速运动成像。 | AI 用于工程科学、工程传感数据重建、多模态学习、神经网络 |
| CVPR | [HIMap: HybrId Representation Learning for End-to-end Vectorized HD Map Construction](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_HIMap_HybrId_Representation_Learning_for_End-to-end_Vectorized_HD_Map_Construction_CVPR_2024_paper.html) | 初筛漏筛补录。面向道路高精地图构建，结合点与地图元素级表示及一致性约束解决车道、道路边界等几何结构错误，在两套驾驶数据评测。 | AI 用于工程科学、高精道路地图构建、表示学习 |
| CVPR | [Teeth-SEG: An Efficient Instance Segmentation Framework for Orthodontic Treatment based on Multi-Scale Aggregation and Anthropic Prior Knowledge](https://openaccess.thecvf.com/content/CVPR2024/html/Zou_Teeth-SEG_An_Efficient_Instance_Segmentation_Framework_for_Orthodontic_Treatment_based_CVPR_2024_paper.html) | 初筛漏筛补录。结合牙齿先验与ViT多尺度聚合，对正畸医师标注的15万张口内照片进行牙齿实例分割验证。 | AI 用于生命科学、医学影像分割、Transformer 架构、知识引导学习、科学数据 |
| International Journal of Mining Science and Technology | [Enhancing microseismic/acoustic emission source localization accuracy with an outlier-robust kernel density estimation approach](https://doi.org/10.1016/j.ijmst.2024.07.005) | 初筛漏筛补录。三维核密度估计识别异常到时对应离群定位点，并结合阻尼修正提升微震与声发射源定位，在断铅和现场爆破实验验证工程监测精度。 | AI 用于工程科学、微震声发射源定位、核方法、异常检测 |
| Information Fusion | [Clustering pipeline for vehicle behavior in smart villages](https://doi.org/10.1016/j.inffus.2023.102164) | 初筛漏筛补录。将车牌相机、来源、收入与假日数据融合聚类，分析五万余车辆的乡村游客与居民流动模式，为交通资源规划提供证据。 | AI 用于社会科学、交通场景建模、聚类 |
| Nature Human Behaviour | [Battling the coronavirus ‘infodemic’ among social media users in Kenya and Nigeria](https://www.nature.com/articles/s41562-023-01810-7) | 初筛漏筛补录。上下文自适应分配及数据估计的个体化干预策略用于真实社交媒体随机实验，直接检验并减少疫情错误信息传播。 | AI 用于社会科学、传染病传播干预、策略学习 |
| Nature Human Behaviour | [Web-browsing patterns reflect and shape mood and mental health](https://www.nature.com/articles/s41562-024-02065-6) | 初筛漏筛补录。自然语言处理量化浏览网页文本情绪，结合实验检验信息选择与心理健康的双向因果关系，直接服务心理与社会科学研究。 | AI 用于社会科学、心理健康评估、自然语言处理 |
| Nature Communications | [Predicting proximal tubule failed repair drivers through regularized regression analysis of single cell multiomic sequencing](https://www.nature.com/articles/s41467-024-45706-0) | 初筛漏筛补录。用正则化回归从单细胞RNA和ATAC多组学构建基因调控网络，识别肾损伤修复失败的调控元件及NFAT5驱动因子。 | AI 用于生命科学、基因调控网络推断、正则化学习、多组学整合分析 |
| Nature Communications | [Metabolomic profiles of sleep-disordered breathing are associated with hypertension and diabetes mellitus development](https://www.nature.com/articles/s41467-024-46019-y) | 初筛漏筛补录。以主成分分析和联合惩罚回归提取睡眠呼吸障碍的代谢物签名，并在独立人群验证与后续高血压及糖尿病发生的关联，直接支持疾病风险生物标志物研究。 | AI 用于生命科学、生物标志物发现、疾病风险预测、主成分分析、正则化学习 |
| Nature Communications | [Using rare genetic mutations to revisit structural brain asymmetry](https://www.nature.com/articles/s41467-024-46784-w) | 初筛漏筛补录。通过模式学习和多变量基因—脑—行为融合分析552名CNV携带者及290名对照的脑不对称，识别罕见遗传变异关联的脑侧化模式。 | AI 用于生命科学、影像生物标志物提取、表示学习 |
| Nature Communications | [Neurocomputational mechanisms involved in adaptation to fluctuating intentions of others](https://www.nature.com/articles/s41467-024-47491-2) | 初筛漏筛补录。通过竞争与合作专家间仲裁的学习模型预测人类社会决策，并结合fMRI定位可靠性及预测误差信号，直接解释社会适应的神经计算机制。 | AI 用于生命科学、神经行为联合建模、混合专家 |
| Nature Communications | [scLENS: data-driven signal detection for unbiased scRNA-seq data analysis](https://www.nature.com/articles/s41467-024-47884-3) | 初筛漏筛补录。提出自动信号维度判定和降维方法以恢复单细胞RNA测序生物学信号，解决稀疏高噪数据的分析失真并与多种降维工具比较。 | AI 用于生命科学、单细胞表征学习、降维 |
| Nature Communications | [Revealing the hidden structure of disordered materials by parameterizing their local structural manifold](https://www.nature.com/articles/s41467-024-48449-0) | 初筛漏筛补录。用凝聚聚类和扩散映射学习玻璃局部结构流形，揭示冷却速率与原子局部对称性的关系。 | AI 用于物质科学、材料结构分析、聚类、降维 |
| Nature Communications | [Heterogeneity in strategy use during arbitration between experiential and observational learning](https://www.nature.com/articles/s41467-024-48548-y) | 初筛漏筛补录。构建以预测误差动态加权经验与观察学习的计算模型，并以在线人类行为实验解释策略群体差异及自闭特征、焦虑等维度关联。 | AI 用于社会科学、神经行为联合建模、强化学习 |
| Nature Communications | [Using scalable computer vision to automate high-throughput semiconductor characterization](https://www.nature.com/articles/s41467-024-48768-2) | 初筛漏筛补录。自适应计算机视觉自动提取钙钛矿带隙与环境稳定性，在数百组分上与专家评估核验，直接加速高通量材料表征。 | AI 用于物质科学、材料性质预测、材料稳定性预测、科学评测 |
| Nature Communications | [Partitioning and aggregating cross-tissue and tissue-specific genetic effects to identify gene-trait associations](https://www.nature.com/articles/s41467-024-49924-4) | 初筛漏筛补录。MTWAS通过非参数插补及高维特征筛选整合跨组织基因表达预测，并在GTEx、单细胞及84项GWAS中验证疾病关联发现。 | AI 用于生命科学、转录组分析、特征选择 |
| Nature Communications | [Molecularly specific detection towards trace nitrogen dioxide by utilizing Schottky-junction-based Gas Sensor](https://www.nature.com/articles/s41467-024-50443-5) | 初筛漏筛补录。将阻抗角等多通道传感响应输入主成分分析，辨识12类气体的分子特征并支持痕量二氧化氮检测。 | AI 用于物质科学、化学物质检测、主成分分析 |
| Nature Communications | [Evaluating batch correction methods for image-based cell profiling](https://www.nature.com/articles/s41467-024-50613-5) | 初筛漏筛补录。系统比较Harmony、Seurat RPCA等学习型批次校正方法在Cell Painting细胞图像表型数据中的效果，支持跨实验室生物学数据整合。 | AI 用于生命科学、细胞图像批次校正、科学评测、主成分分析 |
| Nature Communications | [Resilient water infrastructure partnerships in institutionally complex systems face challenging supply and financial risk tradeoffs](https://www.nature.com/articles/s41467-024-51660-8) | 初筛漏筛补录。将多目标智能搜索与水资源系统模拟结合，优化加州供水基础设施投资伙伴关系，量化供水效益与财务风险权衡。 | AI 用于工程科学、水系统控制、多目标优化、搜索与规划 |
| Nature Communications | [scCAD: Cluster decomposition-based anomaly detection for rare cell identification in single-cell expression data](https://www.nature.com/articles/s41467-024-51891-9) | 初筛漏筛补录。scCAD以迭代簇分解和异常检测识别单细胞稀有类型，在25个数据集及癌症案例验证。 | AI 用于生命科学、细胞类型识别、聚类、异常检测 |
| Nature Communications | [Repatterning of mammalian backbone regionalization in cetaceans](https://www.nature.com/articles/s41467-024-51963-w) | 初筛漏筛补录。结合分段回归和谱聚类比较62种鲸类脊椎区域，提出分层区域假说并解释水生运动演化中的骨架重组。 | AI 用于生命科学、生物表型重建、聚类 |
| Nature Communications | [Missing microbial eukaryotes and misleading meta-omic conclusions](https://www.nature.com/articles/s41467-024-52212-w) | 初筛漏筛补录。对环境宏组学数据进行序列聚类和簇重叠分析，改进原生生物分类注释与群落组成推断，属于聚类用于生态数据解释。 | AI 用于生命科学、功能注释、聚类 |
| Nature Communications | [Evolutionarily conserved fMRI network dynamics in the mouse, macaque, and human brain](https://www.nature.com/articles/s41467-024-52721-8) | 初筛漏筛补录。逐帧聚类跨物种fMRI时间序列，发现保守脑共激活模式及动力学组织规律。 | AI 用于生命科学、神经连接推断、聚类 |
| Nature Communications | [Concurrent optoacoustic tomography and magnetic resonance imaging of resting-state functional connectivity in the mouse brain](https://www.nature.com/articles/s41467-024-54947-y) | 初筛漏筛补录。独立成分分析用于分离小鼠脑功能成像信号并比较光声与磁共振功能连接，直接揭示BOLD血流动力学来源。 | AI 用于生命科学、神经连接推断、独立成分分析 |
| Nature Neuroscience | [Inhibitory plasticity supports replay generalization in the hippocampus](https://www.nature.com/articles/s41593-024-01745-w) | 初筛漏筛补录。用Hebbian脉冲时序可塑性规则构建多层次神经计算模型解释海马记忆回放泛化，并经小鼠光遗传实验验证。 | AI 用于生命科学、神经记忆机制建模、脉冲神经网络 |
| Nature Protocols | [Web-based multi-omics integration using the Analyst software suite](https://www.nature.com/articles/s41596-023-00950-4) | 初筛漏筛补录。多组学整合流程通过联合降维和生物网络分析真实胰岛组织及血浆数据，直接支持多组学科学研究，属有实质方法内容的研究流程。 | AI 用于生命科学、多组学整合分析、降维 |
| Nature Protocols | [Identification and validation of microbial biomarkers from cross-cohort datasets using xMarkerFinder](https://www.nature.com/articles/s41596-024-00999-9) | 初筛漏筛补录。跨队列微生物标志物识别框架，以特征选择和分类模型处理队列异质性，并提供内外部验证及疾病诊断机制解释。 | AI 用于生命科学、生物标志物发现、特征选择、机器学习 |

## 标签和元数据

本轮使用109种标签，其中100种复用现有词项，新增9项；共享词表由762项增至771项。提交前再次同步并检查中英文名称、维度和别名，未发现同义重复。未明确支持的方法或训练阶段不标。

| 维度 | 新增中文标签 | 英文 | 适用范围 |
|---|---|---|---|
| method | 独立成分分析 | Independent component analysis | 将多变量观测分解为统计独立成分，用于生物信号或科学数据结构识别。 |
| method | 降维 | Dimensionality reduction | 从高维科学数据提取低维结构或表示，适用于未明确具体算法的降维贡献。 |
| task | 建筑属性制图 | Building attribute mapping | 利用遥感及地面观测推断建筑属性并生成空间分布图。 |
| task | 视觉注视轨迹预测 | Visual scanpath prediction | 根据个体和任务信息预测人类视觉注视位置及其序列。 |
| task | 高精道路地图构建 | High-definition road map construction | 从传感数据构建车道、道路边界等矢量化高精度地图。 |
| task | 交通参与者轨迹预测 | Traffic participant trajectory prediction | 预测车辆、行人等道路交通参与者的未来运动轨迹。 |
| task | 微震声发射源定位 | Microseismic and acoustic emission source localization | 从监测信号估计微震或声发射事件空间位置，服务岩土工程及结构安全监测。 |
| task | 细胞图像批次校正 | Cell image batch correction | 校正细胞成像表型数据跨批次、设备或实验室的系统性差异。 |
| task | 手物接触估计 | Hand-object contact estimation | 从观测数据重建手与物体的抓握接触区域，服务操作测量与接触行为研究。 |

- 75篇正式页面引用元数据已核对；65篇取得题名、年份匹配的Crossref书目；67篇核实DOI。作者字段冲突及访问失败记录在逐条审计中，未核实值不当作已核实。
- 53个公开PDF端点通过HTTP HEAD检查，其他端点留空或标为未核验。未下载或读取PDF。代码／项目链接保留原数据，本轮未声明新增可用性核验。

## 累计进度与剩余工作

| 指标 | 累计 |
|---|---|
| 已审 | 20,333条 |
| 纳入 | 2,534篇 |
| 排除 | 16,608条（无AI4S实质关系、非研究文种或不属本批范围） |
| 待定 | 1,191条（证据不足或摘要问题） |
| 漏筛纳入 | 1,383篇（已含在纳入总数内） |
| 核验补齐完整摘要 | 1,712条 |
| 尚未审核 | 10,135条 |

**剩余3,170条有供给摘要／待核描述可继续，另6,965条缺可用摘要暂缓。** 两者合计10,135条未审；已审待定1,191条另列。全量审核和官网补漏尚未完成。

唯一键、原字段、旧17,333条完整记录、标签规范和数量闭合校验通过：20,333已审＋10,135未审＝30,468。跨审核同键重合890条、判定不同46条，本轮新增重合0条；仅作审计，未修改他人文件或负责人登记。

交付：[个人JSON](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101.json)、[累计统计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/summary.json)、[逐条审计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation13-batch-decisions.jsonl)、[抽查记录](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation13-batch-qc.json)。实际上传以GitHub提交和本地publication.json为准。
