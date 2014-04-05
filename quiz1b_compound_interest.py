# compound interest exercise
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    future_money = present_value * ((1 + rate_per_period) ** periods)
    return future_money

print future_value(1000, .02, 365, 3)
print future_value(500, .04, 10, 10)
