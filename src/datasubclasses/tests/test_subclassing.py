import unittest

from datasubclasses import init, tool


@init()
class Foo:
    x: int
    y: int

    def __init__(self, x) -> None:
        type(self).__bases__[0].__init__(self, x, x)


class Test1(unittest.TestCase):
    def test_1a(self):
        foo = Foo(42)
        self.assertEqual(foo.x, 42)
        self.assertEqual(foo.y, 42)


if __name__ == "__main__":
    unittest.main()
