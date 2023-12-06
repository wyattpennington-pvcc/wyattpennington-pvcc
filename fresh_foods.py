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

# Function to print the payroll information
def print_payroll_info(name, job_code, hours_worked, gross_pay, deductions, net_pay):
    print(f"{name.strip()} ({job_code}) - Hours Worked: {hours_worked}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Federal Tax: ${deductions[0]:.2f}")
    print(f"State Tax: ${deductions[1]:.2f}")
    print(f"Social Security: ${deductions[2]:.2f}")
    print(f"Medicare: ${deductions[3]:.2f}")
    print(f"Retirement: ${deductions[4]:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")
    print("\n")

# Get current date and time
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Print payroll information for each employee
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

    # Print payroll information
    print("\nPayroll Information")
    print(f"Company Name: XYZ Company")
    print(f"Date and Time: {current_datetime}")
    print("\nEmployee Details:")
    print_payroll_info(name, job_code, hours_worked, gross_pay, [total_deductions]*5, net_pay)
