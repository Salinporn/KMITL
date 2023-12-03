import ZODB, ZODB.FileStorage
import persistent
import transaction
import BTrees._OOBTree
from enrollment import *

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root


root.course = BTrees.OOBTree.BTree()
root.student = BTrees.OOBTree.BTree()

grading=[
    {"Grade": "A", "min": 80, "max": 100},
    {"Grade": "B", "min": 70, "max": 79},
    {"Grade": "C", "min": 60, "max": 69},
    {"Grade": "D", "min": 50, "max": 59},
    {"Grade": "F", "min": 0, "max": 49}
]

root.course[101] = Course(101, 'Computer Programming', 4, grading)
root.course[201] = Course(201, 'Web Programming', 4, grading)
root.course[202] = Course(202, 'Software Engineering Principle', 5, grading)
root.course[301] = Course(301, 'Artificial Intelligence', 3, grading)

root.student[86] = Student([], id=86, name='Mr. Name ForExample', password="password")
root.student[86].enrollCourse(Enrollment(root.course[101], root.student[86], 75))
root.student[86].enrollCourse(Enrollment(root.course[201], root.student[86], 81))
root.student[86].enrollCourse(Enrollment(root.course[202], root.student[86], 81))
root.student[86].enrollCourse(Enrollment(root.course[301], root.student[86], 57))

async def retrieveCourse(id):
    return root.course[id]

from fastapi import FastAPI, Body, Request
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

@app.get("/login/")
async def login():
    html_content = """<html>
    <head> <title>Login Page</title> </head>
    <style> h1 { text-align:center; } 
    .id, .password { width: 100%; height: 30px; } </style>
    <body>
    <form action="/login/" method="post">
    <h1>Login</h1>
    <div id="info">
    <br><label>ID:</label><br>
    <input type="text" class="id" name="id"><br>
    <br><label>Password:</label><br>
    <input type="password" class="password" name="password"><br><br>
    <button type="submit">Log In</button>
    </div>
    </form>
    </body>
    </html>"""
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/login/")
async def perform_login(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = await request.form()

    id = int(data["id"])
    
    if id in root.student:
        password = data["password"]
        if root.student[id].login(id, password):
            return RedirectResponse(url=f"/update/?id={id}", status_code=302)
    return {"error": "Invalid login"}
    
@app.get("/update/")
async def transcript_entry_form():
    name = root.student[86].name
    id = root.student[86].id
    html_content = """<html>
    <head> <title>Transcript Entry Form</title> </head>
    <style> h1 { text-align: center; }
    th, td { border: solid 1px black; }
    </style>
    <body>
    <form action="/transcript" method="get">
    <h1>Transcript Entry Form</h1>
    <br> Name: """ + name + """<br> StudentId: """ + str(id) + """<br><br>
    <table class="enrollments" style="width: 100%;">
    <tr>
    <th>Course Code</th>
    <th>Couse Name</th>
    <th>Credits</th>
    <th>Score</th>
    </tr>
    <tr><td>""" + str(root.course[101].id) + """</td><td>""" + root.course[101].name + """</td><td>""" + str(root.course[101].credit) + """</td><td><input type="text" name="score_101"></td></tr>
    <tr><td>""" + str(root.course[201].id) + """</td><td>""" + root.course[201].name + """</td><td>""" + str(root.course[201].credit) + """</td><td><input type="text" name="score_201"></td></tr>
    <tr><td>""" + str(root.course[202].id) + """</td><td>""" + root.course[202].name + """</td><td>""" + str(root.course[202].credit) + """</td><td><input type="text" name="score_202"></td></tr>
    <tr><td>""" + str(root.course[301].id) + """</td><td>""" + root.course[301].name + """</td><td>""" + str(root.course[301].credit) + """</td><td><input type="text" name="score_301"></td></tr>
    </table>
    <br><button type="submit">Submit</button>
    </body>
    </html>"""
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/transcript/")
async def transcript():
    name = root.student[86].name
    id = root.student[86].id
    html_content = """<html>
    <head>
        <title>Unofficial Transcript</title>
        <style>
            body, html {
                height: 100%;
                text-align: center;
                justify-content: center;
                margin: auto;
                max-width: 900px;
            }
            table {
                text-align: center;
                justify-content: center;
            }
            th {
                border: 1px solid black;
                padding: 8px;
            }
            
            img {
                width: 100%; 
                height: auto; 
                display: block;
                margin: 0 auto; 
            }
            .center_top_col{
                width: 50%; 
                text-align: center;
                padding-right: 160px;
            }

            .left_top_col {
                width: 35%; 
                text-align: left;
            }
            .mid_top_col {
                width: 15%; 
                text-align: left;
            }
            .right_top_col {
                text-align: left;
            }

            .content_table {
                border-collapse: collapse;
                width: 100%;
                border: 1px solid black;
            }
            .content_table td {
                border: 1px solid black;
                padding: 8px;
                border-bottom: none;
                border-top: none;
            }
            .content_table tbody {
                border-bottom: 1px solid black;
            }
        </style>
    </head>
    <body>
        <br><br>
        <h1>( Unofficial Transcript )</h1>
        <table>
            <tbody>
                <tr>
                    <td></td>
                    <td class="center_top_col">
                        <h2>School of Engineering</h2>
                    </td>
                </tr>
                <tr>
                    <td class="left_top_col">
                        <label for="student_name" style="font-style: italic;">Name</label>
                        <input type="text" id="student_name" readonly>
                    </td>
                </tr>
            </tbody>
        </table>
        <br>
        <table class="content_table">
            <thead>
                <th style="width: 90%;">
                    <p>COURSE TITLE</p>
                </th>
                <th style="width: 5%;">
                    <p>CREDIT</p>
                </th>
                <th style="width: 5%;">
                    <p>SCORE</p>
                </th>
                <th style="width: 5%;">
                    <p>GRADE</p>
                </th>
            </thead>
            <tbody id="content_body">
                <tr>
                    <td>""" + root.course[101].name + """</td>
                    <td>""" + str(root.course[101].credit) + """</td>
                    <td>""" + str(root.student[86].enrolls[0].score) + """</td>
                    <td>""" + str(root.course[101].scoreGrading(root.student[86].enrolls[0].score)) + """</td>
                </tr>
                <tr>
                    <td>""" + root.course[201].name + """</td>
                    <td>""" + str(root.course[201].credit) + """</td>
                    <td>""" + str(root.student[86].enrolls[1].score) + """</td>
                    <td>""" + str(root.course[201].scoreGrading(root.student[86].enrolls[1].score)) + """</td>
                </tr>
                <tr>
                    <td>""" + root.course[202].name + """</td>
                    <td>""" + str(root.course[202].credit) + """</td>
                    <td>""" + str(root.student[86].enrolls[2].score) + """</td>
                    <td>""" + str(root.course[202].scoreGrading(root.student[86].enrolls[2].score)) + """</td>
                </tr>
                <tr>
                    <td>""" + root.course[301].name + """</td>
                    <td>""" + str(root.course[301].credit) + """</td>
                    <td>""" + str(root.student[86].enrolls[3].score) + """</td>
                    <td>""" + str(root.course[301].scoreGrading(root.student[86].enrolls[3].score)) + """</td>
                </tr>
            </tbody>
        </table>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
