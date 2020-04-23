has_high_income = True
has_credit = True

if has_high_income and has_credit:  #both conditions are must be True
    print("Eligble for Loan")
else:
    print("Not eligble")

has_high_income = True
has_credit = False

if has_high_income and has_credit:
    print("Eligble for Loan")
else:
    print("Not eligble")

has_high_income = True
has_credit = False

if has_high_income or has_credit:   #if there are one True then condition execute
    print("Eligble for Loan")
else:
    print("Not eligble")

has_high_income = True
has_credit = True

if has_high_income and not has_credit:   #not like that negetive..it converterts true value False
    print("Eligble for Loan")
else:
    print("Not eligble")