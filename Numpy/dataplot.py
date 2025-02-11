import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataplot.csv')

df.plot()

print(df.corr())
plt.show()

# Scatter Plot
# Specify that you want a scatter plot with the kind argument:
# kind = 'scatter'
# A scatter plot needs an x- and a y-axis.
# In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.
# Include the x and y arguments like this:
# x = 'Duration', y = 'Calories'
# Example

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('dataplot.csv')

# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

# plt.show()

# Remember: In the previous example, we learned that the correlation between "Duration" and "Calories" 
# was 0.922721, and we concluded with the fact that higher duration means more calories burned.
# By looking at the scatterplot, I will agree.




# Histogram
# Use the kind argument to specify that you want a histogram:
# kind = 'hist'
# A histogram needs only one column.
# A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?
# In the example below we will use the "Duration" column to create the histogram:
# Example
# df["Duration"].plot(kind = 'hist')