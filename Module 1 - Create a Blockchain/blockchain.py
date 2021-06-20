# Module 1: Create a Blockchain
# To be installed
# Flask == 0.12.2
# Postman HTTP Client

# Importing Libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1: Building a blockchain

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1 , previous_hash = '0') # Can choose arbitrary values for proof and previous_hash, sticking to common practice values
        
    def create_block(self, proof, previous_hash):
        block : {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]