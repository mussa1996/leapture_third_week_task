import bcrypt

password="mussa"
password=password.encode('utf-8')
hashed_password=bcrypt.hashpw(password,bcrypt.gensalt())
print(hashed_password)
#compare and confirm password with bcrypt
password = str(input("input password: ")) 
password = password.encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt(10)) 
check = str(input("check password: ")) 
check = check.encode('utf-8') 
if bcrypt.checkpw(check, hashed):
 print("login success")
else:
 print("incorrect password")