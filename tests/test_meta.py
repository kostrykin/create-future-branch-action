import datetime
import unittest

import meta


class meta_Test(unittest.TestCase):

    def test(self):
        fixtures = [
            (
                datetime.datetime(2025, 1, 15),
                {
                    'branch': 'future/ws26',
                    'branch-name': 'ws26',
                }
            ),
            (
                datetime.datetime(2025, 3, 15),
                {
                    'branch': 'future/ws26',
                    'branch-name': 'ws26',
                }
            ),
            (
                datetime.datetime(2025, 4, 15),
                {
                    'branch': 'future/ss26',
                    'branch-name': 'ss26',
                }
            ),
            (
                datetime.datetime(2025, 8, 15),
                {
                    'branch': 'future/ss26',
                    'branch-name': 'ss26',
                }
            ),
            (
                datetime.datetime(2025, 9, 15),
                {
                    'branch': 'future/ws26',
                    'branch-name': 'ws26',
                }
            ),
            (
                datetime.datetime(2025, 12, 15),
                {
                    'branch': 'future/ws26',
                    'branch-name': 'ws26',
                }
            ),
        ]
        for today, expected in fixtures:
            with self.subTest(today=today):
                actual = meta.expand(today)
                self.assertEqual(actual, expected)