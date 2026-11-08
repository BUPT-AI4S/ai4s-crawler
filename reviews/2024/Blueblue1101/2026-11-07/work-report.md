# 王婉婷｜AI4S批量续审工作汇报

2026年11月8日 · 2024年论文 · Blueblue1101 · continuation7

**本轮接续审核400条：纳入5篇、排除364条、待定31条，补齐并核验完整摘要91条。** 此前已上传的11,533条完整记录保持一致。本轮覆盖21个刊会来源，新增确认的5篇均来自已采集但未进入初筛候选的记录；新爬论文为0篇。

## 方法与结果

按每批40条读取已有完整摘要，逐条保存判断和理由。检查科学／工程任务、AI实际作用及两者关系；仅保留原创研究、正式会议研究论文和有实质学术内容的综述。关键词没有用于代替语义判定，正文和PDF均未用于审核。

| 结果 | 条数 | 原因 |
|---|---|---|
| 纳入 | 5 | 摘要明确支持AI对具体科学或工程任务的贡献，复核元数据及标签 |
| 相关性排除 | 359 | 无AI实质参与，或仅通用视觉、生成、常规计算等，缺少具体科学工程贡献 |
| 文种排除 | 5 | 明确的Comment、Viewpoint、Opinion及读者评论 |
| 待定：摘要问题 | 12 | 致谢、背景片段等不构成完整摘要，先放置 |
| 待定：关系或类型证据不足 | 19 | 摘要尚未说清AI作用，或正式文种与记录匹配仍有疑点 |

本轮383条按摘要语义处理、5条按明确文种处理、12条仅完成摘要问题核查，不能将400条全称为完整摘要精筛。按固定随机种子抽查20条排除记录：纳入／排除结论未变，但6条改为按相关性排除，避免仅凭Perspective等名称排除实质综述。另复核5篇纳入及通用姿态估计边界项；抽查不代表全量准确率保证。

## 各刊会本轮工作量

补摘要是元数据工作量，与纳入数不相加；下表均为既有采集数据的续审。

| 来源 | 本轮已审 | 纳入 | 排除 | 待定 | 补齐完整摘要 |
|---|---|---|---|---|---|
| Nature Communications | 200 | 1 | 191 | 8 | 0 |
| Trends in Microbiology | 44 | 0 | 40 | 4 | 43 |
| CVPR | 42 | 4 | 37 | 1 | 0 |
| Trends in Cognitive Sciences | 27 | 0 | 22 | 5 | 27 |
| Nature Physics | 18 | 0 | 18 | 0 | 0 |
| Clinical Gastroenterology and Hepatology | 10 | 0 | 5 | 5 | 3 |
| Chem | 8 | 0 | 8 | 0 | 5 |
| Molecular Cell | 7 | 0 | 6 | 1 | 6 |
| Nature Ecology & Evolution | 6 | 0 | 6 | 0 | 0 |
| Nature Microbiology | 6 | 0 | 6 | 0 | 0 |
| Nature Chemical Biology | 5 | 0 | 5 | 0 | 0 |
| The Lancet Regional Health - Europe | 4 | 0 | 3 | 1 | 0 |
| The Lancet Planetary Health | 4 | 0 | 2 | 2 | 0 |
| Cell Discovery | 4 | 0 | 1 | 3 | 0 |
| Energy Storage Materials | 3 | 0 | 3 | 0 | 2 |
| Nano Energy | 3 | 0 | 2 | 1 | 2 |
| Seminars in Cancer Biology | 2 | 0 | 2 | 0 | 2 |
| Nature Human Behaviour | 2 | 0 | 2 | 0 | 0 |
| Nature Neuroscience | 2 | 0 | 2 | 0 | 0 |
| Nature Geoscience | 2 | 0 | 2 | 0 | 0 |
| Information Fusion | 1 | 0 | 1 | 0 | 1 |
| **合计** | 400 | 5 | 364 | 31 | 91 |

## 新确认纳入的5篇论文与标签

