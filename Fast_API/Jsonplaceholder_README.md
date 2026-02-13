## 🧠 What is a Virtual Environment?

A virtual environment (venv) is an isolated Python environment where you can:

Install project-specific packages

Avoid version conflicts

Keep global Python clean

Maintain different dependencies for different projects

Example:
Project A → FastAPI 0.95
Project B → FastAPI 0.110
Both can run safely using separate venvs.

### ✅ Step 1: Check Python Installation

Open terminal / CMD:

python --version


OR

python3 --version


If not installed → Download from:
👉 https://www.python.org/downloads/

⚠️ During installation (Windows), check:
✔️ “Add Python to PATH”

### ✅ Step 2: Create a Virtual Environment

Go to your project folder:

cd FAST_API


Create venv:

🔹 Windows
python -m venv myenv

🔹 macOS / Linux
python3 -m venv myenv


This creates a folder:

FAST_API/
   ├── myenv/

### ✅ Step 3: Activate Virtual Environment
🪟 Windows (CMD)
```
myenv\Scripts\activate
```

🪟 Windows (PowerShell)
```
myenv\Scripts\Activate.ps1
```

🍎 macOS / Linux
```
source venv/bin/activate
```

if getting any error like "running scripts is disabled on this system", This error happens in Windows PowerShell because script execution is blocked by default for security reasons.
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
myenv\Scripts\activate
```


If successful, you’ll see:
```
(myenv) C:\my_project>
```

### ✅ Step 4: Install Packages

Now install packages inside myenv:
```
pip install fastapi uvicorn pydantic
```

Check installed packages:
```
pip list
```

### ✅ Step 5: Freeze Requirements

Save dependencies:
```
pip freeze > requirements.txt
```

Later install from file:
```
pip install -r requirements.txt
```

✅ Step 6: Deactivate Virtual Environment
```
deactivate
```

## 🐳 Using Virtual Environment with FastAPI (Example)
```
python -m venv myenv
myenv\Scripts\activate
pip install fastapi uvicorn pydantic
```

## 📦 What Each Package Does
| Package  | Purpose                          |
| -------- | -------------------------------- |
| fastapi  | Web framework                    |
| uvicorn  | ASGI server to run FastAPI       |
| pydantic | Data validation & request models |


⚡ Alternative Tools (Advanced)

Instead of venv, you can use:
| Tool       | Purpose                           |
| ---------- | --------------------------------- |
| virtualenv | Advanced version of venv          |
| pipenv     | Combines pip + venv               |
| poetry     | Dependency + packaging management |
| conda      | For data science                  |

## 🚀 Hit Postman from Python code
You want to trigger this endpoint from Python:

https://jsonplaceholder.typicode.com/posts


Let me show you both GET and POST versions clearly.

**✅ 1️⃣ POST Request (Same as Your Postman Example)**

Install requests (if not installed)
```
pip install requests
```

Python Code
```
import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response Body:", response.json())
```

**🔎 What happens internally?**

    -   requests.post() → sends HTTP POST
    -   json=payload → converts Python dict → JSON automatically
    -   Server returns response
    -   response.json() → converts JSON → Python dict

**✅ Expected Output**
```
Status Code: 201
Response Body: {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
    'id': 101
}
```

**✅ 2️⃣ GET Request Example (Fetch Posts)**

If you just want to fetch posts:
```
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("Status Code:", response.status_code)
print("First Post:", response.json()[0])
```