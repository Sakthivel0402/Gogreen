#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb

cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="gogreen")
cur = con.cursor()

print("""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Nursery Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script></head>
<script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>


    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900&display=swap');
    *{
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
        font-family: "Poppins", sans-serif;
        font-weight: 300;
    }
    body{
            background-color: #83efef6b;
        color: #002A32;
        font-family: "Inria Sans", sans-serif;


    }
    .main-header {
            position: relative;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            height: 100px;
        }

        .main-header h1 {
            margin-left: -150px;

            text-align: center;
            flex-grow: 1;
        }

        .logout-btn {
            background-color: rgb(244, 67, 54);
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 17px;
            box-shadow: 0 4px 6px rgba(244, 67, 54, 0.71); 
            transition: all ease 0.6s;
        }

        .logout-btn:hover {
            background-color: #d32f2f;
            box-shadow: 0 6px 8px rgba(255, 112, 101, 0.71);
        }

        .main-header img {
            max-width: 350px;
        }
    form .container{
        width: 500px;



    }
    .custom-shadow {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  .blur-effect {
    backdrop-filter: blur(1px); 
    background-color: rgba(255, 255, 255, 0.2); 
    padding: 20px;
    border-radius: 10px;
  }
  .form-control:focus {
        outline: none; 
       border-color: rgba(115, 213, 214, 0.838);; 
        box-shadow: 0 0 5px rgba(28, 197, 200, 0.838);
    }


    </style>
</head>

<body>
 <div class="main-header">
        <a class="mt-5" href="./index.py"><img src="./assets/GG-logo3.png" width="150px"></a>

    </div>
    <form action="" method="post" enctype="multipart/form-data">

        <div class="container border mt-5 rounded-4  custom-shadow mb-5 blur-effect">
            <h2 class="text-center mb-4 fw-bold">Nursery Login</h2>
            <div class="row">
                <div class="ms-5 col-md-10">
                    <img src="assets/user (1).png" class="mb-1" width="15px" alt=""> <label for="" class="form-label mt-5"> Nursery ID</label> <br>
                    <input type="text" name="username" id="" class="form-control">
                </div>
            </div>
            <div class="row">
                <div class="col-md-10 mt-4 ms-5">
                    <img src="assets/padlock.png" class="mb-1" width="15px" alt=""> <label for="" class="form-label">Password</label> <br>
                    <input type="password" name="password" id="" class="form-control">
                    <div class="col-md-5 mt-3 me-1 float-end">
                        <a href="./nurseryForgotpwd.py" class="text-danger text-decoration-none">Forgot password?</a>
                    </div>

                </div>
            </div>
            <div class="row">
                <div class="col-md-3"></div>
                <div class="col-md-3 mt-4 d-flex justify-content-center">
                    <input type="submit" class="btn btn-primary" value="Login" name="login">
                </div>
                <div class="col-md-3 mt-4 d-flex justify-content-center">
                    <a type="submit" href="./index.py" class="btn btn-danger">Back</a>
                </div>
                <div class="col-md-3"></div>
            </div>
            <div class="row">
                <div class="col-md-6 mt-5  ">
                    <a href="./nurseryreg.py" class="text-primary text-decoration-none">Didn't have an account? (Signup)</a>
                </div>
                </div>
     </div>   
</form>
</body>""")
submit = store.getvalue("login")
if submit != None:
    userID = store.getvalue("username")
    password = store.getvalue("password")
    query=f"""select id from nurseryreg where nurseryid='{userID}' and password='{password}'"""
    cur.execute(query)
    idpwd=cur.fetchone()

    if idpwd!=None:
        print(f"""
                <script>alert("Login Successful!")
                location.href="nurseryDashboard.py?id={idpwd[0]}"
                </script>""")
    else:
        print(f"""
                    <script>alert("Please enter the correct ID or Password!") </script>""")

