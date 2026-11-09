# 王婉婷｜AI4S批量续审工作汇报

2026年11月8日 · 2024年论文 · Blueblue1101 · continuation8

**本轮新处理800条，是上一轮400条的两倍：纳入15篇、排除739条、待定46条；补齐并核验完整摘要53条。** 覆盖27个刊会来源，旧11,933条完整记录保持一致。

15篇新增纳入均来自已经采集、但未进入初筛候选的记录，属于**漏筛补录**；本轮新爬论文为0篇，不计作官网漏采补齐。

## 审核方法与结果

使用main `b3d3f97` 的当前规则和共享词表，按每批20—40条读取摘要，逐条保存结论、理由和摘要哈希。分别核对具体科学／工程任务、AI的实际作用及两者关系。只保留原创研究、正式会议研究论文和有实质内容的综述；不读取正文或PDF，不以关键词命中代替语义判断。

| 处理结果 | 条数 | 原因 |
|---|---|---|
| 纳入 | 15 | 摘要支持AI对具体科学或工程任务的贡献；书目和标签已复核 |
| 相关性排除 | 734 | 没有AI实质参与，或仅通用算法、视觉生成与性能评测，缺少具体科学工程任务 |
| 文种排除 | 5 | 明确的专家评论、观点文章或针对他文的评论 |
| 待定：摘要问题 | 4 | 摘要截断，或仅有背景／目的，缺少完整结果与结论 |
| 待定：证据不足 | 42 | 未说明AI算法、具体科学贡献或两者关系，需补方法证据 |

其中791条完成摘要语义判断，5条按明确文种处理，4条只完成摘要质量核查，不能将800条全部称为完整摘要精筛。固定随机种子抽查20条排除记录（5条文种、15条相关性），重读后均维持结论；另核对全部15篇纳入。抽查结果不能代表全量准确率。

## 各刊会本轮工作量

补摘要数属于元数据工作量，与纳入数不相加。以下均为既有数据续审，缺摘要或访问异常的其他记录继续暂缓。

| 来源 | 本轮已审 | 纳入 | 排除 | 待定 | 补齐完整摘要 |
|---|---|---|---|---|---|
| Nature Communications | 570 | 5 | 535 | 30 | 0 |
| CVPR | 67 | 9 | 56 | 2 | 0 |
| Molecular Cell | 24 | 0 | 22 | 2 | 11 |
| Nature Physics | 19 | 0 | 19 | 0 | 0 |
| Nature Chemical Biology | 16 | 0 | 14 | 2 | 0 |
| Nature Neuroscience | 16 | 0 | 15 | 1 | 0 |
| Trends in Microbiology | 14 | 0 | 13 | 1 | 14 |
| Nature Human Behaviour | 10 | 0 | 9 | 1 | 0 |
| Journal of Energy Chemistry | 8 | 0 | 8 | 0 | 5 |
| Nature Microbiology | 8 | 0 | 8 | 0 | 0 |
| Nano Energy | 7 | 0 | 7 | 0 | 4 |
| Chem | 5 | 0 | 5 | 0 | 4 |
| Trends in Cognitive Sciences | 5 | 0 | 2 | 3 | 5 |
| The Lancet Regional Health - Europe | 4 | 0 | 4 | 0 | 0 |
| Information Fusion | 4 | 1 | 2 | 1 | 4 |
| Energy Storage Materials | 3 | 0 | 3 | 0 | 1 |
| Seminars in Cancer Biology | 3 | 0 | 3 | 0 | 3 |
| Clinical Gastroenterology and Hepatology | 3 | 0 | 1 | 2 | 0 |
| Trends in Food Science & Technology | 2 | 0 | 2 | 0 | 0 |
| The Lancet Planetary Health | 2 | 0 | 2 | 0 | 0 |
| Nature Ecology & Evolution | 2 | 0 | 2 | 0 | 0 |
| Cell Discovery | 2 | 0 | 1 | 1 | 0 |
| Nature Geoscience | 2 | 0 | 2 | 0 | 0 |
| The Lancet Haematology | 1 | 0 | 1 | 0 | 1 |
| Journal of Materials Science & Technology | 1 | 0 | 1 | 0 | 1 |
| Smart Learning Environments | 1 | 0 | 1 | 0 | 0 |
| Nature Protocols | 1 | 0 | 1 | 0 | 0 |
| **合计** | 800 | 15 | 739 | 46 | 53 |

## 15篇漏筛纳入论文与标签

