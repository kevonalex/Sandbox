import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the function you want to fit
def func(x, a, b, c):
    return a * x**2 + b * x + c

def obtain_polynomial(vbuck_source, x_data, y_data):

    # Fit the curve
    params, covariance = curve_fit(func, x_data, y_data)

    # Extract coefficients
    a, b, c = params

    # Define the polynomial function
    def poly_function(x):
        return a * x**2 + b * x + c

    # Test the polynomial function
    x_test = np.linspace(min(x_data), max(x_data), 100)
    y_test = poly_function(x_test)

    # Print the polynomial equation
    print(f"The {vbuck_source} polynomial obtained is: {a} * x^2 + {b} * x + {c}")
    return [a, b, c]

def poly_function(coefficient_array, x):
    a = coefficient_array[0]
    b = coefficient_array[1]
    c = coefficient_array[2]

    return a * x**2 + b * x + c


# Pricing data (VB)
y_data = np.array([1000, 2800, 5000, 13500])

################# ADD/EDIT VBUCK SUPPLIER PRICING DATA #################

### EPIC GAMES ###

epic_x_data = np.array([6.99, 17.49, 27.99, 69.99])
epic_polynomial = obtain_polynomial("Epic", epic_x_data, y_data)
epic_x_curve = np.linspace(min(epic_x_data), max(epic_x_data), 100)
epic_y_curve = poly_function(epic_polynomial, epic_x_curve)

### ASDA ###

asda_x_data = np.array([6.99, 17.49, 27.99, 69.99])
asda_polynomial = obtain_polynomial("ASDA", asda_x_data, y_data)
asda_x_curve = np.linspace(min(asda_x_data), max(asda_x_data), 100)
asda_y_curve = poly_function(asda_polynomial, asda_x_curve)

### GAME ###

game_x_data = np.array([6.49, 15.99, 25.99, 63.99])
game_polynomial = obtain_polynomial("GAME", game_x_data, y_data)
game_x_curve = np.linspace(min(game_x_data), max(game_x_data), 100)
game_y_curve = poly_function(game_polynomial, game_x_curve)

### G2A ###

g2a_x_data = np.array([8.97, 19.58, 37.09, 89.02])
g2a_polynomial = obtain_polynomial("G2A", g2a_x_data, y_data)
g2a_x_curve = np.linspace(min(g2a_x_data), max(g2a_x_data), 100)
g2a_y_curve = poly_function(g2a_polynomial, g2a_x_curve)

# plots
plt.plot(epic_x_curve, epic_y_curve, label='Epic Games Exchange Rate')
plt.plot(asda_x_curve, asda_y_curve, label='Asda Exchange Rate')
plt.plot(game_x_curve, game_y_curve, label='GAME Exchange Rate')
plt.plot(g2a_x_curve, g2a_y_curve, label='G2A Exchange Rate')

plt.xlabel('British Pounds (GBP)')
plt.ylabel('V-Bucks (VB)')
plt.title('GBP/VB')

plt.xlim(0, 100)
plt.ylim(0, 15000)
plt.legend()
plt.grid(True)
plt.show()