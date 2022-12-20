import requests
key = "e369f4d8b7464a52b956274c83ace328"
api_address1 = "https://newsapi.org/v2/top-headlines?country=us&apiKey="+ key


json_data1 = requests.get(api_address1).json()
ar =[]

def news():
    for i in range(3):
        ar.append("Number" + str(i+1) + ", " + json_data1["articles"][i]["title"]+".")
        return ar