| 来源 | 论文 | 摘要依据 | 标签 |
|---|---|---|---|
| CVPR | [Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping](https://openaccess.thecvf.com/content/CVPR2024/html/Costanzino_Multimodal_Industrial_Anomaly_Detection_by_Crossmodal_Feature_Mapping_CVPR_2024_paper.html) | 初筛漏筛补录。跨模态学习点云与图像特征映射，直接用于工业制造缺陷检测并降低部署资源开销。 | AI 用于工程科学、工业缺陷检测、多模态学习 |
| CVPR | [Producing and Leveraging Online Map Uncertainty in Trajectory Prediction](https://openaccess.thecvf.com/content/CVPR2024/html/Gu_Producing_and_Leveraging_Online_Map_Uncertainty_in_Trajectory_Prediction_CVPR_2024_paper.html) | 初筛漏筛补录：在线高精地图模型输出不确定性并用于自动驾驶轨迹预测，直接改善真实驾驶数据的预测性能。 | AI 用于工程科学、自动驾驶感知、不确定性量化 |
| CVPR | [Multi-Space Alignments Towards Universal LiDAR Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Multi-Space_Alignments_Towards_Universal_LiDAR_Segmentation_CVPR_2024_paper.html) | 初筛漏筛补录：跨数据、特征和标签空间对齐训练统一LiDAR分割模型，针对多传感器驾驶场景感知并在多个驾驶数据集验证。 | AI 用于工程科学、自动驾驶感知、多模态学习 |
| CVPR | [Learnable Earth Parser: Discovering 3D Prototypes in Aerial Scans](https://openaccess.thecvf.com/content/CVPR2024/html/Loiseau_Learnable_Earth_Parser_Discovering_3D_Prototypes_in_Aerial_Scans_CVPR_2024_paper.html) | 初筛漏筛补录：无监督概率重建学习三维原型，对真实航空LiDAR大尺度点云进行可解释分解和语义分割，直接服务航空测绘。 | AI 用于地球宇宙科学、地表覆盖制图、无监督学习 |
| CVPR | [Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation](https://openaccess.thecvf.com/content/CVPR2024/html/Ma_Hierarchical_Diffusion_Policy_for_Kinematics-Aware_Multi-Task_Robotic_Manipulation_CVPR_2024_paper.html) | 初筛漏筛补录。分层扩散策略结合可微机器人运动学，直接解决多任务机械臂规划和轨迹控制并有实机验证。 | AI 用于工程科学、机器人操作控制、扩散模型 |
| CVPR | [Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Driving_into_the_Future_Multiview_Visual_Forecasting_and_Planning_with_CVPR_2024_paper.html) | 初筛漏筛补录：驾驶世界模型生成多视角未来视频，以图像奖励比较驾驶动作并规划轨迹，直接支持安全自动驾驶规划。 | AI 用于工程科学、自动驾驶决策、生成建模 |
| CVPR | [Panacea: Panoramic and Controllable Video Generation for Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2024/html/Wen_Panacea_Panoramic_and_Controllable_Video_Generation_for_Autonomous_Driving_CVPR_2024_paper.html) | 初筛漏筛补录。生成时空一致且可控的多视角驾驶视频，直接扩充自动驾驶BEV感知训练数据。 | AI 用于工程科学、科学训练数据生成、生成建模 |
| CVPR | [PARA-Drive: Parallelized Architecture for Real-time Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2024/html/Weng_PARA-Drive_Parallelized_Architecture_for_Real-time_Autonomous_Driving_CVPR_2024_paper.html) | 初筛漏筛补录：系统研究端到端自动驾驶模块连接，提出并行感知、预测、规划架构，提升驾驶性能与实时性。 | AI 用于工程科学、自动驾驶感知、自动驾驶决策 |
| CVPR | [Binding Touch to Everything: Learning Unified Multimodal Tactile Representations](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Binding_Touch_to_Everything_Learning_Unified_Multimodal_Tactile_Representations_CVPR_2024_paper.html) | 初筛漏筛补录：统一多传感器触觉表征与视觉语言模态对齐，展示零样本机器人抓取预测，直接支持机器人触觉感知。 | AI 用于工程科学、机器人抓取、多模态学习 |
| Information Fusion | [Utility-based context-aware multi-agent recommendation system for energy efficiency in residential buildings](https://doi.org/10.1016/j.inffus.2024.102559) | 初筛漏筛补录。上下文感知多智能体推荐模型结合用电行为和价格，直接优化住宅负荷转移并评估节能成本。 | AI 用于工程科学、能源系统优化 |
| Nature Communications | [Pianno: a probabilistic framework automating semantic annotation for spatial transcriptomics](https://www.nature.com/articles/s41467-024-47152-4) | 初筛漏筛补录：贝叶斯框架基于标志基因自动注释空间转录组结构语义和细胞分布，并结合聚类发现人脑特异神经元亚型。 | AI 用于生命科学、空间转录组分析、贝叶斯学习 |
| Nature Communications | [Curriculum learning for ab initio deep learned refractive optics](https://www.nature.com/articles/s41467-024-50835-7) | 初筛漏筛补录：课程学习从随机曲面自动设计复合折射透镜，并设计手机形态大视场景深光学系统，AI直接参与光学工程设计。 | AI 用于工程科学、光子器件设计、课程学习 |
| Nature Communications | [Interpretable semi-supervised clustering enables universal detection and intensity assessment of diverse aviation hazardous winds](https://www.nature.com/articles/s41467-024-51597-y) | 初筛漏筛补录。可解释半监督聚类融合风场先验和概率模型，直接从雷达激光雷达检测航空危险风并评估强度。 | AI 用于地球宇宙科学、半监督学习、聚类 |
| Nature Communications | [Human detection of political speech deepfakes across transcripts, audio, and video](https://www.nature.com/articles/s41467-024-51998-z) | 初筛漏筛补录。以AI语音合成深伪刺激开展预注册随机人类实验，检验政治信息辨识机制及视听模态作用。 | AI 用于社会科学、生成建模 |
| Nature Communications | [Dopamine builds and reveals reward-associated latent behavioral attractors](https://www.nature.com/articles/s41467-024-53976-x) | 初筛漏筛补录。具身循环网络决策模型模拟多巴胺学习和动机吸引子，并以小鼠光遗传实验验证神经机制预测。 | AI 用于生命科学、神经学习机制建模、循环神经网络 |

## 元数据与标签核验

- 15篇均核对题名、作者和2024年出版信息：14篇匹配官方页面引用元数据，Information Fusion的1篇匹配出版社登记的Crossref元数据。该文摘要明确报告推荐系统及家庭实证结果，但出版社落地页未提供可用引用元数据，已记录局限。
- 15篇均取得核验DOI，其中9篇CVPR补入原记录缺失的DOI；13篇匹配Crossref，另2篇以Nature官方引用元数据确认。
- 9个CVF公开PDF端点通过HTTP HEAD核验，未下载或读取正文；5篇Nature论文的PDF出现Cookie错误跳转，1篇Information Fusion没有已核实的公开PDF，均明确留空或标为未核验。
- Learnable Earth Parser摘要声明的作者项目页通过HEAD检查；其余代码和项目链接未获证实的不猜填。
- 本轮复用757项共享词表中的25种标签，无新增词项。任务标签包括工业缺陷检测、光子器件设计、空间转录组分析、自动驾驶感知与决策、机器人抓取与操作控制、能源系统优化、神经学习机制建模等；方法包括课程学习、多模态学习、扩散模型、贝叶斯学习、半监督学习等。逐篇完整标签见上表。

## 累计进度与剩余工作

| 指标 | 累计结果 |
|---|---|
| 已审记录 | 12,733 |
| 纳入 | 2,380篇 |
| 排除 | 9,573条（无AI4S实质关系、非研究文种或不属本批范围） |
| 待定 | 780条 |
| 确认漏筛纳入 | 1,229篇（已包含在纳入总数内） |
| 核验补齐完整摘要 | 1,437条 |
| 仍未审 | 17,735条 |

**全量审核尚未完成。** 未审17,735条中，6,965条缺可用摘要先暂缓，10,770条有供给摘要或待核描述，可从断点继续。其中仍可能有摘要质量问题，不能全部视为合格完整摘要。按摘要长度安排阅读顺序，本轮纳入比例不外推到剩余记录。官网漏采核验沿用既有审计，本轮没有扩大其已核验范围。

此前1,574条初筛候选（包括1,383条个人旧记录）均已复核。唯一键、原字段、旧11,933条完整记录、757项词表和总量闭合校验通过：12,733已审＋17,735未审＝30,468。跨审核文件同键重合890条、判定不同46条，本轮新增重合0条；未修改他人文件或负责人登记。

交付：[个人JSON](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101.json)、[累计统计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/summary.json)、[本轮逐条审计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation8-batch-decisions.jsonl)、[抽查记录](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation8-batch-qc.json)。实际上传以GitHub提交记录及本地publication.json为准。
