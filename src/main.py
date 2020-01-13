#!/usr/bin/env python3

import requests
import argparse


# dns for china list
DNS_RESOLVER_IPV4 = ["119.29.29.29", "223.5.5.5"]
DNS_RESOLVER_IPV6 = ["2400:3200:baba::1"]


# init argparse
parser = argparse.ArgumentParser(description="Auto generate dns forwarding list for DNSCrypt-Proxy from "
                                             "'dnsmasq-china-list' project.")
parser.add_argument("-i6", "--ipv6", nargs="?", help="Add ipv6 dns into the forwarding list.", default=False,
                    type=bool, dest="ipv6")
parser.add_argument("-a", "--apple", nargs="?", default=False, type=bool, dest="apple",
                    help="Add apple china list into the forwarding list.")
parser.add_argument("-o", "--out", nargs="?", default="forwarding_list.txt", type=str, dest="out",
                    help="Output file name")


def fetch_china_list():
    url = 'https://github.com/felixonmars/dnsmasq-china-list/blob/master/accelerated-domains.china.conf?raw=true'
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        raise FileNotFoundError('Unable to open china list.')


def fetch_apple_list():
    url = 'https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/apple.china.conf'
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        raise FileNotFoundError('Unable to open apple china list')


def parse_data(data):
    servers = data.splitlines()
    urls = []
    for server in servers:
        s = server.split("/")
        urls.append(s[1])

    return urls


def write_to_file(file_name, urls, dns_list):
    with open("../" + file_name, "w") as f:
        for url in urls:
            dns = ",".join(dns_list)
            line = "{0} {1}\n".format(url, dns)
            f.write(line)


if __name__ == "__main__":
    args = parser.parse_args()
    should_append_ipv6_dns = args.ipv6
    should_add_apple_china_list = args.apple
    output_file = args.out

    dns_servers = DNS_RESOLVER_IPV4
    if should_append_ipv6_dns:
        dns_servers += DNS_RESOLVER_IPV6

    china_list = fetch_china_list()
    url_list = parse_data(china_list)

    if should_add_apple_china_list:
        apple_list = fetch_apple_list()
        apple_url_list = parse_data(apple_list)
        url_list += apple_url_list

    write_to_file(output_file, url_list, dns_servers)
