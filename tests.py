from credit_card_validator import credit_card_validator
import random
import unittest

class TestCase(unittest.TestCase):
    def test_1(self):
        prefixes = [4, 50, 51, 55, 56, 2220, 2221, 2720, 2721, 33, 34, 35, 37, 38]
        lengths = [14, 15, 16, 17]
        tests_to_generate = 500000
        for i in range(tests_to_generate):
            # Pick a random prefix from prefix array
            prefix = random.choice(prefixes)
            # pick a random length from lenths array
            length = random.choice(lengths)
            # add prefix to card variable
            card = ''
            card = card + ''.join(str(prefix))
            # add random digits for remaining length of card
            remaining = length - len(card)
            for dig in range(remaining):
                card = card + ''.join(str(random.randint(0, 9)))
            credit_card_validator(card)

if __name__ == '__main__':
    unittest.main()
   
