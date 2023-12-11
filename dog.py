dog_names = ["Sadie", "Diego", "molly", "Ella", "Milo", "bubby", "rocky", "Annabelle", "gonzo", "sweetie-pie"]

# Sort the list in alphabetical order
sorted_dog_names = sorted(dog_names, key=lambda x: x.lower())

# Print the sorted list
print("Dog names in alphabetical order:")
for name in sorted_dog_names:
    print(name)

# Create a list of dog names from first to last
print("\nDog names from first to last:")
for name in dog_names:
    print(name)
