# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
stat, p = shapiro(data)

print("start")

print('p=%.3f' %p)
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')

print("done")


print("#")
from scipy.stats import normaltest

data2 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945, 0.121, -0.945]
stat, p = normaltest(data2)

print("start")

print('p=%.3f' %p)
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')

print("done")