# Instalacja

Pod Pythonem 3.3+, nie wymaga instalowania dodatkowych paczek:

```python
from unittest import mock
```

Pod Pythonem 2.7 i 3.x, wymaga instalacji `pip install mock`:

```python
import mock
```

Wersja najbardziej uniwersalna:

```python
try:
    from unittest import mock
except ImportError:
    import mock
```

# Mocki imitujące funkcje

```python
>>> m = mock.Mock()  # konfiguracja mocka (na początku testu)
>>> m(42, foo=3)  # testowany kod wywołuje mocka zamiast prawdziwej funkcji
```

Pod koniec testu możemy sprawdzić, co się działo z mockiem:

```python
>>> m.assert_called_once_with()
>>> m.call_args
m(42, foo=3)
>>> m.call_args == mock.call(2, 4)
False
```

## Zwracanie wartości (`return_value`)

```python
>>> m = mock.Mock()
>>> m.return_value = 'foo'
>>> m()
'foo'
```

Mocka można skonfigurować od razu przy jego tworzeniu.
Poniższy kod jest równoważny wcześniejszemu:

```python
>>> m = mock.Mock(return_value='foo')
>>> m()
'foo'
```

## Rzucanie wyjątku (`side_effect`)

```python
>>> m = mock.Mock(side_effect=KeyError)
>>> m()
Traceback (most recent call last):
  ...
KeyError
```

## Zwracanie różnych wartości przy kolejnych wywołaniach

```python
>>> m = Mock()
>>> m.side_effect = [
...     '1',
...     '2',
...     KeyError,
...     '3',
... ]
>>> m()
'1'
>>> m()
'2'
>>> m()
Traceback (most recent call last):
  ...
KeyError
>>> m()
'3'
```

## Delegowanie do własnej funkcji

```python
>>> m = mock.Mock()
>>> m.side_effect = lambda x: x+2
>>> m(5)
7
```

## Asercje funkcji-mocka

```python
m.assert_called_with(10)
m.assert_called_once_with(10)
m.assert_any_call(3)
m.assert_called_with(3)
m.assert_not_called()
m.called
m.call_count
m.call_args
m.call_args_list
```

# Zagnieżdżanie mocków

```python
m.foo
m.foo.bar.egg.spam
m.foo.bar.egg.spam()
m.mock_calls
```

# `MagicMock` vs `Mock`

```python
mm = mock.MagicMock()
m = mock.Mock()
mm['a']
m['a']
len(mm)
len(m)
int(mm)
int(m)
list(mm)
list(m)
42 in mm
42 in m
```

# Auto-spec

```python
dumb_os_mock = mock.Mock()
dumb_os_mock.remove('file')  # correct usage
dumb_os_mock.remoev()  # issue: accessing not existing method doesn't raise exception
dumb_os_mock.remove.asser_called_with('another file')  # issue: misspelled assert make test pass even though it should fail

import os
os_mock = mock.Mock(spec=os)
os_mock.remove('file')  # correct usage
os_mock.remoev()
os_mock.asser_called_with('another file')  #
os_mock.remove.asser_called_with('another file')  # literówka -- niestety wyjątek nie zostanie rzucony
```

## Issues with auto-spec

```python
class Something:
    def __init__(self):
        self.foo = 42
something_mock = mock.Mock(spec=Something)
something_mock.foo
something_mock.foo = 42
something_mock.foo
```

# Mocking context managers

```python
with mock.patch('__main__.open') as open_mock:
    with open('foo', 'r') as s:
        s.read()
open_mock
open_mock.call_args_list
open_mock.mock_calls
```

# `mock.ANY` utility

```python
open_mock.assert_called_once_with(ANY, 'r')
open_mock.assert_called_once_with(mock.ANY, 'r')
```