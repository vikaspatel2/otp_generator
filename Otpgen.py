
#vik_python 3.7.1

import random as r

#function for otp generate

def otpgen():
  otp=""
  for i in range(4):
  
       otp+= str(r.randint(1,9))
  
  print("your One Time Password")
  
  print(otp)

otpgen()
