# 订阅自动转换脚本

1. 此脚本三天执行一次，利用github Action自动进行订阅转换
2. 将config.ini中的url进行转换
3. ini文件内容说明

| Name   | Value | 说明                                                                |
| ------ | ----- | ------------------------------------------------------------------- |
| clash  | url1  | 如果需要v2ray链接转clash，则将v2ray链接填入config.ini此处中         |
| mixed  | url1  | 如果需要clash链接转v2ray，则将v2ray链接填入config.ini中vx测试号中获 |
| common | type  | clash/mixed 类型为clash则为v2ray转clash                             |
| common | api   | 后端地址                                                            |
|        |       |                                                                     |
