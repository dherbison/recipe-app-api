from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase
from unittest.mock import patch


class CommandTests(TestCase):

    def setUp(self):
        # mocks with gi
        self.gi = patch('django.db.utils.ConnectionHandler.__getitem__')

    def test_wait_for_db_ready(self):
       with self.gi as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    # basicall the same as the gi with above
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        with self.gi as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
