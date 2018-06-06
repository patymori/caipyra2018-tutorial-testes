import unittest
from unittest.mock import patch, MagicMock

import db_driver
from database import DatabaseManager


class DatabaseManagerTest(unittest.TestCase):

    def test_connect_calls_db_driver_connect(self):
        database_manager = DatabaseManager(
            uri='https://db:5555',
            user='admin',
            password='supersenha'
        )
        with patch.object(db_driver, 'connect') as mocked_connect:
            database_manager.connect()
            mocked_connect.assert_called_once_with(
                uri='https://db:5555',
                user='admin',
                password='supersenha'
            )


if __name__ == '__main__':
  unittest.main()

