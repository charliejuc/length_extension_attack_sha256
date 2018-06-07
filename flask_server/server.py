import json, base64
from flask import Flask, request
from sys import stderr
from hashlib import sha256, sha512

def sha256_hex(message):
	return sha256(message)\
			.hexdigest()

def dbl_sha256_hex(message):
	return sha256_hex(
		sha256(message)
			.digest()
	)

def sha512_hex(message):
	return sha512(message)\
			.hexdigest()


def hmac_sha512_hex(key, message):
	return sha512_hex(
			key + sha512(key + message).digest()
		)

app = Flask(__name__)

username = 'Mike'
hash_pass = 'fsdafas21fdsasdf873729482*?sdfsa--s'

@app.route('/get_user_data', methods=['POST'])
def get_user_data():
	data = request.form or request.get_json()

	signature = data.get('signature', None)
	data_to_show = data.get('data_to_show', '')

	if signature is None:
		return json.dumps({
				'error': 'No signature'
			})

	message = base64.b64decode(data_to_show)
	full_message = hash_pass.encode() + message

	# valid_signature = hmac_sha512_hex(hash_pass.encode(), message)
	valid_signature = sha256_hex(full_message)

	print('Valid Signature: ', valid_signature)
	print('Signature: ', signature)

	if valid_signature != signature:
		return json.dumps({
				'error': 'Invalid signature'
			})

	response_data = {
		'valid': True
	}

	if b'username' in message:
		response_data['username'] = username

	if b'credit_card' in message:
		response_data['credit_card'] = 'XXXX-XXXX-XXXX-XX37'

	return json.dumps(response_data)


app.run(debug=True, host='0.0.0.0')