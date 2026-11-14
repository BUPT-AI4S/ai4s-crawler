# 王婉婷｜2024 年待定论文批量复核与官网总量核验

更新日期：2026-11-14。范围：当前名下49个来源；基于 main `03f22ce`。

已推送GitHub，监控主数据与网站备用快照均已发布并校验。内置浏览器仍显示旧快照的情况单独记录，见[发布核验记录](sync-status.md)。

本轮处理 **1,232 条原待定**：完整复核 **936 条摘要**，其中 **54 条转纳入、26 条转排除、856 条仍待定**；另外 **296 条摘要缺失或质量有问题，按要求暂放**。待定总数由 **1,232 降至 1,152**。本次没有新增爬取论文，54条均为已有记录重新判定。

累计结果：**纳入1,863条、排除19,260条、待定1,152条、未审0条**（当前49个来源，22,275条交付）。当前初筛候选仍为1,149条，需补摘要为0；它与全量交付中的待定队列是不同口径。

## 怎么复核

按来源、年份、论文ID锁定1232条原待定。先检查摘要可用性，再由模型逐条阅读完整可用摘要；批次并行处理后统一复核边界案例和标签。判断依据是“明确科学/工程任务 + AI实质参与”，不用关键词命中代替判断，不读取正文。缺少AI作用、任务关系或文种证据的继续待定。

转纳入论文的正式题名及已有DOI均已核对；CVPR复用/核对官方开放PDF链接。其余出版方提供PDF入口不等于已确认可公开下载，未把受限PDF标为新核实的公开链接；未发现的代码/项目链接不猜填。54条使用现有中英文规范标签，新增词条0。

## 各来源处理量

| 来源 | 原待定 | 完整摘要复核 | 转纳入 | 转排除 | 摘要问题暂放 | 剩余待定 |
|---|---:|---:|---:|---:|---:|---:|
| Advances in Applied Energy | 3 | 3 | 0 | 0 | 0 | 3 |
| Applied Catalysis B Environment and Energy | 4 | 1 | 0 | 0 | 3 | 4 |
| Artificial Intelligence Review | 16 | 16 | 6 | 1 | 0 | 9 |
| Cell Discovery | 34 | 5 | 0 | 0 | 29 | 34 |
| Chem | 7 | 2 | 0 | 0 | 5 | 7 |
| Clinical Gastroenterology and Hepatology | 60 | 3 | 0 | 0 | 57 | 60 |
| Energy Storage Materials | 3 | 2 | 0 | 0 | 1 | 3 |
| eTransportation | 1 | 1 | 0 | 0 | 0 | 1 |
| European Conference on Artificial Intelligence | 46 | 46 | 2 | 13 | 0 | 31 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | 105 | 102 | 21 | 3 | 3 | 81 |
| Information Fusion | 16 | 14 | 5 | 4 | 2 | 7 |
| International Journal of Mining Science and Technology | 0 | 0 | 0 | 0 | 0 | 0 |
| Journal of Advanced Research | 9 | 8 | 0 | 1 | 1 | 8 |
| Journal of Energy Chemistry | 3 | 1 | 0 | 0 | 2 | 3 |
| Journal of Materials Science & Technology | 0 | 0 | 0 | 0 | 0 | 0 |
| Matter | 3 | 3 | 0 | 0 | 0 | 3 |
| Molecular Cell | 9 | 5 | 0 | 0 | 4 | 9 |
| Molecular Neurodegeneration | 5 | 5 | 1 | 0 | 0 | 4 |
| Nano Energy | 4 | 3 | 0 | 0 | 1 | 4 |
| Nature Chemical Biology | 13 | 13 | 0 | 0 | 0 | 13 |
| Nature Communications | 494 | 492 | 14 | 3 | 2 | 477 |
| Nature Computational Science | 11 | 11 | 0 | 0 | 0 | 11 |
| Nature Ecology & Evolution | 10 | 10 | 1 | 0 | 0 | 9 |
| Nature Geoscience | 1 | 1 | 0 | 0 | 0 | 1 |
| Nature Human Behaviour | 17 | 17 | 2 | 0 | 0 | 15 |
| Nature Microbiology | 8 | 8 | 0 | 0 | 0 | 8 |
| Nature Neuroscience | 28 | 28 | 0 | 0 | 0 | 28 |
| Nature Physics | 2 | 2 | 1 | 0 | 0 | 1 |
| Nature Protocols | 8 | 8 | 0 | 0 | 0 | 8 |
| Neuron | 19 | 18 | 0 | 0 | 1 | 19 |
| npj Science of Learning | 9 | 9 | 0 | 1 | 0 | 8 |
| Pharmacological Reviews | 1 | 1 | 0 | 0 | 0 | 1 |
| Renewable and Sustainable Energy Reviews | 26 | 21 | 0 | 0 | 5 | 26 |
| Science Immunology | 28 | 1 | 0 | 0 | 27 | 28 |
| Science Translational Medicine | 19 | 15 | 0 | 0 | 4 | 19 |
| Seminars in Cancer Biology | 0 | 0 | 0 | 0 | 0 | 0 |
| Smart Learning Environments | 8 | 8 | 0 | 0 | 0 | 8 |
| The Lancet Haematology | 4 | 1 | 0 | 0 | 3 | 4 |
| The Lancet Healthy Longevity | 41 | 2 | 0 | 0 | 39 | 41 |
| The Lancet Planetary Health | 37 | 2 | 0 | 0 | 35 | 37 |
| The Lancet Regional Health - Europe | 59 | 5 | 0 | 0 | 54 | 59 |
| Trends in Biotechnology | 3 | 2 | 0 | 0 | 1 | 3 |
| Trends in Cognitive Sciences | 20 | 20 | 0 | 0 | 0 | 20 |
| Trends in Ecology & Evolution | 4 | 3 | 0 | 0 | 1 | 4 |
| Trends in Endocrinology and Metabolism | 0 | 0 | 0 | 0 | 0 | 0 |
| Trends in Food Science & Technology | 25 | 9 | 1 | 0 | 16 | 24 |
| Trends in Microbiology | 5 | 5 | 0 | 0 | 0 | 5 |
| Trends in Molecular Medicine | 2 | 2 | 0 | 0 | 0 | 2 |
| Trends in Neurosciences | 2 | 2 | 0 | 0 | 0 | 2 |
| **合计** | **1,232** | **936** | **54** | **26** | **296** | **1,152** |

