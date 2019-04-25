from contextlib import redirect_stdout
import io
import unittest


SHAPES = {
    'circle': Circle,
    'dot': Dot,
}

def Shape(shape):
    try:
        cls_ = SHAPES[shape]
    except KeyError as e:
        keys = list(SHAPES.keys())
        e.message = e.message + f"No such shape. Choose one of {keys}"
        raise
    return cls_()


class Circle:
    def draw(self):
        print('o')


class Dot:
    def draw(self):
        print('.')


class Rectangle:
    def draw(self):
        print('[]')


class ShapeTests(unittest.TestCase):
    def test_circle(self):
        self._test(shape=Shape('circle'),
                   expected_output='o')

    def test_dot(self):
        self._test(shape=Shape('dot'),
                   expected_output='.')

    def test_rectangle(self):
        self._test(shape=Rectangle(),
                   expected_output='[]')

    def _test(self, shape, expected_output):
        f = io.StringIO()
        with redirect_stdout(f):
            shape.draw()
        output = f.getvalue()
        self.assertEqual(output, expected_output+'\n')


if __name__ == "__main__":
    unittest.main()
