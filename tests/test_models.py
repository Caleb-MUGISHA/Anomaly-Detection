import unittest
from src.database.models import Transaction, get_engine

class TestModels(unittest.TestCase):
    def setUp(self):
        self.engine = get_engine()
        
    def test_table_creation(self):
        Transaction.__table__.create(self.engine)
        # Verify table exists
        self.assertTrue(self.engine.dialect.has_table(self.engine, 'transactions'))
