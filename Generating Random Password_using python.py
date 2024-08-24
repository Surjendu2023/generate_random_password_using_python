import string
import random

val=string.ascii_letters+string.digits+string.punctuation #concate data from atoz,1to9,special character

genarate_random_value=random.choice(val) #generating a single random data from given variable

password=""  #empty varriable

for i in range(1,8):#numbers of time repeating and appending the genarate_random_value
    password+=(random.choice(string.ascii_letters+string.digits+string.punctuation))

print('your 8 digit random password is :',password)    