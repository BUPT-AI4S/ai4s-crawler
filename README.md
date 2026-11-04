# AI4S 论文采集与精筛

2024 年使用 [14,126 篇初筛候选](metadata/2024/ai4s.json)，快照时间为北京时间 2026-11-04 20:34。批次和来源计数见 [snapshot.json](metadata/2024/snapshot.json)。

1. 按团队当期分工，用来源编号（论文 JSON 的 `venue`）找到自己负责的候选。使用 [AI4S 精筛技能](skills/ai4s-paper-review/SKILL.md) 逐篇判断、打标签并核对元数据。
2. 在 [刊会核验清单](reviews/venue-review.csv) 填写自己负责的来源。核对期刊中科院分区和 CCF B 会议当届的正式长文与评审证据，见 [刊会核验规则](skills/ai4s-paper-review/references/venue-review.md)。
3. 对纳入论文核对 DOI、论文页、公开 PDF、代码和项目链接。按 [JSON 交付说明](skills/ai4s-paper-review/references/team-handoff.md) 每人交一个 `reviews/<批次>/<GitHub用户名>.json`。
4. 将本人核验行和论文 JSON 放入同一个 PR，写明负责人、批次、来源编号和纳入/排除/待定/未审篇数，提及 @Roman100021。每人对自己提交的数据负责。

[2024 原始书目](metadata/2024/papers.json) 使用 Git LFS，可用 `git lfs pull --include="metadata/2024/papers.json"` 取回。各年份的元数据都在 [metadata](metadata/) 下。运行说明见 [CRAWLER.md](CRAWLER.md)，来源配置见 [teacher_sources.json](teacher_sources.json)。
