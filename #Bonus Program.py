#Bonus Program to enter the total amount of sales for Jan-Dec

import matplotlib.pyplot as plt

#Function to get the total sales for each month
def get_sales():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = []
    for month in months:
        sales.append(float(input("Enter total sales for {}: $".format(month))))
        return sales

#Main program
sales = get_sales()

#Plotting the graph
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.plot(months, sales, marker='o')
plt.title("Total Sales per Month")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.grid(True)
plt.show()