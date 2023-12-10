import sys

# Define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# Define global variables
inout = 1  # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0
tuition = 0
capfee = 0
insfee = 0
actfee = 0
total = 0
balance = 0

############## Define program functions #############

def main():
    another_student = True
    while another_student:
        get_user_data()
        perform_calculations()

        # Open the HTML file for writing
        with open('output.html', 'w') as output_file:
            display_results(output_file)

        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.lower() == "n":
            another_student = False

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global tuition, capfee, insfee, actfee, total, balance  # balance is total minus scholarship
    if inout == 1:
        tuition = RATE_TUITION_IN * numcredits
    elif inout == 2:
        tuition = RATE_TUITION_OUT * numcredits
    capfee = numcredits * RATE_CAPITAL_FEE
    insfee = numcredits * RATE_INSTITUTION_FEE
    actfee = numcredits * RATE_ACTIVITY_FEE
    total = tuition + capfee + insfee + actfee
    balance = total - scholarshipamt

def display_results(output_file):
    # Redirect standard output to the HTML file
    sys.stdout = output_file

    print('<html>')
    print('<head><title>Tuition & Fees</title></head>')
    print('<body>')

    print('<h1>Piedmont Virginia Community College</h1>')
    print('<p>Tuition $ ' + format(tuition, ',.2f') + '</p>')
    print('<p>Capital Fee $ ' + format(capfee, ',.2f') + '</p>')
    print('<p>Institution Fee $ ' + format(insfee, ',.2f') + '</p>')
    print('<p>Activity Fee $ ' + format(actfee, ',.2f') + '</p>')
    print('<p>Total $ ' + format(total, ',.2f') + '</p>')
    print('<p>Scholarship Amount $ ' + format(scholarshipamt, ',.2f') + '</p>')
    print('<p>Remaining Balance $ ' + format(balance, ',.2f') + '</p>')

    print('</body>')
    print('</html>')

    # Flush the output to make sure it's written to the file
    sys.stdout.flush()

    # Restore standard output to the console
    sys.stdout = sys.__stdout__
