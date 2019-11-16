m = (len(x) * np.sum(x*y_noise) - np.sum(x) * np.sum(y_noise)) / (len(x)*np.sum(x*x) - np.sum(x) ** 2)
b = (np.sum(y_noise) - m *np.sum(x)) / len(x)

print("기울기: ", m)
print("절편: ", b)

def linear_regression_theta(x, m, b):
  return m*x + b

y_hat = linear_regression_theta(x, m, b)

plt.plot(x, y_hat)
plt.scatter(x, y_noise, c="red")
plt.show()

# https://devarea.com/linear-regression-with-numpy/#.XdA_bVczYuU
