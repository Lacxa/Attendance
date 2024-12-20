import requests


def ping_net():
    try:
        code = requests.get("https://attendance-scan-c7af7-default-rtdb.firebaseio.com/")

        print(code.status_code)

        if code.status_code == 200:
            return True

    except:
        return False

