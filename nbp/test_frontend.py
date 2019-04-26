import datetime

from mock import Mock, patch
from nose2.tools import such

from frontend import home
from backend import NoData

with such.A('Home Page') as it:
    with it.having('exchange rate form'):
        @it.has_setup
        def setup():
            date = '2017/02/01'
            it.currency = 'USD'
            rate = 4.0012
            cfactor = 1
            it.expected_date = datetime.date(
                2017, 2, 1)

            it.backend_patcher = patch('frontend.backend')
            it.backend_mock = it.backend_patcher.start()
            it.request_patcher = patch('frontend.request')
            it.request_mock = it.request_patcher.start()

            it.request_mock.method = 'POST'
            it.request_mock.form = dict(
                date=date,
                currency=it.currency)

            it.backend_mock.get_exchange_rate.return_value = (rate, cfactor)

        @it.has_teardown
        def tearDown():
            it.backend_patcher.stop()
            it.request_patcher.stop()

        with it.having('a currency'):
            @it.has_setup
            def setup():
                it.html = home()

            @it.should('pass date and currency to backend')
            def test():
                it.backend_mock.get_exchange_rate.assert_called_once_with(
                    date=it.expected_date,
                    currency=it.currency)

            @it.should('return formatted exchange rate provided by backend')
            def test():
                assert '1 USD = 4.0012 PLN' in it.html

        with it.having('a currency with cfactor different from one'):
            @it.has_setup
            def setup():
                it.request_mock.form['currency'] = 'ISK'
                rate = 3.1234
                cfactor = 100
                it.backend_mock.get_exchange_rate.return_value = (rate, cfactor)

                it.html = home()

            @it.should('return formatted exchange rate with valid cfactor')
            def test():
                assert '100 ISK = 3.1234 PLN' in it.html

        with it.having('non working day'):
            @it.has_setup
            def setup():
                it.backend_mock.NoData = KeyError
                it.backend_mock.get_exchange_rate.side_effect = it.backend_mock.NoData

                it.html = home()

            @it.should('return message that there is no data for such day')
            def test():
                assert 'No data for this day' in it.html

    it.createTests(globals())