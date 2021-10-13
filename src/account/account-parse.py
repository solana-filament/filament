import json
import os
import solana
import typing
from dotenv import load_dotenv
from dotenv import dotenv_values

from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction, TransactionInstruction, AccountMeta
from transaction import Transaction


def get_account():
    # Initalize env and client
    load_dotenv()
    # load .env
    cluster = os.environ.get("MAINNET_URL")
    solana_client = Client(cluster)
    print(solana_client)
    config = dotenv_values(".env.local")

    transactions = get_list_of_transaction_limit(
        config['P_ADDRESS'], solana_client, 200
    )
    solana_client.get_balance("65vCqwh1tkFhbXSRFCoKqDMN8YVVp9bh7uHh4c4AhD4T", "processed")
    count = 0
    transaction_objects = []
    for transaction in transactions["result"]:
        transaction_objects.append(
            initalize_transaction(
                transaction["blockTime"],
                transaction["confirmationStatus"],
                transaction["signature"],
                transaction["slot"],
            )
        )
        print(transaction_objects[count].summary())
        count += 1
    print("Total Transactions: ", count)


def get_list_of_transaction_limit(
    account: str, client: Client, limit_amount: int
) -> typing.List:
    return client.get_confirmed_signature_for_address2(account, limit=limit_amount)


def get_list_of_transaction(account: str, client: Client) -> typing.Dict:
    return client.get_confirmed_signature_for_address2(account)


def initalize_transaction(
    blockTime: str, confirmationStatus: str, signature: str, slot: str
) -> Transaction:
    return Transaction(blockTime, confirmationStatus, signature, slot)


get_account()
