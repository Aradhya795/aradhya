# Shipping Cost Calculator

## Input package weight and shipping rate 
weight = float(input(Enter the package weight in kilograms:"))
rate = float(input(Enter the shipping rate in kilograms:"))

## Calculate shipping cost
Shipping_cost = weight * rate

## Display the result
print(f"Shipping cost: {shipping_cost} USD")
