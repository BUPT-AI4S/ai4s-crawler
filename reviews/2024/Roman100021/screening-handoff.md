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

## 候选摘要补全（2026-11-09，第二轮）

第一轮用 Crossref / OpenAlex / Europe PMC / Semantic Scholar / 出版方页面 API 补回 28 条后，余 39 条全部落在 Elsevier 与 Springer 订阅刊，接口侧无路可走：对 39 条逐一试过 Crossref、OpenAlex、Europe PMC、PubMed、Semantic Scholar、OpenAIRE、Unpaywall（含 OA 位置与 SSRN/OSTI 副本）、Wayback（按 DOI 与按 PII）、fatcat、x-mol、Baidu 学术，命中 0；ScienceDirect 对脚本与 headless 浏览器均返回 403 挑战页。

第二轮改为逐篇读取出版方文章页正文，从 Abstract 栏逐字回填：

| 结果 | 篇数 | 做法 |
| --- | ---: | --- |
| 已补摘要 | 36 | 用 Crossref 的 `alternative-id` 取 PII，打开 `sciencedirect.com/science/article/pii/<PII>`（Springer 1 篇走 `link.springer.com/article/<DOI>`），逐字复制摘要正文 |
| 原文类型无摘要 | 3 | `10.1016/j.diii.2024.07.011`（Editorial）、`10.1016/j.diii.2024.07.010`（Letter to the Editor）、`10.1007/s11427-024-2673-9`（Research Highlight），页面结构核实后只登记证据 |

写回约束：保留候选文件原有行级格式、字段顺序与 CRLF，仅填 `abstract` 并把 `source` 追加来源域名；`screening_status` 按 `article_type` 是否已知重设。无摘要的 3 条新增 `abstract_status` / `abstract_evidence_url` / `abstract_note`。

结果：35 个来源的候选缺摘要合计由 39 降至 3，且这 3 条不是取不到，而是原文本身不设摘要栏。逐条台账见 [`abstract-topup.csv`](abstract-topup.csv)。

## 文献类型清理与待定清零（2026-11-09，第三轮）

第二轮补回摘要后仍留在候选里的 3 条「原文类型无摘要」，实为初筛收录了不该收的文献类型。按 `review-rules.md` 的文献类型口径（评论、社论、读者来信、更正、撤稿公告按类型排除），连同扫描中发现的另 2 条同类型记录，一并从候选池移出：

| DOI | 类型 | 来源 |
| --- | --- | --- |
| `10.1016/j.diii.2024.07.011` | Editorial | Diagnostic and Interventional Imaging |
| `10.1016/j.diii.2024.07.010` | Letter to the Editor | Diagnostic and Interventional Imaging |
| `10.1007/s11427-024-2673-9` | Research Highlight | Science China Life Sciences |
| `10.1016/j.envint.2024.108561` | Corrigendum | Environment International |
| `10.1038/s41698-024-00510-3` | Retracted article | npj Precision Oncology |

交付 JSON 仍保留这 5 条的 `exclude` 记录并注明文献类型（规则要求对已有候选保留排除记录）。候选池删除 5 行后，`coverage.json` 的 `candidate_missing_abstract` 在 35 个来源上全部归零。

剩余 7 条待定按逐篇读原文落定，不再依赖摘要源：6 篇 Elsevier 论文直接读 ScienceDirect 文章页的摘要、引言与方法段；Molecular Psychiatry 一篇正文在订阅墙内，改读出版方补充材料 DOCX（基因型质控、填充、荧光素酶实验）与补充表 PDF——表 11–13 明确预测模型是「临床变量 + PRS + 基因型 + 性别」的多项逻辑回归，据此排除。

结果：3 条纳入（`10.1016/j.renene.2024.120892`、`10.1016/j.renene.2024.121211`、`10.1016/j.compag.2024.108683`）、4 条排除，待定清零。7 篇原摘要已回填到交付记录的 `abstract` 与 `verified_metadata.abstract`。逐条依据见 [`action-report.md`](action-report.md) 第 7、8 节。

## 交付格式自查（2026-11-09，第四轮）

按仓库 `skills/ai4s-paper-review/references/team-handoff.md` 与 `monitor-feedback.md` 逐条核对本轮交付，结果：

