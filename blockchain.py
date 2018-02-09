# -*- coding: utf-8 -*-
from genesis import *
from new_block import *

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    blocks_to_add = next_block(previous_block)
    blockchain.append(blocks_to_add)
    previous_block = blocks_to_add
    print("Blockがチェーンに追加されました".format(blocks_to_add.index))
    print("Hash : {}".format(blocks_to_add.hash))
