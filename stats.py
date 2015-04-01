import pandas as pd

from scipy import stats


data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()

data = [i.split(', ') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

print df
print
print

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print "The mean for the Alcohol dataset is: " 
print df['Alcohol'].mean() 
# 5.4436363636363634
print

print "The median for the Alcohol dataset is:"
print df['Alcohol'].median() 
# 5.63
print

# If all numbers occur equally often, stats.mode() will return the smallest number
print "The mode for the Alcohol dataset is:" 
print stats.mode(df['Alcohol']) 
# 4.02
print

print "The mean for the Tobacco dataset is: " 
print df['Tobacco'].mean() 
# 3.6181818181818186
print

print "The median for the Tobacco dataset is:"
print df['Tobacco'].median() 
# 3.53
print

print "The mode for the Tobacco dataset is:" 
print stats.mode(df['Tobacco']) 
# 2.71
print

print "The range for the Alcohol dataset is:"
print max(df['Alcohol']) - min(df['Alcohol'])
# 2.4500000000000002
print

print "The standard deviation for the Alcohol dataset is:"
print df['Alcohol'].std() 
# 0.79776278087252406
print

print "The variance for the Alcohol dataset is:"
print df['Alcohol'].var() 
# 0.63642545454546284
print

print "The range for the Tobacco dataset is:"
print max(df['Tobacco']) - min(df['Tobacco'])
# 1.8499999999999996
print

print "The standard deviation for the Tobacco dataset is:"
print df['Tobacco'].std() 
# 0.59070835751355388
print

print "The variance for the Tobacco dataset is:"
print df['Tobacco'].var() 
# 0.3489363636363606














