# 王婉婷｜AI4S批量续审工作汇报

2026年11月8日 · 2024年论文 · Blueblue1101 · continuation10

**本轮新处理1,000条，比上一轮多100条：纳入25篇、排除912条、待定63条；补齐并核验完整摘要32条。** 覆盖18个刊会来源，旧13,633条完整记录保持一致。

25篇新增纳入均来自已经采集、但未进入初筛候选的记录，属于**漏筛补录**。本轮新爬论文为0篇，不计作官网漏采补齐。

## 审核方法与结果

按仓库main `f054fad` 的当前skill和757项共享词表，每批读取40条供给摘要，逐条记录判定、理由和摘要哈希；显示被截断的内容单独重读。根据具体科学／工程任务、AI作用和二者关系判断，不读正文或PDF，也不以关键词代替语义审核。缺可用摘要及抓取异常记录先暂缓。

| 处理结果 | 条数 | 原因 |
|---|---|---|
| 纳入 | 25 | 摘要支持AI对具体科学或工程任务的贡献，书目及标签已复核 |
| 相关性排除 | 910 | 未显示AI实质参与，或仅通用模型／基准评测而无具体科学工程贡献 |
| 文种排除 | 2 | 欧盟卫生治理倡议、研究注册倡议，属于观点建议而非本批保留的研究或实质性综述 |
| 待定：摘要问题 | 1 | 题名是金属大环框架，摘要却描述脑视觉行波，明显错配；未将错配文本回填 |
| 待定：证据不足 | 62 | 摘要未说清AI算法、科学任务或两者关系；包括复核后从拟纳入转待定的1篇 |

1,000条中，997条完成摘要语义判断，2条按明确文种处理，1条完成摘要质量核查。固定随机种子重读20条初判排除记录（18条相关性、2条文种），全部维持。26篇初步拟纳入均再次检查：25篇保留，1篇幼儿信息搜索研究因Markov分析是否构成AI尚不明确转待定。抽查结果不外推为全量准确率。

## 各刊会本轮工作量

下表均为既有数据续审；补摘要数是元数据工作量，不与纳入数相加。

| 来源 | 本轮已审 | 纳入 | 排除 | 待定 | 补齐完整摘要 |
|---|---|---|---|---|---|
| Nature Communications | 822 | 15 | 753 | 54 | 0 |
| Molecular Cell | 44 | 0 | 44 | 0 | 24 |
| Nature Microbiology | 36 | 0 | 35 | 1 | 0 |
| CVPR | 23 | 4 | 19 | 0 | 0 |
| Nature Human Behaviour | 15 | 2 | 10 | 3 | 0 |
| Nature Chemical Biology | 15 | 0 | 13 | 2 | 0 |
| Nature Neuroscience | 14 | 3 | 9 | 2 | 0 |
| Chem | 12 | 0 | 11 | 1 | 6 |
| Nature Physics | 5 | 1 | 4 | 0 | 0 |
| Cell Discovery | 4 | 0 | 4 | 0 | 0 |
| Energy Storage Materials | 2 | 0 | 2 | 0 | 0 |
| Nature Ecology & Evolution | 2 | 0 | 2 | 0 | 0 |
| International Journal of Mining Science and Technology | 1 | 0 | 1 | 0 | 0 |
| Trends in Food Science & Technology | 1 | 0 | 1 | 0 | 1 |
| The Lancet Haematology | 1 | 0 | 1 | 0 | 1 |
| The Lancet Regional Health - Europe | 1 | 0 | 1 | 0 | 0 |
| Nano Energy | 1 | 0 | 1 | 0 | 0 |
| Nature Protocols | 1 | 0 | 1 | 0 | 0 |
| **合计** | 1000 | 25 | 912 | 63 | 32 |

## 25篇漏筛纳入论文与标签

