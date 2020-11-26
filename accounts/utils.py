from random import randint

from kavenegar import *

api = KavenegarAPI('3264344264755A6C6F3352492F71684D50616A455930764D714B68634F784A544D55436C76684348715A453D')

def random_number_generator():
    rand_num = randint(10000, 99999)
    return rand_num


def send_message(phone_number, message, random_number):
    full_message = message + str(random_number)
    try:
        params = { 'sender' : '1000596446', 'receptor': phone_number, 'message' :full_message }
        response = api.sms_send( params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)
    return random_number
