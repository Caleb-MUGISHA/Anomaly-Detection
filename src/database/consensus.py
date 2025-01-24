from sqlalchemy import text
from typing import List
import logging
from .models import get_engine

class DatabaseCluster:
    def __init__(self, nodes: List[str]):
        self.nodes = [get_engine() for _ in nodes]  # Simplified for example
        self.quorum = len(nodes) // 2 + 1
        
    def write_transaction(self, transaction: dict) -> bool:
        successes = 0
        query = text("""
            INSERT INTO transactions 
            (user_id, amount, currency, timestamp, merchant, location, is_fraud)
            VALUES (:user_id, :amount, :currency, :timestamp, :merchant, :location, :is_fraud)
        """)
        
        for engine in self.nodes:
            try:
                with engine.connect() as conn:
                    conn.execute(query, **transaction)
                    conn.commit()
                    successes += 1
                    if successes >= self.quorum:
                        return True
            except Exception as e:
                logging.error(f"Database write failed: {str(e)}")
        return False
