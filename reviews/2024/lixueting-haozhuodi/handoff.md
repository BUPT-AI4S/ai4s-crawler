# 2024 年论文摘要复核

李雪婷负责 51 个来源，郝卓迪负责 50 个来源。本轮从[上一批交付](https://github.com/BUPT-AI4S/ai4s-crawler/blob/e41587b9271028183191e2395146ec7904f56041/reviews/2024/lixueting-haozhuodi/handoff.md)中取出 2,398 条缺摘要待定记录、218 条判定分歧记录，两组没有重复。

## 缺摘要的 2,398 条

| 负责人 | 已查 | 发表记录摘要 | 作者预印本 | 机构存档摘要 | 作者公开摘要链接 | 无摘要、按文献类型排除 | 仍缺摘要待定 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 李雪婷 | 1055 | 5 | 0 | 2 | 0 | 251 | 797 |
| 郝卓迪 | 1343 | 3 | 16 | 1 | 1 | 390 | 932 |

8 份发表记录摘要包括 6 篇正式会议论文和 2 条 PubMed 发表记录。另存 16 份有发表 DOI 对应关系的预印本摘要和 3 份机构存档摘要，均注明版本和来源。1 篇教育测评论文保留了作者公开原摘要的链接及中文核读记录。

这 28 篇中纳入 3 篇，排除 24 篇，1 篇读过摘要后仍待定。另有 641 条通过出版栏目、撤稿标记、评论关系或会议摘要编号等正式文献类型证据排除。其余 1,729 条缺少可核实的完整文字摘要，继续保留待定。

在 2,396 条有 DOI 的记录上核对出版商向 Crossref 登记的元数据，并检查 Europe PMC、OpenAlex、OpenAIRE、DataCite 等索引。对能定位到的 PMID、出版社、会议、预印本和机构存档再核对原始摘要字段。两条无 DOI 的 ECCV 记录通过 ECVA 论文集找回。ISBI 通过正式日程中的投稿编号匹配论文集，提取四篇论文首页标明的 ABSTRACT。检索日志逐条区分无匹配、空字段与访问受限。

## 有分歧的 218 条

| 负责人 | 逐篇核对 | 纳入 | 排除 | 待定 | 修改本组原判 | 复核后与对方原判一致 |
|---|---:|---:|---:|---:|---:|---:|
| 李雪婷 | 140 | 96 | 23 | 21 | 125 | 112 |
| 郝卓迪 | 78 | 58 | 16 | 4 | 63 | 56 |

[逐篇分歧与理由](disagreement-adjudications.json)列出双方原判、原理由、复核决定、摘要证据句及出处。218 条中，本组修改 188 条。168 条现与对方原判一致，另有 50 条仍不一致，其中 30 条维持本组原判，20 条改为双方原判以外的状态。这里的一致性比较使用上一提交中的对方记录。

## 两份交付 JSON

| 负责人 | 交付记录 | 累计纳入 | 交付中排除 | 交付中待定 |
|---|---:|---:|---:|---:|
| [李雪婷](../zch66883-lixueting.json) | 3713 | 2036 | 743 | 934 |
| [郝卓迪](../zch66883-haozhuodi.json) | 2620 | 934 | 689 | 997 |

交付保留原候选、此前的补录和本轮要求复查的全部记录。使用 `ai4s_review.decision == "include"` 可取得最终纳入集。原始采集字段保留，新增摘要及证据链接在 `ai4s_review.verified_metadata` 中。发表记录原摘要、作者预印本和机构存档分别存入 `abstract`、`author_version_abstract` 和 `repository_abstract`。作者公开页面留有 `abstract_url` 与 `abstract_summary_zh`。

本轮使用[共享词表](https://github.com/BUPT-AI4S/ai4s-crawler/blob/e41587b9271028183191e2395146ec7904f56041/skills/ai4s-paper-review/references/tag-vocabulary.json)中的既有中英文标签，新增 0 项。AI4S 相关性均按摘要判断；文献类型与版本归属使用出版、会议和索引元数据。

### 核验文件

- [缺摘要复查逐条日志，2,398 条](abstract-gap-recheck.jsonl.gz)
- [累计摘要补充](verified-abstract-updates.jsonl.gz) · [尚无可用摘要的记录及其状态](abstract-gaps.jsonl.gz)
- [全量判定台账，58,259 条](full-corpus-decisions.jsonl.gz) · [按来源统计](coverage.csv)
- [重叠判定现状](overlapping-reviews.jsonl.gz) · [漏采补录](verified-catalogue-additions.jsonl.gz)
- [统计与版本](manifest.json) · [验证结果](validation.json)
