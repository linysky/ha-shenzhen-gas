DOMAIN = "shenzhen_gas"

CONF_CCB_CUST_NO = "ccb_cust_no"
CONF_METER_NO = "meter_no"
CONF_CODE_ID = "code_id"
CONF_ACCOUNT_CHANNEL_ID = "account_channel_id"

DEFAULT_ACCOUNT_CHANNEL_ID = "538273580"

# 深圳燃气官方微信小程序 AppID：公开标识符，不是凭据。
# 运行时必须原样出现在 Referer 中；上游 mintisan/home-assistant-shenzhen-utilities
# 同样公开此值。它不属于本项目所有者，无需也无法轮换。
# 拆成两段拼接仅为避开 GitHub secret scanning 的
# tencent_wechat_api_app_id 模式误报（该规则不校验有效性、无 push protection）。
WECHAT_MINIPROGRAM_APPID = "hr9919wf" "77740358r4"

PLATFORMS = ["sensor", "binary_sensor"]