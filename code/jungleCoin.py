import hashlib


class JungleCoin:

    def __init__(self, previous_block_hash, transaction_list, data=None):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        if data is None:
            self.block_data = f"\n - {' - '.join(transaction_list)} - {previous_block_hash}"
        else:
            self.block_data = data

        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

