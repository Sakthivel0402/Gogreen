#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="GoGreen")
cur = con.cursor()
id = store.getvalue("id")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>completed orders</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/boxicons@2.1.4/dist/boxicons.js"></script>
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" integrity="sha512-Kc323vGBEqzTmouAECnVceyQqyqdsSiqLQISBL29aUW4U/M7pSPA/gEUZQqv1cwx4OnYxTxve5UMg5GT6L4JJg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
        * {
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
            font-family: "Poppins", sans-serif;
            font-weight: 300;
        }
        body {
            background-color: #83efef6b;
        }
        .active {
            background-color: #2c2a2ab9 !important;
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
        .content {
            margin-left: 230px;
            padding: 20px;
            transition: all 0.5s ease;
        }
        .table-container {
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
            height: 30px;
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
        .cart-container {
            max-width: 1100px;
            border-radius: 15px;
            margin: 0 auto;
            font-family: Arial, sans-serif;
            background-color: #fafafa;
            padding: 20px;
        }
        .cart-container h2 {
            font-size: 24px;
            color: #4b4b00;
            margin-bottom: 20px;
        }
        .cart-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 3px solid #c2a86f;
            flex-wrap: wrap;
            gap: 10px;
        }
        .product-info {
            display: flex;
            align-items: center;
            flex: 2;
        }
        .product-img {
            width: 80px;
            height: auto;
            margin-right: 10px;
            border-radius: 5px;
        }
        .product-details {
            color: #6b6b00;
        }
        .product-details p {
            margin: 0;
            font-size: 14px;
            color: #6b6b00;
        }
        .price, .total {
            flex: 1;
            text-align: center;
            font-size: 16px;
            color: #4b4b00;
        }
        .quantity-control {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .quantity-btn {
            background-color: #28AFB0;
            border-radius: 50%;
            border: 0.5px solid rgba(120, 163, 242, 0.623);
            color: #ffffff;
            font-weight: 600;
            width: 25px;
            height: 25px;
            cursor: pointer;
            font-size: 14px;
        }
        .quantity-input {
            width: 40px;
            text-align: center;
            border: 1px solid #c2a86f;
            border-radius: 5px;
            background-color: #83efef6b;
            color: #000000;
            font-weight: 500;
        }
        .quantity-btn:active {
            background-color: #c2a86f;
            color: #000000;
        }
        .delete-btn {
            background-color: transparent;
            border: none;
            cursor: pointer;
            font-size: 24px;
            font-weight: 700;
            color: #ea2828;
        }
        .continue-shopping {
            background-color: #ffffff;
            color: #ff1d0d;
            border: 3px solid #ff1d0d;
            padding: 2px 5px;
            height:45px !important;
            cursor: pointer;
            font-family: "Poppins", sans-serif !important;
            margin-top: 20px;
            font-weight: 700;
            text-align: center;
            display: inline-block;
            transition: all 0.1s ease-out;
        }
        .continue-shopping:hover {
            background-color: #ff1d0d;
            color: #ffffff;
            font-weight: 700;
            transition: all 0.1s ease-out;
        }

          .continue-shopping2 {
            background-color: #FFD670;
            color: #000000;
            border: 3px solid #000000;
            padding: 2px 5px;
            height:45px !important;
            cursor: pointer;
            font-family: "Poppins", sans-serif !important;
            margin-top: 20px;
            font-weight: 700;
            text-align: center;
            display: inline-block;
            transition: all 0.1s ease-out;
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
        .continue-shopping2:hover {
            background-color: #000000;
            color: #FFD670;
            font-weight: 700;
            transition: all 0.1s ease-out;
        }

        .cart-headings {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 3px solid #c2a86f;
            font-weight: bold;
            color: #4b4b00;
            margin-bottom: 10px;
            gap: 10px;
        }
        .heading-product {
            flex: 2;
            font-weight: 400;
        }
        .heading-price, .heading-quantity, .heading-total {
            flex: 1;
            text-align: center;
            font-weight: 400;
        }
        .yourcart {
            border-bottom: 1px solid #c2a86f;
            font-weight: 700;
            font-size: 35px !important;
        }
        .no-products {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 70vh; /* Full viewport height */
            text-align: center;
            font-size: 24px;
            }
            
            
             .star-rating {
            direction: rtl; /* This flips the order of elements */
            display: inline-flex;
            font-size: 30px;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        .star-rating input {
            display: none;
        }
        .star-rating label {
            color: #ccc;
            padding: 0 5px;
            transition: color 0.2s;
        }
        .star-rating input:checked ~ label,
        .star-rating input:checked ~ label ~ label {
            color: #f39c12;
        }
        .star-rating label:hover,
        .star-rating label:hover ~ label {
            color: #f39c12;
        }
        .feedback-form {
    background-color: rgba(255, 255, 255, 0.2); /* Semi-transparent background */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(10px); /* Adds the frosted glass effect */
    -webkit-backdrop-filter: blur(10px); /* For Safari */
    max-width: 600px;
    width: 100%;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.3); /* Optional: adds a border with some transparency */
}  

        .feedback-form textarea {
            width: 100%;
            height: 100px;
            background-color: rgba(255, 255, 255, 0.3);
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ddd;
            margin-bottom: 20px;
           box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            resize: none;
        }
        .feedback-form .btn1 {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            background-color: #439A86;
            color: #ffffff;
            font-size: 16px;
            cursor: pointer;
            transition: all ease 0.6s;
        }    
        .feedback-form .btn1:hover {    
            background-color: #327163 !important;
         transition: all ease 0.6s;


    </style>
</head>
<body>
""")
q = f"""SELECT * FROM userreg WHERE id='{id}'"""
cur.execute(q)
query = cur.fetchall()

if query:
    print(f"""
    <div class="header">
        <h1 class="ms-5" style="color: #fff;"> Orders</h1>
        <a href="./userLogin.py?id={id}" class="logout-btn text-decoration-none">Logout</a>
    </div>
    <div class="sidebar">
        <img src="./assets/GG-logo3.png" width="150px" alt="Go Green Logo">
        <a href="./userDashboard.py?id={id}" class="mt-4 "><i class='bx bx-home'></i> Home</a>
        <a href="./viewPlantsandseeds.py?id={id}"><i class='bx bx-leaf'></i> View Plants & Seeds</a>
        <a href="#"><i class='bx bx-search'></i> Find Medicine Plants</a>
        <button class="dropdown-btn active"><i class='bx bx-cart'></i> Order Management
            <i class="bx bx-chevron-down ms-auto"></i>
        </button>
        <div class="dropdown-container">
            <a href="./userCart.py?id={id}"><i class='bx bx-cart'></i> Your cart</a>
            <a   href="./userCurrentorders.py?id={id}"><i class='bx bx-time'></i> Current orders</a>
            <a class="active" href="./userCompletedorders.py?id={id}"><i class='bx bx-check'></i> Completed orders</a>
            <a href="./userCancelled.py?id={id}"><i class='bx bx-x'></i> Cancelled orders</a>
        </div>
    </div>
    <div class="content">
    """)

    q = f"""SELECT * FROM orders where customerid='{id}' and status='completed'  """
    cur.execute(q)
    query = cur.fetchall()

    if query:
        print("""<h2> Completed orders:</h2>
                    <div class="card mt-3">
                        <table>
                            <thead>
                                <tr>
                                    <th>S.No</th>
                                    <th>Order ID</th>
                                    <th>Nursery Name</th>
                                    <th>Plant name</th>
                                    <th>Plant image</th>
                                    <th>Quantity</th>
                                    <th>Date</th>
                                    <th>Status</th>
                                    <th>Feedback</th>
                                </tr>
                            </thead>
                            <tbody>""")

        sno = 1
        rendered_feedback_buttons = set()

        for i in query:
            feed = i[33]
            stars = i[34]
            o_id = i[0]
            order_id = i[18]
            nur_id = i[15]
            deli_id = i[3]
            status = i[21]
            quantity = i[19]
            date = i[32]

            # Fetch nursery shop name
            n = f"""SELECT shopname FROM nurseryreg WHERE nurseryid='{nur_id}'"""
            cur.execute(n)
            nur = cur.fetchone()

            # Start row and display data
            print(f"""
                    <tr>
                        <td>{sno}</td>
                        <td>{order_id}</td>
                        <td>{nur[0]}</td>
                        <td>{deli_id}</td>
                        <td><img src="./assets/{i[4]}" width="100px"></td>
                        <td>{quantity}</td>
                        <td>{date}</td>
                        <td><span class="badge bg-success">{status}</span></td>
            """)

            if not feed and not stars and order_id not in rendered_feedback_buttons:
                print(f"""
                        <td><button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal{o_id}">
                            Give feedback
                        </button></td>

                        <!-- Modal for feedback -->
                        <div class="modal fade" id="exampleModal{o_id}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                          <div class="modal-dialog modal-xl">
                            <div class="modal-content">
                              <div class="modal-header">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">Please give your valuable feedback!</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                              </div>
                              <div class="modal-body">
                                <form action="" method="post">
    <input type="hidden" name="order_id" value="{order_id}">
    <div class="feedback-form mt-5 mx-auto">
        <h2 class="mt-2 mb-3">Feedback Form</h2>
        <textarea name="comments" placeholder="Write your feedback here..." required></textarea>
        <div class="star-rating mb-4">
            <input type="radio" name="rating" id="star5" value="5"><label for="star5"><i class="fa-solid fa-star"></i></label>
            <input type="radio" name="rating" id="star4" value="4"><label for="star4"><i class="fa-solid fa-star"></i></label>
            <input type="radio" name="rating" id="star3" value="3"><label for="star3"><i class="fa-solid fa-star"></i></label>
            <input type="radio" name="rating" id="star2" value="2"><label for="star2"><i class="fa-solid fa-star"></i></label>
            <input type="radio" name="rating" id="star1" value="1"><label for="star1"><i class="fa-solid fa-star"></i></label>
        </div>
        <input type="submit" class="btn1 feed" name="submit" value="Submit Feedback">
    </div>
</form>

                              </div>
                            </div>
                          </div>
                        </div>
                """)
                rendered_feedback_buttons.add(order_id)
            else:
                print(f"<td><span style='display:inline' class='fw-bold'> {feed} </span> <span style='display:block;'  class='fw-bold mx-3 mt-3'>  {stars} <p style='color:#f39c12; display:inline;'>  <i class='fa-solid fa-star'></i> </p> </span> </td>")

            print("</tr>")
            sno += 1

    else:
        print("""
                <div class="no-products">
                    <h1>No orders found :(</h1>
                </div>
                """)
    print("""
        <div class="footer">
            <p>&copy; 2024 Go Green Online Nursery | Date: <span id="date"></span></p>
        </div>
        </body>
        </html>
        """)

    print("""
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
        """)


submit = store.getvalue("submit")
if submit != None:
    order_id = store.getvalue("order_id")
    stars = store.getvalue("rating")
    comments = store.getvalue("comments")
    status = f"""UPDATE orders SET feedback='{comments}', stars='{stars}' WHERE orderid='{order_id}'"""
    cur.execute(status)
    con.commit()
    print(f"""<script>
                alert("Thanks for your valuable feedback!");
                location.href="userDashboard.py?id={id}";
              </script>""")



