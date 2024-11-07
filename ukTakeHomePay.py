# importing the modules
import numpy as np 
import matplotlib.pyplot as plt 

basicRateStart = 12570
higherRateStart = 50270
additionalRateStart = 125140
lossOfPersonalAllowanceStart = 100000

maxLossOfPersonalAllowanceTax = basicRateStart*0.4
maxBasicTax = (higherRateStart-basicRateStart)*0.2  
maxHigherTax = (additionalRateStart-higherRateStart)*0.4

lowerNationalInsuranceStart = 242*52
higherNationalInsuranceStart = 967*52

maxLowerNI = (higherNationalInsuranceStart-lowerNationalInsuranceStart)*0.08

studenLoanThreshold = 24990

def applyTax(x):
    ##pension contributions:
    x*=0.95
    result = x

    # tax bands
    if x > basicRateStart:
        result -= min(maxBasicTax, (x-basicRateStart)*0.2)
    if x > higherRateStart:
        result -= min(maxHigherTax, (x-higherRateStart)*0.4)
    if x > additionalRateStart:
        result -= (x-additionalRateStart)*0.45

    #loss of personal allowance
    if x>lossOfPersonalAllowanceStart:
        result -= min(maxLossOfPersonalAllowanceTax,(x-lossOfPersonalAllowanceStart)*0.2)

    #national insurance
    if x > basicRateStart:
        result -= min(maxLowerNI, (x-lowerNationalInsuranceStart)*0.08)
    if x > higherNationalInsuranceStart:
        result -= (x-higherNationalInsuranceStart)*0.02

    #student loan
    if x > studenLoanThreshold:
        result -= (x-studenLoanThreshold)*0.09
    return result

# data to be plotted
x = np.arange(1000, 500000,1000) 
y = [applyTax(i) for i in x ]
 
# plotting
plt.title("Line graph") 
plt.xlabel("X axis") 
plt.ylabel("Y axis") 
plt.plot(x, y, color ="red") 
plt.plot(x, x, color ="blue") 
plt.grid()
plt.show()