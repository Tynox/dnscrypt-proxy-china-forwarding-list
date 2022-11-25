#!/usr/bin/env python3

from enum import Enum
import os
import requests

# dns for china list
DNS_RESOLVER_IPV4 = ["119.29.29.29", "223.5.5.5"]
DNS_RESOLVER_IPV6 = ["2400:3200:baba::1"]


# File prefix
FILE_PREFIX = "./"
if os.getcwd().endswith("src"):
    FILE_PREFIX = "../"


# output file type
class OutputType(Enum):
    DNSCRYPT_IPV4_WITHOUT_APPLE = 0
    DNSCRYPT_IPV4_WITH_APPLE = 1
    DNSCRYPT_IPV6_WITHOUT_APPLE = 2
    DNSCRYPT_IPV6_WITH_APPLE = 3
    ADGUARD_IPV4_WITHOUT_APPLE = 4
    ADGUARD_IPV4_WITH_APPLE = 5


# output files
OUTPUT_FILES: {OutputType: str} = {
    OutputType.DNSCRYPT_IPV4_WITHOUT_APPLE: "forwarding_china_list",
    OutputType.DNSCRYPT_IPV4_WITH_APPLE: "forwarding_china_list_with_apple_service",
    OutputType.DNSCRYPT_IPV6_WITHOUT_APPLE: "forwarding_china_list_ipv6",
    OutputType.DNSCRYPT_IPV6_WITH_APPLE: "forwarding_china_list_with_apple_service_ipv6",
    OutputType.ADGUARD_IPV4_WITHOUT_APPLE: "adguard_china_list",
    OutputType.ADGUARD_IPV4_WITH_APPLE: "adguard_china_list_with_apple_service"
}


def fetch_china_list() -> str:
    url = 'https://github.com/felixonmars/dnsmasq-china-list/blob/master/accelerated-domains.china.conf?raw=true'
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        raise FileNotFoundError('Unable to open china list.')


def fetch_apple_list() -> str:
    url = 'https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/apple.china.conf'
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        raise FileNotFoundError('Unable to open apple china list')


def parse_data(data) -> [str]:
    servers = data.splitlines()
    urls = []
    for server in servers:
        s = server.split("/")
        urls.append(s[1])

    return urls


def write_dnscrypt_forward_config_to_file(file_name: str, urls: [str], dns_list: [str]):
    with open(FILE_PREFIX + file_name, "w") as f:
        for url in urls:
            dns = ",".join(dns_list)
            line = "{0} {1}\n".format(url, dns)
            f.write(line)


def write_adguard_forward_config_to_file(file_name: str, urls: [str], dns_list: [str]):
    with open(FILE_PREFIX + file_name, "w") as f:
        for url in urls:
            line = "[/{0}/]{1}\n".format(url, dns_list[0])
            f.write(line)


if __name__ == "__main__":
    china_list = parse_data(fetch_china_list())
    apple_list = parse_data(fetch_apple_list())

    for key, value in OUTPUT_FILES.items():
        if key is OutputType.DNSCRYPT_IPV4_WITHOUT_APPLE:
            write_dnscrypt_forward_config_to_file(value, china_list, DNS_RESOLVER_IPV4)
        elif key is OutputType.DNSCRYPT_IPV4_WITH_APPLE:
            write_dnscrypt_forward_config_to_file(value, china_list + apple_list, DNS_RESOLVER_IPV4)
        elif key is OutputType.DNSCRYPT_IPV6_WITHOUT_APPLE:
            write_dnscrypt_forward_config_to_file(value, china_list, DNS_RESOLVER_IPV4 + DNS_RESOLVER_IPV6)
        elif key is OutputType.DNSCRYPT_IPV6_WITH_APPLE:
            write_dnscrypt_forward_config_to_file(value, china_list + apple_list, DNS_RESOLVER_IPV4 + DNS_RESOLVER_IPV6)
        elif key is OutputType.ADGUARD_IPV4_WITHOUT_APPLE:
            write_adguard_forward_config_to_file(value, china_list, DNS_RESOLVER_IPV4)
        elif key is OutputType.ADGUARD_IPV4_WITH_APPLE:
            write_adguard_forward_config_to_file(value, china_list + apple_list, DNS_RESOLVER_IPV4)
