# AI4S 论文采集与精筛

2024 年使用 [15,352 篇初筛候选](metadata/2024/ai4s.json)，快照时间为北京时间 2026-11-05 10:31。批次和来源计数见 [snapshot.json](metadata/2024/snapshot.json)。

1. **先核验期刊和会议。** 按团队分工在 [刊会核验清单](reviews/venue-review.csv) 填写「是否建议纳入」，并记录依据。期刊核对中科院分区，CCF B 会议核对当届正式长文和评审证据。结论为「不建议纳入」的来源，直接跳过该来源的论文精筛和打标。「暂缓纳入」或「待核实」的来源，等结论明确后再处理。见 [刊会核验规则](skills/ai4s-paper-review/references/venue-review.md)。
2. **只精筛「建议纳入」来源的论文。** 用来源编号（论文 JSON 的 `venue`）找到候选，使用 [AI4S 精筛技能](skills/ai4s-paper-review/SKILL.md) 逐篇判断、打标签并核对元数据。
3. 对纳入论文核对 DOI、论文页、公开 PDF、代码和项目链接。按 [JSON 交付说明](skills/ai4s-paper-review/references/team-handoff.md) 每人交一个 JSON。2024 年的文件放到 [reviews/2024/](reviews/2024/)，命名为 `<GitHub用户名>.json`。后续年份按 `reviews/<年份>/` 存放。
4. 论文精筛完成后，将本人论文 JSON 提交到仓库，并在提交说明中写明负责人、批次、来源编号和纳入/排除/待定/未审篇数。刊会核验可以先单独提交。

## 核验完期刊或会议怎么提交

1. 打开 [刊会核验清单](reviews/venue-review.csv)，按来源编号（`source_code`）找到自己负责的行。在「是否建议纳入」填写「建议纳入」「暂缓纳入」「不建议纳入」或「待核实」。空白表示尚未填写。
2. 同一行填负责人（`owner`）、核验年份（`review_year`）、相应分区或等级、证据链接（`evidence_urls`）和理由（`rationale`）。例如，建议剔除时填写「不建议纳入」，并写明具体问题和可核查的出处。
3. 保存 CSV 后提交并推送到仓库，也可以在 GitHub 网页直接编辑提交。提交标题写「刊会核验 + GitHub 用户名」，提交说明列出来源编号。只改本人负责的行，核验完成即可提交。

[2024 原始书目](metadata/2024/papers.json) 使用 Git LFS，可用 `git lfs pull --include="metadata/2024/papers.json"` 取回。各年份的元数据都在 [metadata](metadata/) 下。2024 年的 436 本期刊另按来源编号存放在 `metadata/<来源编号>/2024/`，每刊提供全量书目 `papers.json` 和初筛候选 `ai4s.json`。分刊文件与年度汇总使用同一快照。运行说明见 [CRAWLER.md](CRAWLER.md)，来源配置见 [teacher_sources.json](teacher_sources.json)。

2026 年的 [全量书目](metadata/2026/papers.json) 共 367,930 篇，[初筛候选](metadata/2026/ai4s.json) 共 29,342 篇。年度文件已并入早期顶会，逐来源结果在 `metadata/<来源编号>/2026/`。各来源覆盖情况、摘要计数和词表版本见 [2026 快照](metadata/2026/snapshot.json)。下载通过 LFS 保存的 2026 文件可运行 `git lfs pull --include="metadata/2026/*,metadata/*/2026/*"`。精筛范围仍以团队的刊会核验结论为准。
