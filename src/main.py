#!/usr/bin/env python3

from enum import Enum
import requests

# dns for china list
DNS_RESOLVER_IPV4 = ["119.29.29.29", "223.5.5.5"]
DNS_RESOLVER_IPV6 = ["2400:3200:baba::1"]


# output file type
class OutputType(Enum):
    IPV4_WITHOUT_APPLE = 0
    IPV4_WITH_APPLE = 1
    IPV6_WITHOUT_APPLE = 2
    IPV6_WITH_APPLE = 3


# output files
OUTPUT_FILES: {OutputType: str} = {
    OutputType.IPV4_WITHOUT_APPLE: "forwarding_china_list",
    OutputType.IPV4_WITH_APPLE: "forwarding_china_list_with_apple_service",
    OutputType.IPV6_WITHOUT_APPLE: "forwarding_china_list_ipv6",
    OutputType.IPV6_WITH_APPLE: "forwarding_china_list_with_apple_service_ipv6"
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


def write_to_file(file_name: str, urls: [str], dns_list: [str]):
    with open("../" + file_name, "w") as f:
        for url in urls:
            dns = ",".join(dns_list)
            line = "{0} {1}\n".format(url, dns)
            f.write(line)


if __name__ == "__main__":
    china_list = parse_data(fetch_china_list())
    apple_list = parse_data(fetch_apple_list())

    for key, value in OUTPUT_FILES.items():
        if key is OutputType.IPV4_WITHOUT_APPLE:
            write_to_file(value, china_list, DNS_RESOLVER_IPV4)
        elif key is OutputType.IPV4_WITH_APPLE:
            write_to_file(value, china_list + apple_list, DNS_RESOLVER_IPV4)
        elif key is OutputType.IPV6_WITHOUT_APPLE:
            write_to_file(value, china_list, DNS_RESOLVER_IPV4 + DNS_RESOLVER_IPV6)
        elif key is OutputType.IPV6_WITH_APPLE:
            write_to_file(value, china_list + apple_list, DNS_RESOLVER_IPV4 + DNS_RESOLVER_IPV6)
