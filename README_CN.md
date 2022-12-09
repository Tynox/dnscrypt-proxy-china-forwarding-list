[[ENGLISH]](https://github.com/Tynox/dnscrypt-proxy-china-forwarding-list/blob/master/README.md)

# dnscrypt-proxy-china-forwarding-list

dnscrypt-proxy / adguard home 域名转发名单，转发大陆境内服务的域名DNS请求到 DNSPod公共DNS 或者 阿里云公共DNS。

域名列表来自于 **[dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)**。

## 文件说明

| 文件 | 软件 | 软件 |
| ---- | ---- | ---- |
| adguard_china_list | adguard home | 只转发境内服务域名，不包含苹果相关域名。转发到 DNSPod IPv4 公共DNS。 |
| adguard_china_list_with_apple_service | adguard home | 转发境内服务域名以及苹果相关域名。转发到 DNSPod IPv4 公共DNS。 |
| forwarding_china_list | dnscrypt-proxy | 只转发境内服务域名，不包含苹果相关域名。转发到 DNSPod IPv4 公共DNS 或者 阿里云IPv4公共DNS。 |
| forwarding_china_list_ipv6 | dnscrypt-proxy | 只转发境内服务域名，不包含苹果相关域名。转发到 DNSPod IPv4 公共DNS 或者 阿里云IPv4/IPv6公共DNS。 |
| forwarding_china_list_with_apple_service | dnscrypt-proxy | 转发境内服务域名以及苹果相关域名。转发到 DNSPod IPv4 公共DNS 或者 阿里云IPv4公共DNS。 |
| forwarding_china_list_with_apple_service_ipv6 | dnscrypt-proxy | 转发境内服务域名以及苹果相关域名。转发到 DNSPod IPv4 公共DNS 或者 阿里云IPv4公共DNS。 |

## 最新列表

**[下载最新列表](https://github.com/Tynox/dnscrypt-proxy-china-forwarding-list/releases/latest)**

## 编译

```
pip3 install -r requirements.txt
python3 src/main.py
```