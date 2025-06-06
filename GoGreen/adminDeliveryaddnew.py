#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb,smtplib,os,random

cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="GoGreen")
cur = con.cursor()

query="""select max(id) from delireg"""
cur.execute(query)
delivery=cur.fetchone()

if delivery[0]!=None:
    if delivery[0]<10:
        num="DELI000"+str(delivery[0]+1)
    elif delivery[0]<100:
        num = "DELI00" + str(delivery[0]+1)
    elif delivery[0]<1000:
        num = "DELI0" + str(delivery[0]+1)
else:
    num="DELI0001"
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delivery person registration</title>
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
        background-color: #83efef6b;
    }
        .header {
            background-color: #28AFB0;
            padding: 20px;
            color: #002A32;
            display: flex;
            justify-content: space-around;
            text-align: center;
        }
      
    .sidebar {
        width: 230px;
        background: #28AFB0;
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        padding-top: 20px;
        transition: all 0.5s ease;
    }
    .sidebar a, .dropdown-btn {
        padding: 15px 20px;
        text-decoration: none;
        font-size: 16px;
        font-weight: 400;
        color: #ffffff;
        background-color: #217980;
        display: flex;
        align-items: center;
        gap: 10px;
        transition: background 0.3s, color 0.3s;
        border-radius: 5px;
        border: none;
        margin: 5px 10px;
        width: 90%;
    }
    .sidebar a:hover, .dropdown-btn:hover {
        background-color: #2c2a2a94;
        color: #fff;
        width: 90%;
    }
    .active{
        background-color: #2c2a2ab9 !important;
    }
    .dropdown-container {
        display: none;
        background-color: #28AFB0;
        padding-left: 20px;
    }
    .dropdown-container a {
        font-size: 14px;
        padding: 10px;
        color: #fff;
    }
    .dropdown-container a:hover {
        background-color: #00000097;
        color: #fff;
    }
    .sidebar img {
        display: block;
        margin: 0 auto 20px;
        width: 150px;
        border-radius: 10px;
    }
    .sidebar .bx {
        font-size: 18px;
    }
    .content {
        margin-left: 230px;
        padding: 20px;
        transition: all 0.5s ease;
    }.table-container {
            background: #ebfffdda;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 15px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #6B4B3E;
            color: white;
        }
        .footer {
            text-align: center;
            background: #28AFB0;
            color: white;
            position: fixed;
            bottom: 0;
            height:30px;
            width: calc(100% - 220px);
            left: 230px;
        }
        .logout-btn {
    background-color: #ff4b4b;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    position: absolute;
    right: 20px;
    top: 20px;
    transition: background-color 0.3s, box-shadow 0.3s;
}

.logout-btn:hover {
    background-color: #ea2828;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); 
}
::selection {
    background-color: #af4c70; /* Change this to your desired background color */
    color: white; /* Change the text color of the selected content */
}
.span1 {
    color: #28AFB0;
    font-weight: 400;
    margin-left: 6px;
  }

  </style>""")

print(f"""
<body>
    <div class="header">
        <h1 class="ms-5" style="color: #fff;"> Delivery Person Registration</h1>
                <a href="./adminLogin.py" class="logout-btn text-decoration-none">Logout</a>

    </div>

   <div class="sidebar">
        <img src="./assets/GG-logo3.png" width="150px" alt="Go Green Logo">
        
        <a href="./adminDashboard.py" class="mt-4"><i class='bx bx-home'></i> Home</a>
        
        <button class="dropdown-btn"><i class='bx bx-cart'></i> Order Management
            <i class="bx bx-chevron-down ms-auto"></i>
        </button>
        <div class="dropdown-container">
            <a href="./adminCurrentorders.py"><i class='bx bx-time'></i> Current orders</a>
            <a href="./adminCompleted.py"><i class='bx bx-check'></i> Completed orders</a>
            <a href="./adminCancelledorders.py"><i class='bx bx-x'></i> Cancelled orders</a>
            <a  href="./adminReviews.py"><i class='bx bx-comment'></i> Customer reviews</a>
        </div>
        
        <button class="dropdown-btn"><i class='bx bx-leaf'></i> Nursery
            
            <i class="bx bx-chevron-down ms-auto"></i>
        </button>
        <div class="dropdown-container">
            <a  href="./adminNurseryrequests.py"><i class='bx bx-plus'></i> New requests
                </a>
            <a href="./adminNurseryexisting.py"><i class='bx bx-building'></i> Existing nurseries</a>
            <a href="./adminNurserycancelled.py"><i class='bx bx-x-circle'></i> Cancelled nurseries</a>
        </div>
        
        <button class="dropdown-btn active"><i class='bx bx-package'></i> Delivery 
            <i class="bx bx-chevron-down ms-auto"></i>
        </button>
        <div class="dropdown-container">
            <a class="active" href="./adminDeliveryaddnew.py"><i class='bx bx-user-plus'></i> Add new employee</a>
            <a href="./adminDeliveryexisting.py"><i class='bx bx-group'></i> Existing employees</a>
        </div>
    
     <a  href="./adminUserdetails.py"><i class='bx bx-user'></i> User Details</a>
        <a href="./adminaddnewmedicine.py"><i class='bx bx-leaf'></i> Add Medicine Plants</a>
    </div>""")
print(f"""
     <div class="content">
    <form action=""  method="post" enctype="multipart/form-data">

        <div class="container border mt-4 rounded-4 p-5 custom-shadow mb-5 blur-effect">
        <div class="row ">

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
                <div class="col-md-3"> <label for="" class="form-label">vehicle type</label> 
                    <select name="vehicletype" class="form-select" aria-label="Default select example">
                        <option selected> select here</option>
                        <option value="Bike">Bike</option>
                        <option value="Car">Car</option>
                        <option value="Van">Van</option>
                      </select>              </div>
              
                <div class="col-md-3">   <label for="" class="form-label">License picture</label> 
                    <input type="file" name="licensepic" placeholder="" class="form-control" id=""> 
              </div>
              
              <div class="col-md-3">   <label for="" class="form-label">Employee ID</label> 
                <input type="text"  disabled name="deliID" placeholder="Ex: {num}" class="form-control" id=""> 
          </div>
              </div>

            
            
            <div class="row mt-5 mb-2">  
                <div class="col-md-3"></div>
                <div class="col-md-3 ">
            <input type="submit" class="btn btn-primary  float-end" name="submit" id=""></div>
            <div class="col-md-3 ">
                <a class="btn btn-danger" href="./index.py">Cancel</a></div>
                <div class="col-md-3"></div>
            <div class="col-md-9"></div></div>

        </div>
    </div>
