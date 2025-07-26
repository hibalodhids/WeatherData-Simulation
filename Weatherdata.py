import numpy as np
# 1. Generate synthetic temperature data for 30 days
#example
# Let's say temperatures range from 15°C to 40°C
np.random.seed(34)
temperatures =  np.random.uniform(low=15.0, high=40.0, size=30)

print("🌡️ Daily Temperatures (°C) for 30 days:\n", np.round(temperatures, 2))

# 2. Calculate basic statistics

mean_temp = np.mean(temperatures)
median_temp = np.median(temperatures)
min_temp = np.min(temperatures)
max_temp = np.max(temperatures)
std_temp = np.std(temperatures)
hot_days = np.sum(temperatures > 35)

# 3 print data
print("\n📊 Temperature Statistics:")
print(f"Mean Temperature     : {mean_temp:.2f}°C")
print(f"Median Temperature   : {median_temp:.2f}°C")
print(f"Minimum Temperature  : {min_temp:.2f}°C")
print(f"Maximum Temperature  : {max_temp:.2f}°C")
print(f"Std Deviation        : {std_temp:.2f}°C")
print(f"🔥 Days above 35°C    : {hot_days} days")



