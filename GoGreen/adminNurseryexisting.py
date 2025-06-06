#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, smtplib

cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="GoGreen")
cur = con.cursor()

select = f"""select * from nurseryreg where regstatus='accepted'"""
cur.execute(select)
query = cur.fetchall()

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin-accepted nursery requests</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
        <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" integrity="sha512-Kc323vGBEqzTmouAECnVceyQqyqdsSiqLQISBL29aUW4U/M7pSPA/gEUZQqv1cwx4OnYxTxve5UMg5GT6L4JJg==" crossorigin="anonymous" referrerpolicy="no-referrer" />

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

    </style>
</head>
<body>

    <div class="header">
        <h1 class="ms-5" style="color: #fff;"> Existing Nurseries</h1>
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
        
        <button class="dropdown-btn active"><i class='bx bx-leaf'></i> Nursery
            
            <i class="bx bx-chevron-down ms-auto"></i>
        </button>
        <div class="dropdown-container">
            <a  href="./adminNurseryrequests.py"><i class='bx bx-plus'></i> New requests
                </a>
            <a class="active" href="./adminNurseryexisting.py"><i class='bx bx-building'></i> Existing nurseries</a>
            <a  href="./adminNurserycancelled.py"><i class='bx bx-x-circle'></i> Cancelled nurseries</a>
        </div>
        
        <button class="dropdown-btn"><i class='bx bx-package'></i> Delivery 
            <i class="bx bx-chevron-down ms-auto"></i>
        </button>
        <div class="dropdown-container">
            <a href="./adminDeliveryaddnew.py"><i class='bx bx-user-plus'></i> Add new employee</a>
            <a href="./adminDeliveryexisting.py"><i class='bx bx-group'></i> Existing employees</a>
        </div>
    
       <a  href="./adminUserdetails.py"><i class='bx bx-user'></i> User Details</a>
        <a href="./adminaddnewmedicine.py"><i class='bx bx-leaf'></i> Add Medicine Plants</a>
    </div>""")
if query:
    print("""
    <div class="content">


        <div class="table-container mt-4">
            <h2 class="mb-4">New requests form nurseries:</h2>
            <table>
                <tr class=" text-center">
                    <th>S.No</th>
                    <th>Nursery ID</th>
                    <th>Shop Name</th>
                    <th>Shop Address</th>
                    <th>Shop picture </th>
                    <th>Status </th>
                    <th>Action</th>
                </tr>""")
    sno = 1
    for i in query:
        print(f"""
                <tr>
                    <td>{sno}</td>
                    <td>{i[19]}</td>
                    <td>{i[1]}</td>
                    <td>{i[6] + " , " + i[7]}</td>
                    <td><img src="./assets/{i[2]}" width="100px"></td>
                    <td ><p class="badge text-bg-warning">{i[21]}</p></td>
                    <td><button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#exampleModal{i[0]}">View Details</button></td>
                </tr>""")
        print(f"""



        <!-- Modal -->
        <div class="modal fade " id="exampleModal{i[0]}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-xl">
            <div class="modal-content">
              <div class="modal-header">
                 <h1 class="modal-title fs-5" id="exampleModalLabel">Shop details</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class=" d-flex p-5 "><form method="post">
              <div > <h5>Company name: <span class="span1">{i[1]} </span></h5> <h5>Shop picture (1): <img src="./assets/{i[2]}" alt="" width="100px" height="100px"></h5> <h5>Shop picture (2): <img src="./assets/{i[3]}" alt="" width="100px" height="100px"></h5> <h5>Company email: <span class="span1">{i[4]}</span></h5> <h5>Company phone: <span class="span1">{i[5]}</span></h5> <h5>Address line1: <span class="span1">{i[6]}</span></h5> <h5>Address line2: <span class="span1">{i[7]}</span></h5> <h5>city: <span class="span1">{i[8]}</span></h5> 
                     <h5>Zipcode: <span class="span1">{i[9]}</span></h5> <h5>State: <span class="span1">{i[10]}</span></h5> <h5>Country: <span class="span1">{i[11]}</span></h5> <h5>License number: <span class="span1">{i[12]}</span></h5> <h5>License picture: <img src="./assets/{i[13]}" alt="" width="100px" height="100px"></h5> <h5>Available plant types: <span class="span1">{i[14] + ", " + i[15] + ", " + i[16] + ", " + i[17] + ", " + i[18]}</span class="span1"></h5><h5>NURSERY ID: <span class="span1">{i[19]}</span></h5>
                     </div>  
                     <input type="hidden" name="selected_email" value="{i[4]}">
                     <input type="hidden" name="selected_shop" value="{i[1]}">
                     <input type="hidden" name="selected_shopID" value="{i[20]}">     
           </div>
              <div class="modal-footer">

        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <input type="hidden" name="declined_id" value="{i[0]}">
              </div>
            </div>
          </div>
        </div>""")
        sno += 1
    print(f"""
            </table>
        </div>""")


else:
    print("""<h2 class="text-center mt-5"> No requests found as of now..</h2>""")


print("""   
    <div class="footer ">
        <p >&copy; 2024 Go Green Online Nursery |  Date: <span id="date"></span></p>
    </div>
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


decline = store.getvalue("decline")
if decline != None:
    declined_id = store.getvalue("declined_id")
    selected_email = store.getvalue("selected_email")
    selected_shop = store.getvalue("selected_shop")
    selected_shopID = store.getvalue("selected_shopID")
    fromadd = 'sakthivelsubash0402@gmail.com'
    password2 = 'evcp ltxn ywkb uycx'
    toadd = selected_email
    subject = """Nursery registration process"""
    body = f"Hello, {selected_shop}!. Your company does not met with our qualifications. So it has been blocked. "
    msg = f"""Subject: {subject}\n\n{body}"""
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(fromadd, password2)
    server.sendmail(fromadd, toadd, msg)
    server.quit()
    q = f"""UPDATE `nurseryreg` SET `regstatus`='blocked' where id='{declined_id}'"""
    cur.execute(q)
    con.commit()
    print(f"""<script> location.href="adminNurseryrequests.py"
        alert("{selected_shop} blocked!")</script>""")