</form> 
 
    <div class="footer ">
        <p >&copy; 2024 Go Green Online Nursery |  Date: <span id="date"></span></p>
    </div>""")


print("""
    <script>
        document.getElementById("date").textContent = new Date().toLocaleDateString();

        var dropdown = document.getElementsByClassName("dropdown-btn");
        for (var i = 0; i < dropdown.length; i++) {
            dropdown[i].addEventListener("click", function() {
                this.classList.toggle("active");
                var dropdownContent = this.nextElementSibling;
                if (dropdownContent.style.display === "block") {
                    dropdownContent.style.display = "none";
                } else {
                    dropdownContent.style.display = "block";
                }
            });
        }

        var dropdown = document.getElementsByClassName("dropdown-btn");
    for (var i = 0; i < dropdown.length; i++) {
        dropdown[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var dropdownContent = this.nextElementSibling;
            if (dropdownContent.style.maxHeight) {
                dropdownContent.style.maxHeight = null;
            } else {
                dropdownContent.style.maxHeight = dropdownContent.scrollHeight + "px";
            }
        });
    }
    </script> 
</body>
</html>
""")


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
        vehicletype = store.getvalue("vehicletype")
        licensepic = store['licensepic']
        if licensepic.filename:
            proof1 = os.path.basename(licensepic.filename)
            open("assets/" + proof1, "wb").write(licensepic.file.read())
        employeeid = store.getvalue("deliID")

        emailquery = """select mail from delireg"""
        cur.execute(emailquery)
        emailloop = cur.fetchall()
        c = 0
        for i in emailloop:
            if i[0] == mail:
                    c += 1
        if c > 0:
            print("""<script>alert("Entered email already exists! Please enter a new mail address")</script>""")
        else:
            r = random.randint(1000, 9999)
            slymail = mail[0:4]
            password = slymail + str(r)
            fromadd = 'sakthivelsubash0402@gmail.com'
            password2 = 'evcp ltxn ywkb uycx'
            toadd = mail
            subject = """Delivery person registration process"""
            body = f"Congratulations {fname}!. You are successfully registered with our company. This is your Employee ID: {num}\n and password:{password}"
            msg = f"""Subject: {subject}\n\n{body}"""
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(fromadd, password2)
            server.sendmail(fromadd, toadd, msg)
            server.quit()
            query2 = f""" insert into delireg (firstname,lastname,dob,gender,mail,phone,address1,address2,city,zipcode,state,country,vehicletype,license,employeeID,password,employeestatus) values ('{fname}','{lname}','{dob}','{gender}','{mail}','{phone}','{add1}','{add2}', '{city}', '{zip}', '{state}','{country}','{vehicletype}','{proof1}','{num}','{password}','yes')"""
            cur.execute(query2)
            con.commit()
            print(f""" <script>
                alert("Employee Registered!");
                </script>""")

