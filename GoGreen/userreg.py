#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, smtplib
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="GoGreen")
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>user registration</title>
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
      
    body{
            background-color: #F0FFF0;
        color: #008080;
        
        
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
        width: auto;
        
        

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
       border-color: #0a86ab; 
        box-shadow: 0 0 5px #086481dd;
    }


       
    </style>
</head>


<body>
    <div class="main-header" >
        <a class="mt-4" href="./index.py"><img src="./assets/GG-logo3.png"  width="120px"></a>
        
    </div>
    <form action="" method="post" enctype="multipart/form-data">

        <div class="container border mt-4 rounded-4 p-5 custom-shadow mb-5 blur-effect">
        <div class="row ">
        <h1 class="d-flex justify-content-center align-items-center"><img src="assets/user.gif" width="60px" alt="">   User Registration</h1></div>

        <div class="row mt-5">
            <div class="row mb-4"><h2>Personal Details <img src="assets/personal details.gif" alt="" width="50px"></h2></div>
        <div class="col-md-3">
        <label for="" class="form-label">First name</label>
        <input type="text" name="fname" class="form-control " placeholder="John" id="">
        </div>
        <div class="col-md-3">
        <label for="" class="form-label">Last name</label>
        <input type="text" name="lname" class="form-control" placeholder="wick" id="">
        </div>
        <div class="col-md-3">
        <label for="" class="form-label">Date Of Birth</label>
        <input type="date" name="dob" class="form-control"  id="">
        </div>
        <div class="col-md-3">
        <label for="" class="form-label">Gender</label> <br>
            <input type="radio" name="gender" value="male" class="form-check-input " id="">
            <label for="">Male</label>

        <input type="radio" name="gender" value="female" class="form-check-input ms-4" id="">
        <label for="">Female</label>
        </div>
        </div>

        <div class="row mt-4">
            <div class="col-md-3">
                <label for="" class="form-label">Phone</label>
                <input type="text" name="phone" placeholder="+91 9876543210" class="form-control" id=""> 
            </div>
            <div class="col-md-3">
                <label for="" class="form-label">Email</label>
                <input type="text" name="email" placeholder="example@gmail.com" class="form-control" id=""> 
            </div>
            <div class="col-md-3">
                <label for="" class="form-label">Address line 1</label>
                <input type="text" name="address1" placeholder=" Ex: 53/7, abc street" class="form-control" id=""> 
            </div>
            <div class="col-md-3">
                <label for="" class="form-label">Address line 2</label>
                <input type="text" name="address2" placeholder="Ex: efg colony" class="form-control" id=""> 
            </div>
            </div>

            <div class="row mt-4">
                <div class="col-md-3">
                    <label for="" class="form-label">Zipcode</label>
                    <input type="text" name="zipcode" placeholder="Ex: 638004" class="form-control" id=""> 
                </div>
                <div class="col-md-3">
                    <label for="" class="form-label">City</label>
                    <select name="city" class="form-select" id="">
                        <option value="">Select City</option>
                        <option value="Ariyalur">Ariyalur</option>
                        <option value="Chengalpattu">Chengalpattu</option>
                        <option value="Chennai">Chennai</option>
                        <option value="Coimbatore">Coimbatore</option>
                        <option value="Cuddalore">Cuddalore</option>
                        <option value="Dharmapuri">Dharmapuri</option>
                        <option value="Dindigul">Dindigul</option>
                        <option value="Erode">Erode</option>
                        <option value="Kallakurichi">Kallakurichi</option>
                        <option value="Kanchipuram">Kanchipuram</option>
                        <option value="Kanyakumari">Kanyakumari</option>
                        <option value="Karur">Karur</option>
                        <option value="Krishnagiri">Krishnagiri</option>
                        <option value="Madurai">Madurai</option>
                        <option value="Mayiladuthurai">Mayiladuthurai</option>
                        <option value="Nagapattinam">Nagapattinam</option>
                        <option value="Namakkal">Namakkal</option>
                        <option value="Nilgiris">Nilgiris</option>
                        <option value="Perambalur">Perambalur</option>
                        <option value="Pudukkottai">Pudukkottai</option>
                        <option value="Ramanathapuram">Ramanathapuram</option>
                        <option value="Ranipet">Ranipet</option>
                        <option value="Salem">Salem</option>
                        <option value="Sivaganga">Sivaganga</option>
                        <option value="Tenkasi">Tenkasi</option>
                        <option value="Thanjavur">Thanjavur</option>
                        <option value="Theni">Theni</option>
                        <option value="Tuticorin">Tuticorin</option>
                        <option value="Trichy">Trichy</option>
                        <option value="Tirunelveli">Tirunelveli</option>
                        <option value="Tirupathur">Tirupathur</option>
                        <option value="Tiruppur">Tiruppur</option>
                        <option value="Tiruvallur">Tiruvallur</option>
                        <option value="Tiruvannamalai">Tiruvannamalai</option>
                        <option value="Tiruvarur">Tiruvarur</option>
                        <option value="Vellore">Vellore</option>
                        <option value="Viluppuram">Viluppuram</option>
                        <option value="Virudhunagar">Virudhunagar</option>
                        </select>
                    </div>
                <div class="col-md-3">
                    <label for="" class="form-label">State</label>
                    <select name="state" class="form-select" id="">
                        <option value="">Select State</option>
                        <option value="Andhra Pradesh">Andhra Pradesh</option>
                        <option value="Arunachal Pradesh">Arunachal Pradesh</option>
                        <option value="AssamBihar">AssamBihar</option>
                        <option value="Bihar">Bihar</option>
                        <option value="Chhattisgarh">Chhattisgarh</option>
                        <option value="Goa">Goa</option>
                        <option value="Gujarat">Gujarat</option>
                        <option value="Haryana">Haryana</option>
                        <option value="Himachal Pradesh">Himachal Pradesh</option>
                        <option value="Jharkhand">Jharkhand</option>
                        <option value="Karnataka">Karnataka</option>
                        <option value="Kerala">Kerala</option>
                        <option value="Madhya Pradesh">Madhya Pradesh</option>
                        <option value="Maharashtra">Maharashtra</option>
                        <option value="Manipur">Manipur</option>
                        <option value="Meghalaya">Meghalaya</option>
                        <option value="Mizoram">Mizoram</option>
                        <option value="Nagaland">Nagaland</option>
                        <option value="Odisha">Odisha</option>
                        <option value="Punjab">Punjab</option>
                        <option value="Rajasthan">Rajasthan</option>
                        <option value="Sikkim">Sikkim</option>
                        <option value="Tamil Nadu">Tamil Nadu</option>
                        <option value="Telangana">Telangana</option>
                        <option value="Tripura">Tripura</option>
                        <option value="Uttar Pradesh">Uttar Pradesh</option>
                        <option value="Uttarakhand">Uttarakhand</option>
                        <option value="West Bengal">West Bengal</option>
                        </select>
                    </div>
                <div class="col-md-3">
                    <label for="" class="form-label">Country</label>
                    <input type="text" name="country" placeholder="INDIA" class="form-control" id=""> 
                </div>
               </div>
               <div class="row mt-5">
                <div class="col-md-3"><img src="assets/user (1).png" class="mb-1" width="15px" alt=""> <label for="" class="form-label">Create username</label> 
              <input type="text" name="username" placeholder="" class="form-control" id=""> 
              </div>
              
                <div class="col-md-3"> <img src="assets/padlock.png" class="mb-1" width="15px" alt="">  <label for="" class="form-label">Create password</label> 
                    <input type="password" name="password" placeholder="" class="form-control" id=""> 
              </div></div>

            
            
            <div class="row mt-5 mb-2">  
                <div class="col-md-3"></div>
                <div class="col-md-3 ">
            <input type="submit" class="btn btn-primary  float-end" name="submit" id=""></div>
            <div class="col-md-3 ">
                <a class="btn btn-danger" href="./index.py">Cancel</a></div>
                <div class="col-md-3"></div>
                <div class="row"><div class="col-md-3"><a class="text-decoration-none" href="./userLogin.py"><img src="assets/account.gif" alt="" width="45px"> Already have an account?(Login)</a></div>
            <div class="col-md-9"></div></div>

        </div>
    </div>
