# Transaction class
# Holds important information of a solana transaction
class Transaction:
    def __init__(
        self, blockTime: str, confirmationStatus: str, signature: str, slot: str
    ):
        self.blockTime = blockTime
        self.confirmationStatus = confirmationStatus
        self.signature = signature
        self.slot = slot

    def summary(self) -> str:
        return "signature: {}, slot: {}, blockTime: {}, confirmationStatus: {}".format(
            self.signature, self.slot, self.blockTime, self.confirmationStatus
        )
