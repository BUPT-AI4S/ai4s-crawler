# 王婉婷｜AI4S批量续审工作汇报

2026年11月8日 · 2024年论文 · Blueblue1101 · continuation9

**本轮新处理900条，比上一轮多100条：纳入10篇、排除832条、待定58条；补齐并核验完整摘要46条。** 覆盖21个刊会来源，旧12,733条完整记录保持一致。

10篇新增纳入均来自已经采集、但未进入初筛候选的记录，属于**漏筛补录**。本轮新爬论文为0篇，不计作官网漏采补齐。

## 审核方法与结果

按仓库main `97c2759` 的当前skill和757项共享词表，批量读取完整摘要，逐条记录判定、具体理由和摘要哈希。根据科学／工程任务、AI实际作用及两者关系判断；不读正文或PDF，不以关键词命中替代语义判断。只保留原创研究、正式会议研究论文和有实质内容的综述。

| 处理结果 | 条数 | 原因 |
|---|---|---|
| 纳入 | 10 | 摘要支持AI对具体科学或工程任务的贡献；书目及标签已复核 |
| 相关性排除 | 826 | 未显示AI实质参与，或仅通用算法与基准评测，缺少具体科学工程贡献 |
| 文种排除 | 6 | 采样／数据归档指南、政策倡议或明确观点评论，不属于本批保留的研究及综述 |
| 待定：摘要问题 | 4 | 摘要截断，或仅有背景与目的，不能作为完整摘要判断 |
| 待定：证据不足 | 54 | 摘要没有说清AI方法、具体科学贡献或两者关系，需补方法证据 |

900条中，890条完成摘要语义判断，6条按明确文种处理，4条只完成摘要质量核查。固定随机种子抽查20条初判排除记录：17条维持，1条因识别算法不明改为待定，2条仍排除但改为按相关性排除，避免仅凭观点／展望名称判断文种。全部10篇纳入另行重读核对。该抽查不能代表全量准确率。

## 各刊会本轮工作量

补摘要数属于元数据工作量，不与纳入数相加。表中均为既有数据续审，缺摘要或访问异常的其他记录继续暂缓。

| 来源 | 本轮已审 | 纳入 | 排除 | 待定 | 补齐完整摘要 |
|---|---|---|---|---|---|
| Nature Communications | 649 | 7 | 599 | 43 | 0 |
| Molecular Cell | 59 | 0 | 58 | 1 | 32 |
| Nature Chemical Biology | 35 | 0 | 31 | 4 | 0 |
| CVPR | 32 | 3 | 26 | 3 | 0 |
| Nature Microbiology | 32 | 0 | 31 | 1 | 0 |
| Nature Human Behaviour | 20 | 0 | 20 | 0 | 0 |
| Nature Neuroscience | 15 | 0 | 13 | 2 | 0 |
| Nature Physics | 15 | 0 | 15 | 0 | 0 |
| Chem | 10 | 0 | 10 | 0 | 6 |
| Energy Storage Materials | 6 | 0 | 6 | 0 | 0 |
| Nature Ecology & Evolution | 6 | 0 | 6 | 0 | 0 |
| Nano Energy | 4 | 0 | 4 | 0 | 3 |
| Clinical Gastroenterology and Hepatology | 3 | 0 | 0 | 3 | 0 |
| The Lancet Regional Health - Europe | 3 | 0 | 2 | 1 | 0 |
| Journal of Materials Science & Technology | 2 | 0 | 2 | 0 | 2 |
| Trends in Microbiology | 2 | 0 | 2 | 0 | 2 |
| Cell Discovery | 2 | 0 | 2 | 0 | 0 |
| Nature Geoscience | 2 | 0 | 2 | 0 | 0 |
| Seminars in Cancer Biology | 1 | 0 | 1 | 0 | 1 |
| The Lancet Planetary Health | 1 | 0 | 1 | 0 | 0 |
| Smart Learning Environments | 1 | 0 | 1 | 0 | 0 |
| **合计** | 900 | 10 | 832 | 58 | 46 |

## 10篇漏筛纳入论文与标签

