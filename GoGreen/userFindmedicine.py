#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, random
from datetime import datetime

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
    <title>Find medicinal plants</title>
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
         .active{
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
.headline {
            text-align: center;
            font-size: 36px;
            font-weight: 700;
            margin-top: 30px;
            margin-bottom: 20px;
            color: #de7112;
        }

        .searchbar-container {
            display: flex;
            justify-content: center;
            margin-bottom: 50px;
        }

        .searchbar {
            width: 80%;
            background-color: #28b0b0bb;;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            display: flex;
            gap: 15px;
            justify-content: center;
        }

        .searchbar input[type="search"] {
            width: 100%;
            border-radius: 5px;
            font-size: 17px;
            outline: none !important;
        }
       .searchbar input[type="search"]:focus {
    outline: 2px solid #563F1B !important; /* Add custom outline when focused */
    box-shadow: 0 0 10px #92641bdf; /* Optional: Add a glowing effect */
}

/* Search button initial styling */
.button {
    padding: 12px 20px;
    background-color: #63A088;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 18px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.3s ease; /* Add transition for hover effect */
}

/* Hover effect for search button */
.button:hover {
    background-color: #467260;
    transform: scale(1.02); /* Slightly enlarge the button on hover */
}

.hidden-content {
        transform: translateX(-100%);
        opacity: 0;
        transition: transform 0.5s ease-in-out, opacity 0.5s ease-in-out;
    }

    .hover-image:hover + .hidden-content {
        transform: translateX(0);
        opacity: 1;
    }


    </style>
</head>
<body>""")
print(f"""

    <div class="header">
        <h1 class="ms-5" style="color: #fff;">Find medicinal plants</h1>
        <a href="./userLogin.py" class="logout-btn text-decoration-none">Logout</a>
    </div>""")
print(f"""
    <div class="sidebar">
        <img src="./assets/GG-logo3.png" width="150px" alt="Go Green Logo">

        <a href="./userDashboard.py?id={id}" class="mt-4 "><i class='bx bx-home'></i> Home</a>

        <a  href="./viewPlantsandseeds.py?id={id}"><i class='bx bx-leaf'></i> View Plants & Seeds</a>
        <a class="active" href="./userFindmedicine.py?id={id}"><i class='bx bx-search'></i> Find Medicine Plants</a>

        <button class="dropdown-btn"><i class='bx bx-cart'></i> Order Management
            <i class="bx bx-chevron-down ms-auto"></i>
        </button>
        <div class="dropdown-container">
            <a href="./userCart.py?id={id}"><i class='bx bx-cart'></i> Your cart</a>
            <a href="./userCurrentorders.py?id={id}"><i class='bx bx-time'></i> Current orders</a>
            <a href="./userCompletedorders.py?id={id}"><i class='bx bx-check'></i> Completed orders</a>
            <a href="./userCancelled.py?id={id}"><i class='bx bx-x'></i> Cancelled orders</a>
        </div>
    </div>




  <div class="container mt-2 me-1 searchbar-container">
    <form class="searchbar" method="post">
      <input class="form-control h-100 me-2" autocomplete="off" type="search" placeholder="Enter your problems" name="product" aria-label="Search">
      <input class="btn btn-secondary button" name="search" type="submit" value="Search">
    </form>
</div>

  </div>""")
p = f"""select * from userreg where id='{id}' """
cur.execute(p)
user = cur.fetchall()

if user:
    print(f"""<div class="content">
        <div class="container">
            <div class="row">""")

    search = store.getvalue("product")

    if search:
        p = f"SELECT * FROM products WHERE medicinaluse LIKE '%{search}%' ORDER BY RAND()"
    else:
        p = "SELECT * FROM products ORDER BY RAND()"

    cur.execute(p)
    products = cur.fetchall()

    for i in products:
        gram_text = " for 50 gram" if i[1] == "Seeds" else ""
        print(f"""
            <div class="col-md-4 mb-5">
                <div class="card" style="width: 300px;">
                    <img src="./assets/{i[10]}" height="220px" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{i[3]}</h5>
                        <p class="card-text mb-1"><strong>Product type:</strong> {i[1]} </p>
                        <p class="card-text mb-1"><strong>Category:</strong> {i[2]} </p>
                        <p class="card-text"><strong>Watering Period:</strong> {i[8]}</p>
                        <p class="card-text"><strong>Price:</strong> <span class="fw-bold"> &#8377; {i[11]}</span> {gram_text}</p>
                        <form method="post" enctype="multipart/form-data">
                            <input type="hidden" name="productid" value="{i[13]}">
                            <input type="hidden" name="productname" value="{i[3]}">
                            <input type="hidden" name="producttype" value="{i[1]}">
                            <input type="hidden" name="image1" value="{i[10]}">
                            <input type="hidden" name="category" value="{i[2]}">
                            <input type="hidden" name="description" value="{i[4]}">
                            <input type="hidden" name="color" value="{i[5]}">
                            <input type="hidden" name="growthrate" value="{i[6]}">
                            <input type="hidden" name="soil" value="{i[7]}">
                            <input type="hidden" name="watering" value="{i[8]}">
                            <input type="hidden" name="climate" value="{i[9]}">
                            <input type="hidden" name="stock" value="{i[12]}">
                            <input type="hidden" name="price" value="{i[11]}">
                            <input type="hidden" name="nurseryid" value="{i[14]}">
                            <input type="submit" class="btn btn-primary d-inline" name="addtocart" value="Add to cart">
                            <button type="button" class="btn btn-secondary d-inline" data-bs-toggle="modal" data-bs-target="#staticBackdrop{i[0]}">Details</button>

                    </div>
                    </div>



 <div class="modal fade" id="staticBackdrop{i[0]}" data-bs-backdrop="static" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
                <div class="modal-dialog modal-xl">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" style="font-size: 30px !important;" id="exampleModalLabel">{i[3]}</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <div class="container-fluid">
                                <div class="row">
                                    <div class="col-md-4">
                                        <img src="./assets/{i[10]}" style="border-radius: 15px;" width="400px" alt="">
                                    </div>
                                    <div class="col-md-7 ms-auto">
                                        <p class="fw-bold mb-2">Description:</p>
                                        <p class="mb-4">{i[4]}</p>
                                       <div class="d-block mb-3">
                    <p class="fw-bold mb-2 d-inline">Product type: </p> <p class="d-inline ms-3">{i[1]}</p> 

                    <p class="fw-bold mb-2 ms-5 me-1 d-inline">Category: </p> <i style="font-size: 18px;" class="me-1 fa-solid fa-house-chimney"></i> <p class="d-inline ">{i[2]}</p> </div>
                <div class="d-block mb-3">
                    <p class="fw-bold mb-2  d-inline">Color: </p> <p class="d-inline ms-3 me-5">{i[5]}</p> 

                    <p class="fw-bold mb-2 ms-5 d-inline">Growth rate: </p> <p class="d-inline ms-3">{i[6]}</p> </div>
                    <div class="d-block mb-3">
                        <p class="fw-bold mb-2  d-inline">Soil type: </p> <p class="d-inline ms-3 me-5">{i[7]}</p> 
                        <p class="fw-bold mb-2 ms-5 d-inline">Watering period: </p> <p class="d-inline ms-2 "> <i style="font-size: 18px;" class="me-1 fa-solid fa-droplet"></i> {i[8]} </p> </div>                

                        <div class="d-block mb-3">
                            <p class="fw-bold mb-2  d-inline">Suitale climate: </p> <p class="d-inline ms-3 me-5">{i[9]} <i style="font-size: x-large;" class="fa-solid fa-cloud-sun"></i></p> 
                            <p class="fw-bold mb-2  d-inline">Stocks availble: </p> <p class="d-inline ms-3">{i[12]}</p> </div> 


                        <div class="d-block ms-5 mt-4">
                            <p style="font-size: 30px;" class="fw-bold mb-2  d-inline">Price: </p> <p style="font-size: 30px;" class="d-inline ms-3 me-1">&#8377; {i[11]}</p> for 50 gram

             </div> 

             <div class="d-block ms-5 float-end mt-4">
                <input type="submit" class="btn btn-success me-4" name="addtocart" id="" value="Add to cart">
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Back</button>             

 </div> 
  </div>
</div>
</div>
</div>
</div>
</div>
    </div>

 </form>
                      </div>""")

    print(""" </div>
                      </div>

    </div>

    <script>

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

addtocart = store.getvalue("addtocart")
if addtocart:
    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    productname = store.getvalue("productname")
    producttype = store.getvalue("producttype")
    productid = store.getvalue("productid")
    desc = store.getvalue("description")
    category = store.getvalue("category")
    color = store.getvalue("color")
    soil = store.getvalue("soil")
    growthrate = store.getvalue("growthrate")
    watering = store.getvalue("watering")
    climate = store.getvalue("climate")
    nurseryid = store.getvalue("nurseryid")
    stock = store.getvalue("stock")
    price = store.getvalue("price")
    image1 = store.getvalue("image1")
    q = f"""INSERT INTO `orders` (`customerid`, `productid`, `productname`, `description`, `productype`, `category`, `color`, `growthrate`, `soiltype`, `wateringperiod`, `climate`, `stocks`, `price`, `nurseryid`,`productpic`) VALUES
            ('{id}', '{productid}', '{productname}', '{desc}', '{producttype}', '{category}', '{color}', '{growthrate}', '{soil}', '{watering}', '{climate}', '{stock}', '{price}', '{nurseryid}','{image1}')"""
    cur.execute(q)
    con.commit()
    print(f"""<script>alert("Product moved to cart!")
                location.href="./viewPlantsandseeds.py?id={id}"</script>""")

