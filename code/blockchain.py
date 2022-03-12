from jungleCoin import JungleCoin
import os


class Blockchain:
    def __init__(self):
        self.chain = []
        if not os.path.isfile("blockchain_data/Data/data 1.txt"):
            self.generate_genesis_block()
        else:
            read = open("blockchain_data/sheet.txt").readline()
            for r in range(int(read)):
                self.chain.append(JungleCoin(0, 0, open(f"blockchain_data/Data/data {r + 1}.txt", "r+").read()))

    def generate_genesis_block(self):
        self.chain.append(JungleCoin("0", ['Genesis Block']))
        open("blockchain_data/Data/data 1.txt", "w+").write(f"{self.chain[0].block_data}\n")
        open("blockchain_data/Hash/hash 1.txt", "w+").write(f"{self.chain[0].block_hash}\n")
        open("blockchain_data/sheet.txt", "w+").write(str(1))

    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(JungleCoin(previous_block_hash, transaction_list))
        for i in range(len(self.chain)):
            if not os.path.isfile(f"blockchain_data/Hash/hash {i + 1}.txt"):
                open(f"blockchain_data/Hash/hash {i + 1}.txt", "w+").write(f"{self.chain[i].block_hash}\n")
            else:
                if not open(f"blockchain_data/Hash/hash {i + 1}.txt", "r+").readline() == self.chain[
                    i].block_hash + "\n":
                    open(f"blockchain_data/Hash/hash {i + 1}.txt", "w+").write(f"{self.chain[i].block_hash}\n")
                    open(f"blockchain_data/Data/data {i + 1}.txt", "w+").write(f"{self.chain[i].block_data}")

            if not os.path.isfile(f"blockchain_data/Data/data {i + 1}.txt"):
                open(f"blockchain_data/Data/data {i + 1}.txt", "w+").write(f"{self.chain[i].block_data}")
            open("blockchain_data/sheet.txt", "w+").write(str(i + 1))

    def display_chain(self):
        print("-------------------------------------------------------------------------------------------------------")
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")
        print("-------------------------------------------------------------------------------------------------------")

    def erase(self):
        for o in range(int(open("blockchain_data/sheet.txt", "r+").readline())):
            os.remove(f"blockchain_data/Data/data {o + 1}.txt")
            os.remove(f"blockchain_data/Hash/hash {o + 1}.txt")
        open("blockchain_data/sheet.txt", "w+").write("")

    @property
    def last_block(self):
        return self.chain[-1]
