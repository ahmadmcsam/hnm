import unittest
from src.hello_world.main import hello

class TestHello(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello('World'), 'Hello, World!')

    def test_hello_name(self):
        self.assertEqual(hello('Alice'), 'Hello, Alice!')

if __name__ == '__main__':
    unittest.main()