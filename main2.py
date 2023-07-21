# Program description: Sales chart for months January to December
# Written by: Ryan Guinchard
# Written on: 2023-07-21

# Import modules
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = []

for month in months:
    salesAmt = float(input(f"Enter the sales amount for {month}: "))
    sales.append(salesAmt)

plt.plot(months, sales)
plt.title("End of Year Sales")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.show()