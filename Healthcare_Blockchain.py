# MedChain - Pooya Farrokhi - Fall 2022
# Blockchain (MITS-6900G)
# Professor Ahmed Munieb Sheikh
import sys
import json
import hashlib

from flask import Flask
from time import time
from uuid import uuid4
from urllib.parse import urlparse
from flask.globals import request
from flask.json import jsonify
import datetime
import binascii
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode
from uuid import uuid4

'''############################## Entities #############################'''


# The central authority that controls the permissions and the blockchain
class CA(object):
    def __init__(self):
        self._clients = []
        # Generate key-pair for the CA
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(2048, random)
        self._public_key = self._private_key.publickey()
        # add CA as a client
        self._clients.append({
            'client_id': str(uuid4()).replace('-', ""),
            'public_key': b64encode(self._public_key.exportKey()).decode('ascii'),
            'persona_level': 'CA',
            'name': 'Central Authority',
            'address': 'Ontario Tech University'
        })

    # add client to the public key directory, determining the accessibility, and returning the private key
    # persona levels supported: patient - practitioner - pharmacy
    def new_client(self, persona, name, address):
        # check validation with authorities
        if not validated(persona, name, address):
            return None
        # Generate key-pair for the CA
        random = Crypto.Random.new().read
        private_key = RSA.generate(2048, random)
        public_key = self._private_key.publickey()
        client_id = str(uuid4()).replace('-', "")
        # Add the right persona
        self._clients.append({
            'client_id': client_id,
            'public_key': b64encode(public_key.exportKey()).decode('ascii'),
            'persona_level': persona,
            'name': name,
            'address': address
        })
        # returning the private key to the client during the signup. The private_key will not be saved.
        return b64encode(private_key.exportKey()).decode('ascii'), client_id

    def get_persona_level(self, client_id):
        for client in self._clients:
            if client['client_id'] == client_id:
                return client['persona_level']
        return None

    def get_public_key(self, client_id):
        for client in self._clients:
            if client['client_id'] == client_id:
                return client['public_key']
        return None
    '''
    # calculate nonce
    def calculate_nonce(self, index, previous_block_hash, transactions):
        nonce = 0
        while self.validate_Proof(index, previous_block_hash, transactions, nonce) is False:
            nonce += 1
            # print(nonce)
        print(f'nonce is : {nonce}')
        return nonce
    '''

    # Validate the previous block in the chain
    def validate_block(self, block):
        # get and remove the signed hash
        blk = block.copy()
        last_hash_signed = blk.pop('current_signed_hash', None)
        last_block_hash = MedCrypt().hash(blk)
        if _ca.validate_signature(last_block_hash, last_hash_signed):
            return last_block_hash
        return None

    # Validate the signature with every certified public key in the system
    def validate_signature(self, original, signed):
        for client in self._clients:
            if MedCrypt(public_key=client['public_key']).verify_signature(original, signed):
                return True
        return False

    '''
    def validate_Proof(self, index, previous_block_hash, transactions, nonce):
        data = f'{index},{previous_block_hash},{transactions},{nonce}'.encode()
        hash_data = hashlib.sha256(data).hexdigest()
        return hash_data[:len(self.difficulty_level)] == self.difficulty_level
    '''

    @property
    def private_key(self):
        return b64encode(self._private_key.exportKey()).decode('ascii')

    @property
    def public_key(self):
        return b64encode(self._public_key.exportKey()).decode('ascii')

    @property
    def clients(self):
        return self._clients


# verification process with government or other authorities
def validated(persona, name, address):
    return True  # validate by default

'''
class Client:
    def __init__(self, level):
        self._level = level
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return
binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
'''


# central authority of blockchain
_ca = CA()


