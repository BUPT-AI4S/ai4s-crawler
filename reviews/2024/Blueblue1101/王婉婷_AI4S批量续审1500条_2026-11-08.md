# 王婉婷｜AI4S论文摘要批量审核工作汇报

2026年11月8日 · 2024年论文 · Blueblue1101 · continuation12

**本轮完成1,500条，比上一轮多300条：纳入21篇、排除1,400条、待定79条；核验补齐完整摘要63条。** 覆盖26个来源，旧15,833条完整记录保持不变。

新增纳入均来自已经采集、未进入关键词初筛候选的记录，属于**漏筛补录**。本轮新爬0篇，未扩大官网漏采核验。缺摘要或抓取异常项按要求暂缓。

## 审核方法

按仓库main `e572dda` 当前skill复核，从757项共享词表中查找已有标签。分批读取完整摘要，截断内容另行重读，逐条保存结论、理由、摘要哈希和队列位置。判断依据是明确的科学／工程任务、AI实质作用及二者关系，未以关键词命中替代语义判断，未读取正文或PDF。

21篇拟纳入全部再次核对并打标。固定随机种子抽查20条排除记录（18条相关性排除、2条文种排除），重读后维持原结论。抽查不能代表全量准确率。证据不足的79条保留待定，未强行判为纳入。

## 本轮结果及原因

| 结果 | 条数 | 原因 |
|---|---|---|
| 纳入 | 21 | 摘要支持AI用于明确科学或工程研究任务 |
| 相关性排除 | 1398 | 摘要未显示AI实质参与，或仅有通用模型／基准而缺少实质科学研究任务 |
| 文种排除 | 2 | Matters Arising Response回应及AGA Commentary评论，不属于本批保留的研究正文或实质综述 |
| 待定 | 79 | 摘要没有说清AI算法、研究贡献或二者关系，保留后续查证 |

## 各来源本轮工作量

“补摘要”指已取得的书目摘要经语义核验后写入元数据，不代表本轮新爬论文；已包含在已审记录中，不与纳入篇数相加。

| 来源 | 本轮已审 | 新爬 | 纳入 | 排除 | 待定 | 核验补齐摘要 |
|---|---|---|---|---|---|---|
| Nature Communications | 1134 | 0 | 12 | 1059 | 63 | 0 |
| CVPR | 86 | 0 | 8 | 75 | 3 | 0 |
| Molecular Cell | 56 | 0 | 0 | 56 | 0 | 37 |
| Nature Microbiology | 45 | 0 | 0 | 43 | 2 | 0 |
| Nature Neuroscience | 30 | 0 | 1 | 25 | 4 | 0 |
| Nature Physics | 27 | 0 | 0 | 27 | 0 | 0 |
| Nature Chemical Biology | 26 | 0 | 0 | 24 | 2 | 0 |
| Nature Human Behaviour | 25 | 0 | 0 | 23 | 2 | 0 |
| Nature Ecology & Evolution | 11 | 0 | 0 | 11 | 0 | 0 |
| Cell Discovery | 9 | 0 | 0 | 8 | 1 | 1 |
| Chem | 7 | 0 | 0 | 7 | 0 | 2 |
| Journal of Materials Science & Technology | 6 | 0 | 0 | 6 | 0 | 6 |
| The Lancet Regional Health - Europe | 5 | 0 | 0 | 5 | 0 | 1 |
| The Lancet Planetary Health | 5 | 0 | 0 | 5 | 0 | 0 |
| Trends in Microbiology | 4 | 0 | 0 | 4 | 0 | 4 |
| Journal of Advanced Research | 4 | 0 | 0 | 4 | 0 | 4 |
| Clinical Gastroenterology and Hepatology | 3 | 0 | 0 | 2 | 1 | 2 |
| Nature Geoscience | 3 | 0 | 0 | 3 | 0 | 0 |
| Nature Protocols | 3 | 0 | 0 | 3 | 0 | 0 |
| Energy Storage Materials | 2 | 0 | 0 | 2 | 0 | 0 |
| The Lancet Haematology | 2 | 0 | 0 | 2 | 0 | 2 |
| Seminars in Cancer Biology | 2 | 0 | 0 | 2 | 0 | 2 |
| Smart Learning Environments | 2 | 0 | 0 | 1 | 1 | 0 |
| International Journal of Mining Science and Technology | 1 | 0 | 0 | 1 | 0 | 0 |
| Information Fusion | 1 | 0 | 0 | 1 | 0 | 1 |
| Nano Energy | 1 | 0 | 0 | 1 | 0 | 1 |
| **合计** | 1500 | 0 | 21 | 1400 | 79 | 63 |

