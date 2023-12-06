import datetime

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",
]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
       "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

# Function to calculate deductions
def calculate_deductions(gross_pay):
    federal_tax_rate = 0.12
    state_tax_rate = 0.03
    social_security_rate = 0.062
    medicare_rate = 0.0145
    retirement_rate = 0.04

    federal_tax = gross_pay * federal_tax_rate
    state_tax = gross_pay * state_tax_rate
    social_security = gross_pay * social_security_rate
    medicare = gross_pay * medicare_rate
    retirement = gross_pay * retirement_rate

    total_deductions = federal_tax + state_tax + social_security + medicare + retirement
    return total_deductions

# Function to calculate net pay
def calculate_net_pay(gross_pay, total_deductions):
    return gross_pay - total_deductions

# Function to write to the output file
def create_output_file():
    ############## output file ###############
    out_file = "payroll.txt"
    f = open(out_file, "w")
    
    # Get current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write header to the file
    f.write("Payroll Information\n")
    f.write(f"Company Name: XYZ Company\n")
    f.write(f"Date and Time: {current_datetime}\n\n")
    
    # Write payroll information for each employee
    for i in range(num_emps):
        name = emp[i]
        job_code = job[i]
        hours_worked = hours[i]

        # Define pay rates
        pay_rates = {'C': 16.50, 'S': 15.75, 'J': 15.75, 'M': 19.50}

        # Calculate gross pay
        pay_rate = pay_rates.get(job_code, 0)
        gross_pay = hours_worked * pay_rate

        # Calculate deductions
        total_deductions = calculate_deductions(gross_pay)

        # Calculate net pay
        net_pay = calculate_net_pay(gross_pay, total_deductions)

        # Write payroll information to the file
        f.write("\nEmployee Details:\n")
        f.write(f"{name.strip()} ({job_code}) - Hours Worked: {hours_worked}\n")
        f.write(f"Gross Pay: ${gross_pay:.2f}\n")
        f.write(f"Federal Tax: ${total_deductions:.2f}\n")
        f.write(f"State Tax: ${total_deductions:.2f}\n")
        f.write(f"Social Security: ${total_deductions:.2f}\n")
        f.write(f"Medicare: ${total_deductions:.2f}\n")
        f.write(f"Retirement: ${total_deductions:.2f}\n")
        f.write(f"Net Pay: ${net_pay:.2f}\n\n")

    # Close the file
    f.close()

# Call the create_output_file function
create_output_file()
