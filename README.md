# AI4S 论文采集与精筛

本仓库按**来源和年份**采集论文并开展 AI4S 精筛。各年份遵循相同流程；每次任务使用该年份最新确认的来源清单、负责人分工和采集快照，不把其他年份的分工或统计直接套用过来。[论文采集与审核监控](https://bupt-ai4s.github.io/review-monitor.html)自动发现已上传候选文件或快照的年份；缺少快照时仍展示候选，采集总数标为未知。

1. **确认来源和分工。** 查看目标年份的 `reviews/source-assignments-<年份>.json` 或团队明确提供的最新分工表；来源已移出清单时不再分配。相应年份的清单或负责人尚未确认时，先核实再处理。刊会核验结论及依据记录在[刊会核验清单](reviews/venue-review.csv)，核验方式见[刊会核验规则](skills/ai4s-paper-review/references/venue-review.md)。
2. **核对采集与候选。** 用来源编号和年份找到该来源全量书目、AI4S 初筛候选及采集快照，对照官网核对总数时注明相同的统计口径。摘要缺漏只统计 AI4S 候选；候选文件未取得时记为未知。
3. **负责人各自精筛。** 每位同学使用自己的 Agent，按 [AI4S 论文审核 skill](skills/ai4s-paper-review/SKILL.md) 处理本人负责的来源。对纳入论文核对 DOI、论文页、公开 PDF、代码和项目链接。按[交付说明](skills/ai4s-paper-review/references/team-handoff.md)保留原字段并追加 `ai4s_review`。
4. **提交并反馈。** 每人将论文数组提交至 `reviews/<年份>/<GitHub用户名>.json`；按[统一阶段反馈规范](skills/ai4s-paper-review/references/monitor-feedback.md)将各来源进展提交至 `reviews/<年份>/feedback/<GitHub用户名>.json`。拉取 `reviews/<年份>/actions/<负责人>.md` 查看个人行动清单。不存在的年份分工或清单需先确认，不视为已完成。

## 刊会核验提交

在[刊会核验清单](reviews/venue-review.csv)按 `source_code` 查找本人负责的来源，填写结论、负责人、核验年份、评级、证据链接和理由；空白表示未填写。只修改自己负责的行，结论及其适用范围以目标年份的最新确认情况为准。刊会核验可单独提交。

## 文件与运行

各年份的全量书目、初筛候选及采集快照分别位于 `metadata/<年份>/papers.json`、`metadata/<年份>/ai4s.json` 和 `metadata/<年份>/snapshot.json`。各来源按 `metadata/<来源编号>/<年份>/` 存放，实际覆盖以仓库文件和快照为准。部分文件使用 Git LFS，需要时针对目标年份执行 `git lfs pull --include="metadata/<年份>/*,metadata/*/<年份>/*"`。采集运行说明见 [CRAWLER.md](CRAWLER.md)。
