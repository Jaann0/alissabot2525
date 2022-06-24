import requests
from flask import Flask,

alfa = input()
url = "https://moviesdatabase.p.rapidapi.com/titles/search/title/" + alfa
querystring = {"info":"mini_info","limit":"2","page":"1","titleType":"movie"}
headers = {
	"X-RapidAPI-Key": "082395124cmsh8f011e89c74584fp1b5c87jsn52b9ca1173b4",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)