import requests
import getpass

BASE_URL = "http://127.0.0.1:8000/api"
AUTH_TOKEN = ""


class TerminalColors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"

br = TerminalColors.BOLD + TerminalColors.RED
bg = TerminalColors.BOLD + TerminalColors.GREEN
by = TerminalColors.BOLD + TerminalColors.YELLOW
bb = TerminalColors.BOLD + TerminalColors.BLUE
def make_request(method, endpoint, data=None):
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {AUTH_TOKEN}"}
   


    if method == "GET":
        response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
    elif method == "POST":
        response = requests.post(f"{BASE_URL}{endpoint}", json=data, headers=headers)
    elif method == "PUT":
        response = requests.put(f"{BASE_URL}{endpoint}", json=data, headers=headers)
    elif method == "DELETE":
        response = requests.delete(f"{BASE_URL}{endpoint}", headers=headers)
    else:
        raise ValueError("Invalid HTTP method")

    return response

def signup():
    print("Signup:")
    email = input("Enter email: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    data = {"email": email, "password": password, "username": username}
    response = make_request("POST", "/auth/signup/", data)
    
    
    

def login():
    print("Login:")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    data = {"password": password, "username": username}
    response = make_request("POST", "/auth/login/", data)
   
    

    global AUTH_TOKEN
    AUTH_TOKEN = response.json().get("access_token", "")
    response.json().get("access_token", "")
    print(f"{TerminalColors.BOLD}{TerminalColors.GREEN}Response:, {response.json()}!{TerminalColors.RESET}")
    
    
    

def get_note_by_id():
    print("Get All Notes:")
    id = input("Enter Note ID: ")
    response = make_request("GET", f"/notes/{id}/")
    print(f"{TerminalColors.BOLD}{TerminalColors.GREEN}Response:, {response.json()}!{TerminalColors.RESET}")
    
    
    

def create_note():
    print("Create Note:")
    title = input("Enter Note Title: ")
    content = input("Enter Note Content: ")
    data = {"title" : title , "content" : content}
    response = make_request("POST", f"/notes/", data)
    print(f"{TerminalColors.BOLD}{TerminalColors.GREEN}Response:, {response.json()}!{TerminalColors.RESET}")
    
    
    

def delete_note():
    print("Delete Note:")
    id = input("Enter Note ID: ")
    response = make_request("DELETE", f"/notes/{id}/")
    if response.status_code == 204:
        print(f"{TerminalColors.BOLD}{TerminalColors.GREEN}Response:, Note Deleted Successfully!{TerminalColors.RESET}")
    else:
        print(f"{TerminalColors.BOLD}{TerminalColors.GREEN}Response: {response.json()}!{TerminalColors.RESET}")
    
    
    

def edit_note():
    print("Edit Note:")
    id = input("Enter Note ID: ")
    title = input("Enter Something to Update Title or Hit Enter to Skip: ")
    content = input("Enter Something to UpdateContent or Hit Enter to Skip: ")
    data = {"title" : title , "content" : content}
    response = make_request("PUT", f"/notes/{id}/", data)
    print(f"{TerminalColors.BOLD}{TerminalColors.GREEN}Response:, {response.json()}!{TerminalColors.RESET}")
    
    
    

def share_note():
    print("Edit Note:")
    id = input("Enter Note ID: ")
    username = input("Enter the username you want to share the note: ")
    data = {"username":username}
    response = make_request("POST", f"/notes/{id}/share/", data)
    print(f"{TerminalColors.BOLD}{TerminalColors.GREEN}Response:, {response.json()}!{TerminalColors.RESET}")
    
    
    

def search_note():
    print("Search Note:")
    keyword = input("Enter a keyword: ")
    response = make_request("GET", f"/search/?q={keyword}")
    print(f"{TerminalColors.BOLD}{TerminalColors.GREEN}Response:, {response.json()}!{TerminalColors.RESET}")
    
    
    

def get_all_notes():
    print("Get a note by its ID:")
    response = make_request("GET", "/notes/")
    print(f"{TerminalColors.BOLD}{TerminalColors.GREEN}Response:, {response.json()}!{TerminalColors.RESET}")
    
    