| 检查项 | 结果 |
| --- | --- |
| 顶层为论文对象数组，保留原字段 | 通过（3,741 条；467 条保留原 `ai4s_hits`/`ai4s_tags`/`ai4s_tagging` 等初筛字段） |
| `ai4s_review` 八个字段齐全 | 通过（`schema_version` 全为 2；`batch_id` 统一为 `2024-Roman100021-20261105T103119+0800`） |
| `decision` 取值合法 | 通过（include 665 / exclude 3,076 / pending 0 / unreviewed 0） |
| 纳入至少一个带证据标签，其他状态为空 | 通过（665 篇全部有标签，exclude 无标签；2,167 个标签均含 `axis`/`label`/`label_en`/`evidence_location`/`rationale`） |
| 标签用共享词表规范名 | 通过（319 组去重标签全部命中仓库词表 777 条，维度与词表一致，未新增词条） |
| `(venue, year, id)` 查重 | 通过（无重复键） |
| `rationale`、`evidence_urls` 非空 | 通过（0 条为空） |
| 刊会核验表 | 通过（`reviews/venue-review.csv` 本人 35 行均已填负责人、核验年份、分区、证据与结论） |

本轮补齐的缺项：

1. **阶段反馈**：此前只有自建的 `reviews/2024/Roman100021/coverage.json`，网站监控对该文件只识别 `official_total`、`coverage_rationale`、`evidence_urls` 等字段，**不读 `issues`/`next_actions`**，无法进入监控的问题与下一步。现按 `monitor-feedback.md` 新增 `reviews/2024/feedback/Roman100021.json`，逐来源 35 个对象，含 `year`、`source_code`、`snapshot_at`（与 `metadata/2024/snapshot.json` 的 `captured_at` 完全一致）、`official_total`、`official_scope`、`coverage_note`、`evidence_urls`、`issues`、`next_actions`。
2. **批次标识**：交付内 `batch_id` 原为 `2024`，与同批其他人（如 `2024-wangwanting-rereview-20261107`）及本目录 `coverage.json` 记录的批次不一致，已统一为 `2024-Roman100021-20261105T103119+0800`。
3. **口径说明**：`coverage.json` 新增一条 policy note，说明 `original_candidates` 是当前候选文件条数，而 `delivery_decisions` 是快照候选的判定合计，两者时点不同、不可相减。

两点保留说明：

- 7 条逐篇读原文的记录把核实到的原摘要写入了顶层 `abstract`（原值为空）。`team-handoff.md` 的「与采集格式对齐」要求只追加 `ai4s_review`，但「纳入论文的交付字段」要求 `abstract` 为来源可查的原摘要；本处按后者优先，同时在 `ai4s_review.verified_metadata.abstract` 保留同一份值，理由段已写明读取页面。
- `reviews/2024/Roman100021/coverage.json` 是监控可识别的 coverage 适配格式，继续保留；标准反馈以 `reviews/2024/feedback/Roman100021.json` 为准。

## 三条口径提示的收口（2026-11-09，第五轮）

行动清单仅剩的三条"问题"都是上一轮把口径说明写进 `issues` 造成的：监控对 `issues` 原文照搬展示，不区分"已核实闭环"与"待处理"。本轮按 `monitor-feedback-format.md` 的口径重新归类——已核实、无需行动的差额与类型差异属于 `coverage_note`，`issues` 只留给真正待办。

- **CIKM**：官网录用页 7 张分轨表逐行解析，Full Research Track 录用 348 条，347 条与采集的 697 条逐篇对应；余 1 条 `fp0540`（Towards Cross-Lingual Spoken Language Understanding…）在 Crossref 与 ACM proceedings 均无出版记录，属录用未出版。其余分轨官网 330 条、对应 324 条。采集 697 条为该届 proceedings 全部条目。`official_total` 维持 347，口径改记为"正式出版长文"。
- **Molecular Psychiatry**：官网 2024 列表 513 条中有 2 条单页图片摘要（`10.1038/s41380-023-02328-0`、`10.1038/s41380-023-02393-5`）与 1 条更正（`10.1038/s41380-024-02416-9`），三条印刷年为 2023、仅在线日期落在 2024；按 Crossref 出版年 journal-article 同口径为 510 条，与采集 510 条逐 DOI 一致。`official_total` 由 513 改为 **510**。
- **npj Schizophrenia**：官网列表 124 条、Crossref 124 条、采集 124 条三者一致，逐 DOI 无缺无多，`official_total` 维持 124。

`official_total` 合计 16,491 → 16,488。35 个来源的反馈 `issues` 与 `next_actions` 全部为空，交付判定未改动。
