good_credit = True
high_income = False
if good_credit or high_income:
	print("Eligible for loan")
else:
	print("Not eligible for loan")

# AND & OR
has_good_credit = True
has_high_income = False
has_criminal_record = False
if has_good_credit or has_high_income and not has_criminal_record:
	print("Eligible for  Loan")
else:
	print("Not eligible for loan")

