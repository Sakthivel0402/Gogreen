#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, smtplib

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
    <title>New mechanic requests</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
        <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>

    <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    *{
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
        font-family: "Poppins", sans-serif;
        font-weight: 300;
    }
        body {
            background-color: #83efef6b;
            color: #002A32;
            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 22px;
            height: 100vh;
        }

        form {
            width: 500px;
        }

        .side-nav1 {
            font-size: 20px;
            font-weight: 500;
        }

        .custom-shadow {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .blur-effect {
            backdrop-filter: blur(1px);
            background-color: rgba(255, 255, 255, 0.2);
            padding: 20px;
            border-radius: 10px;
        }

        #sidebar {
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }

        .main-content {
            flex-grow: 1;
            padding: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            background: rgba(255, 255, 255, 0.01);
        }

        .nav-link {
            padding: 10px 20px;
            color: #000;
            text-decoration: none;
            display: block;
            font-size: 17px; /* Make all text the same size */
            font-weight: 500;
            transition: all ease 0.6s;

        }

        .nav-link:hover {
            background-color: #083D77;
            color: #ffffff !important;
            border-radius: 4px;
        }

        .nav-link:active {
            background-color: #083D77 !important;
            color: #ffffff !important;
        }

        .active {
            background-color: #083D77 !important;
            color: #ffffff;
            border-radius: 4px;
        }

        .text {
            font-size: 17px;
            color: #000000;
            padding: 5px 10px;
            transition: all ease 0.6s;
        }
        .text:hover{
            color: #083D77;
            transition: all ease 0.6s;

        }

        .container {
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(128, 125, 125, 0.527);
        }

        .accordion-button {
            font-size: 17px;
            font-weight: 500;
            padding: 10px 20px;
            border-radius: 10px;
            transition: all ease 0.6s;
            background-color: #FFF8F0;

        }
        .accordion-button:hover{
            background-color: #083D77;
            color: #FFF8F0;
            transition: all ease 0.6s;

        }

        .accordion-body{
            background-color: #FFF8F0;
                    }

        .accordion-body a{
            color: #ff8800;
                    }
        .accordion-item a {
            display: block;
            padding: 10px 20px;
            font-size: 17px;
            font-weight: 500;
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
        .accordion-button{
            box-shadow: none !important;
        }

        .main-header h1 {
            margin-left: -150px;
            text-align: center;
            flex-grow: 1;
        }
        .accordion-button{
            box-shadow: none !important;
        }

        .logout-btn {
            background-color: rgb(244, 67, 54);
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 17px;
            box-shadow: 0 4px 6px rgba(244, 67, 54, 0.71);
            transition: all ease 0.6s;
        }
        .nav-link{
            background-color: #FFF8F0;
            border-radius: 10px !important;
        }

        .logout-btn:hover {
            background-color: #d32f2f;
            box-shadow: 0 6px 8px rgba(255, 112, 101, 0.71);
        }

        .main-header img {
            max-width: 350px;
        }
        .lol{
            color: #ffffff !important;
        }

          form {
        width: 100%;
        max-width: 600px;
        margin: 0 auto; /* Center the form horizontally */
    }

    .form-group {
        margin-bottom: 20px; /* Add space between form groups */
    }

    .form-inline .col-form-label {
        text-align: right;
        padding-right: 15px; /* Align labels to the right with some spacing */
    }

    .form-control {
        width: 668px; /* Make input fields full width */
    }
     .form-control:focus {
        outline: none; 
        border-color: #28a745; 
        box-shadow: 0 0 5px rgba(40, 167, 69, 0.5);
    }

    .form-inline .col-sm-4 {
        padding-right: 15px; /* Add space between input and button */
    }

    .btn {
        width: 100%;
    }
    .btn:hover {
        width: 100%;
        border-color: #28a745; 
        box-shadow: 0 0 5px rgba(40, 167, 69, 0.9);
    }

    </style>
</head>
</head>
<body>

<div class="main-header">
        <a class="mt-5" href="#"><img src="./assets/GG-logo3.png" width="150px"></a>
        <h1>  </h1>
        <a class="logout-btn text-decoration-none" href="./userLogin.py" >Back</a>
    </div>

    <form class="container  w-50 mt-5 bg-light p-5" method="post">
        <h1 class="ms-5 mb-4">Forgot Password</h1>
        <input  type="text" class="form-control mb-3" name="email" autocomplete="off" required  placeholder=" Enter registered Mail ID">
        <input type="submit" class="w-100 text-white btn btn-primary border border-white rounded" name="submit" value="Get password">
    </form>
</body>
</html>
""")

submit = store.getvalue("submit")
if submit != None:
        mail = store.getvalue("email")
        query = f"""select mail from userreg where mail='{mail}'"""
        cur.execute(query)
        sts = cur.fetchone()
        if sts[5]:
            password = sts[14]
            userid = (sts[13])
            name = (sts[1])
            fromadd = 'sakthivelsubash0402@gmail.com'
            password2 = 'evcp ltxn ywkb uycx'
            toadd = mail
            subject = """Forgotten password?"""
            body = f"Hello {name}!.\n We are successfully found your password: {password} for the User ID: {userid}"
            msg = f"""Subject: {subject}\n\n{body}"""
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(fromadd, password2)
            server.sendmail(fromadd, toadd, msg)
            server.quit()
            print(f"""<script> alert("Password sent to {mail}")
            location.href="userLogin.py"</script>""")

        else:
            print("""<script>alert("Please enter the correct Email address.")
                                        location.href="userLogin.py" </script>""")

