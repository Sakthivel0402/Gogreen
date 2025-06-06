#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="GoGreen")
cur = con.cursor()
id = store.getvalue("id")

query = f"""select * from nurseryreg where id='{id}'"""
cur.execute(query)
q = cur.fetchall()

maxid=f"""select max(id) from products"""
cur.execute(maxid)
productid=cur.fetchone()

if productid[0]!=None:
    if productid[0]<10:
        productnum="PRO000"+str(productid[0]+1)
    elif productid[0]<100:
        productnum = "PRO00" + str(productid[0]+1)
    elif productid[0]<1000:
        productnum = "PRO0" + str(productid[0]+1)
else:
    productnum="PRO0001"


nur=f"""select nurseryid from nurseryreg where id='{id}'"""
cur.execute(nur)
nurseryID=cur.fetchone()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manage products</title>
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
    
    .form-container {
            background: #fff;
            padding: 20px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            margin-top: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .form-group textarea {
            resize: vertical;
            min-height: 100px;
        }
        label{
        font-weight:500;
        }

    </style>
</head>
<body>""")

print(f"""
        <div class="header">
            <h1 class="ms-5" style="color: #fff;"> Nursery Dashboard</h1>
            <a href="./nurseryLogin.py" class="logout-btn text-decoration-none">Logout</a>
        </div>

        <div class="sidebar">
            <img src="./assets/GG-logo3.png" width="150px" alt="Go Green Logo">

            <a href="./nurseryDashboard.py?id={id}" class="mt-4 "><i class='bx bx-home'></i> Home</a>

            <a class="active" href="./nurseryManageproducts.py?id={id}"><i class='bx bx-building'></i> Manage Products</a>

            <button class="dropdown-btn "><i class='bx bx-cart'></i> View Orders
                <i class="bx bx-chevron-down ms-auto"></i>
            </button>
            <div class="dropdown-container">
                <a href="./nurseryCurrent.py?id={id}" ><i class='bx bx-time'></i> Current orders</a>
            <a href="./nurseryCompleted.py?id={id}"><i class='bx bx-check'></i> Completed orders</a>
                <a href="./nurseryCancelled.py?id={id}"><i class='bx bx-x'></i> Cancelled orders</a>
            </div>

        <a href="./nurseryReviews.py?id={id}"><i class='bx bx-user-circle'></i>Customer Reviews</a>    
        </div>""")

if q:
    print("""
    <div class="main-content">
                 <div class="form-container">
                    <h3>Add New Product:</h3>
                    <form method="post"  enctype="multipart/form-data">
                        <div class="form-group mt-4">

                        <label class="mt-4" for="product_type">Product type:</label>
    <select class="form-select mt-2 mb-4" id="product_type" name="product_type">
        <option value="">Select  type of product </option>
      <option value="Plants">Plants</option>
      <option value="Seeds">Seeds</option>
    </select>

          <label class="mt-4" for="category">Product category:</label>
    <select class="form-select mt-2 mb-4" id="category" name="category">
        <option value="">Select product category </option>
      <option value="Indoor plants">Indoor plants</option>
      <option value="Outdoor plants">Outdoor plants</option>
      <option value="Succulents">Succulents</option>
      <option value="Flowering plants">Flowering plants</option>
      <option value="Medicinal plants">Medicinal plants</option>
    </select>

                            <label  for="plantName">Product Name:</label>
                            <input type="text" id="plantName" name="plantName" placeholder="Enter product name" required>
                        </div>
                        <div class="form-group">
                            <label for="description">Description:</label>
                            <textarea id="description" name="description" placeholder="Enter product description" required></textarea>
                        </div>
                        <label for="color-select">Choose a color:</label>
    <select class="form-select mt-2" name="color" id="color-select">
        <option value="">Select color</option>
        <option value="green">Green</option>
        <option value="blue">Blue</option>
        <option value="red">Red</option>
        <option value="yellow">Yellow</option>
    </select>

     <label class="mt-4" for="growth">Choose Growthrate:</label>
    <select class="form-select mt-2" name="growthrate" id="growth">
        <option value="">Select growth rate</option>
        <option value="Slow">Slow</option>
        <option value="Medium">Medium</option>
        <option value="Fast">Fast</option>
    </select>

     <label class="mt-4" for="soil">Choose Soil type:</label>
    <select class="form-select mt-2" name="soil_type" id="soil">
        <option value="">Select soil type </option>
        <option value="alluvial">Alluvial Soil </option>
        <option value="black">Black Soil </option>
        <option value="red">Red Soil </option>
        <option value="laterite">Laterite Soil </option>
        <option value="mountain">Mountain Soil </option>
        <option value="desert">Desert Soil </option>
        <option value="peaty">Peaty Soil </option>
        <option value="saline">Saline Soil </option>
    </select>

    <label class="mt-4" for="watering-period">Watering Period:</label>
    <select class="form-select mt-2" id="watering-period" name="watering_period">
        <option value="">Select watering period </option>
      <option value="daily">Daily</option>
      <option value="every-2-days">Every 2 Days</option>
      <option value="weekly">Weekly</option>
      <option value="monthly">Monthly</option>
    </select>

    <label class="mt-4 for="suitable-climate">Suitable Climate:</label>
    <select class="form-select mt-2" id="suitable-climate" name="suitable_climate">
        <option value="">Select suitable climate </option>
      <option value="tropical">Tropical</option>
      <option value="subtropical">Subtropical</option>
      <option value="temperate">Temperate</option>
      <option value="arid">Arid</option>
      <option value="semi-arid">Semi-Arid</option>
      <option value="humid">Humid</option>
      <option value="dry">Dry</option>
      <option value="cold">Cold</option>
    </select>

     <div class="form-group mt-4">
                            <label for="img">Image:</label>
                            <input class="form-control" type="file" id="img" name="image"  required>
                        </div>

                        <div class="form-group mt-4">
                            <label for="price">Price:</label>
                            <input type="number" id="price" name="price" placeholder="Enter product price" required>
                        </div>
                        <div class="form-group">
                            <label for="stock">Stock:</label>
                            <input type="number" id="stock" name="stock" placeholder="Enter stock quantity" required>
                        </div>
                        <input type="submit" name="add" class="btn btn-success" value="Add Product">
                    </form>
                </div>""")

    print(f"""    
   
           
            <div class="card mt-4">
             <h3 class="mb-3">Add or Edit products:</h3>
                <table>
                <thead>
                    <tr>
                        <th>Product ID</th>
                        <th>Product type</th>
                        <th>Product name</th>
                        <th>Image </th>
                        <th>Description</th>
                        <th>Price</th>
                        <th>Stock</th>
                        <th>Actions</th>
                    </tr>
                </thead>""")
    plants=f"""select * from products where nurseryid='{nurseryID[0]}'"""
    cur.execute(plants)
    list=cur.fetchall()
    for i in list:
        ids=i[0]
        print(f"""
                <tbody>
                    <tr>
                        <td>{i[13]}</td>
                        <td>{i[1]}</td>
                        <td>{i[3]}</td>
                        <td><img src="./assets/{i[10]}" width="100px"></td>
                        <td>{i[4]}</td>
                        <td>{i[11]}</td>
                        <td>{i[12]}</td>
                        <td>
                        <form method="post">
                          <button type="button" class="btn btn-primary w-100" data-bs-toggle="modal" data-bs-target="#exampleModal{i[0]}">Edit</button>
                            <input type="submit" name="remove{i[0]}" class="btn btn-danger w-100 mt-3" value="Remove"> </form>
                        </td>
                    </tr>
                </tbody>""")
        print(f"""
                <div class="modal fade " id="exampleModal{i[0]}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                  <div class="modal-dialog modal-xl">
                    <div class="modal-content">
                      <div class="modal-header">
                         <h1 class="modal-title fs-5" id="exampleModalLabel">Edit product details</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="d-flex p-5">
  <form method="post">
    <div>
      <div class="d-flex align-items-center mb-3">
      <input type="hidden" name="ids" value="{i[0]}">
        <h5 class="d-inline">Product Type: <span class="span1">{i[1]}</span></h5>
        <input class="form-control w-25 mx-5" name="value1" type="text" placeholder="Update product type">
        <input type="submit" class="btn btn-success" value="Update" name="update1">
      </div>

      <div class="d-flex align-items-center mb-3">
        <h5 class="d-inline">Category: <span class="span1">{i[2]}</span></h5>
        <input class="form-control w-25 mx-5" name="value2" type="text" placeholder="Update category">
        <input type="submit" class="btn btn-success" value="Update" name="update2">
      </div>

      <div class="d-flex align-items-center mb-3">
        <h5 class="d-inline">Plant Name: <span class="span1">{i[3]}</span></h5>
        <input class="form-control w-25 mx-5" name="value3" type="text" placeholder="Update plant name">
        <input type="submit" class="btn btn-success" value="Update" name="update3">
      </div>

      <div class="d-flex align-items-center mb-3">
        <h5 class="d-inline">Description: <span class="span1">{i[4]}</span></h5>
        <input class="form-control w-25 mx-5" name="value4" type="text" placeholder="Update description">
        <input type="submit" class="btn btn-success" value="Update" name="update4">
      </div>

      <div class="d-flex align-items-center mb-3">
        <h5 class="d-inline">Color: <span class="span1">{i[5]}</span></h5>
        <input class="form-control w-25 mx-5" name="value5" type="text" placeholder="Update color">
        <input type="submit" class="btn btn-success" value="Update" name="update5">
      </div>
    
    <div class="d-flex align-items-center mb-3">
        <h5 class="d-inline">Growthrate: <span class="span1">{i[6]}</span></h5>
        <input class="form-control w-25 mx-5" name="value6" type="text" placeholder="Update growthrate">
        <input type="submit" class="btn btn-success" value="Update" name="update6">
      </div>
      
      <div class="d-flex align-items-center mb-3">
        <h5 class="d-inline">Soil type: <span class="span1">{i[7]}</span></h5>
        <input class="form-control w-25 mx-5" name="value7" type="text" placeholder="Update soil type">
        <input type="submit" class="btn btn-success" value="Update" name="update7">
      </div>
      
      <div class="d-flex align-items-center mb-3">
        <h5 class="d-inline">Watering period: <span class="span1">{i[8]}</span></h5>
        <input class="form-control w-25 mx-5" name="value8" type="text" placeholder="Update watering period">
        <input type="submit" class="btn btn-success" value="Update" name="update8">
      </div>
      
      <div class="d-flex align-items-center mb-3">
        <h5 class="d-inline">Suitable climate: <span class="span1">{i[9]}</span></h5>
        <input class="form-control w-25 mx-5" name="value9" type="text" placeholder="Update Climate">
        <input type="submit" class="btn btn-success" value="Update" name="update9">
      </div>
      
      <div class="d-flex align-items-center mb-3">
        <h5 class="d-inline">Image: <img src="./assets/{i[10]}" width="100px"></h5>
        <input class="form-control w-25 mx-5" name="value10" type="file" placeholder="Update picture">
        <input type="submit" class="btn btn-success" value="Update" name="update10">
      </div>

      <div class="d-flex align-items-center mb-3">
        <h5 class="d-inline">Price: <span class="span1">{i[11]}</span></h5>
        <input class="form-control w-25 mx-5" name="value11" type="text" placeholder="Update price">
        <input type="submit" class="btn btn-success" value="Update" name="update11">
      </div>

      <div class="d-flex align-items-center mb-3">
        <h5 class="d-inline">Stock: <span class="span1">{i[12]}</span></h5>
        <input class="form-control w-25 mx-5" name="value12" type="text" placeholder="Update stock">
        <input type="submit" class="btn btn-success" value="Update" name="update12">
      </div>
    </div>  
  </form>
</div>

                      <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                      </div>
                    </div>
                  </div>
                </div>""")
    print("""
            </table>
            </div>
    
            """)
    print("""

    <div class="footer ">
        <p >&copy; 2024 Go Green Online Nursery |  Date: <span id="date"></span></p>
    </div>""")

else:
    print("""
    <h2 class="text-center mt-5"> No products are here...</h2>""")

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
</html>
""")

