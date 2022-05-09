# -*- coding: utf-8 -*-
"""LinearRegressionBreakdown.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MVPRHPx7DzWA2kkiwJ-IOImKZhE50Jke
"""

from re import M
# Start 7

# Linear Regression will not work if there does not seem to be a correlation 
# between x and y
# Line -> y = mx + b
# m = slope
# b = y intercept
# m = ((mean of x's * mean of all y's) - (mean of x's * y's)) / ((mean of x's)^2 - (mean of x's^2))

# b (y intercept) -> b = (mean of y's) - m(mean of x's)



# Start 8 & 9


from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')


xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope_and_yintercept(xs, ys):

  m = ( ((mean(xs) * mean(ys)) - (mean(xs*ys))) / ((mean(xs))**2 - mean(xs**2)))

  b = ((mean(ys)) - (m*(mean(xs))))


  return m, b

def squared_error(ys_orig, ys_line):

  return sum((ys_line - ys_orig)**2)

def coefficient_of_determination(ys_orig, ys_line):

  y_mean_line = [mean(ys_orig) for y in ys_orig]
  squared_error_regr = squared_error(ys_orig, ys_line)
  squared_error_y_mean = squared_error(ys_orig, y_mean_line)
  return 1 - (squared_error_regr / squared_error_y_mean)

m, b = best_fit_slope_and_yintercept(xs, ys)

print(m, b)

regression_line = [(m*x)+b for x in xs]

predict_x = 8
predict_y = (m*predict_x)+b

r_squared = coefficient_of_determination(ys, regression_line)
print('r_squared: ' + str(r_squared))

# The above line is the same as below: 
#for x in xs:
#  regression_line.append((m*x)+b)

#plt.plot(xs, ys)
plt.scatter(xs, ys)
plt.scatter(predict_x, predict_y, color='g')
plt.plot(xs, regression_line)
plt.show()


# k nearest numbers
# There is a difference between accuracy and confidence
# Will learn how to calculate 'best fit' line



# Start 10

# Explains squared Error
# yHat = regression_line
# SE = error**2 or e**2 
# error = distance between point and best fit line
# r^2 = coefficient of determination, used to determine accuracy 
# you want r^2 higher, closer to 1
# r^2 = 1 - ((SE * yHat) / (SE * mean(y)))