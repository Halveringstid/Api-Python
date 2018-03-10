from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

data = {
    "id":"6969692137",
    "lat" : 50.032379,
    "lon" : 19.923905,
    "message": "Drogo w tym tesco, lol!",
    "author":"karol69",
    "created_at": "ISO8601",
    "type": "message"
}


bdb = BigchainDB('http://80.211.240.79:59984/')
alice = generate_keypair()
tx = bdb.transactions.prepare(
    operation ='CREATE',
    signers = alice.public_key,
    asset = {'data': data, 'metadata': {"type": "message"}})
signed_tx = bdb.transactions.fulfill(
    tx,
    private_keys = alice.private_key)
bdb.transactions.send(signed_tx)