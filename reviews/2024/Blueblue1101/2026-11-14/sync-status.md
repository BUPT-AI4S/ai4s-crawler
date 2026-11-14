# GitHub与监控数据发布记录

本轮复核和汇报已推送至GitHub main，监控数据生成与网站发布任务均成功。

- 数据提交：[1db9a4b](https://github.com/BUPT-AI4S/ai4s-crawler/commit/1db9a4ba4168e452d9d770ac36fb0ade97f569fd)。
- 监控汇总生成：[成功任务](https://github.com/BUPT-AI4S/ai4s-crawler/actions/runs/43581424638)。
- 网站构建与发布：[成功任务](https://github.com/BUPT-AI4S/BUPT-AI4S.github.io/actions/runs/43581486569)，2026-11-14 09:40:43 UTC完成。
- 已独立请求并验证仓库主数据与网站备用快照，均为49个来源、纳入1863、排除19260、待定1152、官网总数未知33、候选待补摘要0。完整结果见[live-verification.json](live-verification.json)。

主数据生成于2026-11-14 09:38:18 UTC；备用快照生成于09:39:42 UTC。

## 浏览器显示核对

内置浏览器刷新及新开标签后，仍显示08:53:07 UTC生成的旧快照（a9d81882c583），与直接请求的两份最新线上数据不一致。具体缓存环节未确认，不能把服务器数据核验写成浏览器显示已更新。若监控页仍显示官网未知35个或待定1232条，请核对页面顶部生成时间；本轮正确值为33个和1152条。

本次没有修改监控页面代码，也没有隐藏真实待办。
