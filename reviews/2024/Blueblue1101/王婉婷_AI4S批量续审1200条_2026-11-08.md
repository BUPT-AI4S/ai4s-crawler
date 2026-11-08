# 王婉婷｜AI4S论文摘要批量审核工作汇报

2026年11月8日 · 2024年论文 · Blueblue1101 · continuation11

**本轮完成1,200条，比上一轮多200条：纳入21篇、排除1109条、待定70条；补齐并核验完整摘要42条。** 覆盖20个来源，旧14,633条完整记录保持不变。

新增纳入均来自既有采集、未进入关键词初筛候选的记录，属于**漏筛补录**。本轮新爬0篇，未扩展官网漏采核验。缺摘要或抓取异常项按要求暂缓。

## 审核方法

采用仓库main `b8abd30` 的现行skill和757项共享词表。按30—50条一批读取完整供给摘要；被截断部分另行重读。逐条保存结论、理由、摘要哈希和队列位置，根据科学／工程任务、AI作用及二者关系判断，未用关键词规则代替语义判断，未读正文或PDF。

28条拟纳入再次核对，7条因摘要未说清AI方法转待定；保留21篇并打标签。固定随机种子抽查20条初判排除，排除结论均维持；其中2条修正排除理由：不能仅因栏目叫Perspective或Protocol就否定学术价值，这两篇排除的依据是没有AI实质作用。抽查结果不代表全量准确率。

## 本轮结果及原因

| 结果 | 条数 | 原因 |
|---|---|---|
| 纳入 | 21 | 摘要支持AI用于明确科学或工程研究任务 |
| 相关性排除 | 1107 | 没有AI实质参与，或只有通用模型／基准而缺少科学研究任务 |
| 文种排除 | 2 | 视觉交互讨论回复、Reaction评论栏目，不属于本批保留的研究或实质综述 |
| 待定：证据不足 | 69 | 摘要未说明AI算法、贡献或文种，包含7条复查后转待定 |
| 待定：摘要问题 | 1 | 两个不同DOI条目却取得相同题名和摘要，页码不同，疑似更正关联错误；未回填可疑文本 |

两条同题名记录保留各自原始键，不删原数据；其中原研究按无AI排除，疑似关联错误项暂缓。本轮数量是审核记录数，不能当作独立论文去重数。

## 各来源本轮工作量

“补摘要”是元数据补录工作量，已包含在已审记录中，不与纳入篇数相加。

| 来源 | 本轮已审 | 新爬 | 纳入 | 排除 | 待定 | 补齐完整摘要 |
|---|---|---|---|---|---|---|
| Nature Communications | 964 | 0 | 17 | 890 | 57 | 0 |
| Molecular Cell | 58 | 0 | 0 | 56 | 2 | 32 |
| Nature Microbiology | 43 | 0 | 1 | 41 | 1 | 0 |
| Nature Chemical Biology | 27 | 0 | 0 | 26 | 1 | 0 |
| CVPR | 26 | 0 | 2 | 23 | 1 | 0 |
| Nature Neuroscience | 19 | 0 | 1 | 15 | 3 | 0 |
| Nature Human Behaviour | 17 | 0 | 0 | 14 | 3 | 0 |
| Chem | 9 | 0 | 0 | 9 | 0 | 5 |
| Cell Discovery | 8 | 0 | 0 | 8 | 0 | 0 |
| Nature Physics | 7 | 0 | 0 | 7 | 0 | 0 |
| Nature Ecology & Evolution | 5 | 0 | 0 | 5 | 0 | 0 |
| Nano Energy | 3 | 0 | 0 | 2 | 1 | 3 |
| Nature Protocols | 3 | 0 | 0 | 2 | 1 | 0 |
| International Journal of Mining Science and Technology | 2 | 0 | 0 | 2 | 0 | 0 |
| Energy Storage Materials | 2 | 0 | 0 | 2 | 0 | 0 |
| Journal of Energy Chemistry | 2 | 0 | 0 | 2 | 0 | 1 |
| The Lancet Regional Health - Europe | 2 | 0 | 0 | 2 | 0 | 0 |
| Seminars in Cancer Biology | 1 | 0 | 0 | 1 | 0 | 1 |
| Trends in Cognitive Sciences | 1 | 0 | 0 | 1 | 0 | 0 |
| The Lancet Planetary Health | 1 | 0 | 0 | 1 | 0 | 0 |
| **合计** | 1200 | 0 | 21 | 1109 | 70 | 42 |

## 新增漏筛纳入论文与标签

