import requests

url = 'http://161.246.5.61:11514/students'
reponse = requests.get(url)

student = {"name": "Mark", "surname": "Lee", "ID": 11222}
studentQuery = {"student_name": "Mark", "student_surname": "Lee", "student_id": 11222}


def post(datain):
    post = requests.post(url + "/new/", json=datain)
    print(post.text)

def post_newForm(datain):
    post = requests.post(url + "/newForm", params=datain)
    print(post.text)

def post2(name, surname, student_id):
    post = requests.post(f"{url}/new/{name}/{surname}/{student_id}")
    print(post.text)

def request_all_student():
    get = requests.get(url + "/html")
    print(get.text)

def request_each_student(id):
    get = requests.get(url + "/" + str(id))
    print(get.text)

post(student)
post_newForm(studentQuery)
post2("Mark2", "Lee2", 1122)

request_all_student()
request_each_student("65011514")
