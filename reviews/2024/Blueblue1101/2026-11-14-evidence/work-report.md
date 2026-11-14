# 王婉婷｜2024年待定论文补证进展

更新日期：2026-11-14。基于 main `b303589`，延续上轮1,152条待定；仅处理当前名下49个来源。

已同步GitHub和监控数据；仓库实时汇总与网站备用快照均已核验一致，见[发布验证记录](sync-status.md)。

本轮对 **856条有摘要但证据不足的记录**继续补证：**45条转纳入、31条转排除**，总待定由 **1,152降至1,076条**。没有新增爬取论文，所有变化均来自已有记录复核。

累计：**纳入1,908条、排除19,291条、待定1,076条、未审0条**。

## 这轮补了什么证据

- 144条对应官网已知访问受阻，直接暂放；其余712条尝试官方页面，取得711条正式元数据，新增访问/取证障碍1条。
- 官方证据只提取题名、DOI、作者、摘要、文献类型及相关链接，不读正文。与已完整阅读的输入摘要逐条对照；不按关键词命中自动下结论。
- 多数官方摘要与输入同文。这部分如改变结论，属于核实文种或纠正旧判断过严，不称为补回新摘要。
- 明确医学/遥感/机器人科研任务且AI实质参与的可纳入；评论、来信等按官网类型排除；摘要明确为非AI实验或传统统计研究的按具体方法排除。算法或作用仍不明的保留待定。
- 54条上轮已转纳入等既有确定结果不在本轮队列，没有重审覆盖。标签复用最新中英文词表，新增词条0。

另外核实题名《Just Add π! Pose Induced Video Transformers for Understanding Activities of Daily Living》中的`π`此前误写为`?`，已在`verified_metadata.title`纠正，原字段保留。

## 各来源结果

| 来源 | 本轮有摘要队列 | 转纳入 | 转排除 | 本轮仍待定 | 来源剩余全部待定 |
|---|---:|---:|---:|---:|---:|
| Advances in Applied Energy | 3 | 0 | 0 | 3 | 3 |
| Applied Catalysis B Environment and Energy | 1 | 0 | 0 | 1 | 4 |
| Artificial Intelligence Review | 9 | 1 | 0 | 8 | 8 |
| Cell Discovery | 5 | 0 | 0 | 5 | 34 |
| Chem | 2 | 0 | 0 | 2 | 7 |
| Clinical Gastroenterology and Hepatology | 3 | 0 | 0 | 3 | 60 |
| Energy Storage Materials | 2 | 0 | 0 | 2 | 3 |
| eTransportation | 1 | 0 | 0 | 1 | 1 |
| European Conference on Artificial Intelligence | 31 | 12 | 5 | 14 | 14 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | 78 | 32 | 9 | 37 | 40 |
| Information Fusion | 5 | 0 | 0 | 5 | 7 |
| International Journal of Mining Science and Technology | 0 | 0 | 0 | 0 | 0 |
| Journal of Advanced Research | 7 | 0 | 0 | 7 | 8 |
| Journal of Energy Chemistry | 1 | 0 | 0 | 1 | 3 |
| Journal of Materials Science & Technology | 0 | 0 | 0 | 0 | 0 |
| Matter | 3 | 0 | 0 | 3 | 3 |
| Molecular Cell | 5 | 0 | 0 | 5 | 9 |
| Molecular Neurodegeneration | 4 | 0 | 1 | 3 | 3 |
| Nano Energy | 3 | 0 | 0 | 3 | 4 |
| Nature Chemical Biology | 13 | 0 | 1 | 12 | 12 |
| Nature Communications | 475 | 0 | 12 | 463 | 465 |
| Nature Computational Science | 11 | 0 | 0 | 11 | 11 |
| Nature Ecology & Evolution | 9 | 0 | 0 | 9 | 9 |
| Nature Geoscience | 1 | 0 | 0 | 1 | 1 |
| Nature Human Behaviour | 15 | 0 | 0 | 15 | 15 |
| Nature Microbiology | 8 | 0 | 0 | 8 | 8 |
| Nature Neuroscience | 28 | 0 | 0 | 28 | 28 |
| Nature Physics | 1 | 0 | 0 | 1 | 1 |
| Nature Protocols | 8 | 0 | 0 | 8 | 8 |
| Neuron | 18 | 0 | 0 | 18 | 19 |
| npj Science of Learning | 8 | 0 | 0 | 8 | 8 |
| Pharmacological Reviews | 1 | 0 | 0 | 1 | 1 |
| Renewable and Sustainable Energy Reviews | 21 | 0 | 0 | 21 | 26 |
| Science Immunology | 1 | 0 | 0 | 1 | 28 |
| Science Translational Medicine | 15 | 0 | 0 | 15 | 19 |
| Seminars in Cancer Biology | 0 | 0 | 0 | 0 | 0 |
| Smart Learning Environments | 8 | 0 | 3 | 5 | 5 |
| The Lancet Haematology | 1 | 0 | 0 | 1 | 4 |
| The Lancet Healthy Longevity | 2 | 0 | 0 | 2 | 41 |
| The Lancet Planetary Health | 2 | 0 | 0 | 2 | 37 |
| The Lancet Regional Health - Europe | 5 | 0 | 0 | 5 | 59 |
| Trends in Biotechnology | 2 | 0 | 0 | 2 | 3 |
| Trends in Cognitive Sciences | 20 | 0 | 0 | 20 | 20 |
| Trends in Ecology & Evolution | 3 | 0 | 0 | 3 | 4 |
| Trends in Endocrinology and Metabolism | 0 | 0 | 0 | 0 | 0 |
| Trends in Food Science & Technology | 8 | 0 | 0 | 8 | 24 |
| Trends in Microbiology | 5 | 0 | 0 | 5 | 5 |
| Trends in Molecular Medicine | 2 | 0 | 0 | 2 | 2 |
| Trends in Neurosciences | 2 | 0 | 0 | 2 | 2 |
| **合计** | **856** | **45** | **31** | **780** | **1076** |

