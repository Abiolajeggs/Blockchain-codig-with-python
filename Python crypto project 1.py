import hashlib
class EthereumCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "_".join(transaction_list) + "_" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Abiola sends 2 ETH to Christopher"
t2 = "Ayodeji sends 5 ETH to Christopher"
t3 = "Christopher sends 30 ETH to Lotanna"
t4 = "lotanna send 10 ETH to Ayodeji"
t5 = "Abiola send 15 ETH to Ayodeji"
t6 = "Christopher sends 45 ETH to Abiola"
t7 = "Abiola sends 4 ETH to Christopher"
t8 = "Ayodeji sends 25 ETH to Christopher"
t9 = "Christopher sends 300 ETH to Lotanna"
t10 = "lotanna send 100 ETH to Ayodeji"
t11 = "Abiola send 125 ETH to Ayodeji"
t12 = "Christopher sends 245 ETH to Abiola"
t13 = "Abiola sends 23 ETH to Christopher"
t14 = "Ayodeji sends 50 ETH to Christopher"
t15 = "Christopher sends 330 ETH to Lotanna"
t16 = "lotanna send 130 ETH to Ayodeji"
t17 = "Abiola send 1235 ETH to Ayodeji"
t18 = "Christopher sends 425 ETH to Abiola"
t19 = "Abiola sends 200 ETH to Christopher"
t20 = "Ayodeji sends 523 ETH to Christopher"
t21 = "Christopher sends 330 ETH to Lotanna"
t22 = "lotanna send 1090 ETH to Ayodeji"
t23 = "Abiola send 135 ETH to Ayodeji"
t24 = "Christopher sends 415 ETH to Abiola"
t25 = "Abiola sends 221 ETH to Christopher"
t26 = "Ayodeji sends 523 ETH to Christopher"
t27 = "Christopher sends 330 ETH to Lotanna"
t28 = "lotanna send 120 ETH to Ayodeji"
t29 = "Abiola send 1125 ETH to Ayodeji"
t30 = "Christopher sends 4325 ETH to Abiola"

initial_block = EthereumCoinBlock("Initial String" , [t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = EthereumCoinBlock(initial_block.block_hash,[t3,t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = EthereumCoinBlock(second_block.block_hash,[t5,t6])
print(third_block.block_data)
print(third_block.block_hash)

fourth_block = EthereumCoinBlock(third_block.block_hash,[t7,t8])
print(fourth_block.block_data)
print(fourth_block.block_hash)

fifth_block = EthereumCoinBlock(fourth_block.block_hash,[t9,t10])
print(fifth_block.block_data)
print(fifth_block.block_hash)

sixth_block = EthereumCoinBlock(fifth_block.block_hash,[t11,t12])
print(sixth_block.block_data)
print(sixth_block.block_hash)

seventh_block = EthereumCoinBlock(sixth_block.block_hash,[t13,t14])
print(seventh_block.block_data)
print(seventh_block.block_hash)

eighth_block = EthereumCoinBlock(seventh_block.block_hash,[t15,t16])
print(eighth_block.block_data)
print(eighth_block.block_hash)

ninth_block = EthereumCoinBlock(eighth_block.block_hash,[t17,t18])
print(ninth_block.block_data)
print(ninth_block.block_hash)

tenth_block = EthereumCoinBlock(ninth_block.block_hash,[t19,t20])
print(tenth_block.block_data)
print(tenth_block.block_hash)
