# 王梦冉2026审核阶段交付（进行中）

按2026分工处理48个来源。原年度候选2202条，已核实漏筛补录19条，台账合计2221条。快照`2026-11-08T21:38:12.854071+08:00`；最近检查main`56e073c0921723916d4e44b79ea95e4857c945a5`。2026尚未结束，当前快照不代表全年最终覆盖。

累计681条已进行摘要内容判读：纳入572、排除72、内容待核37。上一检查点新增334条内容判读：Journal of Hydrology 94条、Science China Information Sciences 36条、npj Parkinson’s Disease 35条、BMC Biology 33条、Computer Methods and Programs in Biomedicine 136条。各条均有独立依据，未声称读取未访问的正文。

另外393条原始空摘要仅完成元数据缺漏登记，标记pending和review_stage=metadata_gate_waiting_for_original_abstract，不计作内容审核完成。台账总状态为纳入572、排除72、待定430、未审1147。待定包含上述393条元数据登记及37条内容待核。原始空摘要404条中已补6条，仍空398条；另有非空摘要截断、正文片段或README混入等质量问题，审计中单列，不能把398理解为全部摘要问题数。

所有原始字段和值保留，仅追加ai4s_review；19条补录沿用源papers.json原对象。纳入标签采用规范中英文词表。纳入后仍需核对正式元数据与公开PDF，只有实际查证值写入verified_metadata。未编辑其他负责人台账、2024/2025数据或监控提示逻辑。

此前ScienceDirect官网卷448 Part A全选并排除Editorial Board，Export citation and abstract to BibTeX导出52条；已核对10条既有候选并核实补录7条初筛漏筛。Part B另查2篇官方论文摘要。原BibTeX与核验范围保存在audits/wangmengran8789-cmame-448PA-20261117.*，单卷导出不等于年度目录对账。该过程补齐4条原候选空摘要及4条补录原对象空摘要；另从Springer修复s11433-025-2848-2误采致谢，并修复两条BJC摘要小于号截断。最近另按同样流程取得卷449 Part A的32条及Part B的26条原引文摘要。逐篇对照后，8条原未审和2条原空摘要待定记录完成纳入，12条初筛漏筛从源全量对象补录纳入。其余36条为非AI数值研究或勘误，逐条理由保存在对应卷审计中，未混入个人候选台账状态数量。原候选空摘要再补2条，新增补录空摘要补3条；仍空398条。Computer Physics Communications的29条非空未审记录也已逐篇处理（26纳入、2排除、1待核），该刊仍有8条空摘要待补。

最近又完成Communications Physics 38条（27纳入、8排除、3待核）及Communications Chemistry 61条（55纳入、3排除、3待核）。

下一步继续处理1147条未审、补398条仍空摘要与其他质量缺口、解决内容待核、核验纳入元数据及公开PDF，并按同口径逐DOI核对48来源2026官方目录。官网总数均保留null；EMNLP/LCTES候选零不代表官网零。本PR保持进行中，未合并发布大屏，不将缺漏提示强制改绿。

