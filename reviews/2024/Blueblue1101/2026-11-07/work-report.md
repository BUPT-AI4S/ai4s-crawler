# 王婉婷｜AI4S论文摘要精筛阶段工作汇报

2026年11月8日 · 2024年论文 · Blueblue1101 · continuation14

**剩余3,170条已有摘要／待核描述全部处理：纳入90篇、排除2,941条、待定139条。当前已有摘要队列清零。** 本轮覆盖28个来源，核验补齐完整摘要513条，原20,333条交付记录保持不变。

累计已审**23,503条**，其中纳入**2,624篇**。另有**6,965条缺可用摘要的记录暂缓**；已审记录中的**1,330条待定**仍需补证。这两类分开统计，不能将已有摘要队列完成等同于全部论文与官网补漏完成。

## 复核方法与结果

按main当前skill，用科学／工程任务、AI实质作用及二者关系判断。批量读取摘要、逐条保存结论、理由和摘要哈希；未读取正文或PDF，未用关键词匹配替代判断。提交前已同步main `af22785`，规则和词表与本轮起点一致。

92篇拟纳入全部复核，最终保留90篇：有机食品鉴别综述因摘要开头残缺改为待定；医疗物联网综述因AI研究深度不足以确认改为待定。固定随机种子抽查30条排除记录，维持原结论；抽查不能代表全量准确率。

| 结果 | 本轮条数 | 原因 |
|---|---|---|
| 纳入 | 90 | 明确科学／工程任务，且摘要支持AI实质作用 |
| 相关性排除 | 2896 | 未显示AI实质参与，或通用模型／基准缺少具体科学研究贡献 |
| 文献类型排除 | 45 | 评论、观点、指南／共识、更正、撤稿等，不属本批原创研究与实质综述 |
| 待定 | 139 | 120条AI作用／贡献证据不足或摘要待补，19条明显片段／错配等无效描述 |

## 各刊会本轮工作量

本轮**新爬0篇**；新增90篇均是已采集记录中的**关键词漏筛补录**。“补齐摘要”是将已取得、已核验的完整书目摘要写回元数据，不与纳入篇数相加；残缺摘要未计入补齐量。

| 刊会 | 本轮已审 | 新爬 | 纳入 | 排除 | 待定 | 补齐摘要 |
|---|---|---|---|---|---|---|
| Nature Communications | 1303 | 0 | 14 | 1249 | 40 | 0 |
| CVPR | 352 | 0 | 58 | 265 | 29 | 0 |
| Clinical Gastroenterology and Hepatology | 178 | 0 | 4 | 165 | 9 | 123 |
| Journal of Advanced Research | 165 | 0 | 1 | 156 | 8 | 165 |
| The Lancet Regional Health - Europe | 155 | 0 | 2 | 147 | 6 | 9 |
| Nature Protocols | 105 | 0 | 0 | 100 | 5 | 0 |
| Nature Ecology & Evolution | 100 | 0 | 1 | 96 | 3 | 0 |
| Nature Geoscience | 90 | 0 | 1 | 88 | 1 | 0 |
| The Lancet Planetary Health | 89 | 0 | 2 | 85 | 2 | 0 |
| Trends in Food Science & Technology | 84 | 0 | 0 | 76 | 8 | 35 |
| Nano Energy | 80 | 0 | 1 | 78 | 1 | 41 |
| International Journal of Mining Science and Technology | 73 | 0 | 0 | 73 | 0 | 0 |
| The Lancet Haematology | 59 | 0 | 0 | 58 | 1 | 47 |
| Energy Storage Materials | 48 | 0 | 0 | 48 | 0 | 2 |
| Nature Physics | 42 | 0 | 0 | 42 | 0 | 0 |
| Cell Discovery | 37 | 0 | 1 | 25 | 11 | 0 |
| Molecular Neurodegeneration | 36 | 0 | 0 | 33 | 3 | 0 |
| Journal of Materials Science & Technology | 31 | 0 | 0 | 31 | 0 | 29 |
| Smart Learning Environments | 28 | 0 | 0 | 24 | 4 | 0 |
| Journal of Energy Chemistry | 27 | 0 | 0 | 27 | 0 | 17 |
| Nature Human Behaviour | 24 | 0 | 2 | 20 | 2 | 0 |
| Information Fusion | 20 | 0 | 3 | 13 | 4 | 20 |
| Seminars in Cancer Biology | 19 | 0 | 0 | 19 | 0 | 19 |
| Chem | 8 | 0 | 0 | 6 | 2 | 3 |
| Nature Microbiology | 6 | 0 | 0 | 6 | 0 | 0 |
| Molecular Cell | 5 | 0 | 0 | 5 | 0 | 0 |
| Trends in Microbiology | 4 | 0 | 0 | 4 | 0 | 3 |
| Nature Neuroscience | 2 | 0 | 0 | 2 | 0 | 0 |
| **合计** | 3170 | 0 | 90 | 2941 | 139 | 513 |

## 新增纳入论文及标签

