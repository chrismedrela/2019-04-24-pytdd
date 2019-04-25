from urllib import request

API_ENDPOINT = 'http://www.nbp.pl/kursy/xml/{}'
TABLE_LIST_FILENAME = 'dir.txt'
TABLE_LIST_ENDPOINT = API_ENDPOINT.format(TABLE_LIST_FILENAME)
TABLE_ENDPOINT = API_ENDPOINT + '.xml'
TABLE_NAME_PREFIX = 'a'
DATE_FORMAT = '%y%m%d'
RATE_SELECTOR_PATTERN = './pozycja/[kod_waluty="{}"]/kurs_sredni'
CFACTOR_SELECTOR_PATTERN = './pozycja/[kod_waluty="{}"]/przelicznik'

# ustawienie proxy
from urllib.request import ProxyHandler, build_opener, install_opener

'''
proxy_handler = ProxyHandler({
    'http': '10.144.1.10:8080', 
    'https': '10.144.1.10:8080',
})
opener = build_opener(proxy_handler)
install_opener(opener)
'''


def get_tables():
    stream = request.urlopen(TABLE_LIST_ENDPOINT)
    bytes = stream.read()
    text = bytes.decode('utf-8-sig')
    tables = text.splitlines()
    return tables


def get_table_name(date):
    tables = get_tables()
    date_as_str = date.strftime(DATE_FORMAT)
    for table_name in tables:
        if is_right_table(table_name, date_as_str):
            return table_name
    return None


def is_right_table(table_name, date_as_str):
    right_prefix = table_name.startswith(TABLE_NAME_PREFIX)
    right_date = table_name.endswith(date_as_str)
    return right_prefix and right_date
