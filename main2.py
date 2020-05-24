#!/usr/bin/env python

from bs4 import BeautifulSoup
import argparse
import requests
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/80.0.3987.149 Safari/537.36'
}


def scrapping_2020(year):
    return 'http://www.sii.cl/valores_y_fechas/utm/utm' + str(year) + '.htm'



def scrapping_2012(year):
    return 'http://www.sii.cl/pagina/valores/utm/utm' + str(year) + '.htm'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Busqueda valor IPC')
    parser.add_argument('--year', '-y', help='Context year to search', type=int)
    parser.add_argument('--month', '-m', help='Month to search', type=int)
    args = parser.parse_args(sys.argv[1:])

    year = args.year
    month = args.month

    if year > 2012:
        url = scrapping_2020(year)
    else:
        url = scrapping_2012(year)

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    tr = soup.findAll('tr')

    if len(tr) > 0:
        for i in range(len(tr)):
            if i == month + 1:
                section = tr[i]
                columns = section.find_all()
                ipc_value = columns[3].text.replace(',', '.')
                print ipc_value
                # print(float(ipc_value))
