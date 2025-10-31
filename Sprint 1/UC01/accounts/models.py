from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    
    #define choices
    PATIENT = "P"
    DOCTOR = "D"

    USER_TYPE_CHOICES = {
        PATIENT: "Patient",
        DOCTOR: "Doctor",
    }
    
    user_type = models.CharField(
        max_length=1,
        choices=USER_TYPE_CHOICES,
        default=PATIENT,
    )

    medical_license_number = models.CharField(max_length=50, default="n/a")
    

    #define state choices
    Alabama = "AL"
    Alaska = "AK"
    Arizona = "AZ"
    Arkansas = "AR"
    California = "CA"
    Colorado = "CO"
    Connecticut = "CT"
    Delaware = "DE"
    Florida = "FL"
    Georgia = "GA"
    Hawaii = "HI"
    Idaho = "ID"
    Illinois = "IL"
    Indiana = "IN"
    Iowa = "IA"
    Kansas = "KS"
    Kentucky = "KY"
    Louisiana = "LA"
    Maine = "ME"
    Maryland = "MD"
    Massachusetts = "MA"
    Michigan = "MI"
    Minnesota = "MN"
    Mississippi = "MS"
    Missouri = "MO"
    Montana = "MT"
    Nebraska = "NE"
    Nevada = "NV"
    New_Hampshire = "NH"
    New_Jersey = "NJ"
    New_Mexico = "NM"
    New_York = "NY"
    North_Carolina = "NC"
    North_Dakota = "ND"
    Ohio = "OH"
    Oklahoma = "OK"
    Oregon = "OR"
    Pennsylvania = "PA"
    Rhode_Island = "RI"
    South_Carolina = "SC"
    South_Dakota = "SD"
    Tennessee = "TN"
    Texas = "TX"
    Utah = "UT"
    Vermont = "VT"
    Virginia = "VA"
    Washington = "WA"
    West_Virginia = "WV"
    Wisconsin = "WI"
    Wyoming = "WY"

    STATE_CHOICES = {
    Alabama: "AL",
    Alaska: "AK",
    Arizona: "AZ",
    Arkansas: "AR",
    California: "CA",
    Colorado: "CO",
    Connecticut: "CT",
    Delaware: "DE",
    Florida: "FL",
    Georgia: "GA",
    Hawaii: "HI",
    Idaho: "ID",
    Illinois: "IL",
    Indiana: "IN",
    Iowa: "IA",
    Kansas: "KS",
    Kentucky: "KY",
    Louisiana: "LA",
    Maine: "ME",
    Maryland: "MD",
    Massachusetts: "MA",
    Michigan: "MI",
    Minnesota: "MN",
    Mississippi: "MS",
    Missouri: "MO",
    Montana: "MT",
    Nebraska: "NE",
    Nevada: "NV",
    New_Hampshire: "NH",
    New_Jersey: "NJ",
    New_Mexico: "NM",
    New_York: "NY",
    North_Carolina: "NC",
    North_Dakota: "ND",
    Ohio: "OH",
    Oklahoma: "OK",
    Oregon: "OR",
    Pennsylvania: "PA",
    Rhode_Island: "RI",
    South_Carolina: "SC",
    South_Dakota: "SD",
    Tennessee: "TN",
    Texas: "TX",
    Utah: "UT",
    Vermont: "VT",
    Virginia: "VA",
    Washington: "WA",
    West_Virginia: "WV",
    Wisconsin: "WI",
    Wyoming: "WY",
    }
    
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
    )