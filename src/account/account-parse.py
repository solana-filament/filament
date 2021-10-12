
import json
import os
import solana
from solana.publickey import PublicKey
from solana.rpc.api import Client
from dotenv import load_dotenv
import typing
def get_account():
    load_dotenv()
    cluster = os.environ.get('MAINNET_URL')
    solana_client = Client(cluster)
    print(solana_client)
    print(os.environ)
    transactions = get_list_of_transaction_limit("65vCqwh1tkFhbXSRFCoKqDMN8YVVp9bh7uHh4c4AhD4T", solana_client, 1000)
    count = 0
    for transaction in transactions['result']:
        print("Signature: ", parse_transaction_for_signature(transaction))
        count += 1
    print("Total Transactions: ", count)


def get_list_of_transaction_limit(account: str, client: Client, limit_amount: int) -> typing.List:
    return client.get_confirmed_signature_for_address2(account, limit = limit_amount)

def get_list_of_transaction(account: str, client: Client) -> typing.List:
    return client.get_confirmed_signature_for_address2(account)

def parse_transaction_for_signature(transaction: typing.List) -> str:
    return transaction['signature']

get_account()