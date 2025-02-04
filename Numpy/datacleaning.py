import pandas as pd

df = pd.read_csv('data.csv')

# Remove Rows, If you want to change the original DataFrame, use the inplace = True argument:
# df.fillna(130, inplace = True) //not recommended

# Replace Only For Specified Columns
# df["Calories"].fillna(130, inplace = True)

# Replace Using Mean, Median, or Mode
# x = df["Calories"].mean()
# x = df["Calories"].median()
# x = df["Calories"].mode()[0]
# df["Calories"].fillna(x, inplace = True)

# Pandas has a to_datetime() method for this:
#     Convert to date:
# import pandas as pd
# df = pd.read_csv('data.csv')
# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())


# Removing Rows
# Remove rows with a NULL value in the "Date" column:

# df.dropna(subset=['Date'], inplace = True)   

# Replacing Values
# One way to fix wrong values is to replace them with something else.
# In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
# Example
# Set "Duration" = 45 in row 7:
# df.loc[7, 'Duration'] = 45

# To replace wrong data for larger data sets you can create some rules, e.g. 
# set some boundaries for legal values, and replace any values that are outside of the boundaries.

# Example
# Loop through all values in the "Duration" column.
# If the value is higher than 120, set it to 120:
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120




# Another way of handling wrong data is to remove the rows that contains wrong data.
# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
# Example
# Delete rows where "Duration" is higher than 120:
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)



# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row:
# Example
# Returns True for every row that is a duplicate, otherwise False:
# print(df.duplicated())




# To remove duplicates, use the drop_duplicates() method.
# Example
# Remove all duplicates:
# df.drop_duplicates(inplace = True)

# Remember: The (inplace = True) 
# will make sure that the method does NOT return a new DataFrame, 
# but it will remove all duplicates from the original DataFrame.







print(df.to_string())