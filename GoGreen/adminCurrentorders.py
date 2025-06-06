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
    <title> Admin current orders</title>
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
    .active {
            background-color: #2c2a2ab9 !important;
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
     .no-products {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 70vh; /* Full viewport height */
            text-align: center;
            font-size: 24px;
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

.logout-btn:hover {
    background-color: #ea2828;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); 
}

    </style>
</head>
<body>""")
print("""

    <div class="header">
        <h1 class="ms-5" style="color: #fff;"> Admin Dashboard</h1>
        <a href="./adminLogin.py" class="logout-btn">Logout</a>
    </div>

    <div class="sidebar">
        <img src="./assets/GG-logo3.png" width="150px" alt="Go Green Logo">
        
        <a href="./adminDashboard.py" class="mt-4"><i class='bx bx-home'></i> Home</a>
        
        <button class="dropdown-btn active"><i class='bx bx-cart'></i> Order Management
            <i class="bx bx-chevron-down ms-auto"></i>
        </button>
        <div class="dropdown-container">
            <a class="active" href="./adminCurrentorders.py"><i class='bx bx-time'></i> Current orders</a>
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

q = """SELECT * FROM orders WHERE status='ordered'"""
cur.execute(q)
query = cur.fetchall()
if query:
    print("""
    <div class="content">
        <h3 class="mt-5">Pending Deliveries:</h3>
        <div class="card mt-3">
            <table>
                <thead>
                    <tr>
                        <th>S.No</th>
                        <th>Order ID</th>
                        <th>Customer Name</th>
                        <th>Nursery Name</th>
                        <th>Delivery person name</th>
                        <th>Delivery Address</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>""")

    sno = 1
    for i in query:
        order_id = i[18]
        nur_id = i[15]
        cus_id = i[1]
        deli_id = i[16]
        status = i[21]

        d = f"""SELECT firstname FROM delireg WHERE id='{deli_id}'"""
        cur.execute(d)
        deli = cur.fetchone()

        n = f"""SELECT shopname FROM nurseryreg WHERE nurseryid='{nur_id}'"""
        cur.execute(n)
        nur = cur.fetchone()

        c = f"""SELECT firstname FROM userreg WHERE id='{cus_id}'"""
        cur.execute(c)
        cus = cur.fetchone()

        print(f"""
            <tr>
                <td>{sno}</td>
                <td>{order_id}</td>
                <td>{cus[0]}</td>
                <td>{nur[0]}</td>
                <td>{deli[0]}</td>
                <td>{i[22] + ", " + i[23] + ", " + i[24] + ", " + i[25] + ", " + i[26] + ", " + i[27]}</td>
                <td><span class="badge bg-success">{status}</span></td>
            </tr>
        """)
        sno += 1

else:
    print("""
    <div class="no-products">
        <h1>No orders found :(</h1>
    </div>
    """)

print("""
                </tbody>
            </table>    
        </div>
    </div>
    <div class="footer">
        <p>&copy; 2024 Go Green Online Nursery | Date: <span id="date"></span></p>
    </div>
    """)

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
