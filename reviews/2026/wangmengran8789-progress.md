# 最新检查点：2026-11-17当前2026参考全集

44刊按当前截至11月17日已登记的完整2026参考目录逐DOI对齐，不以首次登记时间截断。累计补采576条源记录（原先快照前漏项135条及本阶段快照后登记441条；另1条索引年份滞后、最新登记已为2027，仅审计归档）；保留并单列177条2027出版登记历史记录。当前参考对账未决0，官网未知仍null，未承诺年底全年最终查全。原始采集快照字节保留。EMNLP仍缺采2702条，未在本轮掩盖。

累计新增初筛候选12条均未审，个人台账2233条；纳入1555、排除177、待定489，本轮内容精筛新增0。待补摘要401条，原393条未伪称补齐，新增空摘要来自新候选。完整证据及对账表见reviews/2026/audits/wangmengran8789-catalogue-current-20261117/report.md。

以下为此前历史检查点，以本段当前全集结果为准。

# 最新检查点：2026-11-17剩余44刊总量对账

以11月8日历史快照为边界完成44刊可靠参考来源逐DOI对账；补采135条源记录，442条快照后首次登记和177条2027出版登记历史记录均有独立清单并按口径归一。官方总数未知仍null；不冒称2026全年最终查全。EMNLP缺采2702条仍待后续处理。

新增初筛候选3条，均unreviewed；当前个人台账2224条，纳入1555、排除177、待定489、未审3。本轮内容精筛新增0。缺摘要当前394条，其中本轮新候选1条，原393条缺口不变。原始字段和历史快照保留；年份核验仅补入verified_metadata与year_scope_check。详见reviews/2026/audits/wangmengran8789-catalogue-resolution-20261117/report.md。

以下为此前历史检查点，旧统计以本段最新结果为准。

# 王梦冉2026审核阶段交付（进行中）

按2026分工处理48个来源。原年度候选2202条，已核实漏筛补录19条，台账合计2221条。快照`2026-11-08T21:38:12.854071+08:00`；最近检查main`5df29602976068cb1bc51ab48a5e09cf54124c85`。2026尚未结束，当前快照不代表全年最终覆盖。

累计1828条已进行摘要内容判读：纳入1555、排除177、内容待核96。上一检查点新增334条内容判读：Journal of Hydrology 94条、Science China Information Sciences 36条、npj Parkinson’s Disease 35条、BMC Biology 33条、Computer Methods and Programs in Biomedicine 136条。各条均有独立依据，未声称读取未访问的正文。

另外393条原始空摘要仅完成元数据缺漏登记，标记pending和review_stage=metadata_gate_waiting_for_original_abstract，不计作内容审核完成。台账总状态为纳入1555、排除177、待定489、未审0。待定包含上述393条元数据登记及96条内容待核。原始空摘要404条中已补6条，仍空398条；另有非空摘要截断、正文片段或README混入等质量问题，审计中单列，不能把398理解为全部摘要问题数。

所有原始字段和值保留，仅追加ai4s_review；19条补录沿用源papers.json原对象。纳入标签采用规范中英文词表。纳入后仍需核对正式元数据与公开PDF，只有实际查证值写入verified_metadata。未编辑其他负责人台账、2024/2025数据或监控提示逻辑。

此前ScienceDirect官网卷448 Part A全选并排除Editorial Board，Export citation and abstract to BibTeX导出52条；已核对10条既有候选并核实补录7条初筛漏筛。Part B另查2篇官方论文摘要。原BibTeX与核验范围保存在audits/wangmengran8789-cmame-448PA-20261117.*，单卷导出不等于年度目录对账。该过程补齐4条原候选空摘要及4条补录原对象空摘要；另从Springer修复s11433-025-2848-2误采致谢，并修复两条BJC摘要小于号截断。最近另按同样流程取得卷449 Part A的32条及Part B的26条原引文摘要。逐篇对照后，8条原未审和2条原空摘要待定记录完成纳入，12条初筛漏筛从源全量对象补录纳入。其余36条为非AI数值研究或勘误，逐条理由保存在对应卷审计中，未混入个人候选台账状态数量。原候选空摘要再补2条，新增补录空摘要补3条；仍空398条。Computer Physics Communications的29条非空未审记录也已逐篇处理（26纳入、2排除、1待核），该刊仍有8条空摘要待补。

最近又完成Communications Physics 38条（27纳入、8排除、3待核）及Communications Chemistry 61条（55纳入、3排除、3待核）。

Materials & Design的125条已逐篇判读：110纳入、14排除、1待核。若干原摘要公式/数值缺失已逐条标记，仍需官网补全。