## 35个来源官网总数核验

**2个完成同口径核验，1个取得卷期总数但年份口径不一致，32个官网访问返回403。** 未核实的官网总数继续留空，没有用第三方检索数替代。

| 来源 | 已采集 | 官网结果 | 本轮结论 |
|---|---:|---:|---|
| [The Lancet Planetary Health](https://www.thelancet.com/journals/lanplh/home) | 179 | 未核实 | 官网403，暂放 |
| [Trends in Ecology & Evolution](https://www.cell.com/trends/ecology-evolution/home) | 171 | 未核实 | 官网403，暂放 |
| [International Journal of Mining Science and Technology](https://www.sciencedirect.com/journal/international-journal-of-mining-science-and-technology/issues) | 126 | 未核实 | 官网403，暂放 |
| [Chem](https://www.cell.com/chem/home) | 309 | 未核实 | 官网403，暂放 |
| [Matter](https://www.cell.com/matter/home) | 364 | 未核实 | 官网403，暂放 |
| [Applied Catalysis B Environment and Energy](https://www.sciencedirect.com/journal/applied-catalysis-b-environment-and-energy/issues) | 1198 | 未核实 | 官网403，暂放 |
| [Journal of Materials Science & Technology](https://www.sciencedirect.com/journal/journal-of-materials-science-and-technology/issues) | 790 | 未核实 | 官网403，暂放 |
| [eTransportation](https://www.sciencedirect.com/journal/etransportation/issues) | 80 | 未核实 | 官网403，暂放 |
| [Artificial Intelligence Review](https://link.springer.com/journal/10462/volumes-and-issues/57-1) | 414 | 349（2024卷期） | 与2024在线发表口径不同，暂不比较差额 |
| [Information Fusion](https://www.sciencedirect.com/journal/information-fusion/issues) | 522 | 未核实 | 官网403，暂放 |
| [Advances in Applied Energy](https://www.sciencedirect.com/journal/advances-in-applied-energy/issues) | 41 | 未核实 | 官网403，暂放 |
| [Energy Storage Materials](https://www.sciencedirect.com/journal/energy-storage-materials/issues) | 798 | 未核实 | 官网403，暂放 |
| [Journal of Energy Chemistry](https://www.sciencedirect.com/journal/journal-of-energy-chemistry/issues) | 687 | 未核实 | 官网403，暂放 |
| [Nano Energy](https://www.sciencedirect.com/journal/nano-energy/issues) | 1248 | 未核实 | 官网403，暂放 |
| [Renewable and Sustainable Energy Reviews](https://www.sciencedirect.com/journal/renewable-and-sustainable-energy-reviews/issues) | 864 | 未核实 | 官网403，暂放 |
| [Trends in Food Science & Technology](https://www.sciencedirect.com/journal/trends-in-food-science-and-technology/issues) | 462 | 未核实 | 官网403，暂放 |
| [Trends in Cognitive Sciences](https://www.cell.com/trends/cognitive-sciences/home) | 152 | 未核实 | 官网403，暂放 |
| [Smart Learning Environments](https://link.springer.com/journal/40561/volumes-and-issues/11-1) | 64 | 64 | DOI集合完全一致，无漏项 |
| [Science Immunology](https://www.science.org/journal/sciimmunol) | 171 | 未核实 | 官网403，暂放 |
| [Science Translational Medicine](https://www.science.org/journal/stm) | 303 | 未核实 | 官网403，暂放 |
| [Molecular Cell](https://www.cell.com/molecular-cell/home) | 418 | 未核实 | 官网403，暂放 |
| [Neuron](https://www.cell.com/neuron/home) | 346 | 未核实 | 官网403，暂放 |
| [Trends in Biotechnology](https://www.cell.com/trends/biotechnology/home) | 179 | 未核实 | 官网403，暂放 |
| [Trends in Endocrinology and Metabolism](https://www.cell.com/trends/endocrinology-metabolism/home) | 140 | 未核实 | 官网403，暂放 |
| [Trends in Microbiology](https://www.cell.com/trends/microbiology/home) | 179 | 未核实 | 官网403，暂放 |
| [Trends in Molecular Medicine](https://www.cell.com/trends/molecular-medicine/home) | 156 | 未核实 | 官网403，暂放 |
| [Trends in Neurosciences](https://www.cell.com/trends/neurosciences/home) | 128 | 未核实 | 官网403，暂放 |
| [The Lancet Haematology](https://www.thelancet.com/journals/lanhae/home) | 206 | 未核实 | 官网403，暂放 |
| [The Lancet Healthy Longevity](https://www.thelancet.com/journals/lanhl/home) | 145 | 未核实 | 官网403，暂放 |
| [The Lancet Regional Health - Europe](https://www.thelancet.com/journals/lanepe/home) | 333 | 未核实 | 官网403，暂放 |
| [Molecular Neurodegeneration](https://link.springer.com/journal/13024/volumes-and-issues/19-1) | 100 | 100 | DOI集合完全一致，无漏项 |
| [Clinical Gastroenterology and Hepatology](https://www.sciencedirect.com/journal/clinical-gastroenterology-and-hepatology/issues) | 527 | 未核实 | 官网403，暂放 |
| [Journal of Advanced Research](https://www.sciencedirect.com/journal/journal-of-advanced-research/issues) | 218 | 未核实 | 官网403，暂放 |
| [Pharmacological Reviews](https://pharmrev.aspetjournals.org/content/by/year/2024) | 65 | 未核实 | 官网403，暂放 |
| [Seminars in Cancer Biology](https://www.sciencedirect.com/journal/seminars-in-cancer-biology/issues) | 53 | 未核实 | 官网403，暂放 |

**Artificial Intelligence Review 的差异：** 2024年卷57的12期共349条，与采集414条重合348条。官网独有1条在线发表于2023-12-28；采集独有66条，抽查3条均为2024年在线、2025年卷期。因此不能说“漏采65条”或“多采65条”；仍需完成跨年卷期的在线日期核验。证据及完整DOI集合见[目录核验清单](official-count-audit.json)、[成员对照](springer-membership.json)与[跨年日期证据](air-date-evidence.json)。

## 本轮54条转纳入明细与标签

| 来源 | 论文 | 标签 |
|---|---|---|
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Rotation-Agnostic Image Representation Learning for Digital Pathology](https://openaccess.thecvf.com/content/CVPR2024/html/Alfasly_Rotation-Agnostic_Image_Representation_Learning_for_Digital_Pathology_CVPR_2024_paper.html) | AI 用于生命科学、自监督学习、Transformer 架构 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [F3Loc: Fusion and Filtering for Floorplan Localization](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_F3Loc_Fusion_and_Filtering_for_Floorplan_Localization_CVPR_2024_paper.html) | AI 用于工程科学、机器学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Patch2Self2: Self-supervised Denoising on Coresets via Matrix Sketching](https://openaccess.thecvf.com/content/CVPR2024/html/Fadnavis_Patch2Self2_Self-supervised_Denoising_on_Coresets_via_Matrix_Sketching_CVPR_2024_paper.html) | AI 用于生命科学、自监督学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Learning to Produce Semi-dense Correspondences for Visual Localization](https://openaccess.thecvf.com/content/CVPR2024/html/Giang_Learning_to_Produce_Semi-dense_Correspondences_for_Visual_Localization_CVPR_2024_paper.html) | AI 用于工程科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [From Variance to Veracity: Unbundling and Mitigating Gradient Variance in Differentiable Bundle Adjustment Layers](https://openaccess.thecvf.com/content/CVPR2024/html/Gurumurthy_From_Variance_to_Veracity_Unbundling_and_Mitigating_Gradient_Variance_in_CVPR_2024_paper.html) | AI 用于工程科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Adapting Visual-Language Models for Generalizable Anomaly Detection in Medical Images](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_Adapting_Visual-Language_Models_for_Generalizable_Anomaly_Detection_in_Medical_Images_CVPR_2024_paper.html) | AI 用于生命科学、迁移学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [SeaBird: Segmentation in Bird's View with Dice Loss Improves Monocular 3D Detection of Large Objects](https://openaccess.thecvf.com/content/CVPR2024/html/Kumar_SeaBird_Segmentation_in_Birds_View_with_Dice_Loss_Improves_Monocular_CVPR_2024_paper.html) | AI 用于工程科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Action-slot: Visual Action-centric Representations for Multi-label Atomic Activity Recognition in Traffic Scenes](https://openaccess.thecvf.com/content/CVPR2024/html/Kung_Action-slot_Visual_Action-centric_Representations_for_Multi-label_Atomic_Activity_Recognition_in_CVPR_2024_paper.html) | AI 用于工程科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [MemoNav: Working Memory Model for Visual Navigation](https://openaccess.thecvf.com/content/CVPR2024/html/Li_MemoNav_Working_Memory_Model_for_Visual_Navigation_CVPR_2024_paper.html) | AI 用于工程科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Unleashing Unlabeled Data: A Paradigm for Cross-View Geo-Localization](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Unleashing_Unlabeled_Data_A_Paradigm_for_Cross-View_Geo-Localization_CVPR_2024_paper.html) | AI 用于工程科学、无监督学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [CFPL-FAS: Class Free Prompt Learning for Generalizable Face Anti-spoofing](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_CFPL-FAS_Class_Free_Prompt_Learning_for_Generalizable_Face_Anti-spoofing_CVPR_2024_paper.html) | AI 用于工程科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Modality-agnostic Domain Generalizable Medical Image Segmentation by Multi-Frequency in Multi-Scale Attention](https://openaccess.thecvf.com/content/CVPR2024/html/Nam_Modality-agnostic_Domain_Generalizable_Medical_Image_Segmentation_by_Multi-Frequency_in_Multi-Scale_CVPR_2024_paper.html) | AI 用于生命科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Tyche: Stochastic In-Context Learning for Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Rakic_Tyche_Stochastic_In-Context_Learning_for_Medical_Image_Segmentation_CVPR_2024_paper.html) | AI 用于生命科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Feature Re-Embedding: Towards Foundation Model-Level Performance in Computational Pathology](https://openaccess.thecvf.com/content/CVPR2024/html/Tang_Feature_Re-Embedding_Towards_Foundation_Model-Level_Performance_in_Computational_Pathology_CVPR_2024_paper.html) | AI 用于生命科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [GLACE: Global Local Accelerated Coordinate Encoding](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_GLACE_Global_Local_Accelerated_Coordinate_Encoding_CVPR_2024_paper.html) | AI 用于工程科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [On the Estimation of Image-matching Uncertainty in Visual Place Recognition](https://openaccess.thecvf.com/content/CVPR2024/html/Zaffar_On_the_Estimation_of_Image-matching_Uncertainty_in_Visual_Place_Recognition_CVPR_2024_paper.html) | AI 用于工程科学、机器学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [OAKINK2: A Dataset of Bimanual Hands-Object Manipulation in Complex Task Completion](https://openaccess.thecvf.com/content/CVPR2024/html/Zhan_OAKINK2_A_Dataset_of_Bimanual_Hands-Object_Manipulation_in_Complex_Task_CVPR_2024_paper.html) | AI 用于工程科学、大语言模型 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Fantastic Animals and Where to Find Them: Segment Any Marine Animal with Dual SAM](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Fantastic_Animals_and_Where_to_Find_Them_Segment_Any_Marine_CVPR_2024_paper.html) | AI 用于生命科学、深度学习 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Versatile Navigation Under Partial Observability via Value-guided Diffusion Policy](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Versatile_Navigation_Under_Partial_Observability_via_Value-guided_Diffusion_Policy_CVPR_2024_paper.html) | AI 用于工程科学、扩散模型 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Improving Bird's Eye View Semantic Segmentation by Task Decomposition](https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_Improving_Birds_Eye_View_Semantic_Segmentation_by_Task_Decomposition_CVPR_2024_paper.html) | AI 用于工程科学、自编码器 |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | [Towards Learning a Generalist Model for Embodied Navigation](https://openaccess.thecvf.com/content/CVPR2024/html/Zheng_Towards_Learning_a_Generalist_Model_for_Embodied_Navigation_CVPR_2024_paper.html) | AI 用于工程科学、大语言模型 |
| European Conference on Artificial Intelligence | [Night-to-Day: Unpaired Image-to-Image Translation for Nighttime Pedestrian Detection.](https://doi.org/10.3233/faia240542) | AI 用于工程科学、生成对抗网络 |
| European Conference on Artificial Intelligence | [Aligning XAI with EU Regulations for Smart Biomedical Devices: A Methodology for Compliance Analysis.](https://doi.org/10.3233/faia240568) | AI 用于工程科学、可解释机器学习 |
| Artificial Intelligence Review | [The key artificial intelligence technologies in early childhood education: a review](https://doi.org/10.1007/s10462-023-10637-7) | AI 用于社会科学、综述 |
| Artificial Intelligence Review | [Understanding upper-limb movements via neurocomputational models of the sensorimotor system and neurorobotics: where we stand](https://doi.org/10.1007/s10462-023-10694-y) | AI 用于生命科学、综述 |
| Artificial Intelligence Review | [Exploring the integration of artificial intelligence (AI) and augmented reality (AR) in maritime medicine](https://doi.org/10.1007/s10462-024-10735-0) | AI 用于生命科学、综述 |
| Artificial Intelligence Review | [New discrete-time zeroing neural network for solving time-dependent linear equation with boundary constraint](https://doi.org/10.1007/s10462-024-10746-x) | AI 用于数理科学、神经网络 |
| Artificial Intelligence Review | [A review of digital twins and their application in cybersecurity based on artificial intelligence](https://doi.org/10.1007/s10462-024-10805-3) | AI 用于工程科学、综述 |
| Artificial Intelligence Review | [A novel ML-MCDM-based decision support system for evaluating autonomous vehicle integration scenarios in Geneva’s public transportation](https://doi.org/10.1007/s10462-024-10917-w) | AI 用于工程科学、随机森林 |
| Molecular Neurodegeneration | [Single-cell peripheral immunoprofiling of Lewy body and Parkinson’s disease in a multi-site cohort](https://doi.org/10.1186/s13024-024-00748-2) | AI 用于生命科学、机器学习 |
| Trends in Food Science & Technology | [The multi-objective data-driven approach: A route to drive performance optimization in the food industry](https://doi.org/10.1016/j.tifs.2024.104697) | AI 用于工程科学、机器学习、综述 |
| Information Fusion | [Insights into Internet of Medical Things (IoMT): Data fusion, security issues and potential solutions](https://doi.org/10.1016/j.inffus.2023.102060) | AI 用于生命科学、综述、机器学习 |
| Information Fusion | [A survey of route recommendations: Methods, applications, and opportunities](https://doi.org/10.1016/j.inffus.2024.102413) | AI 用于工程科学、机器学习、综述 |
| Information Fusion | [Artificial intelligence for production, operations and logistics management in modular construction industry: A systematic literature review](https://doi.org/10.1016/j.inffus.2024.102423) | AI 用于工程科学、综述 |
| Information Fusion | [Multimodal contrastive learning for brain–machine fusion: From brain-in-the-loop modeling to brain-out-of-the-loop application](https://doi.org/10.1016/j.inffus.2024.102447) | AI 用于生命科学、对比学习 |
| Information Fusion | [Revolutionizing healthcare: IoMT-enabled digital enhancement via multimodal ADL data fusion](https://doi.org/10.1016/j.inffus.2024.102518) | AI 用于生命科学、机器学习 |
| Nature Ecology & Evolution | [Inferring DNA methylation in non-skeletal tissues of ancient specimens](https://doi.org/10.1038/s41559-024-02571-w) | AI 用于生命科学、机器学习 |
| Nature Human Behaviour | [Representation of internal speech by single neurons in human supramarginal gyrus](https://doi.org/10.1038/s41562-024-01867-y) | AI 用于生命科学、脑机接口解码 |
| Nature Human Behaviour | [Power and reproducibility in the external validation of brain-phenotype predictions](https://doi.org/10.1038/s41562-024-01931-7) | AI 用于生命科学、机器学习、科学评测 |
| Nature Communications | [Quantitative measurement of antibiotic resistance in Mycobacterium tuberculosis reveals genetic determinants of resistance and susceptibility in a target gene approach](https://doi.org/10.1038/s41467-023-44325-5) | AI 用于生命科学、科学数据 |
| Nature Communications | [Machine learning-based extrachromosomal DNA identification in large-scale cohorts reveals its clinical implications in cancer](https://doi.org/10.1038/s41467-024-45479-6) | AI 用于生命科学、机器学习 |
| Nature Communications | [Unsupervised classification of brain-wide axons reveals the presubiculum neuronal projection blueprint](https://doi.org/10.1038/s41467-024-45741-x) | AI 用于生命科学、无监督学习 |
| Nature Communications | [Single-pixel p-graded-n junction spectrometers](https://doi.org/10.1038/s41467-024-46066-5) | AI 用于工程科学、隐式神经表示、光谱分析 |
| Nature Communications | [Cell type signatures in cell-free DNA fragmentation profiles reveal disease biology](https://doi.org/10.1038/s41467-024-46435-0) | AI 用于生命科学、机器学习、疾病辅助诊断 |
| Nature Communications | [Deep learning predictions of TCR-epitope interactions reveal epitope-specific chains in dual alpha T cells](https://doi.org/10.1038/s41467-024-47461-8) | AI 用于生命科学、深度学习 |
| Nature Communications | [Utility of polygenic scores across diverse diseases in a hospital cohort for predictive modeling](https://doi.org/10.1038/s41467-024-47472-5) | AI 用于生命科学、逻辑回归、疾病风险预测 |
| Nature Communications | [Efficient characterizations of multiphoton states with an ultra-thin optical device](https://doi.org/10.1038/s41467-024-48213-4) | AI 用于数理科学、机器学习 |
| Nature Communications | [Simple autonomous agents can enhance creative semantic discovery by human groups](https://doi.org/10.1038/s41467-024-49528-y) | AI 用于社会科学 |
| Nature Communications | [Integration of rate and phase codes by hippocampal cell-assemblies supports flexible encoding of spatiotemporal context](https://doi.org/10.1038/s41467-024-52988-x) | AI 用于生命科学、无监督学习 |
| Nature Communications | [MatSwarm: trusted swarm transfer learning driven materials computation for secure big data sharing](https://doi.org/10.1038/s41467-024-53431-x) | AI 用于物质科学、联邦学习、迁移学习 |
| Nature Communications | [Single-cell landscape of innate and acquired drug resistance in acute myeloid leukemia](https://doi.org/10.1038/s41467-024-53535-4) | AI 用于生命科学、无监督学习、多组学整合分析 |
| Nature Communications | [HiDDEN: a machine learning method for detection of disease-relevant populations in case-control single-cell transcriptomics data](https://doi.org/10.1038/s41467-024-53666-8) | AI 用于生命科学、机器学习、单细胞组学分析 |
| Nature Communications | [Learning properties of quantum states without the IID assumption](https://doi.org/10.1038/s41467-024-53765-6) | AI 用于数理科学、量子态性质学习 |
| Nature Physics | [Learning quantum Hamiltonians from high-temperature Gibbs states and real-time evolutions](https://doi.org/10.1038/s41567-023-02376-x) | AI 用于数理科学、机器学习 |

## 本轮26条转排除明细

主要排除通用AI算法、通用软件/硬件或业务应用，现有摘要未显示实质科学研究任务；另有1条出版方确认为观点性Perspective。具体原因逐条保留，未将“证据不足”批量当成排除。

| 来源 | 论文（排除原因） |
|---|---|
| IEEE/CVF Computer Vision and Pattern Recognition Conference | Deep-TROJ: An Inference Stage Trojan Insertion Algorithm through Efficient Weight Replacement Attack（研究对象是神经网络木马与通用分类基准，AI为受攻击对象，摘要未提出独立科学研究任务。） |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | G-FARS: Gradient-Field-based Auto-Regressive Sampling for 3D Part Grouping（通过图网络组合通用三维形状部件，未显示制造装配约束或独立科学问题，属于通用视觉方法。） |
| IEEE/CVF Computer Vision and Pattern Recognition Conference | Describing Differences in Image Sets with Natural Language（核心为图像集合差异描述和模型数据审计，记忆性仅作为示例，未展示认知研究任务的实质检验。） |
| European Conference on Artificial Intelligence | Synthetically Augmented Self-Supervised Fine-Tuning for Diverse Text OCR Correction.（The abstract only presents generic OCR correction and synthetic-noise fine-tuning; historical-document motivation does not establish a specific scientific research contribution.） |
| European Conference on Artificial Intelligence | Designing an XAI Interface for Tree-Based ML Models.（The study concerns a generic user/model explanation protocol without a specified scientific or engineering research task.） |
| European Conference on Artificial Intelligence | Temporal Fairness in Decision Making Problems.（Temporal fairness is formulated as generic optimization; the abstract does not identify the four domains or a substantive scientific use.） |
| European Conference on Artificial Intelligence | Preserving the Privacy of Reward Functions in MDPs through Deception.（A general reward-privacy RL algorithm is evaluated on benchmarks; wildlife protection is a motivation example, not an evidenced scientific task.） |
| European Conference on Artificial Intelligence | Learning Joint Models of Prediction and Optimization.（Generic predict-then-optimize and learned optimization methods; no mathematical problem class or specific scientific application is identified.） |
| European Conference on Artificial Intelligence | DeCoRTAD: Diffusion Based Conditional Representation Learning for Online Trajectory Anomaly Detection.（Generic trajectory anomaly representation learning without an identified physical or scientific target.） |
| European Conference on Artificial Intelligence | Escape Sensing Games: Detection-vs-Evasion in Security Applications.（Generic game-theoretic target arrangement and heuristic equilibrium computation; security scenarios are motivations without evidenced scientific applications.） |
| European Conference on Artificial Intelligence | Compromises in Dialogical Argumentation: Aggregated Policies for Biparty Decision Theory.（Generic automated persuasion and utility aggregation evaluated on synthetic/utility datasets, without a substantive human-behavior research result.） |
| European Conference on Artificial Intelligence | Audience Persona Knowledge-Aligned Prompt Tuning Method for Online Debate.（Persona simulation improves argument-quality models, but no validated human persuasion study is presented.） |
| European Conference on Artificial Intelligence | Enhancing Stance Detection on Social Media via Core Views Discovery.（Core-view extraction improves generic social-media stance classification; no substantive public-cognition research question or result is established.） |
| European Conference on Artificial Intelligence | A Lazy Approach to Neural Numerical Planning with Control Parameters.（Generic neural numerical planning and SMT efficiency across unnamed domains, without a specific scientific task.） |
| European Conference on Artificial Intelligence | Novelty Accommodating Multi-Agent Planning in High Fidelity Simulated Open World.（General-purpose novelty adaptation in agents; military simulator evaluation does not itself establish a specific scientific research contribution.） |
| European Conference on Artificial Intelligence | Enhancing Manufacturing Knowledge Access with LLMs and Context-Aware Prompting.（Natural-language to SPARQL retrieval of manufacturing knowledge; no actual manufacturing process, design, or experimental research task is studied.） |
| Artificial Intelligence Review | Learning search algorithm: framework and comprehensive performance for solving optimization problems（研究核心是通用群智能优化算法和标准基准；仅笼统提及六个工程例题，摘要没有具体科学研究任务贡献。） |
| Information Fusion | Semi-supervised clustering with two types of background knowledge: Fusing pairwise constraints and monotonicity constraints（贡献是融合约束的通用半监督聚类算法；摘要仅说明通用基准及未描述的案例，不能支撑具体科学任务。） |
| Information Fusion | Data fusion in neuromarketing: Multimodal analysis of biosignals, lifecycle stages, current advances, datasets, trends, and challenges（综述主要面向广告推广、产品接受度与营销目标，未展示独立的科学研究任务或AI科学贡献。） |
| Information Fusion | Track initialization and re-identification for 3D multi-view multi-object tracking（贡献为通用多相机目标跟踪与重识别，并在视觉数据集评测，未说明针对科学或工程领域研究问题的直接贡献。） |
| Information Fusion | Imputation of missing values in multi-view data（研究通用多视图缺失值填补及计算效率；真实案例未说明领域和科学任务，现有证据属于通用机器学习方法。） |
| Journal of Advanced Research | 4SQR-Code: A 4-state QR code generation model for increasing data storing capacity in the Digital Twin framework（贡献是二维码编码容量与YOLO解码工具，在数字孪生框架中测试随机样本，未展示实质科学研究任务。） |
| Nature Communications | Data encoding for healthcare data democratization and information leakage prevention（Generic irreversible encoding and model-privacy evaluation; healthcare is the data context, with no concrete medical research task in the abstract.） |
| Nature Communications | Structure and inference in hypergraphs with node attributes（摘要贡献为通用超图社区发现与超边预测方法，未给出具体科学研究问题及对应发现。） |
| Nature Communications | Analog reservoir computing via ferroelectric mixed phase boundary transistors（贡献是储备池计算硬件及通用时间序列预测性能，摘要未给出由 AI 支撑的具体科学研究任务。） |
| npj Science of Learning | Utilizing epigenetics to study the shared nature of development and biological aging across the lifespan（出版方将本文列为Perspective；摘要主要提出将儿童发育与生物衰老连接的观点和研究方向，不属于本批保留的原创研究或实质方法综述，按文献类型排除。） |

## 尚未完成

- **856条**有可用摘要，但摘要仍不能确认AI的实质作用、科学贡献或文献类型。重复只读同一摘要不会自动消除疑点；需要更明确的摘要/官方元数据证据。
- **296条**摘要为空、残缺、混入正文或已被前轮标为不可用，本轮暂放，不宣称已完成实质精筛。
- 官网总数仍有**33个来源**未完成同口径闭环：32个访问受阻，1个跨年口径不一致。真实待办继续显示，不人为清空黄点。

## 交付文件

- [个人论文JSON](../../Blueblue1101.json)：保留全部原始论文字段，只更新审核对象；不改其他负责人/来源记录。
- [本批1232条逐条结果](pending-recheck-decisions.json)、[统计汇总](summary.json)、[转纳入元数据核验](included-metadata-audit.json)。
- [35个来源官网核验](official-count-audit.json)、[请求与分页记录](official-request-log.json)。
- [阶段反馈](../../feedback/Blueblue1101.json)用于GitHub监控自动重算；发布后的实测状态另见[sync-status.md](sync-status.md)。