| 来源 | 论文 | 摘要依据 | 标签 |
|---|---|---|---|
| CVPR | [MLIP: Enhancing Medical Visual Representation with Divergence Encoder and Knowledge-guided Contrastive Learning](https://openaccess.thecvf.com/content/CVPR2024/html/Li_MLIP_Enhancing_Medical_Visual_Representation_with_Divergence_Encoder_and_Knowledge-guided_CVPR_2024_paper.html) | 初筛漏筛补录。医学知识引导图文对比预训练，用于医学影像分类、检测和分割。 | AI 用于生命科学、医学影像分类、医学影像分割、预训练、多模态学习、对比学习、知识引导学习 |
| CVPR | [Deep Single Image Camera Calibration by Heatmap Regression to Recover Fisheye Images Under Manhattan World Assumption](https://openaccess.thecvf.com/content/CVPR2024/html/Wakai_Deep_Single_Image_Camera_Calibration_by_Heatmap_Regression_to_Recover_CVPR_2024_paper.html) | 初筛漏筛补录。热图回归学习相机方向并校正鱼眼畸变，在实际商用相机验证，直接改进测量标定能力。 | AI 用于工程科学、深度学习、监督学习 |
| Nature Communications | [Global evaluation of lineage-specific human papillomavirus capsid antigenicity using antibodies elicited by natural infection](https://www.nature.com/articles/s41467-024-45807-w) | 初筛漏筛补录。对中和抗体数据开展抗原聚类，识别HPV谱系特异性抗原分群及血清型，聚类用于病毒免疫研究。 | AI 用于生命科学、聚类 |
| Nature Communications | [Nuclei-specific hypothalamus networks predict a dimensional marker of stress in humans](https://www.nature.com/articles/s41467-024-46275-y) | 初筛漏筛补录。从下丘脑核团功能连接建立可样本外预测压力评分的模型，研究特定脑网络与人类压力的关系。 | AI 用于生命科学、症状严重度预测、监督学习 |
| Nature Communications | [Neuromorphic antennal sensory system](https://www.nature.com/articles/s41467-024-46393-7) | 初筛漏筛补录。人工突触神经形态感知系统完成触觉纹理分类和磁导航，具有实测仿生传感工程任务。 | AI 用于工程科学、神经网络 |
| Nature Communications | [Optimal blade pitch control for enhanced vertical-axis wind turbine performance](https://www.nature.com/articles/s41467-024-46988-0) | 初筛漏筛补录。遗传算法与自动化风机实验闭环搜索叶片变桨策略，提高发电性能并降低结构载荷。 | AI 用于工程科学、风机载荷控制、演化优化 |
| Nature Communications | [Ozone as an environmental driver of influenza](https://www.nature.com/articles/s41467-024-48199-z) | 初筛漏筛补录。采用PC条件独立图模型因果发现并与状态重建及回归交叉验证，识别臭氧对流感活动的影响。 | AI 用于生命科学、传染病监测、因果推断、概率图模型 |
| Nature Communications | [Sustained IFN signaling is associated with delayed development of SARS-CoV-2-specific immunity](https://www.nature.com/articles/s41467-024-48556-y) | 初筛漏筛补录。使用k-means整合纵向血浆数据并验证患者分群，揭示COVID-19免疫响应和预后差异。 | AI 用于生命科学、聚类 |
| Nature Communications | [Memristor-based adaptive neuromorphic perception in unstructured environments](https://www.nature.com/articles/s41467-024-48908-8) | 初筛漏筛补录。忆阻器神经形态在线适应完成机器人触觉抓握和驾驶环境识别，有真实工程验证。 | AI 用于工程科学、机器人抓取、自动驾驶感知、在线学习 |
| Nature Communications | [Heterogeneous associations of multiplexed environmental factors and multidimensional aging metrics](https://www.nature.com/articles/s41467-024-49283-0) | 初筛漏筛补录。自组织映射学习环境暴露亚群，结合衰老指标揭示不同污染组合的健康关联。 | AI 用于生命科学、聚类、无监督学习 |
| Nature Communications | [Data-driven approaches linking wastewater and source estimation hazardous waste for environmental management](https://www.nature.com/articles/s41467-024-49817-6) | 初筛漏筛补录。用因果发现筛选特征和数据平衡算法建立废水到危险废物的预测框架，验证1024家企业环境管理任务。 | AI 用于地球宇宙科学、因果推断、特征选择、机器学习 |
| Nature Communications | [Single cell expression and chromatin accessibility of the Toxoplasma gondii lytic cycle identifies AP2XII-8 as an essential ribosome regulon driver](https://www.nature.com/articles/s41467-024-51011-7) | 初筛漏筛补录。聚类和伪时间轨迹整合单细胞转录及染色质图谱，揭示弓形虫细胞周期调控与核糖体基因调控子。 | AI 用于生命科学、细胞轨迹推断、聚类 |
| Nature Communications | [Differential stability of task variable representations in retrosplenial cortex](https://www.nature.com/articles/s41467-024-51227-7) | 初筛漏筛补录。线性分类器解码纵向神经群体记录，比较情境、结果及运动选择表征稳定性，直接研究记忆编码机制。 | AI 用于生命科学、神经记忆机制建模、监督学习 |
| Nature Communications | [Multiscale mapping of transcriptomic signatures for cardiotoxic drugs](https://www.nature.com/articles/s41467-024-52145-4) | 初筛漏筛补录。奇异值分解提取药物特异转录模式并结合离群分析和基因组预测心脏毒性相关变异，服务药物安全研究。 | AI 用于生命科学、毒性预测、低秩逼近 |
| Nature Communications | [Changes in cortical manifold structure following stroke and its relation to behavioral recovery in the male macaque](https://www.nature.com/articles/s41467-024-53365-4) | 初筛漏筛补录。将皮质功能连接投影到低维流形，比较卒中前后表征变化并联系行为恢复，降维用于脑损伤机制研究。 | AI 用于生命科学、脑结构功能耦合分析、表示学习 |
| Nature Communications | [Genetic basis of right and left ventricular heart shape](https://www.nature.com/articles/s41467-024-53594-7) | 初筛漏筛补录。PCA从心脏影像学习形态潜在维度，结合GWAS发现心脏形态遗传位点及疾病关系。 | AI 用于生命科学、潜变量建模 |
| Nature Communications | [Integrating spoken instructions into flight trajectory prediction to optimize automation in air traffic control](https://www.nature.com/articles/s41467-024-54069-5) | 初筛漏筛补录。多模态学习融合口头管制指令与轨迹，降低真实航迹预测误差并支持航空安全工程。 | AI 用于工程科学、动力系统轨迹预测、多模态学习 |
| Nature Communications | [Soil carbon in the world’s tidal marshes](https://www.nature.com/articles/s41467-024-54572-9) | 初筛漏筛补录。利用3710处训练数据及环境因子预测潮汐沼泽土壤碳，形成30米全球碳储量图与预测误差估计。 | AI 用于地球宇宙科学、土壤有机碳预测、监督学习 |
| Nature Communications | [Systematic, computational discovery of multicomponent and one-pot reactions](https://www.nature.com/articles/s41467-024-54611-5) | 初筛漏筛补录。将反应机理知识和物理有机规则编码为自主推理系统，设计新多组分反应并实验验证，AI用于化学反应发现。 | AI 用于物质科学、反应结果预测、反应产率预测、知识引导学习、搜索与规划 |
| Nature Neuroscience | [The cell-type underpinnings of the human functional cortical connectome](https://www.nature.com/articles/s41593-024-01812-2) | 初筛漏筛补录。训练分类器从细胞类型分布预测皮质功能网络归属，解释人脑细胞组成与功能连接的关系。 | AI 用于生命科学、脑结构功能耦合分析、监督学习 |
| Nature Microbiology | [Prediction of strain level phage–host interactions across the Escherichia genus using only genomic information](https://www.nature.com/articles/s41564-024-01832-5) | 初筛漏筛补录。训练基因组预测算法推断噬菌体宿主相互作用，并在病原菌上验证个体化噬菌体组合。 | AI 用于生命科学、监督学习 |

## 元数据和标签核验

- 21篇核对正式页面引用元数据；18篇取得题名、年份匹配的Crossref书目；21篇核实DOI。作者冲突、缺失或访问失败按审计文件原样保留，不将未核实项写成已核实。
- 2个公开PDF端点通过HTTP HEAD，其余无可验证端点或出现验证跳转，留空或标为未核验。没有下载或读取PDF。代码／项目链接保持已有数据，本轮未声明新增可用性核验。
- 复用38种现有标签，无新增词项；共享词表仍为757项。未明确支持的方法或训练阶段不打标签。

## 累计进度

| 指标 | 累计 |
|---|---|
| 已审 | 15,833条 |
| 纳入 | 2,436篇 |
| 排除 | 12,426条（无AI4S实质关系、非研究文种或不属本批范围） |
| 待定 | 971条 |
| 漏筛纳入 | 1,285篇（已含在纳入总数内） |
| 核验补齐完整摘要 | 1,557条 |
| 尚未审核 | 14,635条 |

**仍有7,670条供给摘要／待核描述可继续审核，另6,965条缺可用摘要暂缓。** 二者合计14,635条未审。已审待定971条另列，不包含在未审数量中。全量审核与官网补漏尚未完成。

唯一键、原字段、旧14,633条完整记录、标签规范和数量闭合校验通过：15,833已审＋14,635未审＝30,468。跨审核同键重合890条、判定不同46条，本轮新增重合0条；未修改他人文件或负责人登记。

交付：[个人JSON](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101.json)、[累计统计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/summary.json)、[逐条审计](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation11-batch-decisions.jsonl)、[抽查记录](https://github.com/BUPT-AI4S/ai4s-crawler/blob/main/reviews/2024/Blueblue1101/2026-11-07/continuation11-batch-qc.json)。实际上传以GitHub提交和本地publication.json为准。
