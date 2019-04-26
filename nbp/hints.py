HOME_PAGE_TEMPLATE = """
<h1>Home Page</h1>
<p>{msg}</p>
<form method="POST">
  <p>Date: <input type="text" name="date" /></p>
  <p>Currency
    <select name="currency">
      <option value="USD">dolar amerykanski USD</option>
      <option value="THB">bat (Tajlandia) THB</option>
      <option value="ISK">korona islandzka ISK</option>
    </select>
  </p>
  <p><input type="submit" value="Get exchange rate!"></p>
</form>
"""


from xml.etree import ElementTree

API_ENDPOINT = 'http://www.nbp.pl/kursy/xml/{}'
TABLE_LIST_FILENAME = 'dir.txt'
TABLE_LIST_ENDPOINT = API_ENDPOINT.format(TABLE_LIST_FILENAME)
TABLE_ENDPOINT = API_ENDPOINT + '.xml'
TABLE_NAME_PREFIX = 'a'
DATE_FORMAT = '%y%m%d'
RATE_SELECTOR_PATTERN = './pozycja/[kod_waluty="{}"]/kurs_sredni'
CFACTOR_SELECTOR_PATTERN = './pozycja/[kod_waluty="{}"]/przelicznik'


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
