#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
from datetime import datetime
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="GoGreen")
cur = con.cursor()
id=store.getvalue("id")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User orders</title>
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
            <a  class="active" href="./userCurrentorders.py?id={id}"><i class='bx bx-time'></i> Current orders</a>
            <a href="./userCompletedorders.py?id={id}"><i class='bx bx-check'></i> Completed orders</a>
            <a href="./userCancelled.py?id={id}"><i class='bx bx-x'></i> Cancelled orders</a>
        </div>
    </div>
    <div class="content">
    """)

    q = f"""SELECT * FROM orders where customerid='{id}' and status='ordered' or status='delivered' """
    cur.execute(q)
    query = cur.fetchall()



    if query:
        print("""
        <div class="cart-container mt-5 bg-transparent">
            <h2 class="yourcart"><i class=' bx bx-cart'></i> Your orders</h2>  
            <div class="cart-headings ms-5">
                <div class="heading-product ">PRODUCT</div>
                <div class="heading-price ms-5">PRICE</div>
                <div class="heading-quantity">QUANTITY</div>
                <div class="heading-total">STATUS</div>
            </div>
        """)


        for i in query:
            orderid=i[0]
            invalid = f"""select status from orders where id='{i[0]}'"""
            cur.execute(invalid)
            inv=cur.fetchone()
            disable_delete = "disabled" if inv[0]=='delivered' else ""
            disable_cancel = "disabled" if inv[0]=='delivered' else ""
            enable_received = "" if inv[0]=='delivered' else "disabled"
            print(f"""<form method="post">
                <div class="cart-item" data-price="{i[14]}">
                    <div class="product-info">
                        <img src="./assets/{i[4]}" width="100px" class="product-img">
                        <div class="product-details">
                            <strong>{i[3]}</strong>
                            <p>Growth rate: <strong>{i[9]}</strong></p>
                        </div>
                    </div>
                    <div class="price me-5"> {i[14]}</div>
                    <div class="quantity-control">
                        <input type="hidden" name="orderid" value="{orderid}">
                        <input type="hidden" name="deliid" value="{i[16]}">
                        <input type="hidden" name="proid" value="{i[2]}">
                        <input type="number"  value="{i[19]}" min="1" class="quantity-input me-4" readonly name="count">
                       <button type="button" name="delete"  title="Remove" class="delete-btn ms-3" data-bs-toggle="modal" data-bs-target="#exampleModal{i[0]} {disable_delete}">&#128465;</button>

                    </div>
                    </form>
                    <div class="total "> <span class="badge text-bg-success ms-5">{i[21]}</span></span> </div>
                </div>
            """)



            print(f"""
                <div class="modal fade" id="exampleModal{i[0]}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel{i[0]}">Give a reason for cancellation:</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
              <form method="post">
            <label  for="cancelReason">Reason for cancellation:</label>
            <select class="form-select mb-3" name="cancelReason" id="cancelReason" required>
                <option value="" disabled selected>Select a reason</option>
                <option value="changeOfMind">Changed my mind</option>
                <option value="shippingDelays">Delivery is taking too long</option>
                <option value="foundBetterPrice">Found a better price elsewhere</option>
                <option value="wrongProduct">Ordered the wrong product</option>
                <option value="financialReasons">Financial reasons</option>
                <option value="qualityConcerns">Concerns about plant quality</option>
                <option value="gardeningPlansChanged">Change in gardening plans</option>
            </select>
        
            <label for="otherReason">Other reason (if any):</label>
        <div class="form-floating">
          <textarea name="cancelReason" class="form-control" placeholder="Leave a comment here" id="floatingTextarea"></textarea>
          <label for="floatingTextarea">Comments</label>
        </div>
        
        
                
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <input type="submit" class="btn btn-danger" value="Cancel order" name="delete">
                </form>
              </div>
            </div>
          </div>
        </div>""")
            print(f"""
                <div class="modal fade" id="exampleModal2" tabindex="-1" aria-labelledby="exampleModalLabel2" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel2">Give a reason for cancellation:</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
              <form method="post">
            <label  for="cancelReason">Reason for cancellation:</label>
            <select class="form-select mb-3" name="cancelReason" id="cancelReason" required>
                <option value="" disabled selected>Select a reason</option>
                <option value="changeOfMind">Changed my mind</option>
                <option value="shippingDelays">Delivery is taking too long</option>
                <option value="foundBetterPrice">Found a better price elsewhere</option>
                <option value="wrongProduct">Ordered the wrong product</option>
                <option value="financialReasons">Financial reasons</option>
                <option value="qualityConcerns">Concerns about plant quality</option>
                <option value="gardeningPlansChanged">Change in gardening plans</option>
            </select>

            <label for="otherReason">Other reason (if any):</label>
        <div class="form-floating">
          <textarea name="cancelReason" class="form-control" placeholder="Leave a comment here" id="floatingTextarea"></textarea>
          <label for="floatingTextarea">Comments</label>
        </div>



              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary mt-4" data-bs-dismiss="modal">Close</button>
        <input type="submit" class="order-now-btn continue-shopping" name="cancel" value="Cancel order" >
                </form>
              </div>
            </div>
          </div>
        </div>""")

        print(f"""<div class="order-now-container">

                  <form method="post">      <button type="button" name="delete"  title="Remove" class="btn ms-3 continue-shopping" data-bs-toggle="modal" data-bs-target="#exampleModal2" {disable_cancel}>Cancel order</button>
                                <input type="submit"  class="btn ms-2 continue-shopping2" value="Received" name="received" {enable_received}></form>




     <div class="total-amount float-end mt-4 me-5">
                <h3 class="d-inline fw-light"> Total: </h3>
                     <span class="fw-bold" style="font-size:25px" id="total-amount">&#8377; {i[20]}</span>

                </div>
            </div>

            </div>""")

        s=f"""select days from orders where id='{i[0]}' and status='ordered' """
        cur.execute(s)
        select=cur.fetchone()

        if select:
            selection = select[0]
            print(f"""
                        <div class="text-center mt-5"> <h2>Your order will be received in {selection}  days...</h2></div>

            """)
        else:
            print("""  """)

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

cancel = store.getvalue("cancel")
proid = store.getvalue("proid")
count = store.getvalue("count")



if cancel != None:
        current_time = datetime.now().strftime('%d-%m-%Y ')
        d = f"""update delireg set bookedstatus='' where id='{query[0][16]}'"""
        cur.execute(d)
        con.commit()
        for qty, oid in zip(count, orderid):
            q = f"""UPDATE `orders` SET status='cancelled', cancelledtime='{current_time}' WHERE id='{oid}'"""
            cur.execute(q)
            con.commit()
            print(f"""<script>
                              alert("Order cancelled successfully!");
                              location.href="userCurrentorders.py?id={id}";
                          </script>""")


cancelReason=store.getvalue("cancelReason")
delete = store.getvalue("delete")

if delete:
    current_time = datetime.now().strftime('%d-%m-%Y ')
    q = f"""update `orders` set cancelreason='{cancelReason}', cancelledtime='{current_time}', status='cancelled' WHERE id='{orderid}'"""
    cur.execute(q)
    con.commit()
    print(f"""<script>alert("Order cancelled successfully!");
                    location.href="userCurrentorders.py?id={id}";
                              </script>""")

received=store.getvalue("received")
if received != None:
    current_time = datetime.now().strftime('%d-%m-%Y ')
    q = f"""update `orders` set deliveredtime='{current_time}', status='completed' WHERE id='{orderid}'"""
    cur.execute(q)
    con.commit()
    print(f"""<script>alert("Order received successfully!");
                        location.href="userCurrentorders.py?id={id}";
                                  </script>""")



