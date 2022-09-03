import matplotlib.pyplot as plt
  
# x-axis values
x = [1]
# y-axis values
y = [5]
  
# plotting points as a scatter plot
plt.scatter(x, y, label= "stars", color= "green",marker= "*", s=30)
  
# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()
  
# function to show the plot
plt.show()