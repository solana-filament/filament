import json
import os
import solana
import typing
from dotenv import load_dotenv
from dotenv import dotenv_values
import sys

sys.path.append('src')
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction, TransactionInstruction, AccountMeta
from src.account.transaction import Transaction
from src.achievement.checkAchievement import check_voted_on_mango


def get_account():
    # Initalize env and client
    load_dotenv()
    # load .env
    cluster = os.environ.get("MAINNET_URL")
    solana_client = Client(cluster)
    print(solana_client)
    config = dotenv_values(".env.local")
    address = config['A_ADDRESS']
    transactions = get_list_of_transaction_limit(
        address, solana_client, 100
    )
    count = 0
    flag = False
    transaction_objects = []
    for transaction in transactions["result"]:
        transaction_objects.append(
            initalize_transaction(
                transaction["blockTime"],
                transaction["confirmationStatus"],
                transaction["signature"],
                transaction["slot"],
                solana_client.get_confirmed_transaction(transaction["signature"])
            )
        )
        if check_voted_on_mango(transaction_objects[count]):
            flag = True
        print(transaction_objects[count].summary())
        count += 1
    print("Total Transactions: ", count)
    print("Voted: {}".format(flag))
    # print(type(solana_client.get_confirmed_transaction("215d6voD2kEGJCrqYjHqadKd65hzVc7vzMWipdiHu19UxoprhUcABjArEQ3zCePdcDkLtN9mrrmj9U1ZjxH5cb4W")))
    # print("----------------------------")
    # print(solana_client.get_confirmed_transaction(config['COPE_VOTE_ADD'])['result']['meta']['logMessages'])
    # list = solana_client.get_confirmed_transaction(config['COPE_VOTE_ADD'])['result']['meta']['logMessages']


def get_list_of_transaction_limit(
    account: str, client: Client, limit_amount: int
) -> typing.List:
    return client.get_confirmed_signature_for_address2(account, limit=limit_amount)


def get_list_of_transaction(account: str, client: Client) -> typing.Dict:
    return client.get_confirmed_signature_for_address2(account)


def initalize_transaction(
    blockTime: str, confirmationStatus: str, signature: str, slot: str, meta: typing.Dict) -> Transaction:

    return Transaction(blockTime, confirmationStatus, signature, slot, meta)


get_account()
