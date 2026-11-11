# 来源、修改与许可证

- 代码来源：https://github.com/sunsz/ha-shenzhen-gas
- 基准提交：`9693b16fabde6bc69b2b9077b9b1f6183bf3803d`；上游署名 Chaxcy，MIT 许可证。
- 二次来源：https://github.com/mintisan/home-assistant-shenzhen-utilities（版本 1.0.2.post2），含以下修订：渠道 ID 可配置、绑定账户请求契约修正、禁用凭据请求重定向、避免错误日志泄露响应、按中国时区判断昨日、月初补查上月、保留零值、区分请求失败与缺失数据、未确认传感器默认禁用。上游未合并这些变更。
- 本仓库 2026-11-11 拆分为独立集成仓库，补充 hacs.json、README/NOTICE/许可证，并把 manifest 中原先指向已失效 `Chaxcy/ha-shenzhen-gas` 的 documentation/issue_tracker 改指本仓库。
- 许可证：MIT（见 LICENSE、licenses/GAS-MIT.txt，保留原版权声明）。

本集成的数据来源为官方小程序/网页接口，接口可能变化，请以官方账单为准。
本仓库不含任何账户凭据、账单数据或个人配置。
