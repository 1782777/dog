import requests
import cv2

# url ="http://182.92.114.73:8080/"
url ="http://127.0.0.1:8080/"

data ='{"key":"value"}'

res = requests.post(url=url,data=data)
print res.text
