import requests

url = "https://pitchfork.com/reviews/albums/?page="

counter = 1

while True:

    try:
        response = requests.get(url+str(counter))
        print(response.status_code)

    except:
        pass

    counter += 1

