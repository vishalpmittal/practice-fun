import sys
submission_password = sys.argv[1]

if submission_password==None or submission_password.strip()=="":
    print "submission password not provided"
    sys.exit()    

print "Your submission password is "+ submission_password