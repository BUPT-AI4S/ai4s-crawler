# 王婉婷｜AI4S批量续审工作汇报

2026年11月8日 · 2024年论文 · GitHub：Blueblue1101

**本轮新增审核600条：纳入5篇、排除456条、待定139条；补齐并核验完整摘要57条。** 在此前已上传的10,933条基础上续做，旧记录完整保留。

## 处理方法和结果

每批读取40—80条现有摘要或书目描述，逐条保存结论与理由。先排除明确的非研究文种，再判断科学任务、AI作用及两者关系；可能纳入和不确定项单独复核。排序只决定阅读顺序，未用关键词命中代替判定，也未读取正文。

| 结果 | 条数 | 原因 |
|---|---|---|
| 纳入 | 5 | 摘要明确支持AI参与科学或工程任务；书目信息和标签再次核对 |
| 按类型排除 | 233 | 更正、撤稿、研究短评、访谈、会议报道、通信及观点等非本批纳入文种 |
| 按相关性排除 | 223 | 无AI实质参与，或仅通用算法、图像创作及常规计算，未体现具体科学工程贡献 |
| 待定：摘要问题 | 124 | 残缺背景、致谢、占位或其他非完整摘要，未当作无关论文排除 |
| 待定：证据不足 | 15 | AI作用、科学任务关系或正式文献类型仍不明确 |

**抽查：**固定随机种子，从类型排除和相关性排除各抽10条，完整重读后维持判定。另核对5篇纳入论文及4条边界记录。单细胞模型后门攻击论文一度转为待定，随后出版社元数据确认是 **Correspondence**，最终按文献类型排除。两条同题名Chem记录经Europe PMC确认为不同DOI的更正通知。抽查不代表全量准确率已获保证。

## 各刊会本轮工作量

本轮都是原有全量数据中的记录，**新爬论文0篇，确认关键词漏筛补入5篇**。补摘要是元数据工作量，不能与纳入数相加。

| 期刊／会议 | 本轮已审 | 纳入 | 排除 | 待定 | 补齐完整摘要 |
|---|---|---|---|---|---|
| Nature Communications | 131 | 1 | 124 | 6 | 0 |
| Molecular Cell | 102 | 0 | 99 | 3 | 3 |
| The Lancet Regional Health - Europe | 86 | 0 | 40 | 46 | 0 |
| Trends in Microbiology | 63 | 0 | 63 | 0 | 21 |
| The Lancet Planetary Health | 44 | 0 | 12 | 32 | 0 |
| Trends in Cognitive Sciences | 36 | 0 | 32 | 4 | 24 |
| Clinical Gastroenterology and Hepatology | 29 | 0 | 4 | 25 | 1 |
| CVPR | 23 | 3 | 19 | 1 | 0 |
| Chem | 17 | 0 | 15 | 2 | 3 |
| Cell Discovery | 13 | 0 | 7 | 6 | 0 |
| Nature Neuroscience | 9 | 0 | 7 | 2 | 0 |
| Nature Geoscience | 8 | 0 | 8 | 0 | 0 |
| Molecular Neurodegeneration | 7 | 0 | 6 | 1 | 0 |
| Nature Physics | 6 | 0 | 6 | 0 | 0 |
| The Lancet Haematology | 4 | 0 | 1 | 3 | 0 |
| Information Fusion | 4 | 0 | 2 | 2 | 2 |
| Nature Microbiology | 4 | 0 | 3 | 1 | 0 |
| Nature Ecology & Evolution | 3 | 0 | 3 | 0 | 0 |
| Trends in Food Science & Technology | 2 | 0 | 0 | 2 | 0 |
| Seminars in Cancer Biology | 2 | 0 | 2 | 0 | 2 |
| Energy Storage Materials | 1 | 0 | 0 | 1 | 0 |
| Journal of Energy Chemistry | 1 | 0 | 0 | 1 | 0 |
| Smart Learning Environments | 1 | 0 | 1 | 0 | 0 |
| Nano Energy | 1 | 0 | 1 | 0 | 1 |
| Journal of Advanced Research | 1 | 0 | 0 | 1 | 0 |
| Nature Human Behaviour | 1 | 1 | 0 | 0 | 0 |
| Nature Protocols | 1 | 0 | 1 | 0 | 0 |
| **合计** | 600 | 5 | 456 | 139 | 57 |

## 新确认纳入的5篇论文与标签

