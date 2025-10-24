def delivery_fee(distance, rate):
    total_fee = distance * rate
    return total_fee

distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (₱): "))

fee = delivery_fee(distance, rate)

print(f"Total Delivery Fee: ₱{fee:.2f}")
