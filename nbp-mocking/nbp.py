API_ENDPOINT = 'http://www.nbp.pl/kursy/xml/{}'
TABLE_LIST_FILENAME = 'dir.txt'
TABLE_LIST_ENDPOINT = API_ENDPOINT.format(TABLE_LIST_FILENAME)
TABLE_ENDPOINT = API_ENDPOINT + '.xml'
TABLE_NAME_PREFIX = 'a'
DATE_FORMAT = '%y%m%d'
RATE_SELECTOR_PATTERN = './pozycja/[kod_waluty="{}"]/kurs_sredni'
CFACTOR_SELECTOR_PATTERN = './pozycja/[kod_waluty="{}"]/przelicznik'

# ustawienie proxy
from urllib.request import urlopen, ProxyHandler, build_opener, install_opener

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