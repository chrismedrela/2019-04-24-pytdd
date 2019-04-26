import datetime
from collections import namedtuple
from urllib import request

from xml.etree import ElementTree


class NoData(Exception):
    pass

ExchangeRate = namedtuple('ExchangeRate', 'rate cfactor')


API_ENDPOINT = 'http://www.nbp.pl/kursy/xml/{}'
TABLE_LIST_FILENAME = 'dir.txt'
TABLE_LIST_ENDPOINT = API_ENDPOINT.format(TABLE_LIST_FILENAME)
TABLE_ENDPOINT = API_ENDPOINT + '.xml'
TABLE_NAME_PREFIX = 'a'
DATE_FORMAT = '%y%m%d'
RATE_SELECTOR_PATTERN = './pozycja/[kod_waluty="{}"]/kurs_sredni'
CFACTOR_SELECTOR_PATTERN = './pozycja/[kod_waluty="{}"]/przelicznik'

def get_exchange_rate(currency, date):
    table_name = get_table_name(date)
    xml = get_table_as_xml(table_name)
    rate = extract_exchange_rate(xml, currency)
    cfactor = extract_cfactor(xml, currency)
    return rate, cfactor


def get_tables():
    stream = request.urlopen(TABLE_LIST_ENDPOINT)
    bytes = stream.read()
    text = bytes.decode('utf-8-sig')
    tables = text.splitlines()
    return tables


def get_table_name(date):
    tables = get_tables()
    for table_name in tables:
        if is_right_table(table_name, date):
            return table_name
    raise NoData


def is_right_table(table_name, date):
    right_prefix = table_name.startswith(TABLE_NAME_PREFIX)
    date_as_str = date.strftime(DATE_FORMAT)
    right_date = table_name.endswith(date_as_str)
    return right_prefix and right_date


def get_table_as_xml(table_name):
    table_url = TABLE_ENDPOINT.format(table_name)
    raw_xml = request.urlopen(table_url).read()
    xml = ElementTree.fromstring(raw_xml)
    return xml


def extract_exchange_rate(xml, currency):
    rate_selector = RATE_SELECTOR_PATTERN.format(currency)
    rate_as_str = xml.find(rate_selector).text
    rate = float(rate_as_str.replace(',', '.'))
    return rate


def extract_cfactor(xml, currency):
    cfactor_selector = CFACTOR_SELECTOR_PATTERN.format(currency)
    cfactor_as_str = xml.find(cfactor_selector).text
    cfactor = int(cfactor_as_str)
    return cfactor