</form>
</body>
</html>""")


submit= store.getvalue("submit")
if submit!=None:
        fname = store.getvalue("fname")
        lname = store.getvalue("lname")
        dob = store.getvalue("dob")
        gender = store.getvalue("gender")
        mail = store.getvalue("email")
        phone = store.getvalue("phone")
        add1 = store.getvalue("address1")
        add2 = store.getvalue("address2")
        city = store.getvalue("city")
        zip = store.getvalue("zipcode")
        state = store.getvalue("state")
        country = store.getvalue("country")
        username = store.getvalue("username")
        password = store.getvalue("password")
        emailquery = """select mail from userreg"""
        cur.execute(emailquery)
        emailloop = cur.fetchall()
        c = 0
        for i in emailloop:
            if i[0] == mail:
                    c += 1
        if c > 0:
            print("""<script>alert("Entered email already exists! Please enter a new mail address")</script>""")
        else:
            query2 = f""" insert into userreg (firstname,lastname,dob,gender,mail,phone,address1,address2,city,zipcode,state,country,username,password) values ('{fname}','{lname}','{dob}','{gender}','{mail}','{phone}','{add1}','{add2}', '{city}', '{zip}', '{state}','{country}','{username}','{password}')"""
            cur.execute(query2)
            con.commit()
            fromadd = 'sakthivelsubash0402@gmail.com'
            password2 = 'evcp ltxn ywkb uycx'
            toadd = mail
            subject = """User registration process"""
            body = f"Congratulations {fname}!. You are successfully registered with  Go Green :)\n "
            msg = f"""Subject: {subject}\n\n{body}"""
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(fromadd, password2)
            server.sendmail(fromadd, toadd, msg)
            server.quit()
            print(""" <script>
                alert("Registered!");
                </script>""")

