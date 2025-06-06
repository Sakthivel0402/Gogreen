#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="GoGreen")
cur = con.cursor()

query2="""select max(id) from nurseryreg"""
cur.execute(query2)
nursery=cur.fetchone()

if nursery[0]!=None:
    if nursery[0]<10:
        num="NUR000"+str(nursery[0]+1)
    elif nursery[0]<100:
        num = "NUR00" + str(nursery[0]+1)
    elif nursery[0]<1000:
        num = "NUR0" + str(nursery[0]+1)
else:
    num="NUR0001"

print("""


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nursery registration</title>
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
</head>""")

print(f"""
<body>
    <div class="main-header" >
        <a class="mt-4" href="./index.py"><img src="./assets/GG-logo3.png"  width="120px"></a>
        
    </div>
    <form action="" method="post" enctype="multipart/form-data">

        <div class="container border mt-4 rounded-4 p-5 custom-shadow mb-5 blur-effect">
        <div class="row ">
        <h1 class="d-flex justify-content-center align-items-center"> Nursery Registration</h1></div>

        <div class="row mt-5">
            <div class="row mb-4"><h2>Shop Details </h2></div>
        <div class="col-md-3">
        <label for="" class="form-label">Shop name</label>
        <input type="text" name="shopname" class="form-control " placeholder="Ex: ABC Plants" id="">
        </div>
        <div class="col-md-3">
        <label for="" class="form-label">Shop picture 1</label>
        <input type="file" name="pic1" class="form-control" placeholder="wick" id="">
        </div>
        <div class="col-md-3">
        <label for="" class="form-label">Shop picture 2</label>
        <input type="file" name="pic2" class="form-control"  id="">
        </div>
        <div class="col-md-3">
            <label for="" class="form-label">Shop owner's name</label>
            <input type="text" name="ownername" class="form-control " placeholder="Ex: Aadithya" id="">
        </div>
        </div>

        <div class="row mt-4">
            <div class="col-md-3">
                <label for="" class="form-label">Phone</label>
                <input type="text" name="phone" placeholder="+91 9876543210" class="form-control" id=""> 
            </div>
            <div class="col-md-3">
                <label for="" class="form-label">Company email</label>
                <input type="text" name="email" placeholder="example@gmail.com" class="form-control" id=""> 
            </div>
            <div class="col-md-3">
                <label for="" class="form-label">Shop address line 1</label>
                <input type="text" name="address1" placeholder=" Ex: 53/7, abc street" class="form-control" id=""> 
            </div>
            <div class="col-md-3">
                <label for="" class="form-label">Shop address line 2</label>
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
                <div class="col-md-3"> <label for="" class="form-label">Shop license number</label> 
              <input type="text" name="licensenumber" placeholder="" class="form-control" id=""> 
              </div>
              
                <div class="col-md-3">  <label for="" class="form-label">License picture</label> 
                    <input type="file" name="license" placeholder="" class="form-control" id=""> 
              </div>
              <div class="col-md-3 ">  <label for="" class="form-label">Choose nursery type:</label> 
                <div class="form-check ms-3">
                    <input class="form-check-input" name="check" type="checkbox" value="Indoor plants" id="flexCheckDefault">
                    <label class="form-check-label ms-1" for="flexCheckDefault">
                        Indoor plants
                    </label> </div>
                    <div class="form-check ms-3">
  <input class="form-check-input " type="checkbox" name="check2" value="Outdoor plants" id="flexCheckDefault">
  <label class="form-check-label ms-1" for="flexCheckDefault">
    Outdoor plants
  </label>
</div>

    <input class="form-check-input ms-3" type="checkbox" name="check3" value="Succulents" id="flexCheckDefault">
    <label class="form-check-label ms-1" for="flexCheckDefault">
      Succulents
    </label>
    <div class="form-check ms-3">
        <input class="form-check-input" type="checkbox" name="check4" value="Flowering plants" id="flexCheckDefault">
        <label class="form-check-label ms-1" for="flexCheckDefault">
            Flowering plants
        </label>  </div> 
        
        <div class="form-check col-md-3 ms-3">
            <input class="form-check-input" type="checkbox" name="check5" value="Herbs & medicine plants" id="flexCheckDefault">
            <label class="form-check-label ms-1" for="flexCheckDefault">
                Herbs & medicine plants
            </label>     </div>    
                
                
                
                </div>
          <div class="col-md-3">  <label for="" class="form-label">Nursery ID</label> 
            <input type="text" name="id" placeholder="{num}" disabled class="form-control" id=""> 
      </div>
            
            </div>

            
            
            <div class="row mt-5 mb-2">  
                <div class="col-md-3"></div>
                <div class="col-md-3 ">
            <input type="submit" class="btn btn-primary  float-end" name="submit" id=""></div>
            <div class="col-md-3 ">
                <a class="btn btn-danger" href="./index.py">Cancel</a></div>
                <div class="col-md-3"></div>
                <div class="row"><div class="col-md-3"><a class="text-decoration-none" href="./userLogin.py"> Already have an account?(Login)</a></div>
            <div class="col-md-9"></div></div>

        </div>
    </div>
</form>   
</body>
</html>
""")

submit = store.getvalue("submit")
if submit != None:
    shopname = store.getvalue("shopname")
    ownername = store.getvalue("ownername")
    mail = store.getvalue("email")
    phone = store.getvalue("phone")
    add1 = store.getvalue("address1")
    add2 = store.getvalue("address2")
    city = store.getvalue("city")
    zip = store.getvalue("zipcode")
    state = store.getvalue("state")
    country = store.getvalue("country")
    licensenumber = store.getvalue("licensenumber")
    check = store.getvalue("check")
    check2 = store.getvalue("check2")
    check3 = store.getvalue("check3")
    check4 = store.getvalue("check4")
    check5 = store.getvalue("check5")
    pic1 = store['pic1']
    pic2 = store['pic2']
    license = store['license']
    if pic1.filename and pic2.filename and license.filename:
        proof1 = os.path.basename(pic1.filename)
        open("assets/" + proof1, "wb").write(pic1.file.read())
        proof2 = os.path.basename(pic2.filename)
        open("assets/" + proof2, "wb").write(pic2.file.read())
        proof3 = os.path.basename(license.filename)
        open("assets/" + proof3, "wb").write(license.file.read())

        emailquery = """select mail from nurseryreg"""
        cur.execute(emailquery)
        emailloop = cur.fetchall()
        c = 0
        for i in emailloop:
            if i[0] == mail:
                c += 1
        if c > 0:
            print("""<script>alert("Entered email already exists! Please enter a new mail address")</script>""")
        else:
            query = f""" INSERT INTO `nurseryreg`(`shopname`, `pic1`, `pic2`, `mail`, `phone`, `address1`, `address2`, `city`, `zipcode`, `state`, `country`, `licensenumber`, `licensepicture`, `nurserytype(check)`,`check2`,`check3`,`check4`,`check5`, `nurseryid`, `regstatus`) VALUES ('{shopname}','{proof1}','{proof2}','{mail}','{phone}','{add1}','{add2}', '{city}', '{zip}', '{state}','{country}','{licensenumber}','{proof3}','{check}','{check2}','{check3}','{check4}','{check5}','{num}','pending')"""
            cur.execute(query)
            con.commit()
            print(""" <script>
                    alert("Registration requested to admin!");
                    </script>""")
