# Greg's Proof/validation

import hashlib
import requests
import sys
from uuid import uuid4
from timeit import default_timer as timer
import random

def proof_of_work(oldProof, difficulty):
    proof = 0
    while valid_proof(oldProof, proof, difficulty) is False:
        proof += 1
    return proof

def valid_proof(oldProof, proof, difficulty):
    guess = f"{oldProof}{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    # return True or False - [:3] = slice off first 3 digits
    if guess_hash[:difficulty] == "0" * difficulty:
        print("Solution found - ", guess_hash)
        print("Proof found as solution is: ", proof)
        print("Raw guess is - ", guess)
    return guess_hash[:difficulty] == "0" * difficulty


