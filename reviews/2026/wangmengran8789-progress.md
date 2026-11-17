# 王梦冉2026审核阶段交付（进行中）

按已确认2026分工处理48个来源。原年度候选2202条，本轮从已采全量记录中核实补录7条初筛漏筛，台账合计2209条。快照`2026-11-08T21:38:12.854071+08:00`；审核开始检查main`b06974f0902afed254377eefe071d6f8ac643e82`，技能与标签词表无变化。2026尚未结束，当前结果不代表全年最终覆盖。

累计逐篇形成197条判定：纳入137、排除36、待定24；其余2012条未审。本轮新增57条判定（50条原候选及7条补录）。所有原始对象字段和值均保留，仅追加ai4s_review；补录沿用2026源papers.json原对象。其他负责人、2024/2025数据和监控逻辑未改动。

ScienceDirect原验证码页面已恢复访问。依用户流程从Computer Methods in Applied Mechanics and Engineering卷448 Part A全选、取消Editorial Board，使用Export citation and abstract to BibTeX，导出52条原引文摘要。原BibTeX与SHA256、核验范围、补录ID保存在audits/wangmengran8789-cmame-448PA-20261117.*。逐篇审核其中10条原候选及7条经原摘要核实的漏筛记录；本卷不是年度总量，不声称另外35条都已精筛。Part B未显示批量导出控件，转而读取两篇官方论文页摘要。

本轮补齐4条原候选的空摘要，原始空摘要404条中仍有400条未补齐。另修复一条非空但误采为致谢的摘要：10.1007/s11433-025-2848-2，真正摘要和作者从Springer Nature Link取得，写入verified_metadata。补录7条中的4条原全量记录空摘要也通过官方导出补齐，不混作原404条的减少量。另有3条非空摘要存在已知截断/正文片段/README混入问题（MTNA 103003、103072和Current Biology 2026.10.004），仍待补正确原摘要；400只统计仍空的原候选，不能代表全部摘要质量问题。所有新增摘要均来自原文，不使用生成摘要。历次另修复两条BJC摘要的小于号截断。

Science China Physics, Mechanics & Astronomy的14条候选已逐条判定，Science China Materials的24条候选已逐条判定（其中3条待核正文）；这不等于两刊年度目录和所有纳入元数据均完成。纳入标签使用当前规范中英文词表。输入摘要足以判断者据此记录，未伪称读取正文；只有查证过的元数据写入verified_metadata。

剩余工作：逐篇处理未审；解决24条待定；补400条仍空的原候选摘要及其他已发现的摘要质量问题；完成纳入论文元数据与公开PDF核验；按同口径对账48来源2026官方年度目录。官网总数均保留null，不将未知记零。EMNLP/LCTES当前候选零不代表官网论文零。本阶段PR保持进行中，未合并发布大屏，也不据此将提示强制变绿。

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
| npj Parkinson’s Disease | 35 | 0 | 0 | 0 | 0 | 35 | 0 |
| Building and Environment | 75 | 0 | 0 | 0 | 0 | 75 | 23 |
| npj Breast Cancer | 19 | 0 | 16 | 3 | 0 | 0 | 0 |
| Transportation Research Part C Emerging Technologies | 26 | 0 | 22 | 0 | 4 | 0 | 4 |
| Sensors and Actuators B Chemical | 31 | 0 | 0 | 0 | 0 | 31 | 23 |
| Materials & Design | 125 | 0 | 0 | 0 | 0 | 125 | 0 |
| Science China Information Sciences | 36 | 0 | 0 | 0 | 0 | 36 | 0 |
| Energy and Buildings | 72 | 0 | 0 | 0 | 0 | 72 | 9 |
| Knowledge-Based Systems | 125 | 0 | 0 | 0 | 0 | 125 | 61 |
| Journal of Cheminformatics | 119 | 0 | 0 | 0 | 0 | 119 | 0 |
| Applied Soft Computing | 146 | 0 | 0 | 0 | 0 | 146 | 82 |
| Artificial Intelligence in Medicine | 58 | 0 | 0 | 0 | 0 | 58 | 1 |
| British Journal of Cancer | 7 | 0 | 5 | 1 | 1 | 0 | 0 |
| Cell Reports | 39 | 0 | 0 | 0 | 0 | 39 | 0 |
| Current Biology | 15 | 0 | 7 | 5 | 3 | 0 | 0 |
| Science China Materials | 24 | 0 | 13 | 8 | 3 | 0 | 0 |
| The American Journal of Human Genetics | 4 | 0 | 3 | 1 | 0 | 0 | 0 |
| Computer Methods in Applied Mechanics and Engineering | 121 | 7 | 19 | 0 | 0 | 109 | 15 |
| Engineering Structures | 57 | 0 | 0 | 0 | 0 | 57 | 32 |
| Neuropsychopharmacology | 6 | 0 | 3 | 3 | 0 | 0 | 0 |
| Precision Agriculture | 51 | 0 | 0 | 0 | 0 | 51 | 0 |
| Cell Systems | 36 | 0 | 0 | 0 | 0 | 36 | 1 |
| npj Materials Degradation | 21 | 0 | 18 | 1 | 2 | 0 | 0 |
| Translational Psychiatry | 42 | 0 | 0 | 0 | 0 | 42 | 0 |
| Frontiers of Computer Science | 9 | 0 | 2 | 3 | 4 | 0 | 0 |
| Journal of Hydrology | 178 | 0 | 0 | 0 | 0 | 178 | 84 |
| Science China Physics Mechanics and Astronomy | 14 | 0 | 10 | 4 | 0 | 0 | 0 |
| Cell Reports Physical Science | 56 | 0 | 0 | 0 | 0 | 56 | 1 |
| Communications Chemistry | 61 | 0 | 0 | 0 | 0 | 61 | 0 |
| Agricultural and Forest Meteorology | 30 | 0 | 0 | 0 | 0 | 30 | 2 |
| International Journal of Heat and Mass Transfer | 48 | 0 | 0 | 0 | 0 | 48 | 29 |
| Molecular Therapy — Nucleic Acids | 10 | 0 | 5 | 2 | 3 | 0 | 0 |
| Computer Methods and Programs in Biomedicine | 136 | 0 | 0 | 0 | 0 | 136 | 0 |
| Information Sciences | 38 | 0 | 0 | 0 | 0 | 38 | 23 |
| Communications Physics | 38 | 0 | 0 | 0 | 0 | 38 | 0 |
| BMC Biology | 33 | 0 | 0 | 0 | 0 | 33 | 0 |
| International Journal of Medical Informatics | 82 | 0 | 0 | 0 | 0 | 82 | 1 |
| Structure | 10 | 0 | 7 | 2 | 1 | 0 | 0 |
| Engineering With Computers | 59 | 0 | 0 | 0 | 0 | 59 | 0 |
| Computer Physics Communications | 37 | 0 | 0 | 0 | 0 | 37 | 8 |

推送前再次检查main `56e073c0`：年度候选变化属于其他负责人；王梦冉原2202条逐字段一致，当前审核输入保持有效。
