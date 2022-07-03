import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
number = '+91**********'
phonenumber = phonenumbers.parse(number)
print (geocoder.description_for_number(phonenumber,'en'))
print(timezone.time_zones_for_geographical_number(phonenumber))
print(carrier.name_for_number(phonenumber,'en'))
