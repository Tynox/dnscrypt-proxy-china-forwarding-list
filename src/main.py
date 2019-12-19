#!/usr/bin/env python3

import requests
import re


def fetch_china_list():
    url = 'https://github.com/felixonmars/dnsmasq-china-list/blob/master/accelerated-domains.china.conf?raw=true'
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        raise FileNotFoundError('Unable to open china list.')


def parse_data(data):
    server_re = '^server=\/(\S)+\/(\S)+$'

    servers = data.splitlines()
    url_list = []
    for server in servers:
        print(server)


if __name__ == "__main__":
    china_list = fetch_china_list()
    parse_data(china_list)