| 来源 | 论文 | 摘要依据 | 标签 |
|---|---|---|---|
| CVPR | [PIE-NeRF: Physics-based Interactive Elastodynamics with NeRF](https://openaccess.thecvf.com/content/CVPR2024/html/Feng_PIE-NeRF_Physics-based_Interactive_Elastodynamics_with_NeRF_CVPR_2024_paper.html) | 初筛漏筛补录。将神经辐射场与非线性超弹性无网格模拟耦合，利用学习密度表示设置离散核，支持真实物体弹性动力学模拟。 | AI 用于数理科学、物理过程动态建模、神经辐射场、物理与数据融合建模 |
| CVPR | [HouseCat6D - A Large-Scale Multi-Modal Category Level 6D Object Perception Dataset with Household Objects in Realistic Scenarios](https://openaccess.thecvf.com/content/CVPR2024/html/Jung_HouseCat6D_-_A_Large-Scale_Multi-Modal_Category_Level_6D_Object_Perception_CVPR_2024_paper.html) | 初筛漏筛补录：多模态物体位姿数据集提供高精度标注及密集机器人平行夹爪抓取标注，并评估位姿网络，直接支持机器人感知与抓取研究。 | AI 用于工程科学、机器人抓取、科学数据 |
| CVPR | [Text-Guided Variational Image Generation for Industrial Anomaly Detection and Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Lee_Text-Guided_Variational_Image_Generation_for_Industrial_Anomaly_Detection_and_Segmentation_CVPR_2024_paper.html) | 初筛漏筛补录。文本引导生成无缺陷图像，缓解制造业缺陷检测训练样本不足，直接改善工业异常检测与分割。 | AI 用于工程科学、工业缺陷检测、生成建模 |
| CVPR | [CLIP-BEVFormer: Enhancing Multi-View Image-Based BEV Detector with Ground Truth Flow](https://openaccess.thecvf.com/content/CVPR2024/html/Pan_CLIP-BEVFormer_Enhancing_Multi-View_Image-Based_BEV_Detector_with_Ground_Truth_Flow_CVPR_2024_paper.html) | 初筛漏筛补录：对比学习以真值信息监督自动驾驶多视图BEV表征，直接改进驾驶场景三维目标检测。 | AI 用于工程科学、自动驾驶感知、对比学习 |
| Nature Communications | [Bio-inspired multimodal learning with organic neuromorphic electronics for behavioral conditioning in robotics](https://www.nature.com/articles/s41467-024-48881-2) | 初筛漏筛补录：有机神经形态电路在线融合多模态感觉，通过关联学习使机器人识别并回避危险物体，具有实体机器人行为验证。 | AI 用于工程科学、机器人操作控制、多模态学习 |

## 元数据与词表核对

- 5篇均按官方页面的题名、作者顺序和2024年出版日期核对；4篇CVPR匹配Crossref并补DOI，Nature Communications论文DOI由出版社引用元数据确认。
- 4个CVF PDF端点通过HTTP HEAD核验，未下载正文；Nature PDF仍有Cookie错误跳转，已标未核验，不将HTTP 200视为有效公开PDF。
- HouseCat6D的Crossref作者顺序与CVF不同，保留CVF正式论文集顺序，并记录差异。
- PIE-NeRF摘要给出的项目页已检查可访问；其他未查到的代码、项目及数据链接不猜填。
- 使用main `6de707f` 的757项共享词表；5篇共使用13种已有规范标签，本轮无新增词项，词表完整保留。包括工业缺陷检测、生成建模、物理过程动态建模、神经辐射场、物理与数据融合建模、自动驾驶感知、对比学习、机器人操作控制、多模态学习、机器人抓取、科学数据及两个领域标签。
- 两条同题名的微生物组疾病预测综述均因AI方法证据不足保留待定，记录重复线索，未计为两篇新增纳入。

## 累计进度与剩余工作

| 指标 | 累计结果 |
|---|---|
| 已审记录 | 11,933 |
| 纳入 | 2,365篇 |
| 排除 | 8,834条（无AI4S实质关系、非研究文种或不属本批范围） |
| 待定 | 734条 |
| 确认漏筛纳入 | 1,214篇（已包含在纳入总数内） |
| 核验补齐完整摘要 | 1,384条 |
| 仍未审 | 18,535条 |

**全量审核尚未完成。** 余下18,535条中，6,965条缺可用摘要先暂缓，11,570条有供给摘要或待核描述保留续审。队列包含摘要质量问题，不能将11,570条都视为合格完整摘要。本批按摘要长度安排阅读顺序，其纳入比例不能外推到剩余记录。官网漏采核验沿用历史审计，本轮没有扩大已核验范围。

此前1,574条初筛候选及其中1,383条个人旧记录均已复核。本轮唯一键、原字段、旧11,533条完整记录、共享757项词表及总量闭合校验通过：11,933已审＋18,535未审＝30,468。历史跨审核人同键重合890条、判定不同46条，本轮新增重合0；未修改他人文件或负责人登记。

交付：[个人JSON](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101.json)、[累计统计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/summary.json)、[本轮逐条审计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation7-batch-decisions.jsonl)、[抽查记录](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation7-batch-qc.json)。本轮成果随本次提交，实际上传以GitHub提交记录和本地publication.json为准。
