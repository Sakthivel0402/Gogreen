#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, smtplib
import random

cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="GoGreen")
cur = con.cursor()
id = store.getvalue("id")

query = f"""select * from delireg where id='{id}'"""
cur.execute(query)
q = cur.fetchall()
name = q[0][1]
deliID = q[0][15]

random_number = random.randint(1, 5)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> delivery pending requests</title>
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
    top: 20px;
    transition: background-color 0.3s, box-shadow 0.3s;
}

.logout-btn:hover {
    background-color: #ea2828;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); 
}
.main-content {
            margin-left: 250px;
            padding: 20px;
            width: calc(100% - 250px);
        }
        .main-content h2  {
            margin-top: 0;
            color: #4CAF50;
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

        .active{
        background-color: #2c2a2ab9 !important;
    }

    </style>
</head>
<body>""")
print(f"""

    <div class="header">
        <h1 class="ms-5" style="color: #fff;"> Delivery Dashboard</h1>
        <a href="./deliveryLogin.py" class="logout-btn text-decoration-none">Logout</a>
    </div>

    <div class="sidebar">
        <img src="./assets/GG-logo3.png" width="150px" alt="Go Green Logo">

        <a href="./deliveryDashboard.py?id={id}" class="mt-4 "><i class='bx bx-home'></i> Home</a>

        <a  href="./deliveryPendingrequests.py?id={id}"><i class='bx bx-time'></i> Pending Requests</a>
        <a class="active" href="./deliveryOngoing.py?id={id}"><i class='bx bx-cart'></i> Ongoing Orders</a>
        <a href="./deliveryCompleted.py?id={id}"><i class='bx bx-check'></i> Completed Orders</a>
        <a href="./deliveryCancelled.py?id={id}"><i class='bx bx-x'></i> Cancelled Orders</a>



    </div>""")

print(f"""    
    <div class="main-content">

""")
q = f"""select * from orders where deliverymanid='{id}' and status='ordered' and deliverymanstatus='confirmed'"""
cur.execute(q)
query = cur.fetchall()

if query:
    print("""
            <h3 class="mt-5">Pending Deliveries:</h3>
            <div class="card mt-3">

            <table>
                <thead>
                    <tr>
                        <th>S.No</th>
                        <th>Order ID</th>
                        <th>Customer Name</th>
                        <th>Nursery Name</th>
                        <th>Plant picture</th>
                        <th>Plant name</th>
                        <th>Quantity</th>
                        <th>Delivery Address</th>
                        <th>Status</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>""")

    sno = 1
    for i in query:
        order_id = i[18]
        nur_id = i[15]
        cus_id = i[1]

        n = f"""select shopname from nurseryreg where nurseryid='{nur_id}'"""
        cur.execute(n)
        nur = cur.fetchone()

        c = f"""select firstname from userreg where id='{cus_id}'"""
        cur.execute(c)
        cus = cur.fetchone()
        print(f"""
            <tr>
                <td>{sno}</td>
                <td>{order_id}</td>
                <td>{cus[0]}</td>
                <td>{nur[0]}</td>
                <td><img src="./assets/{i[4]}" width="100px"></td>
                <td>{i[3]}</td>
                <td>{i[19]}</td>
                    <td>{i[22] + ", " + i[23] + ", " + i[24] + ", " + i[25] + ", " + i[26] + ", " + i[27]}</td>
                <td ><p class="badge bg-success">{i[30]}</p></td><form method="post">
                <td class=""><input type="submit" name="accept" class="btn btn-warning" value="Delivered"></form></td>

            </tr>
        """)
        sno += 1
    print("""</tbody>
            </table>    
            </div>

        </div>

    <div class="footer ">
        <p >&copy; 2024 Go Green Online Nursery |  Date: <span id="date"></span></p>
    </div>""")

else:
    print("""<h2 class="text-center mt-5"> No requests found as of now..</h2>""")

print("""    <script>
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
</html>""")

accept = store.getvalue("accept")

if accept != None:
    q = f"""update delireg set bookedstatus='' where id='{id}'"""
    cur.execute(q)
    query = con.commit()
    q1 = f"""update orders set deliverymanstatus='finished', status='delivered' where orderid='{order_id}'"""
    cur.execute(q1)
    query1 = con.commit()
    print(f"""<script>alert("Product delivered successfully!")
             location.href="deliveryOngoing.py?id={id}"
                </script>""")