## 新增漏筛纳入论文与标签

| 来源 | 论文 | 摘要依据 | 标签 |
|---|---|---|---|
| CVPR | [LPSNet: End-to-End Human Pose and Shape Estimation with Lensless Imaging](https://openaccess.thecvf.com/content/CVPR2024/html/Ge_LPSNet_End-to-End_Human_Pose_and_Shape_Estimation_with_Lensless_Imaging_CVPR_2024_paper.html) | 初筛漏筛补录。针对实际无透镜成像系统设计神经解码器，从光学编码测量恢复人体姿态与形状并实测验证。 | AI 用于工程科学、人体姿态识别、深度学习 |
| CVPR | [LASIL: Learner-Aware Supervised Imitation Learning For Long-term Microscopic Traffic Simulation](https://openaccess.thecvf.com/content/CVPR2024/html/Guo_LASIL_Learner-Aware_Supervised_Imitation_Learning_For_Long-term_Microscopic_Traffic_Simulation_CVPR_2024_paper.html) | 初筛漏筛补录。变分自编码器与模仿学习改进城市微观交通仿真，在真实交通数据上评价宏微观真实性。 | AI 用于工程科学、交通场景建模、模仿学习、变分自编码器 |
| CVPR | [RCooper: A Real-world Large-scale Dataset for Roadside Cooperative Perception](https://openaccess.thecvf.com/content/CVPR2024/html/Hao_RCooper_A_Real-world_Large-scale_Dataset_for_Roadside_Cooperative_Perception_CVPR_2024_paper.html) | 初筛漏筛补录。构建真实路侧协同感知数据及检测跟踪基准，直接研究道路感知盲区与区域覆盖问题，支撑交通工程中的AI感知。 | AI 用于工程科学、自动驾驶感知、交通目标跟踪、科学数据 |
| CVPR | [WildlifeMapper: Aerial Image Analysis for Multi-Species Detection and Identification](https://openaccess.thecvf.com/content/CVPR2024/html/Kumar_WildlifeMapper_Aerial_Image_Analysis_for_Multi-Species_Detection_and_Identification_CVPR_2024_paper.html) | 初筛漏筛补录。通过视觉模型识别航空影像中的野生动物，构建专家标注资源以支持生态种群监测。 | AI 用于生命科学、野生动物识别、目标检测、科学数据 |
| CVPR | [MS-MANO: Enabling Hand Pose Tracking with Biomechanical Constraints](https://openaccess.thecvf.com/content/CVPR2024/html/Xie_MS-MANO_Enabling_Hand_Pose_Tracking_with_Biomechanical_Constraints_CVPR_2024_paper.html) | 初筛漏筛补录。将肌肉骨骼及肌腱动力学与学习模型整合，利用仿真闭环约束人体手部运动重建。 | AI 用于生命科学、人体姿态识别、多层感知机、物理与数据融合建模 |
| CVPR | [UVEB: A Large-scale Benchmark and Baseline Towards Real-World Underwater Video Enhancement](https://openaccess.thecvf.com/content/CVPR2024/html/Xie_UVEB_A_Large-scale_Benchmark_and_Baseline_Towards_Real-World_Underwater_Video_CVPR_2024_paper.html) | 初筛漏筛补录。以真实水下成像退化为对象构建大规模视频数据并用监督网络改善水下视频质量。 | AI 用于工程科学、水下图像增强、卷积神经网络、监督学习、科学数据 |
| CVPR | [ERMVP: Communication-Efficient and Collaboration-Robust Multi-Vehicle Perception in Challenging Environments](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_ERMVP_Communication-Efficient_and_Collaboration-Robust_Multi-Vehicle_Perception_in_Challenging_Environments_CVPR_2024_paper.html) | 初筛漏筛补录。针对车辆协同感知的带宽限制及定位误差设计学习式信息融合，在真实和模拟道路数据验证。 | AI 用于工程科学、自动驾驶感知 |
| CVPR | [TUMTraf V2X Cooperative Perception Dataset](https://openaccess.thecvf.com/content/CVPR2024/html/Zimmer_TUMTraf_V2X_Cooperative_Perception_Dataset_CVPR_2024_paper.html) | 初筛漏筛补录。构建道路与车载传感器协同感知数据资源及融合模型，覆盖真实交通安全相关驾驶情景。 | AI 用于工程科学、自动驾驶感知、交通目标跟踪、多模态学习、科学数据 |
| Nature Communications | [Statistical method scDEED for detecting dubious 2D single-cell embeddings and optimizing t-SNE and UMAP hyperparameters](https://www.nature.com/articles/s41467-024-45891-y) | 初筛漏筛补录。scDEED评估单细胞嵌入可靠性并优化t-SNE和UMAP超参数，直接改善细胞分群图谱分析。 | AI 用于生命科学、单细胞表征学习、科学评测 |
| Nature Communications | [High-order sensory processing nanocircuit based on coupled VO2 oscillators](https://www.nature.com/articles/s41467-024-45992-8) | 初筛漏筛补录。VO2耦合振荡神经形态感知网络配合决策模块完成触觉和手势识别，有实际硬件工程验证。 | AI 用于工程科学、人体姿态识别 |
| Nature Communications | [Interrogations of single-cell RNA splicing landscapes with SCASL define new cell identities with physiological relevance](https://www.nature.com/articles/s41467-024-46480-9) | 初筛漏筛补录。SCASL以替代剪接图谱进行单细胞聚类，发现肿瘤早期细胞和发育谱系，直接贡献生物学分析方法。 | AI 用于生命科学、细胞类型识别、聚类 |
| Nature Communications | [Perception of motion salience shapes the emergence of collective motions](https://www.nature.com/articles/s41467-024-49151-x) | 初筛漏筛补录。从鸟群数据提炼自适应感知交互规则，并在约百个机器人群中验证自主疏散组织能力。 | AI 用于工程科学、动物行为分析、机器人运动控制 |
| Nature Communications | [Demixing fluorescence time traces transmitted by multimode fibers](https://www.nature.com/articles/s41467-024-50306-z) | 初筛漏筛补录。非负矩阵分解从多模光纤原始视频分离多源荧光时间轨迹，为微创脑活动测量提供方法并实验验证。 | AI 用于生命科学、工程传感数据重建、非负矩阵分解 |
| Nature Communications | [Integrated triboelectric nanogenerator and radiative cooler for all-weather transparent glass surfaces](https://www.nature.com/articles/s41467-024-50872-2) | 初筛漏筛补录。利用进化算法优化辐射冷却组件并与摩擦发电集成，通过实测验证能源玻璃性能。 | AI 用于工程科学、能源系统优化、演化优化 |
| Nature Communications | [Fasting induces metabolic switches and spatial redistributions of lipid processing and neuronal interactions in tanycytes](https://www.nature.com/articles/s41467-024-50913-w) | 初筛漏筛补录。单细胞聚类和伪空间分析识别下丘脑室管膜细胞亚群，揭示禁食引起的代谢与空间重分布。 | AI 用于生命科学、细胞类型识别、聚类 |
| Nature Communications | [Efficient learning of ground and thermal states within phases of matter](https://www.nature.com/articles/s41467-024-51439-x) | 初筛漏筛补录。提出样本高效学习量子基态与热态及可观测量的方法和理论保证，直接服务多体物理推断。 | AI 用于数理科学、量子态性质学习、机器学习 |
| Nature Communications | [Unique genetic and risk-factor profiles in clusters of major depressive disorder-related multimorbidity trajectories](https://www.nature.com/articles/s41467-024-51467-7) | 初筛漏筛补录。动态贝叶斯网络筛选抑郁症相关共病，并学习七类终生疾病负担轨迹，关联遗传与临床风险因素。 | AI 用于生命科学、疾病分型、概率图模型、聚类 |
| Nature Communications | [The morphospace of the brain-cognition organisation](https://www.nature.com/articles/s41467-024-52186-9) | 初筛漏筛补录。学习三维脑认知潜在嵌入空间，预测未见功能激活并解码观影内在状态，直接研究认知组织。 | AI 用于生命科学、神经表征学习、潜变量建模 |
| Nature Communications | [Single-cell morphometrics reveals T-box gene-dependent patterns of epithelial tension in the Second Heart field](https://www.nature.com/articles/s41467-024-53612-8) | 初筛漏筛补录。联合空间PCA学习单细胞形态模式并关联上皮应力和基因调控，直接研究心脏形态发生。 | AI 用于生命科学、细胞表征建模、主成分分析 |
| Nature Communications | [Sensing expectation enables simultaneous proprioception and contact detection in an intelligent soft continuum robot](https://www.nature.com/articles/s41467-024-54327-6) | 初筛漏筛补录。软连续体机器人通过预期与实际感知闭环学习触觉导航，并在人机交互实验中验证。 | AI 用于工程科学、机器人运动控制、机器人接触操作 |
| Nature Neuroscience | [Cortical gene expression architecture links healthy neurodevelopment to the imaging, transcriptomics and genetics of autism and schizophrenia](https://www.nature.com/articles/s41593-024-01624-4) | 初筛漏筛补录。主成分分析学习皮质基因表达结构，跨数据集关联神经发育、自闭症及精神分裂症机制。 | AI 用于生命科学、转录组分析、主成分分析 |

## 标签和元数据

本轮使用39种标签，其中34种复用现有词项，新增5项；共享词表由757项增至762项。提交前再次同步并检查中英文名称、维度和别名，未发现同义重复。未明确支持的方法或训练阶段不标。

| 维度 | 新增中文标签 | 英文 | 适用范围 |
|---|---|---|---|
| method | 主成分分析 | Principal component analysis | 通过正交线性投影提取最大方差方向，用于科学观测的降维、结构识别或特征表示。 |
| method | 非负矩阵分解 | Non-negative matrix factorization | 将非负观测分解为非负因子，用于信号解混、潜在组分发现或科学数据表示。 |
| task | 水下图像增强 | Underwater image enhancement | 针对水下光传播造成的色偏、散射和对比度退化，增强水下图像或视频的可用质量。 |
| task | 野生动物识别 | Wildlife identification | 从自然环境观测或航空影像中检测、定位并识别野生动物物种，支持种群调查和生态保护。 |
| task | 量子态性质学习 | Quantum state property learning | 由量子测量样本学习量子态参数或可观测量期望值，包括基态和热态性质；不要求学习算法在量子硬件上运行。 |

- 21篇正式页面引用元数据已核对；19篇取得题名、年份匹配的Crossref书目；20篇核实DOI。作者字段冲突及访问失败记录在逐条审计中，未核实值不当作已核实。
- 8个公开PDF端点通过HTTP HEAD检查，其他端点留空或标为未核验。未下载或读取PDF。代码／项目链接保留原数据，本轮未声明新增可用性核验。

## 累计进度与剩余工作

| 指标 | 累计 |
|---|---|
| 已审 | 17,333条 |
| 纳入 | 2,457篇 |
| 排除 | 13,826条（无AI4S实质关系、非研究文种或不属本批范围） |
| 待定 | 1,050条（证据不足或摘要问题） |
| 漏筛纳入 | 1,306篇（已含在纳入总数内） |
| 核验补齐完整摘要 | 1,620条 |
| 尚未审核 | 13,135条 |

**剩余6,170条有供给摘要／待核描述可继续，另6,965条缺可用摘要暂缓。** 两者合计13,135条未审；已审待定1,050条另列。全量审核和官网补漏尚未完成。

唯一键、原字段、旧15,833条完整记录、标签规范和数量闭合校验通过：17,333已审＋13,135未审＝30,468。跨审核同键重合890条、判定不同46条，本轮新增重合0条；仅作审计，未修改他人文件或负责人登记。

交付：[个人JSON](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101.json)、[累计统计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/summary.json)、[逐条审计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation12-batch-decisions.jsonl)、[抽查记录](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation12-batch-qc.json)。实际上传以GitHub提交和本地publication.json为准。