# MedChain class inspired by works of Mr. Ahmed Munieb Sheikh from the blockchain course.
class MedChain(object):
    def __init__(self):
        # The chain
        self.chain = []
        self.med_data = []
        # create a default previous has block for the first block
        genesis_hash = MedCrypt().hash("genesis_block")
        # append the first block
        self.append_block(
            previous_block_hash=genesis_hash,
            sender_private_key=_ca.private_key
        )

    def append_block(self, previous_block_hash, sender_private_key):
        block = {
            'index': len(self.chain),
            'med_data': self.med_data,
            'timestamp': time(),
            'previous_block_hash': previous_block_hash
        }
        # sign the current block and add to the block
        self.add_signature(block, sender_private_key, 'current_signed_hash')
        # ready to add to chain
        self.chain.append(block)
        self.med_data = []  # reset the med_data for the next block
        return block

    # add signature to current dictionary
    def add_signature(self, dic, sender_private_key, description='signed_hash'):
        med_crypt = MedCrypt(private_key=sender_private_key)
        dic[description] = med_crypt.sign(med_crypt.hash(dic))

    '''
    # add med_data to the blockchain depending on the persona
    def add_med_data(self, sender_id, receiver_id, drugs, days, signature_key):
        self.med_data.append({
            'sender_id': sender_id,
            'receiver_id': receiver_id
        })
        # check the permissions and accessibility
        persona_level = _ca.get_persona_level(sender_id)
        if persona_level is not None:
            if persona_level == 'patient':

            elif persona_level == 'practitioner':
                self.practitioner_add_prescription(sender_id, receiver_id, drugs,  days, signature_key)
            elif persona_level == 'pharmacy':

        return None
    '''

    # add prescription to the blockchain by practitioner
    def practitioner_add_prescription(self, practitioner_id, patient_id, drugs, days, practitioner_private_key):
        prescription_data = {
            'practitioner_id': practitioner_id,
            'patient_id': patient_id,
            'drugs': drugs
        }
        # encrypt prescription data
        encrypted_prescription_data = MedCrypt(public_key=_ca.get_public_key(patient_id)).encrypt(prescription_data)
        # add to prescription
        self.med_data.append({
            'sender_id': practitioner_id,
            'receiver_id': patient_id,
            # duration of validity of the med_data
            'valid_until': time() + (days * 24 * 60 * 60),
            'data': {
                'type': 'prescription',
                'encrypted_data': encrypted_prescription_data
                # 'id'
            }
        })
        # prescription id: hash the prescription data and sign it with practitioner's private key
        self.add_signature(self.med_data[-1]['data'], practitioner_private_key, 'id')
        return self.last_block['index'] + 1, 'ok'  # return the next index for the future block

    # share(add) the created prescription in the blockchain by patient
    def patient_share_prescription(self, patient_id, clinic_id, patient_private_key, days, prescription_id):
        # get the inquired prescription to share
        med_data = self.get_user_med_data(patient_id)
        encrypted_prescription_data = self.get_encrypted_data(med_data, prescription_id)
        if encrypted_prescription_data is None:
            return None, 'Prescription not found'
        # encryption translation: decrypt with patient's private key and encrypt with the clinic's public key
        med_crypt = MedCrypt(private_key=patient_private_key, public_key=_ca.get_public_key(clinic_id))
        encrypted_data = med_crypt.encrypt(med_crypt.decrypt(encrypted_prescription_data))
        # add to prescription
        self.med_data.append({
            'sender_id': patient_id,
            'receiver_id': clinic_id,
            'valid_until': time() + (days * 24 * 60 * 60),
            'data': {
                'type': 'prescription',
                'encrypted_data': encrypted_data,
                'id': prescription_id  # original prescription_id signed by practitioner
            }
        })
        return self.last_block['index'] + 1, 'ok'  # return the next index for the future block

    # add purchase receipt to the blockchain and revoke prescription by pharmacy
    def pharmacy_add_receipt(self, pharmacy_id, patient_id, drugs, days, pharmacy_private_key, prescription_id):
        # get the user chain shared by patients
        med_data = self.get_user_med_data(pharmacy_id)
        encrypted_prescription_data = self.get_encrypted_data(med_data, prescription_id)
        if encrypted_prescription_data is None:
            return None, 'Prescription not found'
        # decrypt
        prescription_data = MedCrypt(private_key=pharmacy_private_key).decrypt(encrypted_prescription_data)
        # check validity of the prescription
        # verify practitioner's signature
        if self.check_prescription(prescription_data) is False:
            return None, 'Prescription signature does not match'
        # encrypt with the patient's public key
        encrypted_data = MedCrypt(public_key=_ca.get_public_key(patient_id)).encrypt(prescription_data)
        # add receipt
        self.med_data.append({
            'sender_id': pharmacy_id,
            'receiver_id': patient_id,
            'valid_until': time() + (days * 24 * 60 * 60),
            'data': {
                'type': 'receipt',
                'encrypted_data': encrypted_data,
                # 'id': receipt_id  # original prescription_id signed by practitioner
            }
        })
        # receipt id: hash the prescription data and sign it with practitioner's private key
        self.add_signature(self.med_data[-1]['data'], pharmacy_private_key, 'id')
        # revoke and add former prescription
        self.med_data.append({
            'sender_id': pharmacy_id,
            'receiver_id': patient_id,
            'valid_until': time(),  # revoked
            'data': {
                'type': 'prescription',
                'encrypted_data': encrypted_data,
                'id': prescription_id  # original prescription_id signed by practitioner
            }
        })
        return self.last_block['index'] + 1, 'ok'  # return the next index for the future block

    def check_prescription(self, prescription_data):
        # verify practitioner's signature
        med_crypt = MedCrypt(public_key=_ca.get_public_key(prescription_data['practitioner_id']))
        prescription_hash = med_crypt.hash(prescription_data)
        # verify signature
        if med_crypt.verify_signature(prescription_hash, prescription_data['id']):
            return True
        return False

    # get specific user's chain with accessible data
    def get_user_med_data(self, client_id):
        med_data = []
        added_ids = []
        # check the blocks from the latest added
        for block in reversed(self.chain):
            for m_data in block['med_data']:
                # only users that are at the end of receiving the med_data should see the blocks
                if m_data['receiver_id'] == client_id:
                    # filter the data with the same id with the latest on the blockchain
                    if m_data['data']['id'] not in added_ids:
                        # to avoid repeated ids
                        added_ids.append(m_data['data']['id'])
                        # check validity and only show the ones valid
                        if time() <= m_data['valid_until']:
                            med_data.append(m_data)
        return med_data

    # get encrypted data using data id
    def get_encrypted_data(self, med_data, data_id):
        for m_data in med_data:
            if m_data['data']['id'] == data_id:
                return m_data['data']['encrypted_data']
        return None

    @property
    def last_block(self):
        return self.chain[-1]


