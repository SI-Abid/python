from matplotlib import pyplot as plt

x = ["yes", "no", "maybe"]
y = [79, 4, 17]

# plot a bar chart
plt.bar(x, y, color="purple")

# show value on bar
for i in range(len(x)):
    plt.text(x[i], y[i]+5, str(y[i])+'%', multialignment='center')

# set title
plt.title("Do you like Python?")
plt.ylabel("Percentage")

# set values on y-axis
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.show()