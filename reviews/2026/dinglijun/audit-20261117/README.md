# 审计文件说明

本目录只涉及丁利军2026年的49个分工来源。交付结果和逐来源统计见[report.md](report.md)，最终逐篇结论在`reviews/2026/dinglijun.json`。候选文件含纳入及尚未解决的原候选；导出最终纳入集应读取`ai4s_review.decision == "include"`。

- `baseline.json`锁定输入提交、分工来源、原始数量和文件哈希；`provenance.json`记录最后核对的主分支、规则及词表版本。
- `bibliography-changes.json`记录933条全量补采。IJCAI补采的是官方编号0620的1篇，并非620篇。
- `semantic-group*.json`、`semantic-ijcai.json`及`semantic-parser-audit.json`为逐篇语义账；`semantic-root-adjudications.json`为最终交叉复核的覆盖修正。
- `semantic-decisions.json`为早期小样本试审记录，已被分组全量审核覆盖，不参与最终构建。
- `bibliography-discrepancy-reconciliation.json`记录89条2027卷期文献的首发日期核验。36条确认2026首发，53条证据不足；首发年份未核实的科学AI论文也暂停2026纳入。
- `enrichment-*.json`记录正式摘要、作者关键词、版本和资源链接等补证。`metadata-corrections.json`记录本轮字段更正，原有值保留在全量记录的`raw_metadata_before_dinglijun_review`中。
- `quality-audit-*-final*.json`为最后独立范围复核；最终修正由root覆盖文件及构建脚本执行，原审核轨迹不被抹去。
- `public-pdf-candidates.json`记录已有的DOI/题名匹配链接；首次与分区检查的尝试记录均保留。公开PDF仅在实际PDF响应验证后进入`verified_metadata.pdf_url`；失败、HTML响应和作者稿版本不会被改写为正式公开版。
- `paper-link-*.json`区分作者声明、将来发布、可访问状态和已验证下载，HTTP成功不证明数据内容可下载。
- `validation.json`检查范围、原记录及原字段保留、全部纳入摘要、双语标签、公开PDF证据、原候选审核覆盖，以及其他负责人的年度论文对象和快照来源项不变。

原始响应保存在`raw-fetch-evidence.tar.gz`和`citation-and-link-evidence.tar.gz`，完整工作清单保存在`worklist.json.gz`。每个压缩包仅含本目录相对路径，哈希和内容校验见归档清单。正常请求的失败也保留，不据此宣称官网不存在相关论文。

如需在同一输入版本复核，可在本目录解压两个证据包及`worklist.json.gz`，从仓库目录运行`python3 reviews/2026/dinglijun/audit-20261117/scripts/dinglijun_2026_finalize.py check`。`build`会重建本人的审核、反馈和元数据；`dinglijun_2026_validate.py <核对主分支提交>`执行独立校验。脚本不构造新的语义判断，读取已完成的逐篇审核账与原始证据。