| 来源 | 论文 | 摘要依据 | 标签 |
|---|---|---|---|
| CVPR | [EarthLoc: Astronaut Photography Localization by Indexing Earth from Space](https://openaccess.thecvf.com/content/CVPR2024/html/Berton_EarthLoc_Astronaut_Photography_Localization_by_Indexing_Earth_from_Space_CVPR_2024_paper.html) | 初筛漏筛补录。学习图像检索模型定位宇航员地球摄影，弥补地球观测数据地理配准缺口，直接支持科研数据利用。 | AI 用于地球宇宙科学、遥感影像分析、监督学习 |
| CVPR | [CRKD: Enhanced Camera-Radar Object Detection with Cross-modality Knowledge Distillation](https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_CRKD_Enhanced_Camera-Radar_Object_Detection_with_Cross-modality_Knowledge_Distillation_CVPR_2024_paper.html) | 初筛漏筛补录。跨模态知识蒸馏提升相机雷达自动驾驶三维感知，直接应对车载低成本传感器配置的工程问题。 | AI 用于工程科学、自动驾驶感知、知识蒸馏、多模态学习 |
| CVPR | [Loose Inertial Poser: Motion Capture with IMU-attached Loose-Wear Jacket](https://openaccess.thecvf.com/content/CVPR2024/html/Zuo_Loose_Inertial_Poser_Motion_Capture_with_IMU-attached_Loose-Wear_Jacket_CVPR_2024_paper.html) | 初筛漏筛补录。自编码器学习衣物与皮肤间次级运动并合成IMU数据，改善宽松穿戴动作捕捉工程的姿态估计。 | AI 用于工程科学、人体姿态识别、科学训练数据生成、自编码器 |
| Nature Communications | [Zebrafish Avatar-test forecasts clinical response to chemotherapy in patients with colorectal cancer](https://www.nature.com/articles/s41467-024-49051-0) | 初筛漏筛补录。决策树融合肿瘤分期和斑马鱼移植实验指标预测结直肠癌患者化疗进展，提供个体治疗响应预测。 | AI 用于生命科学、治疗反应预测、决策树 |
| Nature Communications | [Tracking single hiPSC-derived cardiomyocyte contractile function using CONTRAX an efficient pipeline for traction force measurement](https://www.nature.com/articles/s41467-024-49755-3) | 初筛漏筛补录。无监督聚类分析高通量单心肌细胞牵引力数据，揭示成熟模式、药物响应及疾病突变功能差异。 | AI 用于生命科学、细胞表征建模、聚类 |
| Nature Communications | [Ligand control of regioselectivity in palladium-catalyzed heteroannulation reactions of 1,3-Dienes](https://www.nature.com/articles/s41467-024-49803-y) | 初筛漏筛补录。数据驱动线性回归以配体计算描述符学习化学区域选择性，提取关键参数指导催化合成方法设计。 | AI 用于物质科学、反应结果预测、监督学习 |
| Nature Communications | [Learning interpretable dynamics of stochastic complex systems from experimental data](https://www.nature.com/articles/s41467-024-50378-x) | 初筛漏筛补录。Langevin图网络从实验数据学习可解释随机微分方程，揭示鸟群运动和脑tau病理传播动力学并预测病变。 | AI 用于数理科学、AI 用于生命科学、动力系统辨识、方程发现、图神经网络 |
| Nature Communications | [Diet modifies the association between alcohol consumption and severe alcohol-related liver disease incidence](https://www.nature.com/articles/s41467-024-51314-9) | 初筛漏筛补录。LASSO从饮食变量选择特征构建风险评分，结合队列生存和交互分析揭示饮食对酒精性肝病风险的调节。 | AI 用于生命科学、疾病风险预测、特征选择 |
| Nature Communications | [Quantitative matching of forensic evidence fragments using fracture surface topography and statistical learning](https://www.nature.com/articles/s41467-024-51594-1) | 初筛漏筛补录。多变量统计学习结合三维断裂表面形貌，自动分类法医物证碎片是否匹配，直接支持材料物证鉴定。 | AI 用于工程科学、材料结构分析、监督学习 |
| Nature Communications | [A hierarchical active inference model of spatial alternation tasks and the hippocampal-prefrontal circuit](https://www.nature.com/articles/s41467-024-54257-3) | 初筛漏筛补录。分层主动推断模型连接海马与前额叶认知地图，模拟空间交替和损伤效应以解释神经决策机制。 | AI 用于生命科学、神经概率推断建模、贝叶斯学习 |

## 元数据与标签核验

- 10篇均匹配官方页面的题名、作者顺序和2024年出版信息，并核验DOI；其中9篇另匹配出版社登记的Crossref记录，1篇以Nature官方引用元数据确认。
- 3篇CVPR补入原记录缺失的DOI，公开PDF端点通过HTTP HEAD检查；7篇Nature Communications论文的PDF出现Cookie错误跳转，已标为未核验，不猜填可访问状态。未下载或阅读PDF。
- CRKD摘要声明的项目页、EarthLoc摘要声明的代码仓库均通过HEAD检查，其余未经证实的代码／项目链接不补造。
- 本轮复用26种现有标签，无新增词项，词表仍为757项。逐篇标签见上表。涵盖神经机制、动力系统辨识、地球观测、自动驾驶、治疗反应、化学反应、细胞表征和疾病风险等任务；简单统计关联不自动算AI，明确的学习／特征选择／聚类作用需有摘要依据。

## 累计进度与剩余工作

| 指标 | 累计结果 |
|---|---|
| 已审记录 | 13,633 |
| 纳入 | 2,390篇 |
| 排除 | 10,405条（无AI4S实质关系、非研究文种或不属本批范围） |
| 待定 | 838条 |
| 确认漏筛纳入 | 1,239篇（已包含在纳入总数内） |
| 核验补齐完整摘要 | 1,483条 |
| 仍未审 | 16,835条 |

**全量审核尚未完成。** 剩余16,835条中，6,965条缺可用摘要暂缓，9,870条有供给摘要或待核描述，可从断点继续。这些描述仍可能有质量问题，不能全部视为合格完整摘要。已审待定838条单独保留，不包含在未审16,835条内。

此前1,574条初筛候选（包含1,383条个人旧记录）均已复核。本轮按摘要长度安排阅读顺序，纳入比例不外推到剩余记录；官网漏采核验沿用既有审计，本轮没有扩大其已核验范围。

唯一键、原字段、旧12,733条完整记录、757项词表与总量闭合校验通过：13,633已审＋16,835未审＝30,468。跨审核文件同键重合890条、判定不同46条，本轮新增重合0条；未修改他人文件或负责人登记。

交付：[个人JSON](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101.json)、[累计统计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/summary.json)、[本轮逐条审计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation9-batch-decisions.jsonl)、[抽查记录](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation9-batch-qc.json)。实际上传以GitHub提交记录及本地publication.json为准。
