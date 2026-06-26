partner_1_name = input("Enter the name of partner 1: ")
partner_2_name = input("Enter the name of partner 2: ")
partner_3_name = input("Enter the name of partner 3: ")
partner_1_contribution = float(input("Enter the contribution of partner 1: "))
partner_2_contribution = float(input("Enter the contribution of partner 2: "))
partner_3_contribution = float(input("Enter the contribution of partner 3: "))
total_contribution = partner_1_contribution + partner_2_contribution + partner_3_contribution
partner_1_percentage = (partner_1_contribution / total_contribution) * 100
partner_2_percentage = (partner_2_contribution / total_contribution) * 100
partner_3_percentage = (partner_3_contribution / total_contribution) * 100
print(f"{partner_1_name} contributed {partner_1_percentage:.2f}% of the total.")
print(f"{partner_2_name} contributed {partner_2_percentage:.2f}% of the total.")
print(f"{partner_3_name} contributed {partner_3_percentage:.2f}% of the total.")