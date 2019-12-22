#!/usr/bin/env python3

import requests
import re


# dns for china list
DNS_RESOLVER = ["119.29.29.29", "223.5.5.5", "2400:3200:baba::1"]


def fetch_china_list():
    url = 'https://github.com/felixonmars/dnsmasq-china-list/blob/master/accelerated-domains.china.conf?raw=true'
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        raise FileNotFoundError('Unable to open china list.')


def parse_data(data):
    servers = data.splitlines()
    urls = []
    for server in servers:
        s = server.split("/")
        urls.append(s[1])

    return urls


def write_to_file(urls):
    with open("../forwarding_china_list.txt", "w") as f:
        for url in urls:
            dns = ",".join(DNS_RESOLVER)
            line = "{0} {1}\n".format(url, dns)
            f.write(line)


if __name__ == "__main__":
    china_list = fetch_china_list()
    url_list = parse_data(china_list)
    write_to_file(url_list)
