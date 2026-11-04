# AI4S 论文采集与精筛

2024 年使用 [14,126 篇初筛候选](metadata/2024/ai4s.json)，快照时间为北京时间 2026-11-04 20:34。批次和来源计数见 [snapshot.json](metadata/2024/snapshot.json)。

1. 按团队当期分工，用来源编号（论文 JSON 的 `venue`）找到自己负责的候选。使用 [AI4S 精筛技能](skills/ai4s-paper-review/SKILL.md) 逐篇判断、打标签并核对元数据。
2. 在 [刊会核验清单](reviews/venue-review.csv) 填写自己负责的来源和「是否建议纳入」列。核对期刊中科院分区和 CCF B 会议当届的正式长文与评审证据，见 [刊会核验规则](skills/ai4s-paper-review/references/venue-review.md)。
3. 对纳入论文核对 DOI、论文页、公开 PDF、代码和项目链接。按 [JSON 交付说明](skills/ai4s-paper-review/references/team-handoff.md) 每人交一个 `reviews/<批次>/<GitHub用户名>.json`。
4. 论文精筛完成后，提交本人论文 JSON 的 PR，写明负责人、批次、来源编号和纳入/排除/待定/未审篇数，提及 @Roman100021。刊会核验可以先单独提交。

## 核验完期刊或会议怎么提交

1. 打开 [刊会核验清单](reviews/venue-review.csv)，按来源编号（`source_code`）找到自己负责的行。在「是否建议纳入」填写「建议纳入」「暂缓纳入」「不建议纳入」或「待核实」。空白表示尚未填写。
2. 同一行填负责人（`owner`）、核验年份（`review_year`）、相应分区或等级、证据链接（`evidence_urls`）和理由（`rationale`）。例如，建议剔除时填写「不建议纳入」，并写明具体问题和可核查的出处。
3. 在 GitHub 编辑该 CSV，将修改提交到个人分支。没有仓库写权限时可先 fork。发起合并到本仓库 `main` 的 PR，标题写「刊会核验 + GitHub 用户名」，正文列出来源编号并提及 @Roman100021。只改本人负责的行，核验完成即可提交。

[2024 原始书目](metadata/2024/papers.json) 使用 Git LFS，可用 `git lfs pull --include="metadata/2024/papers.json"` 取回。各年份的元数据都在 [metadata](metadata/) 下。运行说明见 [CRAWLER.md](CRAWLER.md)，来源配置见 [teacher_sources.json](teacher_sources.json)。
