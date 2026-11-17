# Pharmacological Research 2024整刊筛选完成

2024年第199—210卷共510条，正式目录逐卷文章号集合与锁定快照完全一致。

本轮新增175条：纳入3、排除171、待定1。另复核原21待定：6纳入、12排除、3仍待定。整刊累计纳入15、排除491、待定4、未审0。已逐记录覆盖，4篇仍待补证。

本轮104篇研究/综述原摘要逐篇核查（新增84、旧待定20），92条按正式非研究文种排除；16篇另查方法正文。没有把常规对接、分子动力学或统计检索直接判为AI，也不声称全部全文已读。原字段不改，21条旧待定保留previous_review。

末段补查论文页出现CPE00002，107444、107525及107538未能获取可读方法；107092已查ADMET Predictor v11.0，但具体学习模型仍不明。作者、公开PDF、代码未全面独立核验。GitHub命令行DNS失败，已通过浏览器核对main规则、词表及个人行动清单；结果尚未推送。

初筛年候选6条，缺输入原摘要0条；来源候选6条，缺0条。仅候选口径，不拿全量书目缺失充当候选指标。

## 本轮纳入9篇

| 文章号 | 前状态 | 论文 | AI作用 |
|---|---|---|---|
| 107274 | 未审 | [Acute limbic system connectivity predicts chronic cognitive function in mild traumatic brain injury: An individualized differential structural covariance network study](https://www.sciencedirect.com/science/article/pii/S1043661824002196) | 原文第2.3节明确CPM由脑连接矩阵训练认知预测模型，以留一交叉验证产生个体预测，支撑轻度脑损伤认知预后研究。 |
| 107315 | 未审 | [Predictive biomarkers for response to TGF- β inhibition in resensitizing chemo(radiated) esophageal adenocarcinoma](https://www.sciencedirect.com/science/article/pii/S1043661824002603) | 原文2.9及3.1节明确用pHeatmap无监督层次聚类，根据化疗后TGF-β抑制响应将8种食管腺癌细胞系分为响应和不响应组，并分析其差异生物学机制。 |
| 107535 | 未审 | [Integrative radiomics analyses identify universal signature for predicting prognosis and therapeutic vulnerabilities across primary and secondary liver cancers: A multi-cohort study](https://www.sciencedirect.com/science/article/pii/S1043661824004808) | 对多队列肝癌CT影像组学作无监督聚类，构建跨癌种预后及治疗响应特征，并验证生存和生物学关联。 |
| 107038 | 待定 | [Disease2Vec: Encoding Alzheimer’s progression via disease embedding tree](https://www.sciencedirect.com/science/article/pii/S1043661823003948) | Disease2Vec学习疾病嵌入并构建连续疾病树轨迹，预测阿尔茨海默病个体临床阶段；出版方正式原摘要明确方法及科学任务。 |
| 107070 | 待定 | [MMP14high macrophages orchestrate progressive pulmonary fibrosis in SR-Ag-induced hypersensitivity pneumonitis](https://www.sciencedirect.com/science/article/pii/S1043661824000148) | 决策树模型对巨噬细胞上调基因评分筛出MMP14，结合单细胞与细胞动物实验验证肺纤维化机制；原摘要明确AI科学作用。 |
| 107056 | 待定 | [Low-dose Olaparib improves septic cardiac function by reducing ferroptosis via accelerated mitophagy flux](https://www.sciencedirect.com/science/article/pii/S1043661823004127) | 原文第2.9和3.2节明确随机森林筛选败血症铁死亡特征基因并构建诊断模型，进而支持药物筛选和动物机制验证。 |
| 107082 | 待定 | [Identification of Fasudil as a collaborator to promote the anti-tumor effect of lenvatinib in hepatocellular carcinoma by inhibiting GLI2-mediated hedgehog signaling pathway](https://www.sciencedirect.com/science/article/pii/S1043661824000264) | 原文第2.2和2.4节明确借助弹性网药敏模型，并以K-means共识聚类识别肝癌耐药亚型和药物重定位，继以实验验证。 |
| 107390 | 待定 | [Improving glioma drug delivery: A multifaceted approach for glioma drug development](https://www.sciencedirect.com/science/article/pii/S1043661824003359) | 原文第5节系统讨论SVM、随机森林、ANN和深度学习预测血脑屏障通透性，举例DeepBBBP的Mol2vec与MLP/CNN，服务胶质瘤递药科学任务。 |
| 107445 | 待定 | [Baseline gut microbiome as a predictive biomarker of response to probiotic adjuvant treatment in gout management](https://www.sciencedirect.com/science/article/pii/S1043661824003906) | 原文第4.7节明确随机森林疗效分类器，以10折交叉验证筛选12个菌群SGB特征预测痛风益生菌治疗反应，解决此前算法待定。 |

## 待补证4篇

| 文章号 | 论文 | 具体缺口 |
|---|---|---|
| 107092 | New Ref-1/APE1 targeted inhibitors demonstrating improved potency for clinical applications in multiple cancer types | 原文3.1节明确ADMET Predictor v11.0评估药物性质，但未说明所调用的具体学习模型；补充表1及工具模型依据仍需核实。 |
| 107444 | Identification of the TRPA1 cannabinoid-binding site | 已补齐原摘要，明确TRPA1结合位点和分子建模，但结构工具及是否使用AI仍需原文核实。 本轮已读正式目录原摘要，补查论文页未返回可读方法正文；末段访问出现CPE00002，不能据此解决方法疑点。 |
| 107525 | Antagonising Yin Yang 1 ameliorates the symptoms of lupus nephritis via modulating T lymphocyte signaling | 原摘要多组学发现YY1并快速筛选配体，但未列筛选算法，需查是否实质使用AI。 本轮已读正式目录原摘要，补查论文页未返回可读方法正文；末段访问出现CPE00002，不能据此解决方法疑点。 |
| 107538 | Epithelial mitochondrial fission-mediated PANoptosis is crucial for ulcerative colitis and its inhibition by saquinavir through Drp1 | 细胞动物和临床样本证明Drp1机制，in-silico药物筛选算法未说明，需查是否AI。 本轮已读正式目录原摘要，补查论文页未返回可读方法正文；末段访问出现CPE00002，不能据此解决方法疑点。 |

## 全部旧待定复核

| 文章号 | 结论 | 核查依据 |
|---|---|---|
| 106957 | 排除 | 已补齐原摘要：SIRT1自噬调控心肌缺血再灌注的分子机制及药物综述，无AI方法。 |
| 107038 | 纳入 | Disease2Vec学习疾病嵌入并构建连续疾病树轨迹，预测阿尔茨海默病个体临床阶段；出版方正式原摘要明确方法及科学任务。 |
| 107049 | 排除 | 已补齐原摘要：青春期THC暴露、病毒模拟刺激和小鼠脑转录组实验，无AI模型。 |
| 107070 | 纳入 | 决策树模型对巨噬细胞上调基因评分筛出MMP14，结合单细胞与细胞动物实验验证肺纤维化机制；原摘要明确AI科学作用。 |
| 107056 | 纳入 | 原文第2.9和3.2节明确随机森林筛选败血症铁死亡特征基因并构建诊断模型，进而支持药物筛选和动物机制验证。 |
| 107068 | 排除 | 原文确认Discovery Studio受体药效团匹配、AutoDock Vina及GROMACS分子动力学，辅以靶点数据库网络药理，无实质AI学习或知识推理模型。 |
| 107080 | 排除 | 原文第2.2节确认余弦和Jaccard相似度及已知关联加和作检索预测，未建立学习模型或实质知识推理，数据库本身不满足AI4S。 |
| 107082 | 纳入 | 原文第2.2和2.4节明确借助弹性网药敏模型，并以K-means共识聚类识别肝癌耐药亚型和药物重定位，继以实验验证。 |
| 107092 | 待定 | 原文3.1节明确ADMET Predictor v11.0评估药物性质，但未说明所调用的具体学习模型；补充表1及工具模型依据仍需核实。 |
| 107173 | 排除 | 原文2.7节采用SWISS-MODEL模板同源建模和ZDOCK对接，转录组注释为序列相似性检索；未证明实质AI建模。 |
| 107189 | 排除 | 原文2.1节为TargetScan和ENCORI默认参数靶点查询；差异RNA的层次聚类用于表达展示，未建立实质AI预测模型，实验机制研究不满足AI4S。 |
| 107310 | 排除 | 出版方2024正式卷期目录文种为Correspondence，按非研究正文文献类型排除。 |
| 107328 | 排除 | 原文DNMT抑制剂筛选部分明确为Glide HTVS/SP及AutoDock Vina结构对接和体外酶活验证，未见实质AI模型应用。 |
| 107332 | 排除 | 已补齐原摘要：ER应激、UPR与肝脏代谢酶机制综述，无AI方法。 |
| 107363 | 排除 | 原文2.9节采用MOE模板建模与对接，后续微秒分子动力学模拟和突变验证；未采用实质AI学习模型。 |
| 107378 | 排除 | 已补齐原摘要：前瞻PCI登记队列按DAPT时长分组并作风险比统计比较，无AI方法。 |
| 107390 | 纳入 | 原文第5节系统讨论SVM、随机森林、ANN和深度学习预测血脑屏障通透性，举例DeepBBBP的Mol2vec与MLP/CNN，服务胶质瘤递药科学任务。 |
| 107444 | 待定 | 已补齐原摘要，明确TRPA1结合位点和分子建模，但结构工具及是否使用AI仍需原文核实。 本轮已读正式目录原摘要，补查论文页未返回可读方法正文；末段访问出现CPE00002，不能据此解决方法疑点。 |
| 107445 | 纳入 | 原文第4.7节明确随机森林疗效分类器，以10折交叉验证筛选12个菌群SGB特征预测痛风益生菌治疗反应，解决此前算法待定。 |
| 107503 | 排除 | 已补齐原摘要：药物合成、受体结合和细胞小鼠药效实验及SAR，不含AI建模，解决原摘要残缺待定。 |
| 107525 | 待定 | 原摘要多组学发现YY1并快速筛选配体，但未列筛选算法，需查是否实质使用AI。 本轮已读正式目录原摘要，补查论文页未返回可读方法正文；末段访问出现CPE00002，不能据此解决方法疑点。 |
