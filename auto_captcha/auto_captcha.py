import requests
import time
import os

API_KEY = os.getenv("CAPTCHA_API_KEY")
CAPTCHA_URL = "https://2captcha.com/in.php"
RESULT_URL = "https://2captcha.com/res.php"

def solve_captcha(image_path):
    with open(image_path, 'rb') as captcha_file:
        response = requests.post(CAPTCHA_URL, files={'file': captcha_file}, data={
            'key': API_KEY,
            'method': 'post',
            'json': 1
        })
    if response.status_code == 200 and response.json().get("status") == 1:
        captcha_id = response.json().get("request")
    else:
        raise Exception("Error when sending captcha:", response.text)
    
    print("Captcha sent, waiting for results...")

    while True:
        time.sleep(5)
        result = requests.get(RESULT_URL, params={
            'key': API_KEY,
            'action': 'get',
            'id': captcha_id,
            'json': 1
        })
        result_data = result.json()

        if result_data.get("status") == 1:
            print("Captcha solved!")
            return result_data.get("request")
        elif result_data.get("request") == "CAPTCHA_NOT_READY":
            print("The captcha solution is not ready yet, we continue to wait...")
            continue
        else:
            raise Exception("Error when getting result:", result_data)
        
if __name__ == "__main__":
    image_path = 'captcha_image.jpg'
    print(f"Captcha text: {solve_captcha(image_path)}")