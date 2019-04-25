API_ENDPOINT = 'http://www.nbp.pl/kursy/xml/{}'
TABLE_LIST_FILENAME = 'dir.txt'
TABLE_LIST_ENDPOINT = API_ENDPOINT.format(TABLE_LIST_FILENAME)
TABLE_ENDPOINT = API_ENDPOINT + '.xml'
TABLE_NAME_PREFIX = 'a'
DATE_FORMAT = '%y%m%d'
RATE_SELECTOR_PATTERN = './pozycja/[kod_waluty="{}"]/kurs_sredni'
CFACTOR_SELECTOR_PATTERN = './pozycja/[kod_waluty="{}"]/przelicznik'