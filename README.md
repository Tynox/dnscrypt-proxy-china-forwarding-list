# dnscrypt-proxy-china-forwarding-list
Forwarding China domains (with / without apple services) dns requests to Chinese dns servers. Made for dnscrypt-proxy and adguard home.

China domains are from **[dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)**.

## Files

| File name | Software | Descrption |
| ---- | ---- | ---- |
| adguard_china_list | adguard home | Only China domains, without apple services. Forward to DNSPod Public DNS (ipv4). |
| adguard_china_list_with_apple_service | adguard home | China domains & apple services. Forward to DNSPod Public DNS (ipv4). |
| forwarding_china_list | dnscrypt-proxy | Only China domains, without apple services. Forward to DNSPod Public DNS (ipv4) and Alicloud Public DNS (ipv4). |
| forwarding_china_list_ipv6 | dnscrypt-proxy | China domains, without apple services. Forward to DNSPod Public DNS (ipv4) and Alicloud Public DNS (ipv4 / ipv6). |
| forwarding_china_list_with_apple_service | dnscrypt-proxy | China domains & apple services. Forward to DNSPod Public DNS (ipv4) and Alicloud Public DNS (ipv4). |
| forwarding_china_list_with_apple_service_ipv6 | dnscrypt-proxy | China domains & apple services. Forward to DNSPod Public DNS (ipv4) and Alicloud Public DNS (ipv4 / ipv6). |

## Latest lists

**[Download the latest lists](https://github.com/Tynox/dnscrypt-proxy-china-forwarding-list/releases/latest)**

## Build

`
pip3 install -r requirements.txt
python3 src/main.py
`