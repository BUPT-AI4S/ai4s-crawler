# 龙兆科 2024 年论文摘要精筛：阶段交付

本次为**未完成全量漏筛检查的阶段结果**。三个并行代理触发服务额度上限后，保存并提交已完成判断；尚有 5,148 条全量书目未审，见 `unreviewed.json`。用户已明确要求效率优先，爬取失败或受阻项暂缓，不再反复补抓。

负责人：龙兆科（GitHub：AlearnerDL）。批次：2024-20261105-103119；快照：2026-11-05T10:31:19.144426+08:00。来源按 GitHub 当前登记的 49 个建议纳入来源，已与提交 29b0431fc0fabc295722bf54c832e31ae55feaa0 再次核对，范围无变化。

## 交付内容

- `../AlearnerDL.json`：2,294 条论文记录，纳入 1,650，排除 569，待定 75，未审 0。该文件包含全部 1,050 条初筛候选、从全量书目发现的 1,243 条漏筛纳入论文，以及 1 条官网漏采记录（WACV CycleCL，经摘要判断排除）。
- `full-corpus-audit.json`：全量 16,877 条书目逐项状态。纳入 1,650、排除 9,690、待定 389、未审 5,148。非候选的排除/待定记录保留在此审计文件，不混淆为主交付文件的数量。
- `coverage.json`：49 个来源的全量数、初候选数、原始摘要缺失数、审查状态及交付数量。
- `official-directory-audits.json`：已经取得的官方目录核验与 Crossref 登记对照；未独立取得同口径目录的来源不能声明采集完整。
- `unreviewed.json`：后续可直接按 `(venue, year, id)` 接续处理，不需重审已完成项。
- `validation.json`：原字段、1050候选覆盖、重复键、状态、标签及证据字段的结构校验，错误数 0。

## 判断与元数据

只使用原始或可追溯补回的摘要判断AI4S相关性；未阅读正文。PDF仅在少数公开作者版/会议版中提取首页Abstract。官网和目录用于身份、年份、轨道、文章类型和链接核验。保留科学或具体工程任务与AI实质作用均有摘要证据的正式研究及实质性综述；排除社论、宣传、评论、扩展摘要及未纳入的附属轨道。

原记录字段和值均保留，候选文件原有关键词命中和标签字段不覆盖。新增或修正元数据仅在 `ai4s_review.verified_metadata`。部分补回摘要为出版方索引片段，完整性与无效摘要剔除记录分别见相关质量附件；不能把非空文本数解释为完整摘要数。有效摘要仍缺失或AI作用无法确认时保留待定。公开PDF、代码、项目地址未查到的字段允许空缺。

WACV官网846条与快照845条确认缺CycleCL，已补入并排除；Nature目录、ACL论文集、AAMAS主会、IJCAI、KR、ICAPS、NSDI、OSDI及部分网络会议做了成员或轨道核对。USENIX Security官网417篇研究论文与快照存在附属会议混入及1条目录差异；MODELS companion与主会分别记录。Elsevier五刊的Crossref DOI集合与快照匹配，但不等于独立核实出版方完整TOC。其余受阻或未完成目录检查按未闭环保留。

## 共享词表

基于最新提交 `29b0431fc0fabc295722bf54c832e31ae55feaa0` 的61项词表，直接复用已有“卷积神经网络”“随机森林”等条目。新增7项后共68项：

- 演化优化 / Evolutionary optimization：通过种群、适应度选择及变异或重组等演化机制搜索科学或工程问题的解、程序、控制器或特征；包括遗传算法、遗传编程与差分进化。不因模拟生物演化现象本身而使用，也不将所有群智能或树搜索方法并入。
- 主题建模 / Topic modeling：以概率模型、潜变量或神经表征等方法从文档集合中估计潜在主题及其分布，用于科学领域的内容组织、比较或演变分析；不用于仅将已知类别监督分类或随意提及话题的论文。
- 循环神经网络 / Recurrent neural network：通过递归隐状态建模序列依赖的神经网络，包括LSTM和GRU；需实际用于论文方法。
- 神经微分方程 / Neural differential equation：以神经网络参数化微分方程的向量场或动力学，并通过微分方程演化实现预测、建模或控制；区别于以残差损失约束的普通PINN。
- 脉冲神经网络 / Spiking neural network：以离散脉冲事件和神经元时间动力学编码、传递与学习信息的神经网络，用于时序感知、科学测量或工程控制。
- 程序合成 / Program synthesis：依据规范、示例、约束或奖励信号自动构造可执行程序；用于领域科学或工程任务时标注。
- 自动机学习 / Automata learning：从观测序列、查询或运行轨迹推断自动机或状态机，用于系统行为建模和验证。

新词条仅用于已有摘要证据的论文；未把LSTM/GRU、遗传算法等子类都当作泛类的同义词。旧有词条内容完整保留。

## 来源代码

j-0b805d1731, j-82b1ddfc1d, j-8d1b1806d8, uist, percom, icwsm, eccb, nrcardio, npjvaccines, j-dbcb0fcd74, j-ce9a52b1f6, acl, emnlp, icra, wacv, icaps, coling, iccv, kr, ijcai, aamas, naacl, ppsn, sensys, infocom, icnp, secon, iwqos, mobihoc, nsdi, acsac, srds, sp, dsn, ndss, usenix-security, pldi, lctes, models, icpc, saner, issre, ase, cc, icse, icsme, issta, osdi, ipmi

## 后续接续

先处理 `unreviewed.json` 中现有摘要，沿用本批快照与最新词表；爬取问题按用户要求暂缓。完成后重新合并全量审计与论文交付。当前提交不宣称49来源采集完整，也不宣称全量精筛完成。
