import numpy as np

# Set the parameters
mean_demand = 100
std_demand = 25
production_cost = 1
selling_price = 4
disposal_cost = 0.4
quantities = [80, 120, 140]

# Generate demand samples
demand_samples = np.random.normal(mean_demand, std_demand, size=10000)

# Calculate the profit for each demand and quantity combination
def profit():
    profits = {}
    for quantity in quantities:
        profits[quantity] = []
        for demand in demand_samples:
            quantity_produced = min(quantity, demand)
            quantity_leftover = max(0, quantity - demand)
            revenue = selling_price * quantity_produced
            cost = production_cost * quantity + disposal_cost * quantity_leftover
            profit = revenue - cost
            profits[quantity].append(profit)
            
    return profits()


    expected_profits = profits()

    # Calculate the expected profit for each quantity
    expected_profits = {quantity: np.mean(profits[quantity]) for quantity in quantities}

    # Choose the quantity that maximizes the expected profit
    optimal_quantity = max(expected_profits, key=expected_profits.get)
    profits()
