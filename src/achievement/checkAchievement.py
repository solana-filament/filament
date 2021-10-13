import os
from src.account.transaction import Transaction

def check_voted_on_mango(Transaction) -> bool:
    meta = Transaction.meta['result']['meta']['logMessages']
    for i, val in enumerate(meta):
        print(val)
        if(os.environ.get('MANGO_GOVERN')) in val:
            return True
    return False