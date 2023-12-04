room_rates = {
    'SR': 195,
    'DR': 250,
    'SU': 350
}

tax_rates = {
    'sales_tax': 6.5,
    'occupancy_tax': 11.25
}

guest_data = [
    ('Hawthorne', 'LeShonda', 'SR', 2),
    ('Johnson', 'Angelo', 'SR', 1),
    ('Williams', 'Megan', 'DR', 1),
    ('Brown', 'Johanna', 'SU', 6),
    ('Jones', 'Collette', 'DR', 7),
    ('Garcia', 'Alicia', 'SR', 8),
    ('Miller', 'Ronald', 'SU', 3),
    ('Davis', 'Brian', 'DR', 4),
    ('Rodriguez', 'Luis', 'SU', 4),
    ('Martinez', 'Felipe', 'DR', 5),
    ('Hernandez', 'Keesha', 'DR', 1),
    ('Lopez', 'Ellen', 'SU', 3),
    ('Gonzalez', 'Lillie', 'SR', 4),
    ('Wilson', 'Rolando', 'DR', 5),
    ('Anderson', 'Valerie', 'DR', 1),
    ('Tomas', 'Armando', 'SR', 1),
    ('Cho', 'Emma', 'SR', 5),
    ('Moore', 'James', 'SR', 2),
    ('White', 'Danielle', 'SU', 7),
    ('Harris', 'Kenneth', 'DR', 5),
    ('Sanchez', 'Monica', 'SU', 7),
    ('Clark', 'Anita', 'DR', 1),
    ('Ramirez', 'Wendy', 'DR', 1),
    ('Lewis', 'George', 'SU', 1),
    ('Panuchek', 'Gloria', 'SU', 8),
    ('Walker', 'Rhonda', 'DR', 5),
    ('Young', 'Mohammed', 'SR', 2),
    ('Allen', 'April', 'SR', 4),
    ('Martinez', 'Carrie', 'SR', 1),
    ('Collins', 'Juliette', 'SR', 1)
]

# Calculate total cost for each guest
guest_costs = []
for guest in guest_data:
    last_name, first_name, room_type, nights = guest
    room_rate = room_rates[room_type]
    subtotal = room_rate * nights
    sales_tax = subtotal * (tax_rates['sales_tax'] / 100)
    occupancy_tax = subtotal * (tax_rates['occupancy_tax'] / 100)
    total_cost = subtotal + sales_tax + occupancy_tax
    guest_costs.append((last_name, first_name, room_type, nights, subtotal, sales_tax, occupancy_tax, total_cost))

# Generate HTML
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Hotel Billing</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #ADD8E6;
        }
    </style>
</head>
<body>
    <h2>Hotel Billing Information</h2>
    <table>
        <tr>
            <th>Last Name</th>
            <th>First Name</th>
            <th>Room Type</th>
            <th>Nights</th>
            <th>Subtotal</th>
            <th>Sales Tax</th>
            <th>Occupancy Tax</th>
            <th>Total Cost</th>
        </tr>
"""

for guest_cost in guest_costs:
    html_content += "        <tr>\n"
    for data in guest_cost:
        html_content += f"            <td>{data}</td>\n"
    html_content += "        </tr>\n"

html_content += """
    </table>
</body>
</html>
"""

# Write HTML content to a file
with open("hotel_billing.html", "w") as html_file:
    html_file.write(html_content)

print("Hotel billing information has been saved to hotel_billing.html.")