Agricultural and Forest Meteorology的28条非空未审摘要均已判为纳入；该刊另外2条仍为空摘要待补。

Journal of Cheminformatics的119条已逐篇判读：109纳入、7排除、3待核。

上一轮新增138条摘要内容判读：Energy and Buildings 63条（58纳入、2排除、3待核）、Building and Environment 52条（44纳入、4排除、4待核）、Sensors and Actuators B 8条（全部纳入）、Information Sciences 15条（8纳入、7排除）。四刊非空未审均已处理，空摘要候选仍按原记录待补；未将本轮审核冒称官网核验。

本轮已处理此前剩余737条：618纳入、71排除、48内容待核。累计未审已归零；这不等于全部形成最终判定或完成官网元数据核验。新待核主要涉及观点/评论与实质综述类型的区分、AI仅展望、自动化/物理仿真与学习方法的区分。逐条理由见台账及本轮审计。

下一步补398条仍空摘要与其他质量缺口、解决96条内容待核、核验纳入元数据及公开PDF，并按同口径逐DOI核对48来源2026官方目录。官网总数均保留null；EMNLP/LCTES候选零不代表官网零。本PR保持进行中，未合并发布大屏，不将缺漏提示强制改绿。

| 来源 | 原候选 | 补录 | 纳入 | 排除 | 待定 | 未审 | 仍为空摘要 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Environmental Chemistry Letters | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| Conference on Empirical Methods in Natural Language Processing | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Trends in Chemistry | 1 | 0 | 0 | 0 | 1 | 0 | 1 |
| Current Opinion in Green and Sustainable Chemistry | 3 | 0 | 1 | 0 | 2 | 0 | 0 |
| Biomaterials Research | 2 | 0 | 2 | 0 | 0 | 0 | 0 |
| npj 2D Materials and Applications | 6 | 0 | 3 | 3 | 0 | 0 | 0 |
| ACM SIGPLAN/SIGBED International Conference on Languages, Compilers andTools for Embedded Systems | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Drug Discovery Today | 60 | 0 | 37 | 9 | 14 | 0 | 0 |
| npj Parkinson’s Disease | 35 | 0 | 33 | 1 | 1 | 0 | 0 |
| Building and Environment | 75 | 0 | 44 | 4 | 27 | 0 | 23 |
| npj Breast Cancer | 19 | 0 | 16 | 3 | 0 | 0 | 0 |
| Transportation Research Part C Emerging Technologies | 26 | 0 | 22 | 0 | 4 | 0 | 4 |
| Sensors and Actuators B Chemical | 31 | 0 | 8 | 0 | 23 | 0 | 23 |
| Materials & Design | 125 | 0 | 110 | 14 | 1 | 0 | 0 |
| Science China Information Sciences | 36 | 0 | 16 | 18 | 2 | 0 | 0 |
| Energy and Buildings | 72 | 0 | 58 | 2 | 12 | 0 | 9 |
| Knowledge-Based Systems | 125 | 0 | 44 | 18 | 63 | 0 | 61 |
| Journal of Cheminformatics | 119 | 0 | 109 | 7 | 3 | 0 | 0 |
| Applied Soft Computing | 146 | 0 | 52 | 11 | 83 | 0 | 82 |
| Artificial Intelligence in Medicine | 58 | 0 | 55 | 1 | 2 | 0 | 1 |
| British Journal of Cancer | 7 | 0 | 5 | 1 | 1 | 0 | 0 |
| Cell Reports | 39 | 0 | 33 | 2 | 4 | 0 | 0 |
| Current Biology | 15 | 0 | 7 | 5 | 3 | 0 | 0 |
| Science China Materials | 24 | 0 | 13 | 8 | 3 | 0 | 0 |
| The American Journal of Human Genetics | 4 | 0 | 3 | 1 | 0 | 0 | 0 |
| Computer Methods in Applied Mechanics and Engineering | 121 | 19 | 125 | 1 | 14 | 0 | 13 |
| Engineering Structures | 57 | 0 | 23 | 2 | 32 | 0 | 32 |
| Neuropsychopharmacology | 6 | 0 | 3 | 3 | 0 | 0 | 0 |
| Precision Agriculture | 51 | 0 | 45 | 4 | 2 | 0 | 0 |
| Cell Systems | 36 | 0 | 29 | 1 | 6 | 0 | 1 |
| npj Materials Degradation | 21 | 0 | 18 | 1 | 2 | 0 | 0 |
| Translational Psychiatry | 42 | 0 | 30 | 6 | 6 | 0 | 0 |
| Frontiers of Computer Science | 9 | 0 | 2 | 3 | 4 | 0 | 0 |
| Journal of Hydrology | 178 | 0 | 91 | 1 | 86 | 0 | 84 |
| Science China Physics Mechanics and Astronomy | 14 | 0 | 10 | 4 | 0 | 0 | 0 |
| Cell Reports Physical Science | 56 | 0 | 45 | 5 | 6 | 0 | 1 |
| Communications Chemistry | 61 | 0 | 55 | 3 | 3 | 0 | 0 |
| Agricultural and Forest Meteorology | 30 | 0 | 28 | 0 | 2 | 0 | 2 |
| International Journal of Heat and Mass Transfer | 48 | 0 | 16 | 2 | 30 | 0 | 29 |
| Molecular Therapy — Nucleic Acids | 10 | 0 | 5 | 2 | 3 | 0 | 0 |
| Computer Methods and Programs in Biomedicine | 136 | 0 | 134 | 2 | 0 | 0 | 0 |
| Information Sciences | 38 | 0 | 8 | 7 | 23 | 0 | 23 |
| Communications Physics | 38 | 0 | 27 | 8 | 3 | 0 | 0 |
| BMC Biology | 33 | 0 | 31 | 1 | 1 | 0 | 0 |
| International Journal of Medical Informatics | 82 | 0 | 68 | 8 | 6 | 0 | 1 |
| Structure | 10 | 0 | 7 | 2 | 1 | 0 | 0 |
| Engineering With Computers | 59 | 0 | 57 | 1 | 1 | 0 | 0 |
| Computer Physics Communications | 37 | 0 | 26 | 2 | 9 | 0 | 8 |