for i in list:
    remove = store.getvalue(f"remove{i[0]}")
    if remove is not None:
        q = f"DELETE FROM `products` WHERE id='{i[0]}'"
        cur.execute(q)
        con.commit()

        print(f"""
            <script>
                alert("Product removed!");
                location.href="nurseryManageproducts.py?id={id}";
            </script>
        """)
        break


update1=store.getvalue("update1")
if update1!=None:
    value1 = store.getvalue("value1")
    ids = store.getvalue("ids")
    update = f"""update `products` set `producttype`='{value1}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")


update2=store.getvalue("update2")
if update2!=None:
    value2 = store.getvalue("value2")
    ids = store.getvalue("ids")
    update = f"""update `products` set `category`='{value2}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")

update3=store.getvalue("update3")
if update3!=None:
    value3 = store.getvalue("value3")
    ids = store.getvalue("ids")
    update = f"""update `products` set `name`='{value3}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")

update4=store.getvalue("update4")
if update4!=None:
    value4 = store.getvalue("value4")
    ids = store.getvalue("ids")
    update = f"""update `products` set `decription`='{value4}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")

update5=store.getvalue("update5")
if update5!=None:
    value5 = store.getvalue("value5")
    ids = store.getvalue("ids")
    update = f"""update `products` set `color`='{value5}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")

update6=store.getvalue("update6")
if update6!=None:
    value6 = store.getvalue("value6")
    ids = store.getvalue("ids")
    update = f"""update `products` set `growthrate`='{value6}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")

