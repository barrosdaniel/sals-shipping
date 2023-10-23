print("=====================")
print("Sal's Shipping System")
print("=====================")
weight = float(input("Enter parcel weight in Kg: "))

print("Parcel Weight: " + str(weight) + " kg")

# Ground Shipping
ground_shipping_flat_charge = 20.00
ground_shipping_cost_per_kilo = 0.00
ground_shipping_cost = 0.00

if weight <= 2:
    ground_shipping_cost_per_kilo = 1.50
elif weight <= 6:
    ground_shipping_cost_per_kilo = 3.00
elif weight <= 10:
    ground_shipping_cost_per_kilo = 4.00
else:
    ground_shipping_cost_per_kilo = 4.75

ground_shipping_cost = ground_shipping_flat_charge + (
    weight * ground_shipping_cost_per_kilo
)
ground_shipping_cost_string = "Ground Shipping Cost: $ {0:.2f}"
print(ground_shipping_cost_string.format(ground_shipping_cost))

# Ground Shipping Premium
ground_shipping_premium_flat_charge = 125.00
ground_shipping_premium_cost = ground_shipping_premium_flat_charge
ground_shipping_premium_cost_string = "Ground Shipping Premium Cost: $ {0:.2f}"
print(ground_shipping_premium_cost_string.format(ground_shipping_premium_cost))

# Drone Shipping
drone_shipping_flat_charge = 0.00
drone_shipping_cost_per_kilo = 0.00
drone_shipping_cost = 0.00

if weight <= 2:
    drone_shipping_cost_per_kilo = 4.50
elif weight <= 6:
    drone_shipping_cost_per_kilo = 9.00
elif weight <= 10:
    drone_shipping_cost_per_kilo = 12.00
else:
    drone_shipping_cost_per_kilo = 14.25

drone_shipping_cost = drone_shipping_flat_charge + (
    weight * drone_shipping_cost_per_kilo
)
drone_shipping_cost_string = "Drone Shipping Cost: $ {0:.2f}"
print(drone_shipping_cost_string.format(drone_shipping_cost))