# a class for hash, signature, and decryption
class MedCrypt(object):
    def __init__(self, private_key=None, public_key=None):
        if private_key is not None:
            self.private_key = RSA.importKey(b64decode(private_key))
        if public_key is not None:
            self.public_key = RSA.importKey(b64decode(public_key))

    # hash dictionary data
    def hash(self, data):
        # json.dumps covert the Python Object into JSON String
        block_encoder = json.dumps(data, sort_keys=True).encode()  # Convert string to byte string
        hash_bin_array = hashlib.sha256(block_encoder).digest()
        return b64encode(hash_bin_array).decode("utf-8")

    # sign dictionary data using private key
    def sign(self, data):
        signer = PKCS1_v1_5.new(self.private_key)  # private_key
        h = SHA.new(str(data).encode('utf8'))
        return b64encode(signer.sign(h)).decode('ascii')

    def verify_signature(self, original_message, signature):
        sig = b64decode(signature)  # convert string to bytes object
        verifier = PKCS1_v1_5.new(self.public_key)
        digest = SHA.new(str(original_message).encode('utf8'))
        verified = verifier.verify(digest, sig)
        return verified

    # encrypt data using a public key
    def encrypt(self, data):
        cipher = PKCS1_OAEP.new(self.public_key)
        encrypted = cipher.encrypt(str(data).encode('utf8'))
        return b64encode(encrypted).decode('ascii')

    # decrypt data using private key
    def decrypt(self, data):
        encrypted = b64decode(data)
        cipher = PKCS1_OAEP.new(self.private_key)
        plain_text = cipher.decrypt(encrypted)
        return plain_text.decode(encoding="UTF-8")


# node_identifier = str(uuid4()).replace('-', "")
medChain = MedChain()

# Flask
app = Flask(__name__)




@app.route('/signup/new', methods=['POST'])
def do_signup():
    values = request.get_json()
    required_fields = ['persona', 'name', 'address']
    if not all(k in values for k in required_fields):
        return 'Missing Fields', 400
    # three supported personas
    required_personas = ['patient', 'practitioner', 'pharmacy']
    if values['persona'] not in required_personas:
        return 'Unsupported Persona Try \"patient / practitioner / pharmacy\"', 400
    '''
    # check if the person has already signed up by address
    persona = _ca.get_persona_level(values['address'])
    if persona is not None:
        return 'You already signed up!', 400
    '''
    # create new client
    private_key, client_id = _ca.new_client(values['persona'], values['name'], values['address'])
    response = {
        'message': 'client added',
        'client_id': client_id,
        'private_key': private_key
    }
    return jsonify(response), 200

# get signup info
@app.route('/signup/show', methods=['GET'])
def show_signup():
    response = {
        'clients': _ca.clients,
        'length': len(_ca.clients)
    }
    return jsonify(response), 200


# get the complete MedChain
@app.route('/medChain', methods=['GET'])
def show_med_chain():
    response = {
        'chain': medChain.chain,
        'length': len(medChain.chain)
    }
    return jsonify(response), 200


# get the meddata for the queried user client_id
@app.route('/meddata', methods=['GET'])
def show_med_data():
    args = request.args
    if "client_id" not in args:
        return "Unsupported query. Try \"client_id\"", 400
    client_id = args['client_id']
    med_data = medChain.get_user_med_data(client_id)
    response = {
        'med_data': med_data,
        'length': len(med_data)
    }
    return jsonify(response), 200

