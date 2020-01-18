import re
def validate_email(email):
    if re.match("^\w[a-zA-Z0-9\.\+_-]+\@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$", email) != None:
        print("Email address is valid: ", email)
    else:
        print("Not Valid:", email)


validate_email('mayurchavda87@gmail.com')
validate_email('.mayurchavda87@gmail.com')
validate_email('@.mayurchavda87@gmail.com')
validate_email('mayurchavda87@gmail')
validate_email('mayurchavda87@gmail.for.musuem')









#if re.match(r'^\w+[a-zA-Z0-9\.\+_-]+\@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$',email) != None: