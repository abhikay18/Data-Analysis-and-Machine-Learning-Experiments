from scipy.stats import chi2_contingency
from scipy.stats import chi2
from scipy.stats import ttest_ind

# Perform Chisquare Test

# Compute the Observed value

table = [ [35,15],
          [25,25]
          ]
print('\n Obervartion Table')
# Print the observed value
print(table)

#Perform the Chi square test
stat,p,dof,expected = chi2_contingency(table)

# Compute the expected value
print('\n')
print('\n Expectation Table')
print(expected)

# Set the parameters
prob = 0.90

# Find the critical value
critical = chi2.ppf(prob,dof)
# Print the critical value
print('\n')
print('The critical Value')
print(critical)

print('statistical value')
print(stat)

if abs(stat) >= critical:
    print('Stat value greater or equal to critical:Reject Null Hypotheis')
else:
    print('Stat value is less than critical: Accept Alt Hypothesis')

# Perform t-Tests

x = ([6,3,4,5,5,9,7,8])
y = ([4,4,1,3,5,6,2,7])

print('\n')
print('t-Test completed\n\n')
stat,p= ttest_ind(x,y,equal_var=True)

print('\n')
print('Statistical value')
print(stat)
print('p value')
print(p)