# the doctor will add new prescription
@app.route('/prescription/new', methods=['POST'])
def new_prescription():
    values = request.get_json()
    # get private key from query
    args = request.args
    if "private_key" not in args:
        return "Unsupported query. Try \"private_key\"", 400
    required_fields = ['practitioner_id', 'patient_id', 'drugs', 'validity_duration']
    if not all(k in values for k in required_fields):
        return 'Missing Fields', 400
    # check if it is initiated by an actual practitioner
    persona_level = _ca.get_persona_level(values['practitioner_id'])
    if persona_level != 'practitioner':
        return 'You have to be a practitioner to use prescription', 400

    index = medChain.practitioner_add_prescription(
        values['practitioner_id'],
        values['patient_id'],
        values['drugs'],
        values['validity_duration'],  # days
        args['private_key']
    )
    response = {'message': f'MedData will be added to the block {index}'}
    return jsonify(response), 200

#    def patient_share_prescription(self, patient_id, clinic_id, patient_private_key, days, prescription_id):
# the patient will share the prescription
@app.route('/share/new', methods=['POST'])
def new_share():
    values = request.get_json()
    # get private key from query
    args = request.args
    if "private_key" not in args:
        return "Unsupported query. Try \"private_key\"", 400
    required_fields = ['patient_id', 'clinic_id', 'validity_duration', 'prescription_id']
    if not all(k in values for k in required_fields):
        return 'Missing Fields', 400
    # check if it is initiated by a patient
    persona_level = _ca.get_persona_level(values['patient_id'])
    if persona_level != 'patient':
        return 'You have to be a patient to share prescription', 400

    index = medChain.patient_share_prescription(
        values['patient_id'],
        values['clinic_id'],
        args['private_key'],
        values['validity_duration'],  # days
        values['prescription_id']
    )
    response = {'message': f'MedData will be added to the block {index}'}
    return jsonify(response), 200

# the pharmacy will sell the medicine
@app.route('/purchase/new', methods=['POST'])
def new_purchase():
    values = request.get_json()
    # get private key from query
    args = request.args
    if "private_key" not in args:
        return "Unsupported query. Try \"private_key\"", 400
    required_fields = ['pharmacy_id', 'patient_id', 'drugs', 'validity_duration', 'prescription_id']
    if not all(k in values for k in required_fields):
        return 'Missing Fields', 400
    # check if it is initiated by an actual pharmacist
    persona_level = _ca.get_persona_level(values['pharmacy_id'])
    if persona_level != 'pharmacy':
        return 'You have to be a pharmacy to sell products', 400

    index = medChain.pharmacy_add_receipt(
        values['pharmacy_id'],
        values['patient_id'],
        values['drugs'],
        values['validity_duration'],  # days
        args['private_key'],
        values['prescription_id']
    )
    response = {'message': f'MedData will be added to the block {index}'}
    return jsonify(response), 200

'''
Since this is a private blockchain, there is no PoW, but the chain and the participants will be verified.
As a separate variable, the hash of the current blockchain will be signed by the current system adding the block
(e.g. pharmacy, practitioner, ...) and the next time a new block is added, the last block's signature will be 
verified by comparing the last_block_hash and the decrypted value of last_block_hash_signed. In case of any modification
on the previous blocks, the hash values will be changed in the chain, and the decrypted signature will show different
values, which indicates that the chain was compromised.
'''
@app.route('/selective_endorsement', methods=['GET'])
def selective_endorsement():
    # get the key for the block signature
    args = request.args
    if "private_key" not in args:
        return "Unsupported query. Try \"private_key\"", 400
    # calculations to check the integrity of the blocks - check last block
    private_key = _ca.private_key  # private_key = args['private_key']
    last_block_hash = _ca.validate_block(medChain.last_block)
    if last_block_hash is None:
        return 'Blockchain Compromised', 400
    block = medChain.append_block(last_block_hash, private_key)
    response = {
        'message': "new block has been added by selective endorsement",
        'index': block['index'],
        'hash_of_previous_block': block['previous_block_hash'],
        'signature_of_current_block_hash': block['current_signed_hash'],
        'med_data': block['med_data']
    }
    return jsonify(response), 200

'''
# the pharmacy will add the receipt to the blockchain
@app.route('/purchase', methods=['POST'])
def new_purchase():
    values = request.get_json()
    required_fields = ['sender_id', 'receiver_id', drugs, days]
    if not all(k in values for k in required_fields):
        return 'Missing Fields', 400
    # check if prescription was already used from last purchases
    persona_level = _ca.get_persona_level(values['sender_id'])
    if persona_level is None:
        return 'Persona Not Found', 400

    if persona_level == 'patient':
        medChain.patient_share_prescription()
    elif persona_level == 'practitioner':
        medChain.practitioner_add_prescription(values['sender_id'], values['receiver_id'], drugs, days, signature_key)
    elif persona_level == 'pharmacy':
    index = medChain.add_purchase(
        values['patient_id'],
        values['practitioner_id'],
        values['drugs']
    )
    response = {'message': f'Transaction will be added to the block {index}'}
    return jsonify(response), 200
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