| 来源 | 论文 | 摘要依据 | 标签 |
|---|---|---|---|
| CVPR | [Multi-Session SLAM with Differentiable Wide-Baseline Pose Optimization](https://openaccess.thecvf.com/content/CVPR2024/html/Lipson_Multi-Session_SLAM_with_Differentiable_Wide-Baseline_Pose_Optimization_CVPR_2024_paper.html) | 将学习的光流预测与可微位姿求解器联合训练，实现多段不连续视频的统一定位、视觉里程计及全局优化，直接支持物理环境中的定位建图工程任务。 | AI 用于工程科学、视觉同步定位与建图、可微优化 |
| CVPR | [CyberDemo: Augmenting Simulated Human Demonstration for Real-World Dexterous Manipulation](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_CyberDemo_Augmenting_Simulated_Human_Demonstration_for_Real-World_Dexterous_Manipulation_CVPR_2024_paper.html) | 从仿真人类演示通过模仿学习获得机器人操作策略，使用数据增强迁移到真实灵巧操作，并验证未见物体泛化，AI直接参与机器人控制工程任务。 | AI 用于工程科学、机器人操作控制、模仿学习 |
| CVPR | [DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_DrivingGaussian_Composite_Gaussian_Splatting_for_Surrounding_Dynamic_Autonomous_Driving_Scenes_CVPR_2024_paper.html) | 通过三维高斯表示、动态对象图与激光雷达先验重建自动驾驶动态场景，改善多相机一致性和周视图合成，直接贡献于自动驾驶场景建模工程任务。 | AI 用于工程科学、自动驾驶场景重建 |
| Nature Human Behaviour | [How developments in natural language processing help us in understanding human behaviour](https://www.nature.com/articles/s41562-024-01938-0) | 实质方法综述，讨论自然语言处理如何从语言数据分析情绪、社会行为、思维与文化，并比较其与传统调查方法的关系，直接支持社会心理研究。 | AI 用于社会科学、自然语言处理 |
| Nature Communications | [FinaleMe: Predicting DNA methylation by the fragmentation patterns of plasma cell-free DNA](https://www.nature.com/articles/s41467-024-47196-6) | 利用非齐次隐马尔可夫模型从血浆游离DNA片段模式预测甲基化及组织来源，并以80组成对测序数据验证，AI推断直接支持表观遗传与生物标志物研究。 | AI 用于生命科学、DNA甲基化预测、隐马尔可夫模型 |

## 元数据和词表

- 5篇题名、作者、2024年出版信息与Crossref登记逐项匹配；3篇CVPR论文补上DOI，并核对CVF正式论文页。
- 3个CVF PDF地址通过HTTP HEAD确认公开PDF响应；未下载或阅读PDF。2个Nature PDF地址有Cookie错误跳转，保留未确认状态，不把HTTP 200直接视为可用。
- DrivingGaussian代码仓库和CyberDemo项目页均由正式摘要给出，并检查链接可访问；未运行代码。其余未查到的代码或项目链接不猜填。
- 使用main `5eeb5cf` 的754项词表，新增下列3个任务标签，共757项。已有同义词与规范名均先检索。

| 新增中文标签 | 英文规范名 | 含义 |
|---|---|---|
| DNA甲基化预测 | DNA methylation prediction | 利用学习或概率推断模型，从序列、片段组学或其他观测预测DNA甲基化状态或水平。 |
| 视觉同步定位与建图 | Visual simultaneous localization and mapping | 利用视觉数据与学习模型联合估计相机轨迹并构建或对齐物理环境地图。 |
| 自动驾驶场景重建 | Autonomous driving scene reconstruction | 从车辆传感数据重建道路环境与动态对象的三维场景，用于自动驾驶工程研究中的场景表示或视图合成。 |

## 累计进度与交付

累计已审 **11,533条**：纳入 **2,360篇**、排除 **8,470条**、待定 **703条**。累计漏筛纳入 **1,209篇**，完整摘要补齐 **1,293条**。原1,574条初筛候选及其中1,383条旧记录已完成复核。

**全量审核尚未完成。** 30,468条原始记录中仍有 **18,935条未审**：其中6,965条缺可用摘要，暂缓；另11,970条有摘要或待核描述，保留续审队列。本批短摘要和类型描述较集中，不能用本批纳入比例推算其余队列。官网目录补漏沿用此前审计，本次没有扩大已核验覆盖范围。

本轮个人JSON、审计清单、词表及汇报随同提交：

- [个人论文结果](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101.json)
- [本轮统计与逐源覆盖](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/summary.json)
- [抽查与边界复核记录](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation6-batch-qc.json)
- [共享词表](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/skills/ai4s-paper-review/references/tag-vocabulary.json)

已校验唯一键、原字段保留、旧10,933条完整记录一致、标签规范和计数闭合。历史跨审核人重合继续保留审计，不覆盖他人结果；本轮新增重合数见summary.json。实际上传以GitHub提交记录及本地publication.json为准。
