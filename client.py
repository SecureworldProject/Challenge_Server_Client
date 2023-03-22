import requests
import random
import socket   

### GLOBAL VARIABLES ###
props_dict = {}




### FUNCTIONS ###
def init(props):
    global props_dict
    print("Python: starting challenge init()")

    # Save properties in the global variable
    props_dict = props
    
    # Execute the challenge once during the init, so key is calculated from the beginning
    executeChallenge()
    return 0




def executeChallenge():
    print("Python: starting executeChallenge()")
    #Get public IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip=s.getsockname()[0]
    print(ip)
    payload={'reading_id':random.randint(0,100),'ip':ip,'data':'1023'}
    response=requests.post("http://localhost:5000/readings",params=payload)
    print(response.json())
    # Get key as UTF-8 and calculate its length
    key = bytes(response.json(), 'utf-8')
    key_size = len(key)

    # The result is a tuple (key, key_size)
    result = (key, key_size)
    print("Python:", result)

    return result


if __name__ == "__main__":
    # Use a dictionary as example of properties obtained from the json
    props_example_dict = {"param1": "hola", "param2": 3}
    init(props_example_dict)
    executeChallenge()








