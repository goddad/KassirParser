#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
from random import choice
import subprocess
import time
import datetime

url = ''
keyword = ''

def get_proxy_html(url):
	useragents = open('useragents.txt').read().split('\n')
	proxies = open('proxies.txt').read().split('\n')

	useragent = {'User-Agent': choice(useragents)}
	proxy = {'http': choice(proxies)}

	print(useragent)
	print(proxy)

	return get_html(url, useragent, proxy)

def get_html(url, useragent=None, proxy=None):
	page = requests.get(url, stream=True, headers=useragent, proxies=proxy)
	return page.text

def get_available_tickets(html):
	trs = BeautifulSoup(html, 'lxml').find('table', class_='table table-price').find_all('tr')

	for tr in trs:
		try:
			sector_td = tr.find('td', class_='col-sector').text

			if keyword in sector_td:
				subprocess.call(['wall', sector_td.strip() + ", кол-во: " + tr.find('td', class_='col-amount').text.strip()])
				print(sector_td.strip() + ", кол-во: " + tr.find('td', class_='col-amount').text.strip())
		except:
			print('attr text with keyword=' + keyword + ' is not exist')


def renew_proxy_list():
	proxies_page = requests.get('https://free-proxy-list.net/').text
	trs_list = BeautifulSoup(proxies_page, 'lxml').find('table', id='proxylisttable').find('tbody').find_all('tr')
	proxies_list = ""

	for i in range(10):
		ip = trs_list.pop(0).find('td')
		port = ip.find_next_sibling()
		proxy = 'http://' + ip.text + ':' + port.text + '\n'

		proxies_list += proxy

	proxies_list = proxies_list[:-2]

	with open('proxies.txt', 'w') as proxies:
		proxies.write(proxies_list)
		proxies.close()

	# print(proxies_list)

def main():
	global url

	print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
	print(url)

	renew_proxy_list()
	get_available_tickets(get_proxy_html(url))
	
	print('-----------------------------------\n')

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('gimme event URL and keyword!')

	if len(sys.argv) == 3:
		url = sys.argv[1]
		keyword = sys.argv[2]
		main()
	else:
		print('there should be two arguments!')