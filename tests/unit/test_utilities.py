import unittest

import utilities as utilities


class UtilitiesTests(unittest.TestCase):

    def test_hash_matches(self):
        assert utilities.hash_matches('01/01/2020', 'blah') is True


    def test_hash_does_not_match(self):
        assert utilities.hash_matches('tomorrow', 'blah') is False
