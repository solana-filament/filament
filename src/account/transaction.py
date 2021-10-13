from typing import Dict
# Transaction class
# Holds important information of a solana transaction
class Transaction:
    def __init__(
        self, blockTime: str, confirmationStatus: str, signature: str, slot: str, meta: Dict):
        self.blockTime = blockTime
        self.confirmationStatus = confirmationStatus
        self.signature = signature
        self.slot = slot
        self.meta = meta

    def summary(self) -> str:
        return "signature: {}, slot: {}, blockTime: {}, confirmationStatus: {}".format(
            self.signature, self.slot, self.blockTime, self.confirmationStatus
        )
    def set_meta(self, metaData):
        self.meta = metaData
