def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    
    if stored_logins[email] == syeda67(password_to_check):
        return True
    
    return False

def syeda67(password):
    """
    Custom hash function to simulate password hashing (not cryptographically secure).
    For the sake of simplicity, it just returns the reversed string appended with "67" for demonstration.
    """
    return password[::-1] + "67"

def main():
    
    stored_logins = {
        "syeda.khadija@gmail.com": "drowssap67",  
        "code_in_placer@cip.org": "leK67",        
        "student@stanford.edu": "drowssap67"      
    }
    
    print(login("syeda.khadija@gmail.com", stored_logins, "password")) 
    print(login("syeda.khadija@gmail.com", stored_logins, "wrongpassword"))
    
    print(login("code_in_placer@cip.org", stored_logins, "Kel"))
    print(login("student@stanford.edu", stored_logins, "password"))
    print(login("student@stanford.edu", stored_logins, "wrongpassword"))

if __name__ == '__main__':
    main()