## 转纳入明细和标签

| 来源 | 论文 | 纳入依据／标签 |
|---|---|---|
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Poly Kernel Inception Network for Remote Sensing Detection](https://openaccess.thecvf.com/content/CVPR2024/html/Cai_Poly_Kernel_Inception_Network_for_Remote_Sensing_Detection_CVPR_2024_paper.html) | 卷积与注意力网络专门应对遥感目标尺度和背景变化，直接贡献于遥感影像检测任务。 标签：AI 用于地球宇宙科学、遥感影像分析 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Think Twice Before Selection: Federated Evidential Active Learning for Medical Image Analysis with Domain Shifts](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Think_Twice_Before_Selection_Federated_Evidential_Active_Learning_for_Medical_CVPR_2024_paper.html) | 联邦主动学习处理真实多中心医学影像的域偏移和标注成本，医疗研究任务与AI作用明确。 标签：AI 用于生命科学、联邦学习、主动学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Active Open-Vocabulary Recognition: Let Intelligent Moving Mitigate CLIP Limitations](https://openaccess.thecvf.com/content/CVPR2024/html/Fan_Active_Open-Vocabulary_Recognition_Let_Intelligent_Moving_Mitigate_CLIP_Limitations_CVPR_2024_paper.html) | 利用CLIP表征控制具身智能体主动移动和融合视角，直接研究机器人环境感知，无须以缺少实机实验继续待定。 标签：AI 用于工程科学、机器学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Learned Representation-Guided Diffusion Models for Large-Image Generation](https://openaccess.thecvf.com/content/CVPR2024/html/Graikos_Learned_Representation-Guided_Diffusion_Models_for_Large-Image_Generation_CVPR_2024_paper.html) | 针对病理与遥感大图的昂贵标注和空间连续性，以自监督表征指导扩散生成并改善领域分类，直接贡献于科学影像研究。 标签：AI 用于生命科学、AI 用于地球宇宙科学、扩散模型、自监督学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [SkySense: A Multi-Modal Remote Sensing Foundation Model Towards Universal Interpretation for Earth Observation Imagery](https://openaccess.thecvf.com/content/CVPR2024/html/Guo_SkySense_A_Multi-Modal_Remote_Sensing_Foundation_Model_Towards_Universal_Interpretation_CVPR_2024_paper.html) | 以光学/SAR时序和地理上下文预训练遥感基础模型，直接支持多种地球观测任务。 标签：AI 用于地球宇宙科学、科学基础模型、预训练 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [MultiPLY: A Multisensory Object-Centric Embodied Large Language Model in 3D World](https://openaccess.thecvf.com/content/CVPR2024/html/Hong_MultiPLY_A_Multisensory_Object-Centric_Embodied_Large_Language_Model_in_3D_CVPR_2024_paper.html) | 构建可主动获取视觉、触觉和热信息的具身大模型，并评测物体检索、工具使用和任务分解，直接研究具身交互控制。 标签：AI 用于工程科学、大语言模型、机器人任务规划 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [OmniMedVQA: A New Large-Scale Comprehensive Evaluation Benchmark for Medical LVLM](https://openaccess.thecvf.com/content/CVPR2024/html/Hu_OmniMedVQA_A_New_Large-Scale_Comprehensive_Evaluation_Benchmark_for_Medical_LVLM_CVPR_2024_paper.html) | 构建真实医学影像多模态问答基准，覆盖12种模态和20余解剖部位，直接评测医疗视觉语言模型。 标签：AI 用于生命科学、医学图像问答、科学评测 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Systematic Comparison of Semi-supervised and Self-supervised Learning for Medical Image Classification](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_Systematic_Comparison_of_Semi-supervised_and_Self-supervised_Learning_for_Medical_Image_CVPR_2024_paper.html) | 对医学影像分类的半监督与自监督方法进行统一控制的比较，明确支持有限标注和算力下的医疗影像研究。 标签：AI 用于生命科学、医学影像分类、半监督学习、自监督学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Molecular Data Programming: Towards Molecule Pseudo-labeling with Systematic Weak Supervision](https://openaccess.thecvf.com/content/CVPR2024/html/Juan_Molecular_Data_Programming_Towards_Molecule_Pseudo-labeling_with_Systematic_Weak_Supervision_CVPR_2024_paper.html) | 用分子结构知识构造弱监督标签并训练分子分类器，直接解决分子建模标签不足的问题。 标签：AI 用于物质科学、分子表征学习、弱监督学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [GeoChat: Grounded Large Vision-Language Model for Remote Sensing](https://openaccess.thecvf.com/content/CVPR2024/html/Kuckreja_GeoChat_Grounded_Large_Vision-Language_Model_for_Remote_Sensing_CVPR_2024_paper.html) | 针对遥感尺度和区域定位设计视觉语言模型及指令数据，直接支持遥感解译。 标签：AI 用于地球宇宙科学、遥感影像分析、大语言模型 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [S2MAE: A Spatial-Spectral Pretraining Foundation Model for Spectral Remote Sensing Data](https://openaccess.thecvf.com/content/CVPR2024/html/Li_S2MAE_A_Spatial-Spectral_Pretraining_Foundation_Model_for_Spectral_Remote_Sensing_CVPR_2024_paper.html) | 空间光谱掩码预训练专用于遥感数据及其下游任务。 标签：AI 用于地球宇宙科学、科学基础模型、预训练 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Towards Scalable 3D Anomaly Detection and Localization: A Benchmark via 3D Anomaly Synthesis and A Self-Supervised Learning Network](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Towards_Scalable_3D_Anomaly_Detection_and_Localization_A_Benchmark_via_CVPR_2024_paper.html) | 建立三维工业异常数据和自监督重建网络，直接定位物体几何异常。 标签：AI 用于工程科学、自监督学习、科学数据 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [A Category Agnostic Model for Visual Rearrangment](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_A_Category_Agnostic_Model_for_Visual_Rearrangment_CVPR_2024_paper.html) | 为具身智能体设计场景变化匹配和探索策略以恢复物体布局，研究机器人重排控制。 标签：AI 用于工程科学、机器人操作控制 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Rotated Multi-Scale Interaction Network for Referring Remote Sensing Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Rotated_Multi-Scale_Interaction_Network_for_Referring_Remote_Sensing_Image_Segmentation_CVPR_2024_paper.html) | 针对遥感尺度与旋转构建视觉语言分割网络和标注数据，直接改善遥感解译。 标签：AI 用于地球宇宙科学、遥感影像分析 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [HoloVIC: Large-scale Dataset and Benchmark for Multi-Sensor Holographic Intersection and Vehicle-Infrastructure Cooperative](https://openaccess.thecvf.com/content/CVPR2024/html/Ma_HoloVIC_Large-scale_Dataset_and_Benchmark_for_Multi-Sensor_Holographic_Intersection_and_CVPR_2024_paper.html) | 真实车路协同数据与目标标注、任务基准直接支持自动驾驶感知研究。 标签：AI 用于工程科学、科学数据、科学评测 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [IIRP-Net: Iterative Inference Residual Pyramid Network for Enhanced Image Registration](https://openaccess.thecvf.com/content/CVPR2024/html/Ma_IIRP-Net_Iterative_Inference_Residual_Pyramid_Network_for_Enhanced_Image_Registration_CVPR_2024_paper.html) | 用深度残差流网络改善可变形配准，并在FLARE和Mindboggle医学数据验证。 标签：AI 用于生命科学、医学影像配准、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Task-Conditioned Adaptation of Visual Features in Multi-Task Policy Learning](https://openaccess.thecvf.com/content/CVPR2024/html/Marza_Task-Conditioned_Adaptation_of_Visual_Features_in_Multi-Task_Policy_Learning_CVPR_2024_paper.html) | 以任务条件视觉适配与行为克隆学习自主智能体多任务控制策略，在CortexBench任务验证，无须要求列出每个操作对象。 标签：AI 用于工程科学、机器学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Rethinking Transformers Pre-training for Multi-Spectral Satellite Imagery](https://openaccess.thecvf.com/content/CVPR2024/html/Noman_Rethinking_Transformers_Pre-training_for_Multi-Spectral_Satellite_Imagery_CVPR_2024_paper.html) | 针对多光谱卫星影像的尺度和模态差异开展多尺度预训练，直接改善遥感地表分类。 标签：AI 用于地球宇宙科学、遥感影像分析、预训练 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Adversarial Backdoor Attack by Naturalistic Data Poisoning on Trajectory Prediction in Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2024/html/Pourkeshavarz_Adversarial_Backdoor_Attack_by_Naturalistic_Data_Poisoning_on_Trajectory_Prediction_CVPR_2024_paper.html) | 专门研究自动驾驶轨迹预测系统的隐蔽后门与防御，使用物理可行车辆轨迹检验安全风险。 标签：AI 用于工程科学、机器学习、科学评测 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Seeing the Unseen: Visual Common Sense for Semantic Placement](https://openaccess.thecvf.com/content/CVPR2024/html/Ramrakhya_Seeing_the_Unseen_Visual_Common_Sense_for_Semantic_Placement_CVPR_2024_paper.html) | 用CLIP-UNet学习语义放置位置并支持室内整理机器人，直接研究机器人场景交互与物体放置。 标签：AI 用于工程科学、机器人操作控制 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Parameter Efficient Self-Supervised Geospatial Domain Adaptation](https://openaccess.thecvf.com/content/CVPR2024/html/Scheibenreif_Parameter_Efficient_Self-Supervised_Geospatial_Domain_Adaptation_CVPR_2024_paper.html) | 自监督适配解决遥感多传感器模态和少样本差异，直接提升遥感任务的数据效率。 标签：AI 用于地球宇宙科学、遥感影像分析、自监督学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [SatSynth: Augmenting Image-Mask Pairs through Diffusion Models for Aerial Semantic Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Toker_SatSynth_Augmenting_Image-Mask_Pairs_through_Diffusion_Models_for_Aerial_Semantic_CVPR_2024_paper.html) | 扩散模型联合生成卫星影像与分割掩码，直接缓解地球观测标注不足并改善遥感分割。 标签：AI 用于地球宇宙科学、遥感影像分析、扩散模型 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [VoCo: A Simple-yet-Effective Volume Contrastive Learning Framework for 3D Medical Image Analysis](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_VoCo_A_Simple-yet-Effective_Volume_Contrastive_Learning_Framework_for_3D_Medical_CVPR_2024_paper.html) | 通过器官间空间先验构建体积对比预训练，直接提升三维医学影像分析。 标签：AI 用于生命科学、医学图像分析、自监督学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [PairAug: What Can Augmented Image-Text Pairs Do for Radiology?](https://openaccess.thecvf.com/content/CVPR2024/html/Xie_PairAug_What_Can_Augmented_Image-Text_Pairs_Do_for_Radiology_CVPR_2024_paper.html) | 利用大模型和图像合成扩充配对放射影像报告，直接改善医疗影像下游分类。 标签：AI 用于生命科学、医学影像数据增强、大语言模型 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Adapting to Length Shift: FlexiLength Network for Trajectory Prediction](https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Adapting_to_Length_Shift_FlexiLength_Network_for_Trajectory_Prediction_CVPR_2024_paper.html) | 针对自动驾驶与机器人轨迹观测长度变化设计神经网络校准和适配，直接改善运动预测。 标签：AI 用于工程科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [PhyScene: Physically Interactable 3D Scene Synthesis for Embodied AI](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_PhyScene_Physically_Interactable_3D_Scene_Synthesis_for_Embodied_AI_CVPR_2024_paper.html) | 以扩散模型和碰撞、可达性约束生成物理可交互机器人训练场景，为具身交互研究提供数据资源。 标签：AI 用于工程科学、扩散模型、科学数据 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Continual Self-supervised Learning: Towards Universal Multi-modal Medical Data Representation Learning](https://openaccess.thecvf.com/content/CVPR2024/html/Ye_Continual_Self-supervised_Learning_Towards_Universal_Multi-modal_Medical_Data_Representation_Learning_CVPR_2024_paper.html) | 在影像与临床报告间持续自监督预训练，解决医疗多模态冲突与遗忘并验证多项医学任务。 标签：AI 用于生命科学、自监督学习、预训练 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Unmixing Before Fusion: A Generalized Paradigm for Multi-Source-based Hyperspectral Image Synthesis](https://openaccess.thecvf.com/content/CVPR2024/html/Yu_Unmixing_Before_Fusion_A_Generalized_Paradigm_for_Multi-Source-based_Hyperspectral_Image_CVPR_2024_paper.html) | 通过光谱解混与深度生成合成高光谱数据，减少昂贵传感数据采集需求并验证下游分析。 标签：AI 用于工程科学、深度学习、科学数据 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [DiaLoc: An Iterative Approach to Embodied Dialog Localization](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_DiaLoc_An_Iterative_Approach_to_Embodied_Dialog_Localization_CVPR_2024_paper.html) | 多模态融合网络逐轮整合视觉与对话定位，直接研究具身智能体协作定位。 标签：AI 用于工程科学、机器人定位 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Equivariant Multi-Modality Image Fusion](https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_Equivariant_Multi-Modality_Image_Fusion_CVPR_2024_paper.html) | 以成像等变先验实现自监督多模态医学影像融合，直接促进多模态分割与检测。 标签：AI 用于生命科学、医学影像融合、自监督学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Low-Rank Knowledge Decomposition for Medical Foundation Models](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_Low-Rank_Knowledge_Decomposition_for_Medical_Foundation_Models_CVPR_2024_paper.html) | 对医疗基础模型作低秩知识分解以得到专门医疗任务模型，直接改善医疗数据建模与迁移。 标签：AI 用于生命科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [SmartRefine: A Scenario-Adaptive Refinement Framework for Efficient Motion Prediction](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_SmartRefine_A_Scenario-Adaptive_Refinement_Framework_for_Efficient_Motion_Prediction_CVPR_2024_paper.html) | 针对自动驾驶的人车混行环境，通过学习式质量评估和场景适配改善轨迹预测。 标签：AI 用于工程科学、机器学习 |
| European Conference on Artificial Intelligence | [Class-Aware Sample Weight Learning for Cross-Modal Unsupervised Domain Adaptation in Cross-User Wearable Human Activity Recognition.](https://doi.org/10.3233/faia240535) | 为跨用户可穿戴活动识别构建模态适配和样本权重网络，直接解决传感器异构下的人体活动测量问题。 标签：AI 用于工程科学、深度学习 |
| European Conference on Artificial Intelligence | [Bridging the Gap: Generating a Comprehensive Biomedical Knowledge Graph Question Answering Dataset.](https://doi.org/10.3233/faia240615) | 构建精准医学知识图谱问答数据与语义忠实性评测，直接支持知识驱动的生物医学研究。 标签：AI 用于生命科学、科学数据、科学评测 |
| European Conference on Artificial Intelligence | [Molecular Topological Profile (MOLTOP) - Simple and Strong Baseline for Molecular Graph Classification.](https://doi.org/10.3233/faia240663) | 分子拓扑描述符与随机森林直接服务分子图和肽分类，提供分子学习方法的可靠比较基线。 标签：AI 用于物质科学、分子表征学习、随机森林 |
| European Conference on Artificial Intelligence | [Dirichlet Logistic Gaussian Processes for Evaluation of Black-Box Stochastic Systems under Complex Requirements.](https://doi.org/10.3233/faia240719) | 用逻辑高斯过程与贝叶斯模型估计信息物理系统性能分布，直接支持小样本下工程系统可靠性评估。 标签：AI 用于工程科学、贝叶斯学习 |
| European Conference on Artificial Intelligence | [Exploiting Hierarchical Symmetry in Multi-Agent Reinforcement Learning.](https://doi.org/10.3233/faia240741) | 等变图网络和多智能体强化学习提升协作策略，并在实体多机器人系统验证，直接支持机器人控制。 标签：AI 用于工程科学、强化学习 |
| European Conference on Artificial Intelligence | [On the Effects of Irrelevant Variables in Treatment Effect Estimation with Deep Disentanglement.](https://doi.org/10.3233/faia240818) | 深度解耦和自编码器分离无关变量以改善观察数据的处理效应估计，AI直接支持因果推断研究。 标签：AI 用于社会科学、深度学习 |
| European Conference on Artificial Intelligence | [Subsystem Discovery in High-Dimensional Time-Series Using Masked Autoencoders.](https://doi.org/10.3233/faia240844) | 掩码自编码器学习高维传感时间序列的邻接结构并发现子系统，直接支持复杂物理系统结构识别。 标签：AI 用于工程科学、自监督学习 |
| European Conference on Artificial Intelligence | [Survival of the Fittest: Evolutionary Adaptation of Policies for Environmental Shifts.](https://doi.org/10.3233/faia240874) | 演化鲁棒策略优化直接解决动态环境变化下自主智能体的避障路径规划，并验证适应效率。 标签：AI 用于工程科学、强化学习、机器人航迹规划 |
| European Conference on Artificial Intelligence | [Real-Time Goal Recognition Using Approximations in Euclidean Space.](https://doi.org/10.3233/faia240914) | 用规划器与运动模型进行实时目标识别，直接满足机器人连续轨迹规划的时延要求。 标签：AI 用于工程科学、机器人航迹规划 |
| European Conference on Artificial Intelligence | [Leveraging Foundation Models for Zero-Shot IoT Sensing.](https://doi.org/10.3233/faia240942) | 结合传感物理原理和基础模型语义表示实现毫米波、IMU、Wi-Fi零样本感知，直接贡献传感系统研究。 标签：AI 用于工程科学、深度学习 |
| European Conference on Artificial Intelligence | [UDUC: An Uncertainty-Driven Approach for Learning-Based Robust Control.](https://doi.org/10.3233/faia241018) | 通过概率集成模型和对比训练学习系统动力学，直接研究环境失配下的鲁棒控制。 标签：AI 用于工程科学、机器学习 |
| European Conference on Artificial Intelligence | [Generative Pretrained Embedding and Hierarchical Irregular Time Series Representation for Daily Living Activity Recognition.](https://doi.org/10.3233/faia241075) | 预训练时序嵌入和层级模型直接用于环境传感器的人体日常活动识别，贡献于智能感知系统。 标签：AI 用于工程科学、深度学习 |
| Artificial Intelligence Review | [A survey of deep causal models and their industrial applications](https://doi.org/10.1007/s10462-024-10886-0) | 实质综述神经网络因果效应估计、反事实建模及产业应用，直接支持科学因果推断方法研究。 标签：AI 用于社会科学、综述、深度学习 |

## 转排除明细

| 来源 | 论文（排除原因） |
|---|---|
| IEEE/CVF Computer Vision and Pattern Recognition Conference | CAPE: CAM as a Probabilistic Ensemble for Enhanced DNN Interpretation（主要贡献是通用CAM解释与ImageNet等基准性能；CMML细胞影像仅作附加测试，摘要未展示针对疾病研究的新贡献。） |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | ODIN: A Single Model for 2D and 3D Segmentation（研究通用二维/三维分割网络，在视觉与具身基准验证，摘要未描述独立的科学领域研究任务。） |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | Enhancing 3D Object Detection with 2D Detection-Guided Query Anchors（研究通用三维目标检测的查询构建，在nuScenes测试性能；未给出具体科学研究或领域工程机制问题。） |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | Construct to Associate: Cooperative Context Learning for Domain Adaptive Point Cloud Segmentation（通用点云域适应研究仅报告代表性基准，没有明确领域科学研究任务。） |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | GS-IR: 3D Gaussian Splatting for Inverse Rendering（研究照片级新视角生成和重光照等通用图形任务，未显示科学研究任务。） |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | Novel Class Discovery for Ultra-Fine-Grained Visual Categorization（大豆品种仅用于说明超细粒度识别概念，实际贡献是通用新类别发现，没有农业研究贡献。） |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | Towards Robust Learning to Optimize with Theoretical Guarantees（核心是通用学习优化器的泛化界和计算加速，通信等仅作背景例子，没有明确领域科学任务。） |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | MMCert: Provable Defense against Adversarial Attacks to Multi-modal Models（贡献是通用多模态模型的认证鲁棒性，自动驾驶和情感数据作为算法基准，未呈现独立领域科研贡献。） |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | NetTrack: Tracking Highly Dynamic Objects with a Net（鸟群数据用来测试通用动态目标跟踪，论文未提出动物行为或生态学研究任务。） |
| European Conference on Artificial Intelligence | Generalizing Visual Question Answering from Synthetic to Human-Written Questions via a Chain of QA with a Large Language Model.（贡献是通用视觉问答推理流程，胸片与三维图像作为性能基准，未说明独立医学研究贡献。） |
| European Conference on Artificial Intelligence | One-Shot Collaborative Data Distillation.（核心是通用一次通信数据蒸馏，5G攻击检测仅作为附加应用示例，摘要未呈现领域研究发现。） |
| European Conference on Artificial Intelligence | HBIC: A Biclustering Algorithm for Heterogeneous Datasets.（主要提出通用混合属性双聚类，硬皮病数据用于展示算法质量，未报告针对疾病的独立研究贡献。） |
| European Conference on Artificial Intelligence | Global Structural-Temporal Graph Network with Public Opinion for Online Rumor Detection.（研究社交媒体谣言自动识别算法及基准准确率，未提出独立社会科学分析任务。） |
| European Conference on Artificial Intelligence | A Faster Branching Algorithm for the Maximum k-Defective Clique Problem.（采用经典分支和上界技术求图团，社交与生物网络仅为应用背景；未体现AI参与的领域科学研究。） |
| Molecular Neurodegeneration | CSF proteins of inflammation, proteolysis and lipid transport define preclinical AD and progression to AD dementia in cognitively unimpaired individuals（出版社正式文种为Letter to the Editor，按读者来信类型排除。） |
| Smart Learning Environments | Uncovering insights from big data: change point detection of classroom engagement（完整官方摘要说明使用PELT统计变点检测及显著性分析研究课堂参与度，未采用AI模型或AI推理机制。） |
| Smart Learning Environments | Do personal recommendations need to be personalized? Investigating the relationships between student differences and educational recommendations（官方摘要描述问卷调查与相关性分析研究学生推荐偏好，AI推荐仅作研究背景，没有AI实质参与分析。） |
| Smart Learning Environments | Harnessing large language models to develop research-based learning assistants for formative feedback（出版社明确标为Commentary，属于评论，按文献类型排除。） |
| Nature Chemical Biology | Multicellular artificial neural network-type architectures demonstrate computational problem solving（官方摘要说明用工程细菌搭建类神经网络逻辑器件，演示加减法、素数和字母判断；贡献为生物计算硬件，不是AI用于科学问题分析或发现。） |
| Nature Communications | Direct contribution of the sensory cortex to the judgment of stimulus duration（官网完整摘要明确采用大鼠躯体感觉皮层记录、光遗传刺激及从膜电流到时间知觉的机制模型，研究的是生理信号整合；摘要所述模型并非训练得到的人工学习模型，按本批摘要证据排除。） |
| Nature Communications | ProTInSeq: transposon insertion tracking by ultra-deep DNA sequencing to identify translated large and small ORFs（官网完整摘要的核心贡献是通过工程化转座子插入和超深DNA测序检测翻译开放阅读框，并量化翻译噪声与蛋白拓扑，属于实验测量/测序方法；抗菌潜能预测只是结果附述，未形成可核实的AI方法贡献，按摘要证据排除。） |
| Nature Communications | Towards establishing a fungal economics spectrum in soil saprobic fungi（官网完整摘要围绕28种培养真菌的性状测量、生态权衡轴和土壤碳循环相关性展开，属于性状生态学的维度与相关性分析；没有以人工学习模型构成研究方法或贡献，按摘要明确的传统生态统计主线排除。） |
| Nature Communications | Cerebellar Purkinje cells combine sensory and motor information to predict the sensory consequences of active self-motion in macaques（官网完整摘要通过猕猴Purkinje细胞记录及约40个细胞反应的组合模型解释自运动感觉抵消，模型用于生理响应叠加而非人工神经网络学习；按所述实验神经生理及机制建模方法排除。） |
| Nature Communications | Toddlers strategically adapt their information search（官网完整摘要通过婴幼儿/成人眼动实验和Markov模型刻画信息搜索转移策略，研究对象是人类行为，采用的是行为实验与状态转移统计描述，并未使用AI作为研究工具，按该方法主线排除。） |
| Nature Communications | Towards enhanced functionality of vagus neuroprostheses through in silico optimized stimulation（官网完整摘要说明VaStim模拟迷走神经全纤维群、结合猪实验/肌肉反应个性化并优化刺激范式，贡献是生物物理神经模型和仿真效率；摘要中的优化算法不等于机器学习，按所述机制仿真方法排除。） |
| Nature Communications | Dual activities of an X-family DNA polymerase regulate CRISPR-induced insertional mutagenesis across species（官网完整摘要通过跨物种CRISPR修复比较、Polλ敲除/过表达及保守基序实验解释插入突变机制，预测程序仅作为背景动机；本研究的证据主线是DNA修复机制实验，未显示AI实质参与，按摘要证据排除。） |
| Nature Communications | Underlying dimensions of real-time word recognition in cochlear implant users（官网完整摘要用视觉世界范式和主成分分析分解词汇竞争的三个维度，再检验与听力、人口因素及感知结局的关系；属于传统心理测量和统计关联研究，非AI支撑的研究。） |
| Nature Communications | Design of a Cereblon construct for crystallographic and biophysical studies of protein degraders（官网完整摘要描述CRBN蛋白构建体的设计、细菌表达、稳定性与功能测试和二元/三元复合物晶体结构测定；贡献为实验生物物理工具，没有AI建模或学习参与的研究环节，按非AI研究排除。） |
| Nature Communications | Rare variant contribution to the heritability of coronary artery disease（官网完整摘要明确使用GREML-LDMS-I估计遗传率并开展功能注释富集，结论是低连锁不平衡超罕见变异的遗传贡献；核心为传统遗传统计估计与富集分析，按非AI研究排除。） |
| Nature Communications | Border-ownership tuning determines the connectivity between V4 and V1 in the macaque visual system（官网摘要的方法是噪声相关、微刺激估计连接强度及生物线路解释模型，贡献是视觉神经连接机制；按传统实验和机制建模研究排除。） |
| Nature Communications | Ultrasensitive dim-light neuromorphic vision sensing via momentum-conserved reconfigurable van der Waals heterostructure（官网摘要贡献为光晶体管、传感器阵列及低照度乘加运算硬件，以交通灯检测展示性能；属于面向AI的器件研究，未显示AI支撑具体科学发现或工程建模。） |

## 仍待处理与统计口径

剩余1076条包括：上轮296条摘要缺失/质量问题、本轮144条已知官网访问受阻，以及其余取证后仍不足或新增访问障碍的记录。本轮未处理官网总量问题，未知同口径总数仍为33个来源。

剩余待定可明确分为：**635条证据仍不足、296条摘要问题、144条已知官网访问障碍、1条新增连接故障**。

这些待定属于全量已交付记录，不等同于1,149条初筛候选的缺摘要指标。原有已排除且无需摘要的豁免规则保留。

## 交付与验证

- [本轮逐条结果](decisions.json)、[官方元数据证据](official-evidence.json)、[汇总](summary.json)、[校验](validation.json)。
- [个人论文JSON](../../Blueblue1101.json)、[阶段反馈](../../feedback/Blueblue1101.json)。
- [GitHub与监控数据同步记录](sync-status.md)。