本轮官网摘要补证：CMAME第450卷52条、第451卷51条、第452卷Part B 30条，共133条citation-and-abstract BibTeX，均排除Editorial Board。按DOI及题名精确匹配回填5条原候选摘要，放入verified_metadata并保留原字段；仍空393条。5条仍待独立内容判读，本轮新增内容精筛0条，原有判定和标签不变。最新检查main `a31165d54c9b66cc5bb5f190774ea34b9ad0ffb1`。历史段落中的398为上一检查点数。证据详见audits/wangmengran8789-abstract-backfill-20261117.json。

2026-11-17总量核对：48来源已执行本轮来源审计；ECL 40、Engineering With Computers 212与LCTES 19已按官网逐项一致，EMNLP主会官方正文2704、缺采2702已列清单；其余44刊Crossref参考对账差异尚需官网消歧。官网已知4来源、待确认44来源，不等于48来源均已完成查全。报告及完整差异见audits/wangmengran8789-catalogue-20261117/report.md，未修改论文对象及内容审核数量。

## 2026-11-17 缺摘要专项补取（最新断点）

以 main `5ed1b31923ec534eb877cdb0f91895e53ed65847` 的401条缺摘要候选为输入。正常Chrome官网完成17份排除Editorial Board的citation-and-abstract BibTeX导出，按DOI和完整题名匹配补47条；Springer正式页补1条；官网服务CPE00002受阻后，OpenAlex原摘要索引补3条，Europe PMC原摘要补1条。共补52条，有效缺摘要401→349；原始字段、快照、2233条个人记录、1555纳入/177排除/489待定/12未审及全部标签均保留。本轮新增内容精筛0；取得摘要的记录仍须独立内容判读。

全部401条已执行Crossref、OpenAlex、Europe PMC查询并归档（Crossref其中1批20条返回429，保留失败证据）；其余349条未获可核实原摘要，未使用搜索片段或生成文字填充。ScienceDirect第199、198卷和Journal of Hydrology官网均出现CPE00002，重试未恢复；SCIS MafAFP落地页为Letter且未显示Abstract。总量核对已完成状态保持；EMNLP另有2702条源缺采仍未处理。详见 audits/wangmengran8789-abstracts-20261117/report.md 及逐条补证/剩余清单。历史段落数字仅代表当时检查点。

## UTC 2026-11-18 官网原摘要续补（最新断点）

输入main `60a95f05327fd0e7e5efcb44b53c604592990b72`。用户完成官网验证后取得17份排除Editorial Board的原始BibTeX，按DOI及完整题名补43条（ASOC 41、Journal of Hydrology 2），缺摘要349→306。原字段、2233条记录、判定、标签及内容精筛统计保留；本轮新增内容精筛0。水文学第681卷Part A再现CPE00002，Semantic Scholar批量349条请求429，均保存失败证据，未假填摘要。48来源反馈、缺口清单及断点同步，报告 audits/wangmengran8789-abstracts-continue-20261118/report.md。
