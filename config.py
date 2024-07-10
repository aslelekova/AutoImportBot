# config.py

url_auto_ru = "https://auto.ru/-/ajax/desktop-search/listing/"

headers_auto_ru = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru",
    "Connection": "keep-alive",
    "Content-Length": "157",
    "Content-Type": "application/json",
    "Cookie": "from=direct; from_lifetime=1712496104998; layout-config={\"screen_height\":982,\"screen_width\":1512,"
              "\"win_width\":1512,\"win_height\":538}; count-visits=18; "
              "sso_status=sso.passport.yandex.ru:synchronized_no_beacon; bltsr=1; coockoos=1; los=1; "
              "_yasc=KjZeRRnt4VZO6tVpEnyRuCtr/jo3rmbuWfUNF3PD3Cv3GeJ04yBTGyxVLRrDnRAIlTxWuA==; "
              "cmtchd=MTcxMjQ5MzI5NTQ3MQ==; "
              "crookie=L2lrKqT7k5R4nudvxRdNn8HoRy/EETF49VTSe9m+RdtUInKKd5hKC82pnxgbP2M7xexSWBWyVHo7rUf15WfpaBmDYww=; "
              "autoru_sid=101676242%7C1712489186235.7776000.Efle_Bi7pQrpVRix1e47-A"
              ".Wk6KwUNWrdKFi33noZOHp62bSpjFM_UeNtcYR7C7_xI; fp=91bbac569e06df8c670ce31851cb21dc%7C1712489185993; "
              "yaPassportTryAutologin=1; L=Xl5UYUcIdGsFQXNCA1Bzak9VTFgDRHZxDzYqVSM/GyVKJCBHBwQ7.1712487882.15672"
              ".386760.75d619aed6f32b4ef89ceafb53efcb14; "
              "Session_id=3:1712489182.5.0.1712487882238:PpbMUg:cc.1.2:1|516250914.0.2.3:1712487882|61:10021107"
              ".602959.m6arxb6p1bTX6QsWFC5_u0yECrw; "
              "i=Ss5UpiIC2T1KuLyTJH3GPwaf8Jya/MMdEX5rcqVWCpGliACPc68rWosSKGybvP+dFHxkcQVLh3XxneUM/s8gwUcVCio=; "
              "mda2_beacon=1712489182977; "
              "sessar=1.1188.CiDjLiC2qChKzTV__pVLyOQhuXwIXn3VCq-eMteHk6U8EQ"
              ".weShYx77jygVnruzkdQFxVQfcxVWw7AUfh3fLtkpDMQ; yandex_login=lelekova.nastay; "
              "yandexuid=5281238661693844289; "
              "ys=udn.czo5MDE2NTc5OTp2azrQkNC90LDRgdGC0LDRgdC40Y8g0JvQtdC70LXQutC%2B0LLQsA%3D%3D#c_chck.2387338530; "
              "_csrf_token=48621f74fbc84d9f83c8d0b7a6a3aef475528e3ac8465f87; "
              "autoruuid=g661282de2seoj3pebo6q6l8beeci0ja.bda6749430e51fc6c220e73bee9e8782; "
              "suid=08ae2d57eeb27552ec30b593f31049ed.f78f15bb1855570d49d41eb15f8378f3",
    "Host": "auto.ru",
    "Origin": "https://auto.ru",
    "Referer": "https://auto.ru/moskva/cars/vaz/2114/all/?year_from=2008&year_to=2010&page=2",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "same-origin",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/17.4.1 Safari/605.1.15",
    "x-client-app-version": "62.0.13791615",
    "x-client-date": "1712496108415",
    "x-csrf-token": "48621f74fbc84d9f83c8d0b7a6a3aef475528e3ac8465f87",
    "x-page-request-id": "8c4cf9478e816c487ace00ecda702d03",
    "x-requested-with": "XMLHttpRequest",
    "x-retpath-y": "https://auto.ru/moskva/cars/vaz/2114/all/?year_from=2008&year_to=2010&page=2",
    "x-yafp": "{\"a1\":\"xjXoPw==;0\",\"a2\":\"XdOXZ6H2MqHm5jJfEXntmVbJxl9MlRxmxjpsEBTl/uaIQjfk9KIhIw==;1\","
              "\"a3\":\"5HSeooWk7pWwYTHdLl9BEA==;2\",\"a4\":\"wTwLLQ==;3\",\"a5\":\"Vb2p8jD9saAK2A==;4\","
              "\"a6\":\"Y0M=;5\",\"a7\":\"zmd+BvIUnTMVuQ==;6\",\"a8\":\"aT/j1VUGxinVzQ==;7\","
              "\"a9\":\"eN+c7m8/niQ9wA==;8\",\"b1\":\"JcFnrCPXGb/ROw==;9\",\"b2\":\"rg1IrJySC8VlAQ==;10\","
              "\"b3\":\"lI+i0v/frlvhZA==;11\",\"b4\":\"pj90mT5OfFU=;12\",\"b5\":\"cwOmk6F2aqUBIQ==;13\","
              "\"b6\":\"rv++xqngGdL1bQ==;14\",\"b7\":\"BYZU1hjRLBo=;15\",\"b8\":\"+SREprr79EW6Uw==;16\","
              "\"b9\":\"tbPJqQnFIDAHNQ==;17\",\"c1\":\"b/0TYA==;18\",\"c2\":\"CIIKrWeX0xceWJrWLpXTpQ==;19\","
              "\"c3\":\"VgE6jR47ms2iaG2fLubk4g==;20\",\"c4\":\"N8gI2d8VVIw=;21\",\"c5\":\"/MyN0FUlN5I=;22\","
              "\"c6\":\"Ckgvqw==;23\",\"c7\":\"eh7+l8CqS9w=;24\",\"c8\":\"M0A6dxvBaIo=;25\","
              "\"c9\":\"qFL8/luGjow=;26\",\"d1\":\"NZH42/86YOo=;27\",\"d2\":\"Rrs=;28\","
              "\"d3\":\"E1qWkp5MEAgfdg==;29\",\"d4\":\"vGtS0KfiPMY=;30\",\"d5\":\"jCvMNyLgmhRqhg==;31\","
              "\"d7\":\"AI53n2z038w=;32\",\"d8\":\"EOCz1jSVmp6ITzm7Qx/0+h4hV4Yl41w8XFg=;33\","
              "\"d9\":\"rSlzq8Q2oDY=;34\",\"e1\":\"xYBArJUkRHhSdg==;35\",\"e2\":\"hHL6XlWXJAyGxw==;36\","
              "\"e3\":\"C5geTg+HvWMffg==;37\",\"e4\":\"aEY2lKD/Ye0=;38\",\"e5\":\"KzEf0QZvYwE3DQ==;39\","
              "\"e6\":\"FfbE9PrMraw=;40\",\"e7\":\"HvvYr9+H/jH4Vg==;41\",\"e8\":\"KaF/CaeI7SE=;42\","
              "\"e9\":\"J4cBhiox5KQ=;43\",\"f1\":\"H3KPOdzU4jUilg==;44\",\"f2\":\"hUYgTetI0kI=;45\","
              "\"f3\":\"QZPaTyVyafXFxw==;46\",\"f4\":\"rOs2ldPvTPo=;47\",\"f5\":\"n6+XuH6KzmbGGQ==;48\","
              "\"f6\":\"OMHqi55ETl8FeA==;49\",\"f7\":\"qGBA/z9llIBVQQ==;50\",\"f8\":\"oWFw3a+kUKsz4A==;51\","
              "\"f9\":\"EIJk/r32c34=;52\",\"g1\":\"2GDoI+srbQ43JQ==;53\",\"g2\":\"x8hQPPtOi+rKbg==;54\","
              "\"g3\":\"zLoMqQfbIwA=;55\",\"g4\":\"vTrb0X1rIjXLRw==;56\",\"g5\":\"e4z8LYvUSiDqbA==;57\","
              "\"g6\":\"cr6F7F8ddsh8ow==;58\",\"g7\":\"cbbpeRDa2Kc=;59\",\"g8\":\"43x8y6bW3fo=;60\","
              "\"g9\":\"NmAU90Ws8p8=;61\",\"h1\":\"MnH3d3bCKB/9mQ==;62\",\"h2\":\"WLjY37sFFZE95A==;63\","
              "\"h3\":\"5Bgtokl4iosfzQ==;64\",\"h4\":\"cmTc3fPPX8XIwQ==;65\",\"h5\":\"kUw8XwB1uqI=;66\","
              "\"h6\":\"A333jRG4GlUJCg==;67\","
              "\"h7\":\"mw2QwQ1Hj/uZL1/a61WnXbeJ5ZXVJXrWOififltK5CjY59h"
              "+TtErHbINEYmbSXaUJ05yy4rNHmeupSMaLQwHn7sNncEaR4/7uy9L2uFV7l23iciV1iVt1m4n5X5GSrAog"
              "+fJfkrRPB33DTKJlEkilCtOcsuazRNn76UqGisMFp+8DdjBB0fJ+/gva9r6VapdsYnJlfkle9YgJ/N+RkroKILn;68\","
              "\"h8\":\"idT7EydUL2pz7w==;69\",\"h9\":\"UK4kOzpn4OoinA==;70\",\"i1\":\"eT9ciSn2E34=;71\","
              "\"i2\":\"N4voHFLySIh87A==;72\",\"i3\":\"zSQ751q14eW3WQ==;73\",\"i4\":\"5JesqALtTgsnCw==;74\","
              "\"i5\":\"pXG/I0Dp3x8Syg==;75\","
              "\"z1\":\"PiAAAThCFWeABOVSqLUn01I1en02pvoKo/TX/Qt5tZZsVgozWxCGzUC14morQ/7UsKgYTtu1qrvcZUjz94o88w==;76"
              "\",\"z2\":\"qyD6epBj9lqNSE7fejIGxPoppk3+iERqRCUufrzlJ49LD0GvAcrLrFJ2b3RIHk4OMAQ65dtQYSOJZc/ruPCwtA"
              "==;77\",\"y3\":\"WyEnPCGHou5+8Q==;78\",\"y5\":\"ytZ3LVCBnTxp0Q==;79\",\"y7\":\"NIEJciJZ70M5rQ==;80\","
              "\"y8\":\"ELYIhssRfVVVJw==;81\",\"x1\":\"B+9uAbIB1VDflg==;82\",\"x2\":\"3/gC2xruV0VIpQ==;83\","
              "\"z3\":\"Bhb5ix1CojsxwQ==;84\",\"z7\":\"kyctaIN/9Vad7YQn;85\",\"z8\":\"z3hxHXX34Sriqw==;86\","
              "\"y2\":\"vCQnUN5kK0gJxA==;87\",\"y4\":\"ELuE62W7In/khQ==;88\",\"z6\":\"NINzWn5/VNwiHE+n;89\","
              "\"y6\":\"EvWwEfWAjiMJSw==;90\",\"y9\":\"JoX/5KWCr3xyXw==;91\",\"y10\":\"QlGTu8w+viK0Dg==;92\","
              "\"z9\":\"07UqX2L5hEknO+aB;93\",\"y1\":\"R4Tzy9349UF57/Jy;94\",\"x3\":\"qEvVzFRvLIrgig==;95\","
              "\"x4\":\"8LOa6l32yDhGNw==;96\",\"x5\":\"BljPQEUGV7EmJ64Y;97\",\"z5\":\"nxlzayd+1qOiCA==;98\","
              "\"z4\":\"l4BdOsdV/2XPX2uyWS8=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"Fwfh391wtuwNMmpHANwbUdAEZV8=;100\","
              "\"pgrd\":\"eyfOyIRfFwPKCPTY/2TnrKb13dSUWd8bSPxEAxP/3X/aILUBNWc8tBYxEX0AfvOIZGECQRInXudPLBilPMrtd"
              "/3kMrImDwESOHEVp+AFMAP9xLZEljQYwQVcHxFFqDEcoZ1U6/23A5m1tc5KZkm0GV/k+GcK"
              "/rR18wUOuxxAKjgkhQOpgGzrjeZeHg7mzL8xMpb+E0mi8YPRVVUoFDl4ElddDgQ=\"}",
}

TOKEN = '7046062695:AAHh3LLkR7sG8AAhMwmoULeDa4W0UrA4cAg'

headers_encar_com = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'api.encar.com',
    'Origin': 'http://www.encar.com',
    'Referer': 'http://www.encar.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Version/17.5 Safari/605.1.15'
}

url_encar_com = "http://api.encar.com/search/car/list/premium"

username = '01024451703'
password = 'valentina1968'
