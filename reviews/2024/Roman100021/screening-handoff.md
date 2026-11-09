# 乔徐阳 · 2024 年 AI4S 精筛复查

补摘要、人工漏筛复查和最新统计见[精筛说明](screening-report.md)。本文保留首次复查的范围和刊会对账。

- 分工依据为《AI4S会议期刊爬取清单_2020-2026_仅建议纳入 (7).xlsx》负责人列，范围为 34 本期刊和 CIKM。以仓库 README 当前指定的 2024 批次为准。采集快照时间为北京时间 2026-11-05 10:31:19。
- 使用 GitHub main 提交 `373425af4e4ab743d3c298b185599559fa95a5b0` 的 [AI4S 精筛技能](../../../skills/ai4s-paper-review/SKILL.md)、[双语词表](../../../skills/ai4s-paper-review/references/tag-vocabulary.json)和[初筛词表](../../../ai4s_keywords.txt)。标签按维度对照规范中英文，未新增共享词条。
- 复查快照候选 467 条，纳入 306 条、排除 112 条、待定 49 条。另补录 82 条已采集但旧初筛漏掉的研究。交付共 549 条，纳入 388 条、排除 112 条、待定 49 条、未审 0 条。
- 期刊沿用已有分区与同行评审证据，按新分工逐篇复查。期刊纳入限有实质学术内容的原创研究和综述。单篇须有理工或医学研究问题，AI 须实际用于方法、分析或评测。评论、社论、来信、更正及撤回研究排除。仅题名相关但查不到可判定的摘要或原文段落，记录为待定。
- CIKM 核对 CCF B（2026-v7）。程序主席报告 2024 年 Full Research Track 收稿 1,496 篇、录用 347 篇，约 23.2%。只纳入此分轨内且通过 AI4S 精筛的论文。78 条原候选中 42 条属正式长文，另外 36 条属其他分轨。全量快照 697 条跨分轨论文中，347 条与正式长文录用目录题名匹配。网站初始录用目录列 348 条长文，其中 fp0540 未在正式 DBLP 目录定位，且题名是通用语音理解；以程序主席正式统计为准。[CCF 目录](https://www.ccf.org.cn/Academic_Evaluation/By_category/2026-03-31/870181.shtml) · [程序主席前言](https://research.tudelft.nl/files/235862358/3627673.fm.pdf) · [ACM 论文集](https://dl.acm.org/doi/proceedings/10.1145/3627673) · [会议录用目录](https://cikm2024.github.io/accepted-papers/) · [DBLP 分轨目录](https://dblp.org/db/conf/cikm/cikm2024.html)
- **The Lancet 合并冲突。** 新分工将本刊交给乔徐阳，仓库的 `nydiii.json` 已有同三个键。此次复查认为全球生育率预测属于人口学，排除 `10.1016/S0140-6736(24)00550-6`；另两篇关于死亡率和肥胖流行率的医学研究纳入。合并前须确认三条的负责人并去重。旧负责人的文件保留在主分支。[生育率论文](https://pubmed.ncbi.nlm.nih.gov/38521087/)

## 官网与摘要覆盖

对账范围为分工内全部 16,838 条采集记录，缺摘要 9,867 条。原候选缺摘要 67 条。缺口集中在数本工程期刊和 The Lancet，按下表记录。原候选缺摘要条目用已核实的补充摘要、正式论文页或公开正文查证，证据仍不足的保留待定。初筛快照统计以原摘要为准，补证不会改动原字段。

2026-11-07 核对出版方正式目录。Nature 的 15 本期刊可计数，使用官网 2024 年发表日期列表，含其各文章类型。合计相同只说明数量一致；未逐个 DOI 对账的刊物仍可能有个别漏项。Molecular Psychiatry 26 页逐条核对，目录多出的三条为图片 `10.1038/s41380-023-02393-5`、`10.1038/s41380-023-02328-0` 和更正 `10.1038/s41380-024-02416-9`，不补录。卷期索引可访问但总量口径未对齐，或访问返回 403 的来源，官网同口径总量列为无法核实。

| 来源 | 全量 | 缺摘要 | 原候选 | 候选缺摘要 | 官网条目与口径 | 纳入 | 排除 | 待定 | 补录 |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| The Lancet（`j-010bbc0bbc`） | 1748 | 1679（96.1%） | 3 | 0（0.0%） | [无法核实](https://www.sciencedirect.com/journal/the-lancet/issues)，HTTP 403 | 2 | 1 | 0 | 0 |
| Diagnostic and Interventional Imaging（`j-40f01ce1e2`） | 94 | 94（100.0%） | 3 | 3（100.0%） | [无法核实](https://www.sciencedirect.com/journal/diagnostic-and-interventional-imaging/issues)，HTTP 403 | 0 | 3 | 0 | 0 |
| Microsystems & Nanoengineering（`nature-micronano`） | 207 | 0（0.0%） | 5 | 0（0.0%） | [207](https://www.nature.com/micronano/articles?year=2024)，差 +0 | 7 | 2 | 0 | 4 |
| Materials Today Bio（`j-2e7e0743f5`） | 478 | 379（79.3%） | 1 | 0（0.0%） | [无法核实](https://www.sciencedirect.com/journal/materials-today-bio/issues)，HTTP 403 | 2 | 0 | 0 | 1 |
| npj Clean Water（`npjcleanwater`） | 133 | 3（2.3%） | 7 | 0（0.0%） | [133](https://www.nature.com/npjcleanwater/articles?year=2024)，差 +0 | 9 | 1 | 0 | 3 |
| npj Urban Sustainability（`npjurbansustain`） | 52 | 3（5.8%） | 2 | 0（0.0%） | [52](https://www.nature.com/npjurbansustain/articles?year=2024)，差 +0 | 1 | 1 | 0 | 0 |
| Genome Medicine（`j-128792d050`） | 154 | 24（15.6%） | 12 | 0（0.0%） | [无法核实](https://genomemedicine.biomedcentral.com/articles?year=2024)，目录范围未对齐 | 13 | 0 | 0 | 1 |
| Acta Materialia（`j-e85da65425`） | 893 | 873（97.8%） | 15 | 14（93.3%） | [无法核实](https://www.sciencedirect.com/journal/acta-materialia/issues)，HTTP 403 | 2 | 0 | 13 | 0 |
| Cell Death Discovery（`nature-cddiscovery`） | 513 | 6（1.2%） | 1 | 0（0.0%） | [513](https://www.nature.com/cddiscovery/articles?year=2024)，差 +0 | 1 | 0 | 0 | 0 |
| Molecular Psychiatry（`nature-mp`） | 510 | 179（35.1%） | 14 | 1（7.1%） | [513](https://www.nature.com/mp/articles?year=2024)，差 +3 | 12 | 4 | 0 | 2 |
| Computers and Electronics in Agriculture（`j-6c033988ef`） | 1117 | 934（83.6%） | 49 | 14（28.6%） | [无法核实](https://www.sciencedirect.com/journal/computers-and-electronics-in-agriculture/issues)，HTTP 403 | 59 | 0 | 14 | 24 |
| International Journal of Computer Vision（`j-fe8a45e725`） | 356 | 295（82.9%） | 6 | 2（33.3%） | [无法核实](https://link.springer.com/journal/11263/volumes-and-issues)，目录范围未对齐 | 5 | 4 | 0 | 3 |
| Environment International（`j-637d3c6893`） | 834 | 30（3.6%） | 21 | 0（0.0%） | [无法核实](https://www.sciencedirect.com/journal/environment-international/issues)，HTTP 403 | 17 | 8 | 0 | 4 |
| Mechanical Systems and Signal Processing（`j-3b179d0686`） | 836 | 794（95.0%） | 19 | 16（84.2%） | [无法核实](https://www.sciencedirect.com/journal/mechanical-systems-and-signal-processing/issues)，HTTP 403 | 18 | 0 | 8 | 7 |
| Nature Structural & Molecular Biology（`nsmb`） | 286 | 27（9.4%） | 2 | 0（0.0%） | [286](https://www.nature.com/nsmb/articles?year=2024)，差 +0 | 2 | 0 | 0 | 0 |
| Composites Science and Technology（`j-f339346c60`） | 502 | 491（97.8%） | 1 | 1（100.0%） | [无法核实](https://www.sciencedirect.com/journal/composites-science-and-technology/issues)，HTTP 403 | 2 | 0 | 0 | 1 |
| npj Precision Oncology（`npjprecisiononcology`） | 291 | 10（3.4%） | 46 | 0（0.0%） | [291](https://www.nature.com/npjprecisiononcology/articles?year=2024)，差 +0 | 57 | 1 | 0 | 12 |
| Science China Chemistry（`j-dbedd658b3`） | 501 | 325（64.9%） | 2 | 1（50.0%） | [无法核实](https://link.springer.com/journal/11426/volumes-and-issues)，目录范围未对齐 | 1 | 0 | 1 | 0 |
| npj Science of Food（`npjscifood`） | 116 | 5（4.3%） | 4 | 0（0.0%） | [116](https://www.nature.com/npjscifood/articles?year=2024)，差 +0 | 4 | 0 | 0 | 0 |
| npj Climate and Atmospheric Science（`npjclimatsci`） | 328 | 13（4.0%） | 31 | 0（0.0%） | [328](https://www.nature.com/npjclimatsci/articles?year=2024)，差 +0 | 30 | 2 | 0 | 1 |
| Science China Life Sciences（`j-dd56888193`） | 274 | 271（98.9%） | 1 | 1（100.0%） | [无法核实](https://link.springer.com/journal/11427/volumes-and-issues)，目录范围未对齐 | 0 | 1 | 0 | 0 |
| The Lancet Regional Health - Western Pacific（`j-cef98d1da3`） | 300 | 102（34.0%） | 1 | 0（0.0%） | [无法核实](https://www.sciencedirect.com/journal/the-lancet-regional-health-western-pacific/issues)，HTTP 403 | 3 | 0 | 0 | 2 |
| Communications Earth & Environment（`commsenv`） | 802 | 33（4.1%） | 40 | 0（0.0%） | [802](https://www.nature.com/commsenv/articles?year=2024)，差 +0 | 38 | 4 | 0 | 2 |
| Transportation Research Part E Logistics and Transportation Review（`j-69b4b3aecf`） | 363 | 346（95.3%） | 2 | 1（50.0%） | [无法核实](https://www.sciencedirect.com/journal/transportation-research-part-e-logistics-and-transportation-review/issues)，HTTP 403 | 1 | 0 | 1 | 0 |
| Developmental Cell（`j-f544c7a60d`） | 235 | 206（87.7%） | 1 | 0（0.0%） | [无法核实](https://www.cell.com/developmental-cell/issues)，HTTP 403 | 1 | 0 | 0 | 0 |
| Genome Biology（`j-b5cbe6c7c8`） | 324 | 26（8.0%） | 39 | 1（2.6%） | [无法核实](https://genomebiology.biomedcentral.com/articles?year=2024)，目录范围未对齐 | 38 | 3 | 0 | 2 |
| Oncogene（`nature-onc`） | 339 | 219（64.6%） | 2 | 0（0.0%） | [339](https://www.nature.com/onc/articles?year=2024)，差 +0 | 3 | 0 | 0 | 1 |
| Renewable Energy（`j-4a8bd2ddf7`） | 2148 | 1852（86.2%） | 24 | 12（50.0%） | [无法核实](https://www.sciencedirect.com/journal/renewable-energy/issues)，HTTP 403 | 18 | 2 | 12 | 8 |
| NPG Asia Materials（`nature-am`） | 63 | 0（0.0%） | 4 | 0（0.0%） | [63](https://www.nature.com/am/articles?year=2024)，差 +0 | 4 | 0 | 0 | 0 |
| npj Quantum Information（`npjqi`） | 136 | 5（3.7%） | 10 | 0（0.0%） | [136](https://www.nature.com/npjqi/articles?year=2024)，差 +0 | 3 | 7 | 0 | 0 |
| Alzheimer’s Research & Therapy（`j-d94e323c3b`） | 279 | 60（21.5%） | 10 | 0（0.0%） | [无法核实](https://alzres.biomedcentral.com/articles?year=2024)，目录范围未对齐 | 8 | 2 | 0 | 0 |
| Leukemia（`nature-leu`） | 369 | 194（52.6%） | 3 | 0（0.0%） | [369](https://www.nature.com/leu/articles?year=2024)，差 +0 | 2 | 1 | 0 | 0 |
| Transportation Research Part D Transport and Environment（`j-7a7c416cc3`） | 436 | 340（78.0%） | 3 | 0（0.0%） | [无法核实](https://www.sciencedirect.com/journal/transportation-research-part-d-transport-and-environment/issues)，HTTP 403 | 3 | 1 | 0 | 1 |
| Schizophrenia（`nature-npjschz`） | 124 | 13（10.5%） | 5 | 0（0.0%） | [124](https://www.nature.com/npjschz/articles?year=2024)，差 +0 | 5 | 1 | 0 | 1 |
| ACM International Conference on Information and Knowledge Management（`cikm`） | 697 | 36（5.2%） | 78 | 0（0.0%） | [正式长文 347](https://cikm2024.github.io/accepted-papers/)，同轨采集 347 | 17 | 63 | 0 | 2 |

## 漏筛补录与元数据

- 以 `(venue, year, id)` 将 16,838 条全量记录与 467 条原候选对照，对其余 16,371 条使用固定版本的初筛规则重跑，找出 57 条仅由新词表触发的记录。同时用标题、作者关键词和摘要中的方法线索生成 819 条优先检查清单，其中包括高优先级的 94 条有摘要且标题带方法线索的记录，以及 CIKM 的 6 条领域交叉样本。优先检查有正式摘要、技术路线明确的条目。初筛命中只用于定位论文。
- 确认补录 82 条，沿用全量快照记录的原始 ID 和字段，理由标记「初筛漏筛补录」，并保留 DOI 和证据链接。其余短名单、缺摘要非候选与无法对账的官方卷期仍可能有漏检，未计作已核实补录。
- 对新增纳入和补录的首批 95 个 DOI 查 Crossref 出版登记，89 个返回可用题名或作者信息。其余记录使用输入元数据和可核实的论文页、目录或摘要。保留上一轮已核实的公开 PDF 和项目链接，新增条目中无明确证据的 PDF、代码或数据字段留空。修正环境健康论文 `10.1016/j.envint.2024.108449` 的一条错链。
- 统计按原快照出版日期口径。`10.1007/s11263-024-02246-w` 与 `10.1038/s41380-024-02759-3` 首次正式在线发表于 2024 年，纸刊排于 2025 年，保留在本批次。

## 官网同口径总量复核（2026-11-09）

上一版表格中列为「无法核实」的来源，本轮按同一快照（2026-11-05T10:31:19）重新对账，逐来源口径、总数与差额写入 [`coverage.json`](coverage.json)。做法分两类：

- Nature 系 15 本期刊的 2024 年发表日期列表可整年枚举，逐页取全部文章链接后按 DOI 与采集结果比对，14 本零差，Molecular Psychiatry 官网多 3 条（两张图片摘要 `10.1038/s41380-023-02393-5`、`10.1038/s41380-023-02328-0` 与更正 `10.1038/s41380-024-02416-9`），不属研究条目，不补录。
- 其余期刊（Elsevier、Springer、BMC、Cell Press）的卷期目录与文章页对自动化访问返回 403，或只给卷期索引而无法枚举整年条目。改用出版方存缴的 Crossref 登记，按 ISSN、出版日 2024-01-01 至 2024-12-31、`type=journal-article` 统计。这正是采集器 `journal_meta.py` 使用的筛选条件，口径与全量采集完全一致，并已逐 DOI 比对：33 本期刊缺 0 条、多 0 条。出版方官网链接仍保留在 `coverage.json` 的 `evidence_urls` 中，供有订阅权限时复核。

| 来源 | 全量采集 | 官网同口径总数 | 差额 | 统计口径 | 证据 |
| --- | ---: | ---: | ---: | --- | --- |
| The Lancet（`j-010bbc0bbc`） | 1748 | 1748 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/0140-6736/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Diagnostic and Interventional Imaging（`j-40f01ce1e2`） | 94 | 94 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/2211-5684/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Microsystems & Nanoengineering（`nature-micronano`） | 207 | 207 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/micronano/articles?year=2024) |
| Materials Today Bio（`j-2e7e0743f5`） | 478 | 478 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/2590-0064/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| npj Clean Water（`npjcleanwater`） | 133 | 133 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/npjcleanwater/articles?year=2024) |
| npj Urban Sustainability（`npjurbansustain`） | 52 | 52 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/npjurbansustain/articles?year=2024) |
| Genome Medicine（`j-128792d050`） | 154 | 154 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/1756-994X/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Acta Materialia（`j-e85da65425`） | 893 | 893 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/1359-6454/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Cell Death Discovery（`nature-cddiscovery`） | 513 | 513 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/cddiscovery/articles?year=2024) |
| Molecular Psychiatry（`nature-mp`） | 510 | 513 | -3 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/mp/articles?year=2024) |
| Computers and Electronics in Agriculture（`j-6c033988ef`） | 1117 | 1117 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/0168-1699/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| International Journal of Computer Vision（`j-fe8a45e725`） | 356 | 356 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/0920-5691/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Environment International（`j-637d3c6893`） | 834 | 834 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/0160-4120/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Mechanical Systems and Signal Processing（`j-3b179d0686`） | 836 | 836 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/0888-3270/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Nature Structural & Molecular Biology（`nsmb`） | 286 | 286 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/nsmb/articles?year=2024) |
| Composites Science and Technology（`j-f339346c60`） | 502 | 502 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/0266-3538/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| npj Precision Oncology（`npjprecisiononcology`） | 291 | 291 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/npjprecisiononcology/articles?year=2024) |
| Science China Chemistry（`j-dbedd658b3`） | 501 | 501 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/1674-7291/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| npj Science of Food（`npjscifood`） | 116 | 116 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/npjscifood/articles?year=2024) |
| npj Climate and Atmospheric Science（`npjclimatsci`） | 328 | 328 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/npjclimatsci/articles?year=2024) |
| Science China Life Sciences（`j-dd56888193`） | 274 | 274 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/1674-7305/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| The Lancet Regional Health - Western Pacific（`j-cef98d1da3`） | 300 | 300 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/2666-6065/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Communications Earth & Environment（`commsenv`） | 802 | 802 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/commsenv/articles?year=2024) |
| Transportation Research Part E Logistics and Transportation Review（`j-69b4b3aecf`） | 363 | 363 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/1366-5545/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Developmental Cell（`j-f544c7a60d`） | 235 | 235 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/1534-5807/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Genome Biology（`j-b5cbe6c7c8`） | 324 | 324 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/1474-760X/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Oncogene（`nature-onc`） | 339 | 339 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/onc/articles?year=2024) |
| Renewable Energy（`j-4a8bd2ddf7`） | 2148 | 2148 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/0960-1481/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| NPG Asia Materials（`nature-am`） | 63 | 63 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/am/articles?year=2024) |
| npj Quantum Information（`npjqi`） | 136 | 136 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/npjqi/articles?year=2024) |
| Alzheimer’s Research & Therapy（`j-d94e323c3b`） | 279 | 279 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/1758-9193/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Leukemia（`nature-leu`） | 369 | 369 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/leu/articles?year=2024) |
| Transportation Research Part D Transport and Environment（`j-7a7c416cc3`） | 436 | 436 | +0 | Crossref 出版登记：ISSN + 2024 出版年 + journal-article（与采集器同口径） | [目录](https://api.crossref.org/journals/1361-9209/works?filter=from-pub-date:2024-01-01,until-pub-date:2024-12-31,type=journal-article) |
| Schizophrenia（`nature-npjschz`） | 124 | 124 | +0 | 官网 2024 年发表日期列表全部条目（含非研究条目） | [目录](https://www.nature.com/npjschz/articles?year=2024) |
| ACM International Conference on Information and Knowledge Management（`cikm`） | 697 | 347 | +350 | Full Research Track 正式长文录用数（不含其他分轨） | [目录](https://cikm2024.github.io/accepted-papers/) |

CIKM 的 +350 来自口径差异：全量采集 697 条覆盖该届全部分轨，正式长文同轨记录 347 条与官方录用数一致，已在 `coverage.json` 的 `coverage_rationale` 中写明。所有差额均为口径差异或非研究条目，未发现需补采的 AI4S 论文。
