#!C:/Users/Sakthivel murgan/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb
cgitb.enable()
store = cgi.FieldStorage()
con = pymysql.connect(host="localhost", password="", user="root", database="GoGreen")
cur = con.cursor()

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gogreen - Index</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" integrity="sha512-Kc323vGBEqzTmouAECnVceyQqyqdsSiqLQISBL29aUW4U/M7pSPA/gEUZQqv1cwx4OnYxTxve5UMg5GT6L4JJg==" crossorigin="anonymous" referrerpolicy="no-referrer" />

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Poppins", sans-serif;
            font-weight: 300;
        }
        body {
            background-color: aliceblue;
            padding-top: 80px; /* Add space for the fixed navbar */
        }
        .navbar {
            background-color: aliceblue;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            z-index: 10;
        }
        .navbar-brand {
            font-family: "Playwrite CU", cursive;
            font-size: 1.7rem;
            font-weight: 900;
            color: black;
            animation: color-change 20s infinite;
        }
        .nav-item {
            margin-left: 160px;
            font-size: 17px;
        }
        .nav-item.nav-margin {
            margin-left: 10px;
        }
        .nav-item a {
            font-weight: 500;
            color: black;
            transition: all 0.6s;
        }
        .nav-item a:hover {
            color: #297373;
            transform: translateY(-5px);
            scale: 1.02;
            transition: all 0.6s;
        }
        .carousel-inner img {
            height: 500px;
            object-fit: cover;
        }
        .carousel{
        margin-top:50px;
        }
        
.container {
            width: 90%;
            max-width: 1200px;
           transition: all ease 0.6s;

        }
        .row {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            transition: all ease 0.6s;

        }
        .pic-30 {
            width: 30%;
            background-color: #ddd;
            padding: 10px;
            overflow: hidden;
            text-align: center;
            transition: all ease 0.6s;
        }
        .pic-30:hover img {
            transform: scale(1.1);
            transition: all ease 0.6s;

            }
            
        .para-50 {
            width: 50%;
            padding: 10px;
        }
        .gap-20 {
            width: 20%;
        }
    </style>
</head>
<body>

<nav class="navbar navbar-expand-md navbar-light fixed-top">
    <div class="container">
        <a href="./index.py" class="navbar-brand"><img src="./assets/GG-logo3.png" width="80px"></a>
        <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ">
                <li class="nav-item"></li>
                <li class="nav-item"></li>
                <li class="nav-item dropdown" style="margin-left: 700px;">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        LogIn
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                        <li><a class="dropdown-item" href="./userLogin.py">User</a></li>
                        <li><a class="dropdown-item" href="./AdminLogin.py">Admin</a></li>
                        <li><a class="dropdown-item" href="./nurseryLogin.py">Nursery</a></li>
                        <li><a class="dropdown-item" href="./deliveryLogin.py">Delivery</a></li>
                    </ul>
                </li>
                <span class="hi mt-2 fw-bold">|</span>
                <li class="nav-item dropdown" style="margin-left: -1px;">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Register
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                        <li><a class="dropdown-item" href="./userreg.py">User</a></li>
                        <li><a class="dropdown-item" href="./nurseryReg.py">Nursery</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>

<div id="carouselExample" class="carousel slide">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="./assets/slide1.jpg" class="d-block w-100" alt="..." style="cursor:pointer;">
<div class="carousel-caption d-flex flex-column align-items-start" style="left: 10%; bottom: 20%;">
        <h2 style="font-weight:500; color:#D9FFF5 !important;" class="display-5 text-light text-dark">Exclusive Offer</h2>
        <p  style="font-weight:300; " class="text-light">Get up to 50% off on select plants!</p>
        <a href="./userLogin.py" class="btn btn-primary">Shop Now</a>
      </div>
          </div>
    <div class="carousel-item">
      <img src="./assets/slide2.jpg" class="d-block w-100" alt="..." style="cursor:pointer;">
      <div class="carousel-caption d-flex flex-column align-items-start" style="left: 10%; bottom: 20%;">
        <h2 style="font-weight:500; " class="display-5 text-light-">Limited Time Sale</h2>
        <p style="font-weight:300; " class="text-light">Discover our best-selling plants at discounted prices.</p>
        <a href="./userLogin.py" class="btn btn-primary">Shop Now</a>
      </div>
    </div>
    <div class="carousel-item">
      <img src="./assets/index7.jpg" class="d-block w-100" alt="..." style="cursor:pointer;">
      <div class="carousel-caption d-flex flex-column align-items-start" style="left: 10%; bottom: 20%;">
      <h2 style="font-weight:500;" class="display-5 text-light text-dark">New Arrivals</h2>
        <p  style="font-weight:300; " class="text-light">Explore the latest additions to our plant collection.</p>
        <a href="./userLogin.py" class="btn btn-primary">Shop Now</a>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>


<div>
<h1 class="mt-5 mx-5"> What we provide:</h1>
<div class="container mt-5">
    <div class="row mt-5">
        <div class="pic-30">
            <img src="./assets/index1.jpg" alt="Image" style="width: 100%; height: auto; cursor:pointer;">
        </div>
        
        <div class="gap-20"></div>
        <div class="para-50">
            <h1  > Welcome to Go Green!</h1> <h3> Embrace Green Living</h3>
             <p id="plants" class="mt-3">At Go Green, we believe in the power of plants to transform spaces and uplift spirits. Dive into a world of fresh greenery and sustainable gardening essentials tailored for both seasoned gardeners and those just starting out.</p>

        </div>
    </div>

    <div class="row mt-5">
        <div class="para-50">
<h1>Indoor and Outdoor Plants Collection</h1> <h5 class="mt-2"> Discover plants that suit every corner of your home and garden.</h5>
             <p class="mt-3">From air-purifying indoor plants to vibrant outdoor blooms, we have a plant for every space. Create a cozy green nook indoors or a lively garden outdoors with our hand-picked selection designed for easy maintenance and stunning growth.</p>
        </div>
        <div  class="gap-20"></div>
        <div class="pic-30">
            <img src="./assets/index2.jpg" alt="Image" style="width: 100%; height: auto; cursor:pointer;">
        </div>
    </div>
    
    <div class="row mt-5">
        <div class="pic-30">
            <img src="./assets/index5.jpg" alt="Image" style="width: 100%; height: auto; cursor:pointer;">
        </div>
        
        <div class="gap-20"></div>
        <div class="para-50">
<h1>High-Quality Seeds for Your Garden</h1> <h5 class="mt-2">Nurture your garden from the ground up with our premium seeds.</h5>
             <p  class="mt-3">Bring life to your garden with our range of high-quality seeds. We offer vegetable, herb, and flower seeds selected for their robust growth and high yield, helping you plant with confidence and enjoy a bountiful harvest.</p>
                </div>
    </div>

    <div class="row mt-5">
        <div class="para-50">
<h1  id="seeds">Eco-Friendly Gardening Supplies</h1> <h5 class="mt-2">Support the environment with our sustainable gardening tools.</h5>
             <p class="mt-3">Sustainable gardening is just a step away. Our collection of eco-friendly pots, organic fertilizers, and natural pest repellents is designed to reduce waste and promote a healthy, green garden. Join us in our mission to grow a better future.</p>
                      </div>
        <div class="gap-20"></div>
        <div class="pic-30">
            <img   src="./assets/index6.jpg" alt="Image"  style="width: 100%; height: auto; cursor:pointer;">
        </div>
    </div>
</div>

</div>

<p class="d-flex justify-content-center">&copy; 2024 Go Green Online Nursery</p>
</body>
</html>
""")
