# 本地待上传包

用户已恢复浏览器登录；GitHub CLI 新增授权仍待确认，本包没有上传，主任务的全量漏筛检查也尚未全部完成。请先阅读`work-report.md`。

- `repository-files/` 按仓库根目录结构组织。个人论文结果为 `reviews/2024/Blueblue1101.json`；词表与核验材料也在相应目录。
- `reviews/2024/Blueblue1101/2026-11-07/summary.json` 和 `validation.json` 是最终统计与校验。
- `coverage.json` 按来源列已审/未审；`unreviewed.jsonl` 保留 19635 条续查记录；`full-corpus-audit.jsonl` 对全部 30468 条记录列明状态。
- `official-directory-audit.json` 明确区分完整、部分和未核验；`source-quality-audit.json` 保存既有来源核验依据。
- `abstract-backfill-europepmc.json` 是索引摘要补抓；`openaire-descriptions-to-check.json` 仍需内容检查。二者不代表其中每篇已完成精筛。
- `metadata-quality-audit.json` 内含中间审计及最终修复说明；最新计数以summary为准。
- `continuation-quality-rechecks.json` 记录合并前的边界复判和文献类型修复；各组 coverage 是交叉复核前的冻结记录，最终数量以 `summary.json`、`coverage.json` 及个人论文 JSON 为准。
- `checksums.json` 用于检验提交包文件完整性；《待提交说明.md》可用于恢复登录后的提交说明。

恢复上传时，先再次同步最新main并合并共享词表，再应用repository-files；只更新Blueblue1101个人文件、个人核验目录与共享词表，不覆盖其他人的文件。新增词项若届时已有同义项，按仓库规则合并。
