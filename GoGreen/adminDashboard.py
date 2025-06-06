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
    <title>Go Green Admin Dashboard</title>
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
            background: white;
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
    text-decoration:none;
    transition: background-color 0.3s, box-shadow 0.3s;
}
.main-content {
           
            padding: 20px;
            width: calc(100% - 750px);
        }
        .main-content h2  {
            margin-top: 0;
            color: #4CAF50;
        }
    .btn {
            background-color: #28AFB0;
            color: white;
            padding: 10px 15px;
            border: none;
            height:45px;
            width:180px;
            font-size:15px;
            border-radius: 5px;
            cursor: pointer;
            text-align: center;
            display: inline-block;
            margin-top: 10px;
        }
        .btn:hover {
            background-color: #217980;
            color:#ffffff;
        }
        .btn:focus {
            background-color: #000000;
            color:#ffffff;
        }
    .card {
            background: #fff;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
        }
        .card h3 {
            margin: 0 0 10px;
        }
        .card p {
            margin: 5px 0;
        }

.logout-btn:hover {
    background-color: #ea2828;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); 
}
.active {
            background-color: #2c2a2ab9 !important;
        }

    </style>
</head>
<body>

    <div class="header">
        <h1 class="ms-5" style="color: #fff;"> Admin Dashboard</h1>
        <a href="./adminLogin.py" class="logout-btn">Logout</a>
    </div>""")
print("""

    <div class="sidebar">
        <img src="./assets/GG-logo3.png" width="150px" alt="Go Green Logo">
        
        <a href="./adminDashboard.py" class="mt-4 active"><i class='bx bx-home'></i> Home</a>
        
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
print("""
    <div class="content">
        

        
        <div class="main-content">
           <h3>Welcome,</h3> <h2 class="fw-bold"> Admin!</h2>
            <div class="card mt-4">
                <h3>Manage Employee Details</h3>
                <p>Add, update the employees</p>
                <a href="./adminDeliveryaddnew.py" class="btn">Manage Employees</a>
            </div>
            <div class="card">
                <h3>Recent Orders</h3>
                <p>View and manage orders placed by customers.</p>
                <a href="./adminCurrentorders.py" class="btn">View Orders</a>
            </div>
            <div class="card">
                <h3>Nursery Details</h3>
                <p>View recently added nursery details.</p>
                <a href="./adminNurseryexisting.py" class="btn">View Details</a>
            </div>
        </div>
        

    <div class="footer ">
        <p >&copy; 2024 Go Green Online Nursery |  Date: <span id="date"></span></p>
    </div>

    <script>
        document.getElementById("date").textContent = new Date().toLocaleDateString();

        // Script for handling dropdowns
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