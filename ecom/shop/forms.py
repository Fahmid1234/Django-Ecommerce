from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ShippingAddress
from django import forms

class usercreate(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


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

class ShippingForm(forms.ModelForm):
    full_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Full Name'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    phone_no = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone Number'}))
    country = forms.ChoiceField(choices=Country, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Country'}))
    division = forms.ChoiceField(choices=Division, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Division'}))
    district = forms.ChoiceField(choices=District, widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'District'}))
    address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Address1'}))
    address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Address2'}), required=False)
    thana = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Thana/Upazilla'}))
    zipcode = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Zipcode'}))

    class Meta:
        model = ShippingAddress
        fields = ['user', 'full_name', 'email', 'phone_no', 'country', 'division', 'district', 'address1', 'address2', 'thana', 'zipcode']

        exclude = ['user',]

class PaymentForm(forms.Form):
    bkash_num = forms.CharField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Bkash Number'}))
    bkash_txid = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Bkash Transaction ID'}))