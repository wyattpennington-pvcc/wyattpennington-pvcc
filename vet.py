# Global variables for dog
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48
PR_ALL = 0
PR_CHEWS_SMALL = 9.99
PR_CHEWS_MEDIUM = 11.99
PR_CHEWS_LARGE = 13.99

# Global variables for cat
PR_LEUKEMIA = 35
PR_RHINOTRACHEITIS = 30
PR_RABIES = 25
PR_VACCINE_PACKAGE_DISCOUNT = 0.10
PR_CHEWS_CAT = 8.00

def calculate_vet_cost(pet_type, chews_size, needs_bord, needs_dapp, needs_flu, needs_all):
    total_cost = 0
    
    # Calculate costs based on pet type
    if pet_type.lower() == 'dog':
        # Calculate costs for each service for a dog
        if needs_bord:
            total_cost += PR_BORD
        if needs_dapp:
            total_cost += PR_DAPP
        if needs_flu:
            total_cost += PR_FLU
        if needs_all:
            total_cost += PR_ALL
    
        # Calculate cost for chews based on size
        if chews_size == 'small':
            total_cost += PR_CHEWS_SMALL
        elif chews_size == 'medium':
            total_cost += PR_CHEWS_MEDIUM
        elif chews_size == 'large':
            total_cost += PR_CHEWS_LARGE
    elif pet_type.lower() == 'cat':
        # Calculate costs for each service for a cat
        total_cost += PR_LEUKEMIA if needs_bord else 0
        total_cost += PR_RHINOTRACHEITIS if needs_dapp else 0
        total_cost += PR_RABIES if needs_flu else 0
        
        # Calculate discount for full vaccine package
        if needs_all:
            total_cost *= (1 - PR_VACCINE_PACKAGE_DISCOUNT)
        
        # Calculate cost for cat chews
        total_cost += PR_CHEWS_CAT
    
    return total_cost

# Ask the user for the type of pet
pet_type = input("Is the pet a dog or a cat?: ")

# Ask the user for the reason the pet is visiting the vet
reason = input(f"Why is the {pet_type} visiting the vet? (e.g., vaccination, grooming, etc.): ")

# Ask additional questions based on the reason and pet type
if pet_type.lower() == 'dog':
    needs_bord = input("Does the dog need a bordetella shot? (yes/no): ").lower() == 'yes'
    needs_dapp = input("Does the dog need a distemper/parvo shot? (yes/no): ").lower() == 'yes'
    needs_flu = input("Does the dog need a flu shot? (yes/no): ").lower() == 'yes'
    needs_all = input("Does the dog need an overall health check? (yes/no): ").lower() == 'yes'
    chews_size = input("What size of chews does the dog prefer? (small/medium/large): ")
elif pet_type.lower() == 'cat':
    needs_bord = input("Does the cat need a feline leukemia shot? (yes/no): ").lower() == 'yes'
    needs_dapp = input("Does the cat need a feline viral rhinotracheitis shot? (yes/no): ").lower() == 'yes'
    needs_flu = input("Does the cat need a rabies shot? (yes/no): ").lower() == 'yes'
    needs_all = input("Does the cat need a full vaccine package? (yes/no): ").lower() == 'yes'
    chews_size = 'cat'  # For cats, there's only one size of chews

# Calculate the total cost
total_cost = calculate_vet_cost(pet_type, chews_size, needs_bord, needs_dapp, needs_flu, needs_all)

# Display the total cost
print(f"Total cost for the {pet_type}'s vet visit: ${total_cost}")
