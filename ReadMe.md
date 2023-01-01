# 订阅自动转换脚本

2022.10.2更新，加入了配置文件订阅转换

## 使用方法

将本仓库fork，修改config.ini中的自己想要删改的内容，然后运行github action

## 说明

1. 此脚本三天执行一次，利用github Action自动进行订阅转换，并将转换完的订阅存入仓库中
2. 将config.ini中的url进行转换
3. ini文件内容说明

| Name   | Value     | 说明                                                          |
| ------ | --------- | ------------------------------------------------------------- |
| clash  | url1      | 如果需要v2ray链接转clash，则将v2ray链接填入config.ini此处中   |
| mixed  | url1      | 如果需要clash链接转v2ray，则将v2ray链接填入config.ini中此处中 |
| common | api       | 后端地址，边缘订阅后端地址                                    |
| common | configapi | 配置文件地址，默认为ACL4SSR的规则集                           |

## Clash下载链接：

不加速链接

`https://raw.githubusercontent.com/vveg26/SubAutoConv/main/sub/clash/selfnode.yaml`

CDN加速链接：

`https://cdn.jsdelivr.net/gh/vveg26/SubAutoConv@main/sub/clash/selfnode.yaml`

`https://cdn.jsdelivr.net/gh/vveg26/SubAutoConv@main/sub/clash/url1.yaml`


## V2ray

`none`
