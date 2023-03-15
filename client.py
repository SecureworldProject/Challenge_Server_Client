import requests
import random

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
    payload={'reading_id':random.randint(0,100),'ip':'192.168.0.4','data':'1023'}
    key=requests.post("http://localhost:5000/readings",params=payload)
    # Get key as UTF-8 and calculate its length
    key = bytes(key, 'utf-8')
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