| 来源 | 原候选 | 补录 | 纳入 | 排除 | 待定 | 未审 | 仍为空摘要 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Environmental Chemistry Letters | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| Conference on Empirical Methods in Natural Language Processing | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Trends in Chemistry | 1 | 0 | 0 | 0 | 1 | 0 | 1 |
| Current Opinion in Green and Sustainable Chemistry | 3 | 0 | 1 | 0 | 2 | 0 | 0 |
| Biomaterials Research | 2 | 0 | 2 | 0 | 0 | 0 | 0 |
| npj 2D Materials and Applications | 6 | 0 | 3 | 3 | 0 | 0 | 0 |
| ACM SIGPLAN/SIGBED International Conference on Languages, Compilers andTools for Embedded Systems | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Drug Discovery Today | 60 | 0 | 0 | 0 | 0 | 60 | 0 |
| npj Parkinson’s Disease | 35 | 0 | 33 | 1 | 1 | 0 | 0 |
| Building and Environment | 75 | 0 | 0 | 0 | 23 | 52 | 23 |
| npj Breast Cancer | 19 | 0 | 16 | 3 | 0 | 0 | 0 |
| Transportation Research Part C Emerging Technologies | 26 | 0 | 22 | 0 | 4 | 0 | 4 |
| Sensors and Actuators B Chemical | 31 | 0 | 0 | 0 | 23 | 8 | 23 |
| Materials & Design | 125 | 0 | 0 | 0 | 0 | 125 | 0 |
| Science China Information Sciences | 36 | 0 | 16 | 18 | 2 | 0 | 0 |
| Energy and Buildings | 72 | 0 | 0 | 0 | 9 | 63 | 9 |
| Knowledge-Based Systems | 125 | 0 | 0 | 0 | 61 | 64 | 61 |
| Journal of Cheminformatics | 119 | 0 | 0 | 0 | 0 | 119 | 0 |
| Applied Soft Computing | 146 | 0 | 0 | 0 | 82 | 64 | 82 |
| Artificial Intelligence in Medicine | 58 | 0 | 0 | 0 | 1 | 57 | 1 |
| British Journal of Cancer | 7 | 0 | 5 | 1 | 1 | 0 | 0 |
| Cell Reports | 39 | 0 | 0 | 0 | 0 | 39 | 0 |
| Current Biology | 15 | 0 | 7 | 5 | 3 | 0 | 0 |
| Science China Materials | 24 | 0 | 13 | 8 | 3 | 0 | 0 |
| The American Journal of Human Genetics | 4 | 0 | 3 | 1 | 0 | 0 | 0 |
| Computer Methods in Applied Mechanics and Engineering | 121 | 19 | 41 | 0 | 13 | 86 | 13 |
| Engineering Structures | 57 | 0 | 0 | 0 | 32 | 25 | 32 |
| Neuropsychopharmacology | 6 | 0 | 3 | 3 | 0 | 0 | 0 |
| Precision Agriculture | 51 | 0 | 0 | 0 | 0 | 51 | 0 |
| Cell Systems | 36 | 0 | 0 | 0 | 1 | 35 | 1 |
| npj Materials Degradation | 21 | 0 | 18 | 1 | 2 | 0 | 0 |
| Translational Psychiatry | 42 | 0 | 0 | 0 | 0 | 42 | 0 |
| Frontiers of Computer Science | 9 | 0 | 2 | 3 | 4 | 0 | 0 |
| Journal of Hydrology | 178 | 0 | 91 | 1 | 86 | 0 | 84 |
| Science China Physics Mechanics and Astronomy | 14 | 0 | 10 | 4 | 0 | 0 | 0 |
| Cell Reports Physical Science | 56 | 0 | 0 | 0 | 1 | 55 | 1 |
| Communications Chemistry | 61 | 0 | 55 | 3 | 3 | 0 | 0 |
| Agricultural and Forest Meteorology | 30 | 0 | 0 | 0 | 2 | 28 | 2 |
| International Journal of Heat and Mass Transfer | 48 | 0 | 0 | 0 | 29 | 19 | 29 |
| Molecular Therapy — Nucleic Acids | 10 | 0 | 5 | 2 | 3 | 0 | 0 |
| Computer Methods and Programs in Biomedicine | 136 | 0 | 134 | 2 | 0 | 0 | 0 |
| Information Sciences | 38 | 0 | 0 | 0 | 23 | 15 | 23 |
| Communications Physics | 38 | 0 | 27 | 8 | 3 | 0 | 0 |
| BMC Biology | 33 | 0 | 31 | 1 | 1 | 0 | 0 |
| International Journal of Medical Informatics | 82 | 0 | 0 | 0 | 1 | 81 | 1 |
| Structure | 10 | 0 | 7 | 2 | 1 | 0 | 0 |
| Engineering With Computers | 59 | 0 | 0 | 0 | 0 | 59 | 0 |
| Computer Physics Communications | 37 | 0 | 26 | 2 | 9 | 0 | 8 |
