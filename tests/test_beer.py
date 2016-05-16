import unittest
from beer.beer import Beer


class TestBeer(unittest.TestCase):
    def test_serialize_beer(self):
        serialized = Beer.serialize_beer("qmQM.eE-")

        self.assertEqual(serialized, "BEER∫BEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEER∫µ∫µµµµµµµµµµµµµµµµµµµµµµµµµµ∫BEER-BEER∫BEERBEERBEER∫E-")

    def test_deserialize_beer(self):
        deserialized = Beer.deserialize_beer("BEER∫BEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEERBEER∫µ∫µµµµµµµµµµµµµµµµµµµµµµµµµµ∫BEER-BEER∫BEERBEERBEER∫E-")

        self.assertEqual(deserialized, "qmQM.eE-")

    def test_loop_beer(self):
        deserialized = Beer.deserialize_beer(Beer.serialize_beer("QPqpALalYMymberBER,.-12#"))

        self.assertEqual(deserialized, "QPqpALalYMymberBER,.-12#")


if __name__ == '__main__':
    unittest.main()
