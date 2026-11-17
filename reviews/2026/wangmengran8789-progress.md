# 王梦冉2026审核阶段交付（进行中）

本批从最新确认的2026分工开始，48个来源、2202条候选。仅处理王梦冉的2026数据，未修改其他负责人、2024/2025台账或监控脚本。

快照：`2026-11-08T21:38:12.854071+08:00`。候选输入SHA256：`1412d7d77ee5be72c1fb0e7bb99e154e4e37fb0a52f0becd66d140791dc603d2`。输入main：`cf5d3ee36e059366fa181b3a2bc4a0dd52e18e16`；交付前再次检查main：`18a99b1e9b793f053d9c169f79ee0064cf149d2b`，技能和词表无变化。2026尚未结束，当前数据不代表全年最终覆盖。

已逐篇形成140条判定：95纳入、24排除、21待定；2062条保留未审。纳入判定与正式元数据核验分别记录，目前不能声称所有纳入元数据都已核完。未按标题或关键词批量生成纳入/排除结论。既往2024的“待定转排除”未自动套用于2026的新证据疑点。

从官网核对了npj 2D Materials and Applications三篇、Neuropsychopharmacology三篇及British Journal of Cancer两篇。后两篇结果段因小于号解析被截断，已在verified_metadata补回原文；不覆盖原始abstract。其余有摘要的判定依据明确标为输入原摘要，未伪称读取正文。标签全部使用现行规范词表；未新增标签。

原始缺摘要404条仍未解决，逐条列于`audits/wangmengran8789-2026-abstract-gaps.json`，其中仅一个具体论文网址有本轮浏览器受阻记录，其余标为尚未尝试。正常Chrome访问https://doi.org/10.1016/j.cma.2025.118411 后ScienceDirect显示“Are you a robot?”；需要负责人手动验证，未绕过或自动解验证码，也未把未知摘要生成补齐。尚未开展48来源的完整官方年度目录对账，official_total均保留null；EMNLP/LCTES当前候选零不代表官网论文零。

下一步：从unreviewed继续逐篇读摘要；人工验证通过后继续官方摘要导出；逐篇解决21条待定；补核纳入论文元数据和公开PDF；按来源完成2026目录DOI对账。详情见个人反馈和审计清单。阶段PR不等同于任务完成，也不据此把大屏所有提示改绿。

| 来源 | 候选 | 纳入 | 排除 | 待定 | 未审 | 原始缺摘要 |
|---|---:|---:|---:|---:|---:|---:|
| Environmental Chemistry Letters | 1 | 1 | 0 | 0 | 0 | 0 |
| Conference on Empirical Methods in Natural Language Processing | 0 | 0 | 0 | 0 | 0 | 0 |
| Trends in Chemistry | 1 | 0 | 0 | 1 | 0 | 1 |
| Current Opinion in Green and Sustainable Chemistry | 3 | 1 | 0 | 2 | 0 | 0 |
| Biomaterials Research | 2 | 2 | 0 | 0 | 0 | 0 |
| npj 2D Materials and Applications | 6 | 3 | 3 | 0 | 0 | 0 |
| ACM SIGPLAN/SIGBED International Conference on Languages, Compilers andTools for Embedded Systems | 0 | 0 | 0 | 0 | 0 | 0 |
| Drug Discovery Today | 60 | 0 | 0 | 0 | 60 | 0 |
| npj Parkinson’s Disease | 35 | 0 | 0 | 0 | 35 | 0 |
| Building and Environment | 75 | 0 | 0 | 0 | 75 | 23 |
| npj Breast Cancer | 19 | 16 | 3 | 0 | 0 | 0 |
| Transportation Research Part C Emerging Technologies | 26 | 22 | 0 | 4 | 0 | 4 |
| Sensors and Actuators B Chemical | 31 | 0 | 0 | 0 | 31 | 23 |
| Materials & Design | 125 | 0 | 0 | 0 | 125 | 0 |
| Science China Information Sciences | 36 | 0 | 0 | 0 | 36 | 0 |
| Energy and Buildings | 72 | 0 | 0 | 0 | 72 | 9 |
| Knowledge-Based Systems | 125 | 0 | 0 | 0 | 125 | 61 |
| Journal of Cheminformatics | 119 | 0 | 0 | 0 | 119 | 0 |
| Applied Soft Computing | 146 | 0 | 0 | 0 | 146 | 82 |
| Artificial Intelligence in Medicine | 58 | 0 | 0 | 0 | 58 | 1 |
| British Journal of Cancer | 7 | 5 | 1 | 1 | 0 | 0 |
| Cell Reports | 39 | 0 | 0 | 0 | 39 | 0 |
| Current Biology | 15 | 7 | 5 | 3 | 0 | 0 |
| Science China Materials | 24 | 0 | 0 | 0 | 24 | 0 |
| The American Journal of Human Genetics | 4 | 3 | 1 | 0 | 0 | 0 |
| Computer Methods in Applied Mechanics and Engineering | 121 | 0 | 0 | 0 | 121 | 19 |
| Engineering Structures | 57 | 0 | 0 | 0 | 57 | 32 |
| Neuropsychopharmacology | 6 | 3 | 3 | 0 | 0 | 0 |
| Precision Agriculture | 51 | 0 | 0 | 0 | 51 | 0 |
| Cell Systems | 36 | 0 | 0 | 0 | 36 | 1 |
| npj Materials Degradation | 21 | 18 | 1 | 2 | 0 | 0 |
| Translational Psychiatry | 42 | 0 | 0 | 0 | 42 | 0 |
| Frontiers of Computer Science | 9 | 2 | 3 | 4 | 0 | 0 |
| Journal of Hydrology | 178 | 0 | 0 | 0 | 178 | 84 |
| Science China Physics Mechanics and Astronomy | 14 | 0 | 0 | 0 | 14 | 0 |
| Cell Reports Physical Science | 56 | 0 | 0 | 0 | 56 | 1 |
| Communications Chemistry | 61 | 0 | 0 | 0 | 61 | 0 |
| Agricultural and Forest Meteorology | 30 | 0 | 0 | 0 | 30 | 2 |
| International Journal of Heat and Mass Transfer | 48 | 0 | 0 | 0 | 48 | 29 |
| Molecular Therapy — Nucleic Acids | 10 | 5 | 2 | 3 | 0 | 0 |
| Computer Methods and Programs in Biomedicine | 136 | 0 | 0 | 0 | 136 | 0 |
| Information Sciences | 38 | 0 | 0 | 0 | 38 | 23 |
| Communications Physics | 38 | 0 | 0 | 0 | 38 | 0 |
| BMC Biology | 33 | 0 | 0 | 0 | 33 | 0 |
| International Journal of Medical Informatics | 82 | 0 | 0 | 0 | 82 | 1 |
| Structure | 10 | 7 | 2 | 1 | 0 | 0 |
| Engineering With Computers | 59 | 0 | 0 | 0 | 59 | 0 |
| Computer Physics Communications | 37 | 0 | 0 | 0 | 37 | 8 |
