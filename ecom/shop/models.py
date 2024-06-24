from django.db import models
from django.contrib.auth.models import User

# Create your models here.

category = (
    ('Smartwatch', 'Smartwatch'),
    ('Headphone', 'Headphone'),
    ('Power Bank', 'Power Bank'),
    ('Kitchen Accesories', 'Kitchen Accesories'),
    ('Fan', 'Fan'),
)

class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='product_img')
    category = models.CharField(choices=category, max_length=20)

    class Meta:
        verbose_name_plural = "Product"

    def __str__(self):
        return str(self.id)
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = "Cart"

class Carts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = "Carts"

    def __str__(self):
        return str(self.id)
    
Country = (('Bangladesh', 'Bangladesh'),
           ('India', 'India')
           )


Division = (('Dhaka', 'Dhaka'),
             ('Khulna', 'Khulna'),
             ('Rajshahi', 'Rajshahi'),
             ('Rangpur', 'Rangpur'),
             ('Sylhet', 'Sylhet'),
             ('Mymenshing', 'Mymenshing'),
             ('Chattogram', 'Chattogram')
           )

# Divivsion = ('Dhaka', 'Khulna', 'Rajshahi', 'Rangpur', 'Sylhet', 'Mymenshing', 'Chattogram',)

District = (("Bagerhat", "Bagerhat"),
    ("Bandarban", "Bandarban"),
    ("Barguna", "Barguna"),
    ("Barisal", "Barisal"),
    ("Bhola", "Bhola"),
    ("Bogra", "Bogra"),
    ("Brahmanbaria", "Brahmanbaria"),
    ("Chandpur", "Chandpur"),
    ("Chapai Nawabganj", "Chapai Nawabganj"),
    ("Chattogram", "Chattogram"),
    ("Chuadanga", "Chuadanga"),
    ("Cox's Bazar", "Cox's Bazar"),
    ("Cumilla", "Cumilla"),
    ("Dhaka", "Dhaka"),
    ("Dinajpur", "Dinajpur"),
    ("Faridpur", "Faridpur"),
    ("Feni", "Feni"),
    ("Gaibandha", "Gaibandha"),
    ("Gazipur", "Gazipur"),
    ("Gopalganj", "Gopalganj"),
    ("Habiganj", "Habiganj"),
    ("Jamalpur", "Jamalpur"),
    ("Jashore", "Jashore"),
    ("Jhalokathi", "Jhalokathi"),
    ("Jhenaidah", "Jhenaidah"),
    ("Joypurhat", "Joypurhat"),
    ("Khagrachari", "Khagrachari"),
    ("Khulna", "Khulna"),
    ("Kishoreganj", "Kishoreganj"),
    ("Kurigram", "Kurigram"),
    ("Kushtia", "Kushtia"),
    ("Lakshmipur", "Lakshmipur"),
    ("Lalmonirhat", "Lalmonirhat"),
    ("Madaripur", "Madaripur"),
    ("Magura", "Magura"),
    ("Manikganj", "Manikganj"),
    ("Meherpur", "Meherpur"),
    ("Moulvibazar", "Moulvibazar"),
    ("Munshiganj", "Munshiganj"),
    ("Mymensingh", "Mymensingh"),
    ("Naogaon", "Naogaon"),
    ("Narail", "Narail"),
    ("Narayanganj", "Narayanganj"),
    ("Narsingdi", "Narsingdi"),
    ("Natore", "Natore"),
    ("Netrokona", "Netrokona"),
    ("Nilphamari", "Nilphamari"),
    ("Noakhali", "Noakhali"),
    ("Pabna", "Pabna"),
    ("Panchagarh", "Panchagarh"),
    ("Patuakhali", "Patuakhali"),
    ("Pirojpur", "Pirojpur"),
    ("Rajbari", "Rajbari"),
    ("Rajshahi", "Rajshahi"),
    ("Rangamati", "Rangamati"),
    ("Rangpur", "Rangpur"),
    ("Satkhira", "Satkhira"),
    ("Shariatpur", "Shariatpur"),
    ("Sherpur", "Sherpur"),
    ("Sirajganj", "Sirajganj"),
    ("Sunamganj", "Sunamganj"),
    ("Sylhet", "Sylhet"),
    ("Tangail", "Tangail"),
    ("Thakurgaon", "Thakurgaon")
    )
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    phone_no = models.IntegerField()
    country = models.CharField(choices=Country, max_length=15)
    division = models.CharField(choices=Division,max_length=50)
    district = models.CharField(choices=District,max_length=50)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    thana = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)
    

    class Meta:
        verbose_name_plural = "Shipping Address"

    def __str__(self):
        return str(self.id)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    shipping_address = models.TextField(max_length=15000)
    amount_paid = models.FloatField()
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True) 
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.FloatField()

    def __str__(self):
        return str(self.id)