| 刊会 | 论文 | 摘要判断依据 | 标签 |
|---|---|---|---|
| CVPR | [Coupled Laplacian Eigenmaps for Locally-Aware 3D Rigid Point Cloud Matching](https://openaccess.thecvf.com/content/CVPR2024/html/Bastico_Coupled_Laplacian_Eigenmaps_for_Locally-Aware_3D_Rigid_Point_Cloud_Matching_CVPR_2024_paper.html) | 初筛漏筛补录。通过耦合拉普拉斯特征映射学习局部形状匹配，提出自动骨侧识别医学任务和专用骨表面评测。 | AI 用于生命科学、医学解剖形态建模、降维、图匹配 |
| CVPR | [FocusMAE: Gallbladder Cancer Detection from Ultrasound Videos with Focused Masked Autoencoders](https://openaccess.thecvf.com/content/CVPR2024/html/Basu_FocusMAE_Gallbladder_Cancer_Detection_from_Ultrasound_Videos_with_Focused_Masked_CVPR_2024_paper.html) | 初筛漏筛补录。以聚焦掩码自编码器学习超声视频时空表征用于胆囊癌检测，构建专病视频数据并验证诊断准确率。 | AI 用于生命科学、肿瘤检测、掩码建模、自编码器、科学数据 |
| CVPR | [Learning to Navigate Efficiently and Precisely in Real Environments](https://openaccess.thecvf.com/content/CVPR2024/html/Bono_Learning_to_Navigate_Efficiently_and_Precisely_in_Real_Environments_CVPR_2024_paper.html) | 初筛漏筛补录。通过机器人动力学、传感噪声建模和仿真端到端训练降低仿真到现实差距，在实体机器人导航中验证性能与鲁棒性。 | AI 用于工程科学、机器人航迹规划、策略学习、物理与数据融合建模 |
| CVPR | [Rolling Shutter Correction with Intermediate Distortion Flow Estimation](https://openaccess.thecvf.com/content/CVPR2024/html/Cao_Rolling_Shutter_Correction_with_Intermediate_Distortion_Flow_Estimation_CVPR_2024_paper.html) | 初筛漏筛补录。针对滚动快门物理成像的非线性运动失真，以注意力网络估计畸变流并重建全局快门图像。 | AI 用于工程科学、工程传感数据重建、注意力机制 |
| CVPR | [Each Test Image Deserves A Specific Prompt: Continual Test-Time Adaptation for 2D Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Each_Test_Image_Deserves_A_Specific_Prompt_Continual_Test-Time_Adaptation_CVPR_2024_paper.html) | 初筛漏筛补录。针对医疗中心间连续分布变化，设计逐图像视觉提示与记忆机制，改善医学图像分割并避免模型遗忘。 | AI 用于生命科学、医学影像分割、领域适应、提示学习 |
| CVPR | [Differentiable Display Photometric Stereo](https://openaccess.thecvf.com/content/CVPR2024/html/Choi_Differentiable_Display_Photometric_Stereo_CVPR_2024_paper.html) | 初筛漏筛补录。端到端学习显示屏照明图案，结合可微光度立体与真实3D打印训练样本，提高物理测量系统的表面法向重建精度。 | AI 用于工程科学、工程传感数据重建、可微优化、科学训练数据生成 |
| CVPR | [Super-Resolution Reconstruction from Bayer-Pattern Spike Streams](https://openaccess.thecvf.com/content/CVPR2024/html/Dong_Super-Resolution_Reconstruction_from_Bayer-Pattern_Spike_Streams_CVPR_2024_paper.html) | 初筛漏筛补录。针对彩色脉冲相机空间分辨率限制，结合拜耳排列、亚像素运动与特征学习重建高时空分辨率图像。 | AI 用于工程科学、工程传感数据重建、图像超分辨率、神经网络 |
| CVPR | [Continuous Optical Zooming: A Benchmark for Arbitrary-Scale Image Super-Resolution in Real World](https://openaccess.thecvf.com/content/CVPR2024/html/Fu_Continuous_Optical_Zooming_A_Benchmark_for_Arbitrary-Scale_Image_Super-Resolution_in_CVPR_2024_paper.html) | 初筛漏筛补录。自动光学变焦系统采集严格对齐的真实图像，结合局部混合隐式网络解决真实光学退化下任意倍率超分辨率。 | AI 用于工程科学、图像超分辨率、多层感知机、元学习、科学数据 |
| CVPR | [Weak-to-Strong 3D Object Detection with X-Ray Distillation](https://openaccess.thecvf.com/content/CVPR2024/html/Gambashidze_Weak-to-Strong_3D_Object_Detection_with_X-Ray_Distillation_CVPR_2024_paper.html) | 初筛漏筛补录。针对自动驾驶激光雷达遮挡与稀疏观测，构建多时刻完整物体教师并蒸馏到在线检测网络，提高驾驶感知性能。 | AI 用于工程科学、自动驾驶感知、目标检测、知识蒸馏 |
| CVPR | [Vanishing-Point-Guided Video Semantic Segmentation of Driving Scenes](https://openaccess.thecvf.com/content/CVPR2024/html/Guo_Vanishing-Point-Guided_Video_Semantic_Segmentation_of_Driving_Scenes_CVPR_2024_paper.html) | 初筛漏筛补录。结合道路消失点及前向车辆运动先验设计时序分割网络，改进远处道路目标感知。 | AI 用于工程科学、自动驾驶感知、语义分割、知识引导学习 |
| CVPR | [Bridging Remote Sensors with Multisensor Geospatial Foundation Models](https://openaccess.thecvf.com/content/CVPR2024/html/Han_Bridging_Remote_Sensors_with_Multisensor_Geospatial_Foundation_Models_CVPR_2024_paper.html) | 初筛漏筛补录。面向四类遥感传感器预训练联合表征，使用两百万遥感图像，支持地理场景分析、云去除和全色锐化，直接改进地理观测数据处理。 | AI 用于地球宇宙科学、遥感影像分析、多模态学习、掩码建模、预训练、科学基础模型 |
| CVPR | [360Loc: A Dataset and Benchmark for Omnidirectional Visual Localization with Cross-device Queries](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_360Loc_A_Dataset_and_Benchmark_for_Omnidirectional_Visual_Localization_with_CVPR_2024_paper.html) | 初筛漏筛补录。建立全景相机与激光雷达真值定位资源，设计虚拟相机跨设备适配并验证特征匹配和位姿回归定位。 | AI 用于工程科学、机器人定位、领域适应、科学数据、科学评测 |
| CVPR | [Bilateral Event Mining and Complementary for Event Stream Super-Resolution](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_Bilateral_Event_Mining_and_Complementary_for_Event_Stream_Super-Resolution_CVPR_2024_paper.html) | 初筛漏筛补录。针对事件相机空间分辨率不足，双流网络分别建模正负事件并交换信息，改善真实传感器事件流及成像重建。 | AI 用于工程科学、工程传感数据重建、神经网络、图像超分辨率 |
| CVPR | [PH-Net: Semi-Supervised Breast Lesion Segmentation via Patch-wise Hardness](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_PH-Net_Semi-Supervised_Breast_Lesion_Segmentation_via_Patch-wise_Hardness_CVPR_2024_paper.html) | 初筛漏筛补录。针对乳腺超声噪声及病灶模糊边界，利用困难图块增广和对比学习改进半监督病灶分割。 | AI 用于生命科学、医学影像分割、半监督学习、对比学习、数据增强 |
| CVPR | [Continual Learning for Motion Prediction Model via Meta-Representation Learning and Optimal Memory Buffer Retention Strategy](https://openaccess.thecvf.com/content/CVPR2024/html/Kang_Continual_Learning_for_Motion_Prediction_Model_via_Meta-Representation_Learning_and_CVPR_2024_paper.html) | 初筛漏筛补录。针对自动驾驶道路与车辆状态分布变化，以稀疏元表征和记忆样本保留实现持续运动预测。 | AI 用于工程科学、交通参与者轨迹预测、元学习、表示学习、在线学习 |
| CVPR | [Frequency-aware Event-based Video Deblurring for Real-World Motion Blur](https://openaccess.thecvf.com/content/CVPR2024/html/Kim_Frequency-aware_Event-based_Video_Deblurring_for_Real-World_Motion_Blur_CVPR_2024_paper.html) | 初筛漏筛补录。频域跨模态神经特征与事件引导对齐解决真实相机运动模糊，并构建同步混合相机采集平台及数据集。 | AI 用于工程科学、工程传感数据重建、多模态学习、科学数据 |
| CVPR | [Uncertainty-Guided Never-Ending Learning to Drive](https://openaccess.thecvf.com/content/CVPR2024/html/Lai_Uncertainty-Guided_Never-Ending_Learning_to_Drive_CVPR_2024_paper.html) | 初筛漏筛补录。面向自动驾驶连续视频学习，结合逆动力学伪标签、不确定性探索及一致性净化以适应驾驶域变化。 | AI 用于工程科学、自动驾驶决策、自训练、知识蒸馏、不确定性量化 |
| CVPR | [Is Ego Status All You Need for Open-Loop End-to-End Autonomous Driving?](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Is_Ego_Status_All_You_Need_for_Open-Loop_End-to-End_Autonomous_CVPR_2024_paper.html) | 初筛漏筛补录。审计自动驾驶端到端规划对自车状态的依赖和评测偏差，提出道路约束轨迹指标以改进驾驶模型验证。 | AI 用于工程科学、自动驾驶决策、科学评测 |
| CVPR | [Towards Robust Event-guided Low-Light Image Enhancement: A Large-Scale Real-World Event-Image Dataset and Novel Approach](https://openaccess.thecvf.com/content/CVPR2024/html/Liang_Towards_Robust_Event-guided_Low-Light_Image_Enhancement_A_Large-Scale_Real-World_Event-Image_CVPR_2024_paper.html) | 初筛漏筛补录。机器人精确采集对齐的事件与低照图像，利用信噪比引导多模态特征融合改善真实低照成像。 | AI 用于工程科学、工程传感数据重建、多模态学习、科学数据 |
| CVPR | [Localization Is All You Evaluate: Data Leakage in Online Mapping Datasets and How to Fix It](https://openaccess.thecvf.com/content/CVPR2024/html/Lilja_Localization_Is_All_You_Evaluate_Data_Leakage_in_Online_Mapping_CVPR_2024_paper.html) | 初筛漏筛补录。揭示自动驾驶在线地图学习中的地理数据泄漏，并提供不重叠划分和复评，直接改进工程地图泛化评估。 | AI 用于工程科学、高精道路地图构建、科学评测 |
| CVPR | [Extend Your Own Correspondences: Unsupervised Distant Point Cloud Registration by Progressive Distance Extension](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Extend_Your_Own_Correspondences_Unsupervised_Distant_Point_Cloud_Registration_by_CVPR_2024_paper.html) | 初筛漏筛补录。无监督渐进距离扩展学习实现远距离车辆点云配准，面向协同驾驶的完整三维场景感知。 | AI 用于工程科学、自动驾驶感知、自监督学习、表示学习 |
| CVPR | [Instantaneous Perception of Moving Objects in 3D](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Instantaneous_Perception_of_Moving_Objects_in_3D_CVPR_2024_paper.html) | 初筛漏筛补录。针对交通参与者起步微小运动引发的激光雷达混淆，联合学习占据补全和瞬时运动估计，改进安全相关运动感知。 | AI 用于工程科学、自动驾驶感知、交通目标跟踪、深度学习 |
| CVPR | [Cam4DOcc: Benchmark for Camera-Only 4D Occupancy Forecasting in Autonomous Driving Applications](https://openaccess.thecvf.com/content/CVPR2024/html/Ma_Cam4DOcc_Benchmark_for_Camera-Only_4D_Occupancy_Forecasting_in_Autonomous_Driving_CVPR_2024_paper.html) | 初筛漏筛补录。构建自动驾驶未来4D占据状态及运动流数据和评测协议，提供预测网络以研究道路动态环境安全感知。 | AI 用于工程科学、交通场景建模、自动驾驶感知、科学数据、科学评测 |
| CVPR | [Constructing and Exploring Intermediate Domains in Mixed Domain Semi-supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Ma_Constructing_and_Exploring_Intermediate_Domains_in_Mixed_Domain_Semi-supervised_Medical_CVPR_2024_paper.html) | 初筛漏筛补录。针对多医疗中心有限标注及域偏移，设计中间域复制粘贴与对称监督，改善医学影像分割。 | AI 用于生命科学、医学影像分割、半监督学习、领域适应、数据增强 |
| CVPR | [Explaining CLIP's Performance Disparities on Data from Blind/Low Vision Users](https://openaccess.thecvf.com/content/CVPR2024/html/Massiceti_Explaining_CLIPs_Performance_Disparities_on_Data_from_BlindLow_Vision_Users_CVPR_2024_paper.html) | 初筛漏筛补录。基于盲人和低视力用户采集数据系统评估CLIP服务差异，定位照明、残障物品和触觉描述偏差并验证少样本缓解。 | AI 用于社会科学、视觉语言模型、科学评测、小样本学习 |
| CVPR | [DriveWorld: 4D Pre-trained Scene Understanding via World Models for Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2024/html/Min_DriveWorld_4D_Pre-trained_Scene_Understanding_via_World_Models_for_Autonomous_CVPR_2024_paper.html) | 初筛漏筛补录。针对自动驾驶动态场景构建时空世界模型预训练，覆盖感知、预测和规划等驾驶任务并量化性能。 | AI 用于工程科学、自动驾驶感知、状态空间建模、表示学习、预训练 |
| CVPR | [MCD: Diverse Large-Scale Multi-Campus Dataset for Robot Perception](https://openaccess.thecvf.com/content/CVPR2024/html/Nguyen_MCD_Diverse_Large-Scale_Multi-Campus_Dataset_for_Robot_Perception_CVPR_2024_paper.html) | 初筛漏筛补录。构建多传感器多校园机器人感知数据集，以29类激光语义标注和算法评测直接支撑机器人导航与感知研究。 | AI 用于工程科学、机器人定位、科学数据、科学评测 |
| CVPR | [OpticalDR: A Deep Optical Imaging Model for Privacy-Protective Depression Recognition](https://openaccess.thecvf.com/content/CVPR2024/html/Pan_OpticalDR_A_Deep_Optical_Imaging_Model_for_Privacy-Protective_Depression_Recognition_CVPR_2024_paper.html) | 初筛漏筛补录。联合学习去身份光学透镜及抑郁识别网络，保留疾病相关表征并验证临床情感分析数据。 | AI 用于生命科学、心理健康评估、深度学习、隐私保护学习 |
| CVPR | [M3-UDA: A New Benchmark for Unsupervised Domain Adaptive Fetal Cardiac Structure Detection](https://openaccess.thecvf.com/content/CVPR2024/html/Pu_M3-UDA_A_New_Benchmark_for_Unsupervised_Domain_Adaptive_Fetal_Cardiac_CVPR_2024_paper.html) | 初筛漏筛补录。收集双医院胎儿心脏结构数据，采用解剖拓扑匹配的域自适应检测，支持先天性心脏病诊断。 | AI 用于生命科学、医学解剖结构检测、领域适应、知识引导学习、科学数据 |
| CVPR | [From a Bird's Eye View to See: Joint Camera and Subject Registration without the Camera Calibration](https://openaccess.thecvf.com/content/CVPR2024/html/Qian_From_a_Birds_Eye_View_to_See_Joint_Camera_and_CVPR_2024_paper.html) | 初筛漏筛补录。针对无预先标定的多相机空间测量，联合学习视图变换、几何对齐和人机位置方向注册，并进行真实跨域验证。 | AI 用于工程科学、传感器校准、人体姿态识别、几何深度学习、科学数据 |
| CVPR | [Making Visual Sense of Oracle Bones for You and Me](https://openaccess.thecvf.com/content/CVPR2024/html/Qiao_Making_Visual_Sense_of_Oracle_Bones_for_You_and_Me_CVPR_2024_paper.html) | 初筛漏筛补录。利用GPT-4V推理与生成模型辅助甲骨文字形理解，通过人类实验和专门指标验证文化遗产解释效果。 | AI 用于社会科学、文化遗产视觉阐释、视觉语言模型、生成建模 |
| CVPR | [A Simple and Effective Point-based Network for Event Camera 6-DOFs Pose Relocalization](https://openaccess.thecvf.com/content/CVPR2024/html/Ren_A_Simple_and_Effective_Point-based_Network_for_Event_Camera_6-DOFs_CVPR_2024_paper.html) | 初筛漏筛补录。利用事件相机稀疏高时间分辨信号，结合时空层级特征与双向LSTM估计相机六自由度姿态。 | AI 用于工程科学、机器人定位、长短期记忆网络、注意力机制 |
| CVPR | [Projecting Trackable Thermal Patterns for Dynamic Computer Vision](https://openaccess.thecvf.com/content/CVPR2024/html/Sheinin_Projecting_Trackable_Thermal_Patterns_for_Dynamic_Computer_Vision_CVPR_2024_paper.html) | 初筛漏筛补录。构建激光热投影与热成像系统，并训练网络反演热扩散与去除不一致点，验证无纹理物体动态测量。 | AI 用于工程科学、工程传感数据重建、神经网络、物理与数据融合建模 |
| CVPR | [Towards Real-World HDR Video Reconstruction: A Large-Scale Benchmark Dataset and A Two-Stage Alignment Network](https://openaccess.thecvf.com/content/CVPR2024/html/Shu_Towards_Real-World_HDR_Video_Reconstruction_A_Large-Scale_Benchmark_Dataset_and_CVPR_2024_paper.html) | 初筛漏筛补录。建立真实交替曝光HDR视频采集基准并设计双阶段运动对齐网络，解决真实成像中曝光与运动重建问题。 | AI 用于工程科学、工程传感数据重建、卷积神经网络、科学数据 |
| CVPR | [BioCLIP: A Vision Foundation Model for the Tree of Life](https://openaccess.thecvf.com/content/CVPR2024/html/Stevens_BioCLIP_A_Vision_Foundation_Model_for_the_Tree_of_Life_CVPR_2024_paper.html) | 初筛漏筛补录。构建千万级生物图像数据与BioCLIP基础模型，利用生命树分类结构改善物种细粒度识别与生物信息提取。 | AI 用于生命科学、野生动物识别、视觉语言模型、科学基础模型、科学数据 |
| CVPR | [BodyMAP - Jointly Predicting Body Mesh and 3D Applied Pressure Map for People in Bed](https://openaccess.thecvf.com/content/CVPR2024/html/Tandon_BodyMAP_-_Jointly_Predicting_Body_Mesh_and_3D_Applied_Pressure_CVPR_2024_paper.html) | 初筛漏筛补录。融合床垫压力和深度图，学习人体三维形态及体表压力分布，在真实人体数据验证以支持压疮预防。 | AI 用于生命科学、人体姿态识别、多模态学习、可微优化 |
| CVPR | [HPNet: Dynamic Trajectory Forecasting with Historical Prediction Attention](https://openaccess.thecvf.com/content/CVPR2024/html/Tang_HPNet_Dynamic_Trajectory_Forecasting_with_Historical_Prediction_Attention_CVPR_2024_paper.html) | 初筛漏筛补录。针对自动驾驶连续轨迹预测的时间不一致问题，引入历史预测注意力并验证稳定性。 | AI 用于工程科学、交通参与者轨迹预测、注意力机制 |
| CVPR | [SPIN: Simultaneous Perception Interaction and Navigation](https://openaccess.thecvf.com/content/CVPR2024/html/Uppal_SPIN_Simultaneous_Perception_Interaction_and_Navigation_CVPR_2024_paper.html) | 初筛漏筛补录。移动机械臂学习主动视觉、全身与手眼协调，解决杂乱环境下感知和操作的联合工程问题。 | AI 用于工程科学、机器人操作控制、机器人航迹规划、策略学习 |
| CVPR | [CPR-Coach: Recognizing Composite Error Actions based on Single-class Training](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_CPR-Coach_Recognizing_Composite_Error_Actions_based_on_Single-class_Training_CVPR_2024_paper.html) | 初筛漏筛补录。构建心肺复苏错误动作数据与识别模型，通过部署实验验证医疗技能评估，AI直接参与医学训练研究。 | AI 用于生命科学、医疗操作技能评估、深度学习、科学数据 |
| CVPR | [Depth-Aware Concealed Crop Detection in Dense Agricultural Scenes](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Depth-Aware_Concealed_Crop_Detection_in_Dense_Agricultural_Scenes_CVPR_2024_paper.html) | 初筛漏筛补录。面向密集农业场景提出RGB-D作物数据与递归分割网络，融合深度缓解遮挡并检测小型隐蔽作物。 | AI 用于生命科学、目标检测、多模态学习、注意力机制、科学数据 |
| CVPR | [FreeMan: Towards Benchmarking 3D Human Pose Estimation under Real-World Conditions](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_FreeMan_Towards_Benchmarking_3D_Human_Pose_Estimation_under_Real-World_Conditions_CVPR_2024_paper.html) | 初筛漏筛补录。构建同步八手机真实多场景人体运动采集与半自动标注资源，验证三维人体感知的真实环境迁移能力。 | AI 用于工程科学、人体姿态识别、科学数据、科学评测 |
| CVPR | [PACER+: On-Demand Pedestrian Animation Controller in Driving Scenarios](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_PACER_On-Demand_Pedestrian_Animation_Controller_in_Driving_Scenarios_CVPR_2024_paper.html) | 初筛漏筛补录。针对自动驾驶仿真中行人运动多样性与可控性不足，学习联合轨迹跟随和动作跟踪策略以生成可控交通参与者行为。 | AI 用于工程科学、交通场景建模、策略学习、科学训练数据生成 |
| CVPR | [Real-IAD: A Real-World Multi-View Dataset for Benchmarking Versatile Industrial Anomaly Detection](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Real-IAD_A_Real-World_Multi-View_Dataset_for_Benchmarking_Versatile_Industrial_Anomaly_CVPR_2024_paper.html) | 初筛漏筛补录。构建真实工业多视角缺陷数据与样本级指标，并基于生产良品率提出全无监督检测设置，直接服务制造质量研究。 | AI 用于工程科学、工业缺陷检测、无监督学习、科学数据、科学评测 |
| CVPR | [View From Above: Orthogonal-View aware Cross-view Localization](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_View_From_Above_Orthogonal-View_aware_Cross-view_Localization_CVPR_2024_paper.html) | 初筛漏筛补录。利用航空正射视图特征聚合与域适应完成车辆跨视角地理定位，验证整条路线连续位姿估计。 | AI 用于工程科学、机器人定位、领域适应、表示学习 |
| CVPR | [HDRFlow: Real-Time HDR Video Reconstruction with Large Motions](https://openaccess.thecvf.com/content/CVPR2024/html/Xu_HDRFlow_Real-Time_HDR_Video_Reconstruction_with_Large_Motions_CVPR_2024_paper.html) | 初筛漏筛补录。针对交替曝光视频的运动重影与实时成像约束，提出HDR专用光流学习及曝光域损失，实现实时高动态范围重建。 | AI 用于工程科学、工程传感数据重建、神经网络 |
| CVPR | [RELI11D: A Comprehensive Multimodal Human Motion Dataset and Method](https://openaccess.thecvf.com/content/CVPR2024/html/Yan_RELI11D_A_Comprehensive_Multimodal_Human_Motion_Dataset_and_Method_CVPR_2024_paper.html) | 初筛漏筛补录。整合同步激光雷达、IMU、RGB和事件相机建立体育运动测量数据，通过跨注意力融合改善快速复杂动作的姿态与位置恢复。 | AI 用于工程科学、人体姿态识别、多模态学习、注意力机制、科学数据 |
| CVPR | [Physical Backdoor: Towards Temperature-based Backdoor Attacks in the Physical World](https://openaccess.thecvf.com/content/CVPR2024/html/Yin_Physical_Backdoor_Towards_Temperature-based_Backdoor_Attacks_in_the_Physical_World_CVPR_2024_paper.html) | 初筛漏筛补录。针对热红外感知系统安全研究温度、材料与隐蔽性对后门攻击的作用，并在真实路口和停车场进行相机实验。 | AI 用于工程科学、自动驾驶感知、科学评测 |
| CVPR | [Dispel Darkness for Better Fusion: A Controllable Visual Enhancer based on Cross-modal Conditional Adversarial Learning](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Dispel_Darkness_for_Better_Fusion_A_Controllable_Visual_Enhancer_based_CVPR_2024_paper.html) | 初筛漏筛补录。利用红外成像的光照稳定性指导低照可见光恢复，设计跨模态对抗学习与信息融合提升昼夜多传感器成像。 | AI 用于工程科学、工程传感数据重建、生成对抗网络、多模态学习 |
| CVPR | [Dual Prior Unfolding for Snapshot Compressive Imaging](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Dual_Prior_Unfolding_for_Snapshot_Compressive_Imaging_CVPR_2024_paper.html) | 初筛漏筛补录。针对快照压缩成像物理逆问题，联合图像与退化残差深度先验展开，提高重建精度与计算效率。 | AI 用于工程科学、工程传感数据重建、物理与数据融合建模、注意力机制 |
| CVPR | [LUWA Dataset: Learning Lithic Use-Wear Analysis on Microscopic Images](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_LUWA_Dataset_Learning_Lithic_Use-Wear_Analysis_on_Microscopic_Images_CVPR_2024_paper.html) | 初筛漏筛补录。与考古学家构建石器磨损显微图像数据集，评估预训练与少样本模型识别加工材料，直接服务考古工具功能研究。 | AI 用于社会科学、考古器物使用痕迹分析、小样本学习、科学数据、科学评测 |
| CVPR | [Leveraging Frame Affinity for sRGB-to-RAW Video De-rendering](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Leveraging_Frame_Affinity_for_sRGB-to-RAW_Video_De-rendering_CVPR_2024_paper.html) | 初筛漏筛补录。针对移动相机RAW视频采集受限，学习时空映射重建RAW数据并构建专门成像评测基准。 | AI 用于工程科学、工程传感数据重建、神经网络 |
| CVPR | [MMVP: A Multimodal MoCap Dataset with Vision and Pressure Sensors](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_MMVP_A_Multimodal_MoCap_Dataset_with_Vision_and_Pressure_Sensors_CVPR_2024_paper.html) | 初筛漏筛补录。构建足底压力与RGB-D同步人体运动资源并提出动作捕获基线，改善足接触及全局位移的物理测量精度。 | AI 用于工程科学、人体姿态识别、多模态学习、科学数据 |
| CVPR | [SAFDNet: A Simple and Effective Network for Fully Sparse 3D Object Detection](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_SAFDNet_A_Simple_and_Effective_Network_for_Fully_Sparse_3D_CVPR_2024_paper.html) | 初筛漏筛补录。针对自动驾驶远距激光雷达感知的计算扩展问题，提出稀疏特征扩散检测网络并验证长距离准确率及速度。 | AI 用于工程科学、自动驾驶感知、目标检测、深度学习 |
| CVPR | [Boosting Spike Camera Image Reconstruction from a Perspective of Dealing with Spike Fluctuations](https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_Boosting_Spike_Camera_Image_Reconstruction_from_a_Perspective_of_Dealing_CVPR_2024_paper.html) | 初筛漏筛补录。结合光子泊松噪声及脉冲量化机制，设计神经特征对齐重建并在真实脉冲相机数据验证。 | AI 用于工程科学、工程传感数据重建、物理与数据融合建模、注意力机制 |
| CVPR | [CoralSCOP: Segment any COral Image on this Planet](https://openaccess.thecvf.com/content/CVPR2024/html/Zheng_CoralSCOP_Segment_any_COral_Image_on_this_Planet_CVPR_2024_paper.html) | 初筛漏筛补录。针对珊瑚生长形态和属级生态分析构建密集标注数据及语义分割基础模型，直接支持珊瑚礁监测。 | AI 用于生命科学、语义分割、零样本学习、科学基础模型、科学数据 |
| CVPR | [Bring Event into RGB and LiDAR: Hierarchical Visual-Motion Fusion for Scene Flow](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_Bring_Event_into_RGB_and_LiDAR_Hierarchical_Visual-Motion_Fusion_for_CVPR_2024_paper.html) | 初筛漏筛补录。以事件相机桥接RGB与激光雷达的物理互补性，设计分层视觉运动融合进行三维场景流测量。 | AI 用于工程科学、工程传感数据重建、多模态学习 |
| CVPR | [Infrared Adversarial Car Stickers](https://openaccess.thecvf.com/content/CVPR2024/html/Zhu_Infrared_Adversarial_Car_Stickers_CVPR_2024_paper.html) | 初筛漏筛补录。针对红外自动驾驶感知构建车辆物理攻击模型，制作铝贴纸并在真实车辆和不同视角距离下验证安全漏洞。 | AI 用于工程科学、自动驾驶感知、科学评测 |
| CVPR | [VAREN: Very Accurate and Realistic Equine Network](https://openaccess.thecvf.com/content/CVPR2024/html/Zuffi_VAREN_Very_Accurate_and_Realistic_Equine_Network_CVPR_2024_paper.html) | 初筛漏筛补录。从真实马体三维扫描学习带解剖骨架与肌肉形变的参数模型，用于分析关节运动与肌肉变形关系。 | AI 用于生命科学、生物表型重建、表示学习、科学数据 |
| Clinical Gastroenterology and Hepatology | [High-Dimensional Clustering of 4000 Irritable Bowel Syndrome Patients Reveals Seven Distinct Disease Subsets](https://doi.org/10.1016/j.cgh.2022.09.019) | 初筛漏筛补录。对4021例IBS患者开展潜在类别模型聚类，识别七种临床饮食心理疾病亚型，用于疾病异质性研究。 | AI 用于生命科学、疾病分型、聚类、潜变量建模 |
| Clinical Gastroenterology and Hepatology | [Novel Symptom Subgroups in Individuals With Irritable Bowel Syndrome Predict Disease Impact and Burden](https://doi.org/10.1016/j.cgh.2023.02.016) | 初筛漏筛补录。将潜在类别分析模型应用于独立IBS人群，识别七种症状亚群并验证生活质量及疾病负担差异。 | AI 用于生命科学、疾病分型、聚类、潜变量建模 |
| Clinical Gastroenterology and Hepatology | [The Association Between a Mediterranean Diet and Symptoms of Irritable Bowel Syndrome](https://doi.org/10.1016/j.cgh.2023.07.012) | 初筛漏筛补录。用稀疏偏最小二乘识别地中海饮食组成与IBS症状关系，并结合菌群分析提出个体化饮食研究证据。 | AI 用于生命科学、微生物组宿主关联分析、特征选择、稀疏学习 |
| Clinical Gastroenterology and Hepatology | [Algorithm Training and Testing for a Nonendoscopic Barrett’s Esophagus Detection Test in Prospective Multicenter Cohorts](https://doi.org/10.1016/j.cgh.2024.03.003) | 初筛漏筛补录。交叉验证训练并锁定逻辑回归DNA甲基化分类器，在独立多中心队列验证非内镜食管癌前病变检测。 | AI 用于生命科学、疾病辅助诊断、生物标志物评估、逻辑回归 |
| The Lancet Regional Health - Europe | [Quality of life in patients with statin intolerance: a multicentre prospective registry study](https://doi.org/10.1016/j.lanepe.2024.100981) | 初筛漏筛补录。基于多中心临床注册数据用k-means识别他汀不耐受患者分群，分析生活质量及个体化管理差异。 | AI 用于生命科学、疾病分型、聚类 |
| The Lancet Regional Health - Europe | [Development of a prognostic model to predict 90-day mortality in hospitalised cancer patients (PROMISE tool): a prospective observational study](https://doi.org/10.1016/j.lanepe.2024.101063) | 初筛漏筛补录。LASSO选择临床特征并建立外部验证的癌症住院90天死亡预测模型，直接用于临床风险分层。 | AI 用于生命科学、生存结局预测、正则化学习、逻辑回归 |
| The Lancet Planetary Health | [Mapping the distribution of Nipah virus infections: a geospatial modelling analysis](https://doi.org/10.1016/s2542-5196(24)00119-0) | 初筛漏筛补录。使用两个提升回归树模型识别尼帕病毒溢出及地方流行的生态驱动因素并绘制地理风险图。 | AI 用于生命科学、疾病风险预测、梯度提升 |
| The Lancet Planetary Health | [The impact of urban configuration types on urban heat islands, air pollution, CO2 emissions, and mortality in Europe: a data science approach](https://doi.org/10.1016/s2542-5196(24)00120-7) | 初筛漏筛补录。用UMAP降维与k-means聚类识别919座欧洲城市的空间类型，分析热岛、污染、排放与死亡率差异。 | AI 用于社会科学、环境健康关系推断、降维、聚类 |
| Information Fusion | [Multi-level feature fusion network combining attention mechanisms for polyp segmentation](https://doi.org/10.1016/j.inffus.2023.102195) | 初筛漏筛补录。针对结直肠息肉分割的特征冗余及语义冲突，设计多尺度注意力融合网络并验证多种息肉的检测分割能力。 | AI 用于生命科学、医学影像分割、注意力机制、深度学习 |
| Information Fusion | [Multi-task multi-objective evolutionary network for hyperspectral image classification and pansharpening](https://doi.org/10.1016/j.inffus.2024.102383) | 初筛漏筛补录。针对高光谱成像分类与全色融合的任务冲突，构建协同网络和多目标进化优化以提高光谱图像处理性能。 | AI 用于地球宇宙科学、遥感影像分析、多任务学习、演化优化、多目标优化 |
| Information Fusion | [Cyber democracy in the digital age: Characterizing hate networks in the 2022 US midterm elections](https://doi.org/10.1016/j.inffus.2024.102459) | 初筛漏筛补录。利用实体识别、情感分析及社区抽取研究美国中期选举仇恨网络，形成具体社会科学发现。 | AI 用于社会科学、在线仇恨网络分析、自然语言处理、知识图谱 |
| Nano Energy | [Halide perovskite photovoltaics for in-sensor reservoir computing](https://doi.org/10.1016/j.nanoen.2024.109949) | 初筛漏筛补录。利用钙钛矿光伏离子动态构建传感内储备池计算，并以PPG心律失常识别展示实际生理信号处理。 | AI 用于工程科学、心律失常识别、储备池计算、生理信号分析 |
| Journal of Advanced Research | [Lipidomics identified novel cholesterol-independent predictors for risk of incident coronary heart disease: Mediation of risk from diabetes and aggravation of risk by ambient air pollution](https://doi.org/10.1016/j.jare.2023.12.009) | 初筛漏筛补录。弹性网结合重复交叉验证识别脂质预测特征，改进冠心病发病预测并研究环境暴露交互。 | AI 用于生命科学、疾病风险预测、生物标志物发现、正则化学习 |
| Nature Ecology & Evolution | [Cell type evolution reconstruction across species through cell phylogenies of single-cell RNA sequencing data](https://www.nature.com/articles/s41559-023-02281-9) | 初筛漏筛补录。将单细胞表达主成分作为系统发育性状，进行跨哺乳动物眼细胞分类和细胞谱系重建，直接研究细胞类型演化。 | AI 用于生命科学、系统发育推断、主成分分析 |
| Nature Human Behaviour | [Biomimetic versus arbitrary motor control strategies for bionic hand skill learning](https://www.nature.com/articles/s41562-023-01811-6) | 初筛漏筛补录。采用肌电模式识别控制仿生手，比较仿生和任意控制策略下学习、泛化与具身性，直接支撑神经假肢研究。 | AI 用于生命科学、运动功能评估、生理信号分析、机器学习 |
| Nature Human Behaviour | [Conceptual structure and the growth of scientific knowledge](https://www.nature.com/articles/s41562-024-01957-x) | 初筛漏筛补录。用自然语言处理构建260万篇论文概念网络，分析概念结构、创新与科学共识的演化。 | AI 用于社会科学、科研概念网络分析、自然语言处理 |
| Cell Discovery | [Multi-modal molecular determinants of clinically relevant osteoporosis subtypes](https://doi.org/10.1038/s41421-024-00652-5) | 初筛漏筛补录。用深度潜空间融合多组学识别骨质疏松亚型，并验证补钙反应与骨折风险。 | AI 用于生命科学、疾病分型、多组学整合分析、潜变量建模、深度学习 |
| Nature Communications | [PheWAS-based clustering of Mendelian Randomisation instruments reveals distinct mechanism-specific causal effects between obesity and educational attainment](https://www.nature.com/articles/s41467-024-45655-8) | 初筛漏筛补录。对遗传工具的表型关联进行聚类分组，再作孟德尔随机化，揭示肥胖与教育因果估计中的多效性和混杂机制。 | AI 用于生命科学、基因变异效应预测、聚类、因果推断 |
| Nature Communications | [Imputation of plasma lipid species to facilitate integration of lipidomic datasets](https://www.nature.com/articles/s41467-024-45838-3) | 初筛漏筛补录。利用弹性网络预测未测脂质以统一不同分辨率血浆脂质组数据，并在独立队列验证插补和预测性能。 | AI 用于生命科学、多组学整合分析、正则化学习 |
| Nature Communications | [Widespread stable noncanonical peptides identified by integrated analyses of ribosome profiling and ORF features](https://www.nature.com/articles/s41467-024-46240-9) | 初筛漏筛补录。建立基于ORF特征的逻辑回归PepScore预测非经典肽稳定性，并以异位表达实验验证和定位功能研究对象。 | AI 用于生命科学、蛋白质性质预测、逻辑回归、基因组功能注释 |
| Nature Communications | [Thunder-DDA-PASEF enables high-coverage immunopeptidomics and is boosted by MS2Rescore with MS2PIP timsTOF fragmentation prediction model](https://www.nature.com/articles/s41467-024-46380-y) | 初筛漏筛补录。训练仪器特定质谱碎片强度预测模型并结合碰撞截面预测重评分，提高免疫肽识别覆盖和病毒抗原发现。 | AI 用于生命科学、蛋白质组分析、串联质谱预测、监督学习 |
| Nature Communications | [Multi-omic integration of microbiome data for identifying disease-associated modules](https://www.nature.com/articles/s41467-024-46888-3) | 初筛漏筛补录。MintTea通过典型相关分析扩展与共识整合发现跨组学微生物疾病模块，在代谢综合征和结直肠癌中验证预测力及机制关联。 | AI 用于生命科学、微生物组宿主关联分析、多组学整合分析、典型相关分析 |
| Nature Communications | [Integrated proteogenomic and metabolomic characterization of papillary thyroid cancer with different recurrence risks](https://www.nature.com/articles/s41467-024-47581-1) | 初筛漏筛补录。整合蛋白基因组和代谢组进行肿瘤亚型聚类，识别四类甲状腺癌及复发风险、免疫代谢和药物靶点差异。 | AI 用于生命科学、肿瘤分型、多组学整合分析、聚类 |
| Nature Communications | [A polygenic score method boosted by non-additive models](https://www.nature.com/articles/s41467-024-48654-x) | 初筛漏筛补录。GenoBoost使用统计提升学习整合非加性遗传效应，改善多疾病风险预测并识别新的显性遗传位点。 | AI 用于生命科学、疾病风险预测、梯度提升、基因变异效应预测 |
| Nature Communications | [Unveiling unique clinical phenotypes of hip fracture patients and the temporal association with cardiovascular events](https://www.nature.com/articles/s41467-024-48713-3) | 初筛漏筛补录。以潜在类别模型识别髋骨折患者亚型，并跨地区验证心血管事件、死亡和医疗利用差异，直接支撑临床表型研究。 | AI 用于生命科学、疾病分型、聚类、潜变量建模 |
| Nature Communications | [Single-cell total-RNA profiling unveils regulatory hubs of transcription factors](https://www.nature.com/articles/s41467-024-50291-3) | 初筛漏筛补录。以单细胞总RNA测序结合LASSO回归推断转录因子调控枢纽，解释细胞周期和衰老状态转变。 | AI 用于生命科学、基因调控网络推断、正则化学习 |
| Nature Communications | [Crossmodal sensory neurons based on high-performance flexible memristors for human-machine in-sensor computing system](https://www.nature.com/articles/s41467-024-51609-x) | 初筛漏筛补录。以柔性忆阻器构建跨模态脉冲储备池计算系统，验证动态物体识别和实时触觉反馈，直接支撑可穿戴人机交互工程。 | AI 用于工程科学、生物传感信号分析、储备池计算、脉冲神经网络 |
| Nature Communications | [Artificial selection improves pollutant degradation by bacterial communities](https://www.nature.com/articles/s41467-024-52190-z) | 初筛漏筛补录。采用遗传算法启发的选择重组策略进行18轮微生物群落实验，提升污染物降解并揭示群落成员作用。 | AI 用于生命科学、环境修复控制、演化优化 |
| Nature Communications | [Gut microbiota wellbeing index predicts overall health in a cohort of 1000 infants](https://www.nature.com/articles/s41467-024-52561-6) | 初筛漏筛补录。以聚类与轨迹建模识别近千名婴儿肠道微生物发育路线，建立健康指数并预测五年健康结局。 | AI 用于生命科学、微生物组宿主关联分析、疾病风险预测、聚类 |
| Nature Communications | [Allostery can convert binding free energies into concerted domain motions in enzymes](https://www.nature.com/articles/s41467-024-54421-9) | 初筛漏筛补录。将单分子纳米孔动力学分析与隐马尔可夫模型结合，解析腺苷酸激酶结构域运动和变构催化机制。 | AI 用于生命科学、反应动力学建模、隐马尔可夫模型 |
| Nature Communications | [Detecting global and local hierarchical structures in cell-cell communication using CrossChat](https://www.nature.com/articles/s41467-024-54821-x) | 初筛漏筛补录。CrossChat以多分辨率聚类与树检测推断单细胞和空间转录组的层级细胞通信，验证COVID及胚胎皮肤数据。 | AI 用于生命科学、细胞通信推断、聚类 |
| Nature Geoscience | [Sustained increases in atmospheric oxygen and marine productivity in the Neoproterozoic and Palaeozoic eras](https://www.nature.com/articles/s41561-024-01479-1) | 初筛漏筛补录。统计学习分析地球化学沉积记录并结合地球系统模型重建氧气与生产力演化，解释寒武纪动物辐射环境驱动。 | AI 用于地球宇宙科学、海洋缺氧重建、机器学习 |

## 标签与元数据核验

本轮使用119种标签，复用113种现有标签，新增6项；共享词表由771项增至**777项**。已核对中文、英文、维度及别名，未修改原有词项。

| 维度 | 新增标签 | 英文 | 适用范围 |
|---|---|---|---|
| method | 储备池计算 | Reservoir computing | 利用动态储备池将输入转换为丰富的状态表示，并训练读出层完成时序预测或识别。 |
| task | 医疗操作技能评估 | Medical procedure skill assessment | 从操作过程观测识别医疗操作错误或评价技能质量。 |
| task | 考古器物使用痕迹分析 | Archaeological artifact use-wear analysis | 根据器物表面显微磨损等证据推断考古器物的使用方式及加工材料。 |
| task | 科研概念网络分析 | Scientific concept network analysis | 从科学文献提取概念并分析概念网络结构、演化及其与知识创新的关系。 |
| task | 文化遗产视觉阐释 | Visual interpretation of cultural heritage | 结合文化遗产图像和语义知识生成或评估辅助理解的视觉解释。 |
| task | 在线仇恨网络分析 | Online hate network analysis | 利用在线文本与交互网络分析仇恨言论的群体、传播结构及社会情境。 |

- 77篇核对了出版社／会议正式页面的题名、作者、年份；73篇取得题名、年份匹配的Crossref记录。两者存在重叠。核实DOI 76篇，未找到的保留空值，不编造。
- 58个PDF端点通过HTTP HEAD检查，未下载或读取PDF；其他链接明确标为未核验。
- 核对摘要中30个作者声明的代码／项目链接，7个端点可访问。此项只确认端点响应，不代表代码正确性或复现实验验证。
- 原始字段保留，补充／纠正值写入 `ai4s_review.verified_metadata`。作者顺序冲突、缺DOI和访问问题保留逐条记录。

## 累计进度

| 指标 | 累计结果 |
|---|---|
| 已审 | 23,503条 |
| 纳入 | 2,624篇 |
| 排除 | 19,549条（无AI4S实质关系、非研究文种或不属本批范围） |
| 待定 | 1,330条（证据不足、摘要问题或类型待确认） |
| 关键词漏筛纳入 | 1,473篇（已包含在纳入总数中） |
| 核验补齐完整摘要 | 2,225条 |
| 已有摘要队列未处理 | 0 |
| 缺摘要暂缓 | 6,965条 |

校验通过：**23,503已审＋6,965未审＝30,468**；唯一键无重复，原字段和此前20,333条完整记录保持一致，标签符合共享词表。发现跨审核文件同键重合890条、判定不同46条，已列审计供团队汇总时核对，未修改他人文件。

## 交付与剩余边界

[个人JSON](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101.json) · [累计统计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/summary.json) · [本轮逐条审计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation14-batch-decisions.jsonl) · [阶段反馈](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/feedback/Blueblue1101.json)

新来源水平、以前的候选复核和官网目录核验仍见[阶段总结](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/王婉婷_AI4S阶段总结.md)。本轮没有新增来源或扩大官网目录核验，不能宣称所有刊会都无漏采。按你的效率要求，缺摘要／爬取异常先放着，待定记录保留证据缺口。

文件随本次提交同步到GitHub main；实际发布提交与远程哈希核对结果记在本地 `publication.json`。