update7=store.getvalue("update7")
if update7!=None:
    value7 = store.getvalue("value7")
    ids = store.getvalue("ids")
    update = f"""update `products` set `solitype`='{value7}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")

update8=store.getvalue("update8")
if update8!=None:
    value8 = store.getvalue("value8")
    ids = store.getvalue("ids")
    update = f"""update `products` set `wateringperiod`='{value8}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")

update9 = store.getvalue("update9")
if update9 != None:
    value9 = store.getvalue("value9")
    ids = store.getvalue("ids")
    update = f"""update `products` set `suitableclimate`='{value9}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")

update10 = store.getvalue("update10")
if update10 != None:
    value10 = store.getvalue("value10")
    ids = store.getvalue("ids")
    update = f"""update `products` set `image`='{value10}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")

update11 = store.getvalue("update11")
if update11 != None:
    value11 = store.getvalue("value11")
    ids = store.getvalue("ids")
    update = f"""update `products` set `price`='{value11}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")

update12 = store.getvalue("update12")
if update12 != None:
    value12 = store.getvalue("value12")
    ids = store.getvalue("ids")
    update = f"""update `products` set `stock`='{value12}' where id='{ids}'"""
    cur.execute(update)
    con.commit()
    print(f"""<script>alert("detail updated successfully!")
             location.href="nurseryManageproducts.py?id={id}"
                </script>""")



add=store.getvalue("add")
if add != None:
    product_type=store.getvalue("product_type")
    category=store.getvalue("category")
    plantName=store.getvalue("plantName")
    description=store.getvalue("description")
    color=store.getvalue("color")
    growthrate=store.getvalue("growthrate")
    soil_type=store.getvalue("soil_type")
    watering_period=store.getvalue("watering_period")
    suitable_climate=store.getvalue("suitable_climate")
    image=store['image']
    if image.filename:
        proof = os.path.basename(image.filename)
        open("Assets/" + proof, "wb").write(image.file.read())
        price=store.getvalue("price")
        stock=store.getvalue("stock")
        update=f"""INSERT INTO `products`(`producttype`, `category`, `name`, `description`, `color`, `growthrate`, `solitype`, `wateringperiod`, `suitableclimate`, `image`, `price`, `stock`, `productid`, `nurseryid`) VALUES ('{product_type}','{category}','{plantName}','{description}','{color}','{growthrate}','{soil_type}','{watering_period}','{suitable_climate}','{proof}','{price}','{stock}','{productnum}','{nurseryID[0]}')"""
        cur.execute(update)
        con.commit()
        print(f"""<script>alert("Product added successfully!")
         location.href="nurseryManageproducts.py?id={id}"
            </script>""")

