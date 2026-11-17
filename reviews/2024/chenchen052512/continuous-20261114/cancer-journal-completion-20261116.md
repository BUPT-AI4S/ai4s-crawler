# Cancer Letters 2024整刊初筛与候选核查

第580—607卷637条，正式卷期文章号集合与快照完全对应。

本轮新增611条：纳入8、排除546、待定57；另将旧217122由排除改待定并保留previous_review。累计637条：纳入17、排除562、待定58、未审0。

## 实际阅读范围

逐条初筛题名、正式文种及原摘要首尾片段和方法线索句；81篇另读完整原摘要（本轮新记录80篇，旧217122一篇）。14个论文页补查中11个读取正文或公开章节，1个仅见元数据，2个出现CPE00002。另查PMC作者手稿及分类器原始论文。不是637条全摘要精读或全文通读。

90条正式非研究条目排除；Short communication属于研究正文，与Correspondence区分。217322的正式目录未提供摘要，题名为临床试验预期寿命入组标准，作非候选初筛，不声称读过摘要。

初筛年候选3条，缺输入摘要0；来源候选3条，缺0。仅输入候选口径，已补证摘要另记，原字段不回写。

## 本轮补录纳入8篇

|文章号|论文|证据与科学作用|
|---|---|---|
|216711|[Clinicopathological and molecular landscape of 5-year IDH-wild-type glioblastoma survivors: A multicentric retrospective study](https://www.sciencedirect.com/science/article/pii/S0304383524001046)|原摘要明确用brain tumor classifier v12.5精化胶质瘤甲基化分型；结合Capper等分类器基础原始论文确认其为已训练监督分类器。这里为使用现有模型推断，不标训练阶段。|
|216881|[Exhaled volatolomics profiling facilitates personalized screening for gastric cancer](https://www.sciencedirect.com/science/article/pii/S030438352400274X)|完整原摘要明确呼气挥发组结合集成学习检测胃癌，在发现与重复队列验证，另以单细胞和富集分析解释代谢来源。|
|216909|[RAC1high NK cell-based immunotherapy in hepatocellular carcinoma via STAT3-NKG2D axis](https://www.sciencedirect.com/science/article/pii/S0304383524003021)|完整原摘要明确多组学整合机器学习构建NKS肝癌预后签名并识别RAC1干预靶点，科学作用和AI关系直接。|
|216977|[Improving ultrasound diagnostic Precision for breast cancer and adenosis with modality-specific enhancement (MSE) - Breast Net](https://www.sciencedirect.com/science/article/pii/S0304383524003719)|完整原摘要明确训练并外部验证多模态超声MSE-Breast Net，区分乳腺腺病与乳癌，并与BI-RADS及单/双模态模型比较。|
|217216|[Evaluation and integration of cell-free DNA signatures for detection of lung cancer](https://www.sciencedirect.com/science/article/pii/S0304383524006116)|完整原摘要明确集成堆叠模型ESim-seq整合cfDNA特征早筛肺癌，并以独立验证队列评价；另有肺癌亚型多分类模型。|
|217245|[A rigorous multi-laboratory study of known PDAC biomarkers identifies increased sensitivity and specificity over CA19-9 alone](https://www.sciencedirect.com/science/article/pii/S0304383524006402)|原文2.4节明确以LASSO、随机森林和逻辑OR比较选择PDAC标志物组合，并用交叉验证及独立盲法队列验证；并非只做人工阈值组合。|
|217265|[Integration of transcriptomics, proteomics and loss-of-function screening reveals WEE1 as a target for combination with dasatinib against proneural glioblastoma](https://www.sciencedirect.com/science/article/pii/S0304383524006608)|原文2.4及3.6节明确用k-means无监督聚类TCGA胶质瘤队列，识别与细胞周期和治疗敏感性相关的亚型分群；SamNet网络流本身不单独当作AI。|
|217321|[Single-cell RNA-sequencing of human spleens reveals an IDO-1+ tolerogenic dendritic cell subset in pancreatic cancer patients that is absent in normal individuals](https://www.sciencedirect.com/science/article/pii/S030438352400716X)|出版社原摘要及PMC作者手稿Single-cell RNA-sequencing方法确认Seurat整合、Azimuth参考映射后重新聚类mDC为3个亚群，识别IDO1+耐受性树突状细胞。|

## 待定58篇

多数为单细胞或空间组学分析，须明确实际聚类、表征或预测算法；测序技术、细胞群或预后签名本身不足以证明实质AI。旧217122新增Highlights线索提及AI深度学习，但尚需正文案例排除泛论可能。

|文章号|论文|待补证内容|
|---|---|---|
|216483|Bcl-xL mediates interferon-beta secretion by protease-activated receptor 2 deficiency through the mitochondrial permeability transition pore in colorectal cancer metastasis|单细胞分析验证PAR2调节CRC转移免疫环境，需查是重建细胞分群还是复用注释。|
|216495|IRGM is a novel regulator of PD-L1 via promoting S6K1-mediated phosphorylation of YBX1 in hepatocellular carcinoma|单细胞分析IRGM抑制后的HCC免疫细胞，需查具体数据分析算法。|
|216485|The spatial and single-cell analysis reveals remodeled immune microenvironment induced by synthetic oncolytic adenovirus treatment|空间及单细胞展示SynOV重塑肝癌微环境，需查聚类和表征方法。|
|216497|Targeting TAM-secreted S100A9 effectively enhances the tumor-suppressive effect of metformin in treating lung adenocarcinoma|单细胞解析二甲双胍TAM-S100A9作用，需查分群算法。|
|216499|Immuno-genomic analysis reveals eosinophilic feature and favorable prognosis of female non-smoking esophageal squamous cell carcinomas|单细胞与突变签名分析ESCC免疫环境，需查学习分解或聚类方法。|
|216513|Spatial multimodal analysis revealed tertiary lymphoid structures as a risk stratification indicator in combined hepatocellular-cholangiocarcinoma|空间转录组及成像质谱评价TLS，需核实是否实质学习分群或人工评分。|
|216586|Single-cell transcriptome profiling of primary tumors and paired organoids of pancreatobiliary cancer|单细胞比较胰胆肿瘤与类器官异质性和轨迹，需查具体聚类和表征算法。|
|216588|Exosomal lncCRLA is predictive for the evolvement and development of lung adenocarcinoma|单细胞及空间转录组识别混合EMT肿瘤起源细胞，需查分群或计算方法。|
|216607|Single-cell RNA sequencing highlights epithelial and microenvironmental heterogeneity in malignant progression of pancreatic ductal adenocarcinoma|单细胞识别IPMN至PDAC恶性进展细胞与互作，需查聚类和轨迹算法。|
|216664|scRNA-seq of colorectal cancer shows regional immune atlas with the function of CD20+ B cells|单细胞比较不同部位CRC免疫图谱并分析B细胞轨迹，需补计算算法。|
|216656|Neoadjuvant chemotherapy-induced remodeling of human hormonal receptor-positive breast cancer revealed by single-cell RNA sequencing|单细胞识别新辅助化疗后乳癌免疫亚群，需核实聚类与分析算法。|
|216642|Inhibition of ATM promotes PD-L1 expression by activating JNK/c-Jun/TNF-α signaling axis in triple-negative breast cancer|单细胞用于ATM/PD-L1关系，需核实是实质细胞分群还是仅表达相关。|
|216675|Single-cell characterization of infiltrating T cells identifies novel targets for gallbladder cancer immunotherapy|单细胞鉴定12类T细胞及3类胆囊癌，需查分群算法。|
|216708|Up-regulation of RAN by MYBL2 maintains osteosarcoma cancer stem-like cells population during heterogeneous tumor generation|单细胞重建骨肉瘤干细胞分化图谱，需查聚类及轨迹算法。|
|216723|Single-cell transcriptomic analysis reveals the landscape of epithelial-mesenchymal transition molecular heterogeneity in esophageal squamous cell carcinoma|单细胞分析ESCC的EMT异质性并预测药物，需查聚类及药物预测算法。|
|216709|S100A6 drives lymphatic metastasis of liver cancer via activation of the RAGE/NF-kB/VEGF-D pathway|单细胞层面识别S100A6表达差异，需核实计算分群或只是实验细胞测定。|
|216741|Antigen/HLA-agnostic strategies for Characterizing Tumor-responsive T cell receptors in PDAC patients via single-cell sequencing and autologous organoid application|单细胞TCR/RNA与类器官筛肿瘤响应TCR，需核实分析是否实际AI学习。|
|216747|CD63+ cancer-associated fibroblasts confer CDK4/6 inhibitor resistance to breast cancer cells by exosomal miR-20|单细胞发现CD63+ CAF耐药亚群，需核实聚类与表征算法。|
|216778|Association of preoperative aspartate aminotransferase to platelet ratio index with outcomes and tumour microenvironment among colorectal cancer with liver metastases|APRI部分为IPTW/Cox传统统计，但单细胞肿瘤微环境分析的聚类方法仍需核实。|
|216809|Three-dimensional chromatin analysis reveals Sp1 as a mediator to program and reprogram HPV-host epigenetic architecture in cervical cancer|单细胞验证Sp1上皮细胞富集，需查是新分群还是复用标签。|
|216799|Characterization of the distinct immune microenvironments between hepatocellular carcinoma and intrahepatic cholangiocarcinoma|单细胞整合两类肝癌免疫环境并识别EGR1+巨噬细胞簇，需核实分群算法。|
|216813|An effective two-stage NMBzA-induced rat esophageal tumor model revealing that the FAT-Hippo-YAP1 axis drives the progression of ESCC|大鼠ESCC模型多组学及单细胞比较类器官，需核实细胞分析是否实质AI。|
|216814|Candida albicans-myeloid cells-T lymphocytes axis in the tumor microenvironment of oral tumor-bearing mice|单细胞比较白色念珠菌感染口腔肿瘤的免疫细胞，需核实分群算法。|
|216822|Microenvironmental changes in familial adenomatous polyposis during colorectal cancer carcinogenesis|单细胞解析FAP癌变过程微环境，需查实际分群算法。|
|216834|OH2 oncolytic virus: A novel approach to glioblastoma intervention through direct targeting of tumor cells and augmentation of anti-tumor immune responses|单细胞分析OH2溶瘤病毒对胶质瘤微环境影响，需查分群是否实质AI学习。|
|216835|Identification of a DNA-methylome-based signature for prognosis prediction in driver gene-negative lung adenocarcinoma|四CpG甲基化TLA预后签名经内外验证，需查是否实质学习模型或传统Cox积分。|
|216905|Axl as a potential therapeutic target for adamantinomatous craniopharyngiomas: Based on single nucleus RNA-seq and spatial transcriptome profiling|单核RNA与空间转录组定位颅咽管瘤细胞与成纤维亚群，需查具体计算方法。|
|216911|FTO elicits tumor neovascularization in cancer-associated fibroblasts through eliminating m6A modifications of multiple pro-angiogenic factors|单细胞定位FTO在CAF亚群，需查是重新聚类还是仅复用细胞注释。|
|216922|Smoking-induced CCNA2 expression promotes lung adenocarcinoma tumorigenesis by boosting AT2/AT2-like cell differentiation|单细胞追踪AT2样细胞分化和CCNA2作用，需查聚类与轨迹方法。|
|216928|Single-cell transcriptomics reveals the aggressive landscape of high-grade serous carcinoma and therapeutic targets in tumor microenvironment|单细胞识别HGSC肿瘤细胞与CAF/巨噬细胞亚群，需核实聚类方法。|
|216951|The single cell immunogenomic landscape after neoadjuvant immunotherapy combined chemotherapy in esophageal squamous cell carcinoma|单细胞RNA与T/BCR解析食管癌免疫细胞及克隆动态，需查实际分析方法。|
|216963|Preoperative neoadjuvant targeted therapy remodels intra-tumoral heterogeneity of clear-cell renal cell carcinoma and ferroptosis inhibition induces resistance progression|单细胞研究肾癌新辅助治疗异质性及耐药，需查分群及表征算法。|
|216984|Prognostic implication of methylation-based circulating tumor DNA detection prior to surgery in stage I non-small cell lung cancer|甲基化MCED试验预测风险，需核实检测调用的分类器是否机器学习及其科学作用。|
|216991|Harnessing genetic interactions for prediction of immune checkpoint inhibitors response signature in cancer cells|GENIUS利用遗传互作推断免疫治疗响应签名，需核实为实质学习推理还是关联筛选。|
|216985|Colorectal cancer-associated fibroblasts inhibit effector T cells via NECTIN2 signaling|单细胞识别11类成纤维细胞及TinCAF，需核实是否无监督聚类及其算法。|
|217018|Single-cell transcriptomic analysis of the immune microenvironment in pediatric acute leukemia|单细胞解析儿童白血病免疫微环境、T细胞亚群及通讯，需核实聚类与网络算法。|
|216995|Deciphering the TCF19/miR-199a-5p/SP1/LOXL2 pathway: Implications for breast cancer metastasis and epithelial-mesenchymal transition|新EMT评分和计算策略筛TCF19，需查评分、诊断及预后模型的算法。|
|217057|Development and evaluation of a risk prediction tool for risk-adapted screening of colorectal cancer in China|9问卷变量风险评分经大队列及独立筛查验证，需查是否Cox积分或实质机器学习。|
|217062|Unveiling major histocompatibility complex-mediated pan-cancer immune features by integrated single-cell and bulk RNA sequencing|泛癌scRNA、空间组学与MHC.sig分析，需查分群与免疫响应预测算法。|
|217005|Acetylation-dependent deubiquitinase USP26 stabilizes BAG3 to promote breast cancer progression|结构虚拟筛选USP26抑制剂，需查是否普通对接或实际AI评分。|
|217077|Pan-cancer atlas of tumor-resident microbiome, immunity and prognosis|泛癌微生物免疫分型和预后组合的具体算法未明，需查是否机器学习。|
|217117|Histone lactylation dynamics: Unlocking the triad of metabolism, epigenetics, and immune regulation in metastatic cascade of pancreatic cancer|单细胞/多组学乳酸化评分用于分层和预后，需查模型构建及聚类算法。|
|217122|Establishment of advanced tumor organoids with emerging innovative technologies|本轮原摘要及出版方Highlights明确提及AI深度学习改进类器官构建；原排除判定需谨慎复核。方法案例正文未获，暂由排除改待定，需确认是否实质综述而非前景泛论。|
|217133|Irradiated tumor cell-released microparticles enhance the therapeutic efficacy of PD-1 inhibitors by promoting M1-TAMs polarization in NSCLC brain metastases|单细胞验证微粒对巨噬细胞和免疫治疗的影响，需查实际聚类等计算方法。|
|217162|Enhanced cytokine signaling and ferroptosis defense interplay initiates obesity-associated pancreatic ductal adenocarcinoma|单细胞联系肥胖、免疫和铁死亡机制，但具体学习方法仍需核实。|
|217193|Single-cell RNA-seq reveals heterogeneity in metastatic renal cell carcinoma and effect of anti-angiogenesis therapy in the pancreas metastatic lesion|单细胞解码肾癌胰腺转移微环境，需查分群和表征算法。|
|217181|Spatial transcriptomic revealed intratumor heterogeneity and cancer stem cell enrichment in colorectal cancer metastasis|空间转录组、拟时序和细胞通讯揭示转移癌干性，需补聚类和轨迹推断的具体算法。|
|217179|Enhanced desmosome assembly driven by acquired high-level desmoglein-2 promotes phenotypic plasticity and endocrine resistance in ER+ breast cancer|单细胞分析揭示乳腺癌耐药和细胞可塑性，需查是否实质无监督分群或仅复用标签。|
|217180|Single-cell RNA sequencing of OSCC primary tumors and lymph nodes reveals distinct origin and phenotype of fibroblasts|单细胞鉴定成纤维细胞亚群并做拟时序，需查聚类与轨迹推断算法。|
|217177|6-Phosphogluconate dehydrogenase promotes glycolysis and fatty acid synthesis by inhibiting the AMPK pathway in lung adenocarcinoma cells|单细胞识别恶性上皮亚群及PGD表达，需查数据分析算法。|
|217199|Identification of SPP1+ macrophages in promoting cancer stemness via vitronectin and CCL15 signals crosstalk in liver cancer|单细胞鉴定SPP1+巨噬细胞及肿瘤干性机制，需查分群算法及是否实质无监督学习。|
|217243|Hepatic stellate cells promote hepatocellular carcinoma development by regulating histone lactylation: Novel insights from single-cell RNA sequencing and spatial transcriptomics analyses|单细胞和空间转录组分析肝星状细胞互作及拟时序，需补具体分析算法。|
|217267|Localized ablative immunotherapy enhances antitumor immunity by modulating the transcriptome of tumor-infiltrating Gamma delta T cells|单细胞识别6类γδT细胞并评价消融免疫治疗效应，需查细胞聚类与注释方法。|
|217262|Integrated proteomic and glycoproteomic analysis reveals heterogeneity and molecular signatures of brain metastases from lung adenocarcinomas|蛋白/糖蛋白组识别两种脑转移亚型，需核实亚型发现是否无监督学习。|
|217280|Targeted inhibition of CHKα and mTOR in models of pancreatic ductal adenocarcinoma: A novel regimen for metastasis|单细胞与代谢组揭示转移细胞和CHKα机制，需核实细胞分群及是否实际使用AI。|
|217276|Significance of longitudinal Epstein–Barr virus DNA combined with multipoint tumor response for dynamic risk stratification and treatment adaptation in nasopharyngeal carcinoma|纵向EBV-DNA和影像组合为响应分群，需核实算法是手工规则分组还是无监督学习。|
|217286|Evaluation of glucocorticoid-related genes reveals GPD1 as a therapeutic target and regulator of sphingosine 1-phosphate metabolism in CRPC|多队列验证Glu-sig预后签名，但具体模型及是否机器学习未列，需查模型构建。|
|217305|CD94 deficiency or blockade unleashes the anti-tumor immunity in mice and humanized murine models|scRNA-seq揭示CD94缺失后的微环境变化，需查聚类分析是否实质无监督学习。|

## 核验限制

后续出版方页面出现CPE00002；部分PMC页面出现验证页，未绕过访问限制。217321使用公开作者手稿确认计算方法；216711用2024原摘要确认实际调用分类器，用分类器基础原始论文确认监督学习性质，未假定v12.5全部实现。作者、公开PDF和代码未全面独立核验。

GitHub命令行DNS失败，已通过正常浏览器核对main规则、词表及个人行动清单；本地结果尚未推送。
