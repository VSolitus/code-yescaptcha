[English](README.md) | 中文

# 前言

yescaptcha平台验证码识别在渗透测试中的利用

该文件用于配置验证码API识别接口。在常见的渗透测试场景中，带有验证码的登录机制常常给渗透测试工作带来阻碍。若要进一步开展相关利用操作，可结合captcha - killer - modified（https://github.com/c0ny1/captcha-killer）这一Burp插件来实现。 

## 使用指南

#### 填入api的key(获取地址在配置说明页面)

![image-20250310095919192](https://raw.githubusercontent.com/VSolitus/code-yescaptcha/refs/heads/main/pic/image-20250310095919192.png)

#### 启动python环境

```bash
python3 main.py
```

![image-20250310100737905](https://raw.githubusercontent.com/VSolitus/code-yescaptcha/refs/heads/main/pic/image-20250310100737905.png)

#### 以数据包形式导入插件

该接口支持很多识别 可以参考文档来获取

https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/pages/164286

`

POST /ImageToTextTask HTTP/1.1
User-Agent: Apifox/1.0.0 (https://apifox.com)
Content-Type: application/json
Accept: */*
Host: 127.0.0.1:5200
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 4329

{
    "data": "<@BASE64><@IMG_RAW></@IMG_RAW></@BASE64>",
    "class": "true"
}

`

数据包的为插件使用方法 详细方法请访问

https://gv7.me/articles/2019/burp-captcha-killer-usage/

![image-20250310101733765](https://raw.githubusercontent.com/VSolitus/code-yescaptcha/refs/heads/main/pic/image-20250310101733765.png)

### 配置说明

该脚本配置的是需要yescaptcha平台的 API，请按以下步骤设置：

1. 注册账号：

   我的个人推荐链接(https://yescaptcha.com/i/5xjeiZ) tips:吃点回扣哈哈

   访问https://yescaptcha.com/auth/login或者访问推荐链接完成注册登录

2. 获取ClietKey：

   在仪表盘中获取对应的key复制到文档中

   ![image-20250310102326820](https://raw.githubusercontent.com/VSolitus/code-yescaptcha/refs/heads/main/pic/image-20250310102326820.png)
