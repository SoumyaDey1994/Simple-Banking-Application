import random;              # Import Random Module to generate 5 digit Account Number
customerAccounts=[];        #List to contail all existing customer
accountNumbers=[];          #List of all existing account numbers

class Bank:         # Class Bank
    def addNewAccount(self, customer):              # Create Customer's Account Number and Add Customer to Bank's Customer List
        customer.accountNumber=self.__createNewAccountNumber();
        
        accountNumbers.append(customer.accountNumber);  # Add Account Number to AccountNumber List
        customerAccounts.append(customer);              # Add Customer to Customer List
          
    def __createNewAccountNumber(self):              # Function to Generate New Account Number
        accountNumber=int(random.uniform(1,10)*10000)
        while accountNumber in accountNumbers:
            accountNumber=int(random.uniform(1,10)*10000);  #Generate Freash 5 digit Account Number
        return accountNumber;
    
    def showAccountDetails(self, customer):          # Show Account Details of a Customer
        print();
        print("AccountHolder's Name: %s " %(customer.name));
        print("Account Number: {}" .format(customer.accountNumber));
        print("Available Balance: {}INR".format(customer.availableBalance));

    def viewAllAccounts(self):                       # View All Accounts to Administrator
        print();
        adminUserName=input("Enter Admin Username: ");
        adminPassword=int(input("Enter admin Password: "));
        if(adminUserName== "Administrator" and adminPassword== 8017450262 ):    # Administrator Authentication using userName and Password
            print();
            for customer in customerAccounts:
                print("Account Holder's Name: {}\t Account Number: {}" .format(customer.name, customer.accountNumber));
        else:
            print("Invalid Username or Password!!!!!!");
            

class Customer:                         # Class Customer
    def __init__(self,customerName,initialAmount):              # Initializing customer with CustomerName and Initial Amount
        self.name=customerName;
        self.availableBalance=initialAmount;
        
    def depositAmount(self, amount):                 # Deposit Amount to Existing Account
        self.availableBalance= self.availableBalance + amount;
        print(".........Amount %d Deposited Successfully to Your Account....Thank You for Banking With Us.........." %(amount));
        print();
        self.displayBalance();
        
    def withdrawAmount(self, amount):               # Withdraw Amount from Existing Account
        if(amount > self.availableBalance): # Checks wheather Sufficient Balance is there for Withdrawal or not
            print();
            print("Insufficient Balance !!!!! Cannot Process Your Request..............");
        else:
            self.availableBalance= self.availableBalance - amount;
            print(".........Amount %d Successfully Withdrawn From Your Account....Thank You for Banking With Us........." %(amount));
            print();
            self.displayBalance();
            
    def displayBalance(self):                # Display Balance of Existing Account
        print();
        print("\tAccount Holder: {}\t Account Number: {}\t Availbable Balance: {} " .format(self.name, self.accountNumber, self.availableBalance));
        
def displayMenuAndAcceptUserChoice():           # Display Main Menu
    print();
    print("Enter 1 to Create a New Account ");
    print("Enter 2 to Access Your Existing Account ");
    print("Enter 3 to Exit ");
    print("Enter 4 to view All Account Holder's Name with Account Number ");
    print();
    userChoice=int(input("Please Enter an Option to Proceed: "));
    return userChoice;
    
def performActionBasedonUserChoice(userChoice):         # Perform Operations Based on User Choice
    print();
    if(userChoice==1):          # Create New Account
        customerDetails=getUserDetails();
        customer=Customer(customerDetails[0],customerDetails[1]);
        bank.addNewAccount(customer);
        print("\n.....Account Created Sucsessfully.........");
        print("Details of created Account : ");
        bank.showAccountDetails(customer);
        
    elif(userChoice==2):        # Access Existing Account
        print();
        accountNumber=int(input("Enter Your Account Number: "));
        userName=input("Enter Account Holder's Name: ");
        customerAccount=validateCustomer(accountNumber,userName,);
        if(customerAccount== False):
            print("Invalid Account Number Entered...... Please check and Enter Account Number Properly");
        else:
            print("\t................Hello {} !!!!!!!!!!!...................." .format(customerAccount.name));
            option=getOptionFromDisplayedOptions();
            proceedWith(option,customerAccount);
            
    elif(userChoice==3):        # Quit from Application
        quit();
        
    elif(userChoice==4):        # Display All Customer through Administrative Login
        bank.viewAllAccounts();
        
    else:                       # Invalid Choice, Back to Main Menu
        print("Ivalid Option Selected.....Please Choose a Valid Option From Below to Proceed");
        userChoice=displayMenuAndAcceptUserChoice();
        performActionBasedonUserChoice(userChoice);

def getUserDetails():           # Prompt User to Enter his/her Personal Details
        print();
        print("Please Enter Your Full Name: ", end='');
        customerName=input();
        print("Please Enter The Initial Amount You Want to Deposit: ", end='');
        initialAmount=int(input());
        return [customerName, initialAmount];

def validateCustomer(accountNumber, userName):                    # Check wheather customer's account exists or not
    for customer in customerAccounts:
            if(customer.accountNumber== accountNumber and customer.name== userName):
                return customer;
            else:
                continue;
    return False;

def getOptionFromDisplayedOptions():                    # Options to Access Existing Accounts
    print();
    print("Enter 1 to Deposit Amount ");
    print("Enter 2 to Withdraw Amount ");
    print("Enter 3 for Balance Enquiry ");
    print("Enter 4 to Back to Main Menu ");
    print();
    userOption= int(input("Please Select an Option from Above: "));
    return userOption;

def proceedWith(option, customerAccount):                   # Operations with Existing Account
    if(option==1):      # Deposit Amount to account
        print("\n Enter Amount to be Deposited: ", end='');
        amount=int(input());
        customerAccount.depositAmount(amount);
    elif(option==2):    # Withdraw Amount from account
        print("\n Enter Amount to be WithDrawn: ", end='');
        amount=int(input());
        customerAccount.withdrawAmount(amount);
    elif(option==3):    # Know Account Balance
        customerAccount.displayBalance();
    elif(option==4):    # Back to Main Menu
        userChoice=displayMenuAndAcceptUserChoice();
        performActionBasedonUserChoice(userChoice);
    else:               # Invalid Choice Alert.... Back to Options
        print("Invalid Option Selected!!!!!! Please select a valid option(1-4) ");
        option=getOptionFromDisplayedOptions();
        proceedWith(option,customerAccount);
    
    
bank= Bank();       # Create Instance of Bank
print();
print("\t.......................Welcome to ZXY Bank Portal......................");
while True:
   userChoice=displayMenuAndAcceptUserChoice();     # Display Menu and Accept Choice from User
   performActionBasedonUserChoice(userChoice);      # Perform Action based on User Selection
