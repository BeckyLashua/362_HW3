from credit_card_validator import credit_card_validator
import random
import unittest

class TestCase(unittest.TestCase):
    def test_1(self):
        prefixes = [50, 51, 55, 56, 2220, 2221, 2720, 2721, 33, 34, 35, 37, 38]
        lengths = [14, 15, 16, 17]
        tests_to_generate = 10000
        for i in range(tests_to_generate):
            for prefix in range(len(prefixes)):
                for length in range(len(lengths)):
                    card = ''
                    card = card + ''.join(str(prefixes[prefix]))
                    remaining = lengths[length] - len(card)
                    for dig in range(remaining):
                        card = card + ''.join(str(random.randint(0, 9)))
                    credit_card_validator(card)

if __name__ == '__main__':
    unittest.main()
   