| 来源 | 论文 | 摘要依据 | 标签 |
|---|---|---|---|
| CVPR | [Multi-agent Collaborative Perception via Motion-aware Robust Communication Network](https://openaccess.thecvf.com/content/CVPR2024/html/Hong_Multi-agent_Collaborative_Perception_via_Motion-aware_Robust_Communication_Network_CVPR_2024_paper.html) | 初筛漏筛补录。运动感知神经网络融合车辆与基础设施信息，在噪声和带宽约束下提升协同三维目标检测，服务交通感知工程。 | AI 用于工程科学、自动驾驶感知、神经网络 |
| CVPR | [Category-Level Multi-Part Multi-Joint 3D Shape Assembly](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Category-Level_Multi-Part_Multi-Joint_3D_Shape_Assembly_CVPR_2024_paper.html) | 初筛漏筛补录。分层图表示学习同时对齐零件几何和物理接头，直接服务机器人装配与CAD部件设计。 | AI 用于工程科学、机器人装配控制、图神经网络 |
| CVPR | [EvDiG: Event-guided Direct and Global Components Separation](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_EvDiG_Event-guided_Direct_and_Global_Components_Separation_CVPR_2024_paper.html) | 初筛漏筛补录。事件相机记录快速照明变化并用网络去噪恢复颜色，实现直接与全局光分量的视频率分离，改进光学测量能力。 | AI 用于工程科学、图像重建、神经网络 |
| CVPR | [Retrieval-Augmented Embodied Agents](https://openaccess.thecvf.com/content/CVPR2024/html/Zhu_Retrieval-Augmented_Embodied_Agents_CVPR_2024_paper.html) | 初筛漏筛补录。多模态策略检索和生成支持具身机器人操作，在仿真与现实机器人任务验证，直接贡献机器人控制。 | AI 用于工程科学、机器人操作控制、检索增强学习、多模态学习 |
| Nature Human Behaviour | [Images with harder-to-reconstruct visual representations leave stronger memory traces](https://www.nature.com/articles/s41562-024-01870-3) | 初筛漏筛补录。稀疏编码模型压缩图像表征，以重构误差解释记忆准确率和检索反应时，并用模型驱动心理物理实验验证感知记忆机制。 | AI 用于生命科学、神经记忆机制建模、稀疏学习 |
| Nature Human Behaviour | [Principled distillation of UK Biobank phenotype data reveals underlying structure in human variation](https://www.nature.com/articles/s41562-024-01909-5) | 初筛漏筛补录。大规模因子分析从生物库表型学习35个潜在构念，用于澄清遗传信号和疾病健康关联，直接贡献表型结构发现。 | AI 用于生命科学、潜变量建模 |
| Nature Communications | [Computational design of ultra-robust strain sensors for soft robot perception and autonomy](https://www.nature.com/articles/s41467-024-45786-y) | 初筛漏筛补录。机器智能结合软体机器人应变传感器预测运动轨迹和地形高度，直接改善机器人感知与自主能力。 | AI 用于工程科学、机器学习 |
| Nature Communications | [Early detection of emerging viral variants through analysis of community structure of coordinated substitution networks](https://www.nature.com/articles/s41467-024-47304-6) | 初筛漏筛补录。从协同替换网络的稠密社区推断新病毒单倍型并提前检测已知毒株，网络社区发现直接支持病原演化监测。 | AI 用于生命科学、传染病监测、聚类 |
| Nature Communications | [Cross-modality mapping using image varifolds to align tissue-scale atlases to molecular-scale measures with application to 2D brain sections](https://www.nature.com/articles/s41467-024-47883-4) | 初筛漏筛补录。联合估计潜在转录特征分布与形变映射，将分子空间组学对齐脑组织图谱，直接支持生物图谱整合。 | AI 用于生命科学、医学影像配准、空间转录组分析、潜变量建模 |
| Nature Communications | [Deciphering complexity in Pd–catalyzed cross-couplings](https://www.nature.com/articles/s41467-024-47939-5) | 初筛漏筛补录。主成分分析与层次聚类解析高通量钯催化反应的产物分布和溶剂效应，直接支持化学反应机制发现。 | AI 用于物质科学、聚类、无监督学习 |
| Nature Communications | [Recent wetting trend over Taklamakan and Gobi Desert dominated by internal variability](https://www.nature.com/articles/s41467-024-48743-x) | 初筛漏筛补录。结合气候模拟与聚类分析区分天气尺度降水事件，检验沙漠增湿与北大西洋环流的机制联系。 | AI 用于地球宇宙科学、气候建模、聚类 |
| Nature Communications | [Occipital-temporal cortical tuning to semantic and affective features of natural images predicts associated behavioral responses](https://www.nature.com/articles/s41467-024-49073-8) | 初筛漏筛补录。体素建模、主成分分析和行为预测比较揭示视觉皮层对语义情感特征的表征，直接研究神经信息编码与行为关系。 | AI 用于生命科学、视觉神经机制建模、监督学习 |
| Nature Communications | [Simultaneous enhancement of multiple functional properties using evolution-informed protein design](https://www.nature.com/articles/s41467-024-49119-x) | 初筛漏筛补录。从同源蛋白序列学习共变模型EVcouplings，设计多突变酶并实验验证活性和稳定性提升，直接支持蛋白质工程。 | AI 用于生命科学、蛋白质设计、酶设计、蛋白质序列建模、无监督学习 |
| Nature Communications | [A model-free method to learn multiple skills in parallel on modular robots](https://www.nature.com/articles/s41467-024-50131-4) | 初筛漏筛补录。基于中央模式发生器搜索初始状态，在多种真实模块机器人上快速学习运动技能，直接实现机器人控制。 | AI 用于工程科学、机器人运动控制、策略学习 |
| Nature Communications | [A multi-modal, asymmetric, weighted, and signed description of anatomical connectivity](https://www.nature.com/articles/s41467-024-50248-6) | 初筛漏筛补录。多模态回归模型从训练数据学习个体有向带符号脑连接权重，提升连接组建模及脑行为关联分析。 | AI 用于生命科学、神经连接推断、监督学习 |
| Nature Communications | [Symbolic metaprogram search improves learning efficiency and explains rule learning in humans](https://www.nature.com/articles/s41467-024-50966-x) | 初筛漏筛补录。对元程序开展符号搜索，在人类规则学习行为基准上解释学习效率和表现，直接研究人类认知机制。 | AI 用于社会科学、程序合成、搜索与规划 |
| Nature Communications | [Reducing herbivory in mixed planting by genomic prediction of neighbor effects in the field](https://www.nature.com/articles/s41467-024-52374-7) | 初筛漏筛补录。利用基因组预测与Ising启发模型筛选抗食草混种基因型组合，并以田间实验验证减害，直接服务农业设计。 | AI 用于生命科学、作物育种设计、监督学习 |
| Nature Communications | [Sensory experience steers representational drift in mouse visual cortex](https://www.nature.com/articles/s41467-024-53326-x) | 初筛漏筛补录。神经网络模型结合Hebbian学习和突触波动解释小鼠视觉皮层表征漂移，并与成像及视觉剥夺实验对照。 | AI 用于生命科学、神经学习机制建模、神经网络 |
| Nature Communications | [Integrative spatial and genomic analysis of tumor heterogeneity with Tumoroscope](https://www.nature.com/articles/s41467-024-53374-3) | 初筛漏筛补录。Tumoroscope概率模型融合病理、外显子和空间转录数据，学习肿瘤克隆组成及空间位置，直接解析肿瘤异质性。 | AI 用于生命科学、空间转录组分析、多组学整合分析、潜变量建模 |
| Nature Communications | [Warm Arctic-Cold Eurasia pattern helps predict spring wildfire burned area in West Siberia](https://www.nature.com/articles/s41467-024-53470-4) | 初筛漏筛补录。多元线性回归学习冬季气候指标与春季火灾面积关系，并独立预测2019和2020年烧毁面积及排放，支持环境灾害预测。 | AI 用于地球宇宙科学、监督学习 |
| Nature Communications | [Spatial transcriptomics reveals substantial heterogeneity in triple-negative breast cancer with potential clinical implications](https://www.nature.com/articles/s41467-024-54145-w) | 初筛漏筛补录。整合空间转录组和组织学并以分步聚类识别九种乳腺癌空间类型，经外部数据验证并关联预后和治疗。 | AI 用于生命科学、肿瘤分型、空间转录组分析、聚类 |
| Nature Neuroscience | [The logic of recurrent circuits in the primary visual cortex](https://www.nature.com/articles/s41593-023-01510-5) | 初筛漏筛补录。循环兴奋和抑制连接计算模型解释光遗传操控视觉皮层的实验现象，直接研究神经信息处理机制。 | AI 用于生命科学、视觉神经机制建模、循环神经网络 |
| Nature Neuroscience | [Co-dependent excitatory and inhibitory plasticity accounts for quick, stable and long-lasting memories in biological networks](https://www.nature.com/articles/s41593-024-01597-4) | 初筛漏筛补录。兴奋与抑制突触协同可塑性模型解释快速稳定记忆，并在循环神经网络重现运动皮层动力学，直接研究神经学习机制。 | AI 用于生命科学、神经学习机制建模、循环神经网络 |
| Nature Neuroscience | [Maintaining and updating accurate internal representations of continuous variables with a handful of neurons](https://www.nature.com/articles/s41593-024-01766-5) | 初筛漏筛补录。结合果蝇钙成像与可调小型神经网络分析，解释连续头方向表征及噪声敏感性，直接研究神经记忆编码机制。 | AI 用于生命科学、神经记忆机制建模、神经网络 |
| Nature Physics | [Heavy-tailed neuronal connectivity arises from Hebbian self-organization](https://www.nature.com/articles/s41567-023-02332-9) | 初筛漏筛补录。结合Hebbian可塑性的神经网络自组织模型解释连接重尾和聚类，并在多动物连接组验证，直接研究神经网络形成机制。 | AI 用于生命科学、神经学习机制建模、神经连接推断、神经网络 |

## 元数据与标签核验

- 25篇均匹配正式页面的题名、作者和2024年出版信息；24篇核实DOI。EvDiG的Crossref查询失败，官方页未提供DOI，保留空值及失败记录，未反复重试。
- 23篇另取得题名与年份匹配的Crossref信息。其中《Category-Level Multi-Part Multi-Joint 3D Shape Assembly》的Crossref作者列表多出两人，与CVF官方列表冲突；保留CVF作者列表并记录差异，未把Crossref作者核验标成一致。
- 4篇CVPR公开PDF端点通过HTTP HEAD检查；21篇Nature系列PDF发生Cookie验证跳转，标为未核验。没有下载或读取PDF，本轮没有新增代码／项目链接可用性声明。
- 本轮复用38种现有标签，无新增词项，词表保持757项。只保留有摘要依据的维度；对词表中不完全匹配的任务不硬套标签。

## 累计进度与剩余工作

| 指标 | 累计结果 |
|---|---|
| 已审记录 | 14,633 |
| 纳入 | 2,415篇 |
| 排除 | 11,317条（无AI4S实质关系、非研究文种或不属本批范围） |
| 待定 | 901条 |
| 确认漏筛纳入 | 1,264篇（已包含在纳入总数内） |
| 核验补齐完整摘要 | 1,515条 |
| 仍未审 | 15,835条 |

**全量审核尚未完成。** 剩余15,835条中，6,965条缺可用摘要暂缓，8,870条有供给摘要或待核描述可继续审核；其中仍可能存在摘要质量问题。已审待定901条不包含在未审15,835条中。

此前1,574条初筛候选（包含1,383条个人旧记录）均已复核。本轮不扩大官网漏采核验范围，不能把漏筛纳入写成新爬论文。

唯一键、原字段、旧13,633条完整记录、757项词表和计数闭合校验通过：14,633已审＋15,835未审＝30,468。跨审核文件同键重合890条、判定不同46条，本轮新增重合0条；未修改他人文件或负责人登记。

交付：[个人JSON](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101.json)、[累计统计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/summary.json)、[本轮逐条审计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation10-batch-decisions.jsonl)、[抽查记录](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation10-batch-qc.json)。实际上传以GitHub提交记录及本地publication.json为准。
