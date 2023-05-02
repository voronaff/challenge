import requests
import sys
import docker
import time
import unittest

def main():
    ms_app = sys.argv[1]

    ports = {
        "ms_a": 5000,
        "ms_b": 5001,
        "ms_c": 5002
    }

    client = docker.from_env()

    cnt = client.containers.run(ms_app + ":latest", remove=True, detach=True, ports={str(ports[ms_app]) + "/tcp": ports[ms_app]})
    
    time.sleep(8)
    URL = "http://localhost:" + str(ports[ms_app])

    try:
        response = requests.get(URL)
    except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))
        cnt.remove(force=True)
        return 1       
    except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        print(str(e))
        cnt.remove(force=True)
        return 1
    except requests.RequestException as e:
        print("OOPS!! General Error")
        print(str(e))
        cnt.remove(force=True)
        return 1
    except KeyboardInterrupt:
        print("Someone closed the program")
        cnt.remove(force=True)
        return 1
    

    if response.status_code == 200:
        print('OK')
        cnt.remove(force=True)
        return 0
    elif response.status_code == 500:
        print('ERROR')
        cnt.remove(force=True)
        return 1
    else:
        print('ERROR')
        cnt.remove(force=True)
        return 1

if __name__ == "__main__":
    main()