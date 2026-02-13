import requests

def create_post(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"
    
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)

result = create_post("AI Post", "Learning API calls", 10)
print(result)
