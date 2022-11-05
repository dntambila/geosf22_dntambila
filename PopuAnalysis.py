""" This python script consists of different functions to read a World population data file and computes different statistical infererences. Description of each function is given in the docstring. This work was not possible without consulting several sources, websites and references, thus any similarites of my work with another person's work may be both of us have consulted the same references by coincidence. The references for each function is proved in the docstring .
    References:
    https://www.geeksforgeeks.org/how-to-read-text-file-into-list-in-python/
    https://stackoverflow.com/questions/61404473/create-a-list-of-lists-from-reading-a-text-file: accessed on 11/26/2022
    https://www.geeksforgeeks.org/calculate-the-average-variance-and-standard-deviation-in-python-using-numpy
    https://stackabuse.com/calculating-variance-and-standard-deviation-in-python/
    https://realpython.com/python-min-and-max/#:~:text=Use%20Python's%20min()%20and,()%20with%20strings%20and%20dictionaries
    https://stackoverflow.com/questions/16579919/how-do-i-write-a-compare-function
    https://bobbyhadz.com/blog/python-calculate-percentage
"""

# importing packages to be used
import pandas as pd
import numpy as np  
import math as ma

# defining  the functions needed for Population Data analysis

def readUNpopData(path,filetype,out):
    """
    Function is used to read a text file and returns the header-line as a list and data as a list of lists.
    The header and data are read independently as lists.

    Parameters/input
    ----------------
    path: <string>
        The path to the file without the filetype.
    filetype: <string>
        The file type, enter either 'txt' or 'csv'. Note that the current functions can only read txt files.
    ret: <string>
        out takes either 'header' or 'data' returns either the list for the header or data .

    Returns/output
    --------------
    header: <list>
        List of the header line.
    data: <list>
        List of lists for the data line.
    """
    path2 = path+'.'+filetype   #saves the file name
    #  except error handling when opening a data-file
    try:
        rd = open(path2,'r') # opening the file
        if out == 'header':
            print("file exists")
        elif out =='data':
            print("file opened ready to use")
    except IOError:
        print("Error: can\'t find data file!")
    header2 = rd.readline()         # header information saved as a variables
    header = header2.split(",")    # separates the list into a list using the comma
    header[-1] = header[-1].replace('\n','') # removes the trailing \n in the header
    data2 = rd.readlines()                   # read other variable and saves it as a list of lists
    data = [sep.split(",") for sep in data2]  # separates the list into a list using the comma
    # The for-loop for the entire data
    for i in range(len(data)):
        [i][-1] = data[i][-1].replace('\n','') # deletes the trailing \n in the header
        data[i][1:]=[x.replace(' ','') for x in data[i][1:]]
        data[i][1:]=[(int(x)*1000) for x in data[i][1:]]
    rd.close() # closes the file
    # conditional to returns header and data
    if out == 'header': 
        return header
    elif out =='data':
        return data
    
# defining a function for maximum numbers in a list, let call it mymax
def mymax(x):
    """
    Function to find out the maximum number in a list of numbers.
    
    Parameters/input
    ----------------
    x: <list>
        List of numbers. 

    Returns/output
    --------------
    maxim: <numerical>
        A single number for the maximum number in the list of numbers.
    """
    maxim = x[0]   # maximum value in the first index in the list 
    for i in range(len(x)):
        if x[i] > maxim: # condition for the maximum operations
            maxim = x[i]
    return maxim  # returns the maxim number from the list 

def mymax3(x,y1):
    """
    Function used to find out the next two (2nd and 3rd) largest maximum numbers in a list
    
    Parameters/input
    ----------------
    x: <list>
        List of numbers. 
    y1: <numerical>
        single integer number of 2 or 3 for 2nd largest or 3rd largest number respectively.
        
    Returns/output
    --------------
    max2: <numerical>
        A single number for the 2nd largest number in the list of numbers.
    max3: <numerical>
        A single number for the 3rd largest number in the list of numbers. 
    """
    max1 = mymax(x) # rfinds the first maximum using mymax function
    x.remove(max1) # deletes the largest
    max2 = mymax(x) # finds the 2nd largest maximum
    x.remove(max2) # deletes the second largest
    max3 = mymax(x) # finds the 3rd largest maximum
    if y1 == 2:
        return max2 
    elif y1 == 3:
        return max3 
    else:
        print("Please enter either 2 or 3 as y1 for the 2nd or 3rd largest number") # this take care if the input for y1 is only 2 and 3
        
#defining a function to compute sum or total of numbers in a list, let call it mysum
def mysum(x):
    """
    Function used to compute the total sum of numbers passed.
   
    Parameters/input
    ----------------
    x: <numerical>
        A single number or list of numbers. 

    Returns/output
    --------------
    outsum: <numerical>
        A single number for the sum of the numbers.
    """
    outsum = 0 # initialize the sum with zero
    if type(x) == int or type(x) == float: # for one value, returns the same as the sum 
        outsum = x 
    else:
        # for-loop when a list of numbers given it sums up them 
        for i in range(len(x)):
            outsum = outsum + x[i]
    return outsum # returns the sum

# defining a function to compute the mean, let call it mymean
def mymean(x):
    """
    Function to compute the mean of numbers/lists:
    mean = sum(x)/len(x)
    The function make use of mysum function.

    Parameters/input
    ----------------
    x: <list>
        List of numbers. 

    Returns/output
    --------------
    outmean: <numerical>
        A single number for the mean of the numbers.
    """
    outmean = (mysum(x))/len(x)
    return outmean

# defining a function to compute the standard deviation, let call it mystd
def mystd(x):
    """
    Function to compute standard deviation of numbers/lists:
    It take advantages of mysum and mymean functions.

    Parameters/input
    ----------------
    x: <list>
        List of numbers. 

    Returns/output
    --------------
    outstd: <numerical>
        A single value for the standard deviation of numbers/lists.
    """
    square_diff = []     # set an empty square difference  
    for i in range(len(x)):  # for-loop fir the entire lists
        square_diff.append((x[i]-(mymean(x)))**2)    # appends each computed value to the square difference
    outstd = ((1/(len(x)-1))*mysum(square_diff))**(1/2)  # this uses mystd function
    return outstd

# defining a function to compute the percentage, let call it mypercentage      
def mypercentage(initial,final):
    """
    Function to computes the percentage change based on: percent_change = ((final/last - initial/first)/initial/first)*100
    The inputs are the initial/first and final/last number.

    Parameters/input
    ----------------
    initial: <list> or <numerical>
        The initial/starting list of numbers or single numeric value. 
    final: <list> or <numerical>
        The final list of numbers or single numeric value. 
        
    Returns/output
    --------------
    outper: <numerical>
        A single number for the percent change in %.
    """
    outper = (((mysum(final))-(mysum(initial)))/(mysum(initial)))*100 # calculates the percentage change
    return outper

# defining a function that compares the values, let call it mycompare
def mycompare(x,y):
    """
    Function used to compare the value in the first variable x equals the second variable y.

    Parameters/input
    ----------------
    x: <string>
        The value to be compared to another. 
    y: <list> or <string>
        The list or string to which it is being compared. 
        
    Returns/output
    --------------
    True: <boolean>
        Returns true if the two strings are comparable or the input is contained in the list to which it is being compared.
    """
    if type(x) == str and x == y:
        return True
    elif type(y) == list:
        for i in range(len(y)):
            if x == y[i]:
                return True
            
# Main Program
def main():
    header = readUNpopData('WPP2019_INTHOUSAND','txt','header') # reads the header line
    data = readUNpopData('WPP2019_INTHOUSAND','txt','data') # reads the other data
    print(header) # displays header on the screen to aid the user select the country of interest
    # Selecting the country/region to be analyzed later
    countries_regions = ([x[header.index('Region-subregion-country-or-area')] for x in data]) # saves all the available countries in the file to a variable
    SelectCountry = '' # display an interface on the scren for the user input SelectCountry = ''
    
    counter  = 0 # counter to check for failed tries
    while mycompare(SelectCountry,countries_regions) != True: 
        if counter>=4:
            print("Pleas select one of these countries:\n{}\n" .format(countries_regions)) # When 4 attempts fail print all countries on screen
        SelectCountry = input("Select a country of your interest to be analyzed:\n") # accepts user input
        counter = counter + 1 # adds one to counter after each failed attempt


    #1. What was the estimated total world population in 2020?
    year ='2020'
    World_Population2020 = mysum([x[header.index(year)] for x in data]) # sums up the population for 2020 using a list 
    print("\n1.The estimated total world population for {} is {}.".format(year,World_Population2020)) #print 
    
#2. What is the predicted total world population in 2050 and 2100?
    year1 ='2050'
    year2 ='2100'
    World_Population2050 = mysum([x[header.index(year1)] for x in data]) # sums up the population for 2050 using a list comprehension
    World_Population2100 = mysum([x[header.index(year2)] for x in data]) # sums up the population for 2100 using a list comprehension
    print("\n2.The estimated total world population in {} and {} are {} and {} respectively.".format(year1, year2,    World_Population2050,World_Population2100)) #prints out the estimated total world population in 2050 and 2100
    
#3. What is the population increase of the total world population from now (2020) to 2050 and 2100 (in percentage)?  # The computation is based on the population calculated in qn1 and qn2 above
    startyear1 ='2020'
    endyear1 ='2050'
    endyear2 ='2100'
    percent_30yrs = mypercentage(World_Population2020,World_Population2050)
    percent_80yrs = mypercentage(World_Population2020,World_Population2100)
    print("\n3.The population increase from {} to {} is {}%.".format(startyear1, endyear1, round(percent_30yrs,2)))
    print("The population increase from {} to {} is {}%.".format(startyear1, endyear2, round(percent_80yrs,2)))

#4. Which three countries are expected to contain the largest population in 10 years.
# Assumption: Now current year is 2022, so 10 years means the year will be 2032

    year ='2032'
    largest1 = data[[ i[header.index(year)] for i in data ].index(mymax([ i[header.index(year)] for i in data ]))][0] # uses the function mymax to find out the maximum
    largest2 = data[[ i[header.index(year)] for i in data ].index(mymax3([ i[header.index(year)] for i in data ],2))][0] # uses the function mymax3 to find out the 2nd largest
    largest3 = data[[ i[header.index(year)] for i in data ].index(mymax3([ i[header.index(year)] for i in data ],3))][0] # uses the function mymax3 to find out the 3rd largest

    print("\n4.The three countries expected to contain the largest population in 10 years from 2022 are {}, {}, and {} respectively.".format(largest1, largest2, largest3)) #prints out the largest three countries
    
#5. Enter any country/region for the user input request,retrieve a subset of the pandas data frame and return the population numbers for 2020, 2050 and 2100 for this country/region.

    year1 = '2020'
    year2 = '2050'
    year3 = '2100'
    population_2020 = data[[i[header.index('Region-subregion-country-or-area')] for i in data].index(SelectCountry)][header.index(year1)] #returns the population for a particular country, with the user input in the years given above
    population_2050 = data[[i[header.index('Region-subregion-country-or-area')] for i in data].index(SelectCountry)][header.index(year2)]
    population_2100 = data[[i[header.index('Region-subregion-country-or-area')] for i in data].index(SelectCountry)][header.index(year3)]

    print("\n5.The population of {} for the years {}, {}, and {} are {}, {}, and {} repectively.".format(SelectCountry, year1, year2, year3, population_2020, population_2050, population_2100 ))
    
#6. What is the current population and expected population increase in percentage by 2100 for USA, China, India, Nigeria, Egypt, Brazil, Australia, France, Turkey ? (Code this analysis as a loop over a list of these countries, instead of copying-pasting your code for each country).

    countries_regions = ['United States of America', 'China', 'India', 'Nigeria', 'Egypt', 'Brazil', 'Australia', 'France', 'Turkey'] 
    for i in range(len(countries_regions)): 
        current_Population = data[[x[header.index('Region-subregion-country-or-area')] for x in data].index(countries_regions[i])][header.index('2022')] #returns the current population of each country
        population_increase = mypercentage(current_Population,data[[x[header.index('Region-subregion-country-or-area')] for x in data].index(countries_regions[i])][header.index('2100')]) #returns the population increase
        print("\n6.The current population of {} in 2022 is {} and the expected population increase by 2100 is {}%.".format(countries_regions[i],current_Population, round(population_increase,2)))
        
#7. Which country is expected to grow the fastest until 2100 (in percentage, relative to their population in 2020).
    countries_regions = ([x[header.index('Region-subregion-country-or-area')] for x in data])
    population_increase = [] # initializing by assigning zero value
    for i in range(len(countries_regions)):
        population_increase.append(mypercentage(data[[x[header.index('Region-subregion-country-or-area')] for x in data].index(countries_regions[i])][header.index('2020')],
                                    data[[x[header.index('Region-subregion-country-or-area')] for x in data].index(countries_regions[i])][header.index('2100')]))
    countries_regions[population_increase.index(mymax(population_increase))] # the country expected to grow the fastest is the country with the highest population increase, here the function mypercentage is used
    print("\n7.The country expected to grow the fastest from 2020 until 2100 is {} at a percentage rate of {}%.".format(countries_regions[population_increase.index(mymax(population_increase))],round(population_increase[population_increase.index(mymax(population_increase))],2)))
    
#8. What is the mean and standard deviation for percentage growth rates for all countries (worldwide)from today until 2100?

    countries_regions = ([x[header.index('Region-subregion-country-or-area')] for x in data])
    population_increase = []  # initializing by assigning zero value
    for i in range(len(countries_regions)):
        population_increase.append(mypercentage(data[[j[header.index('Region-subregion-country-or-area')] for j in data].index(countries_regions[i])][header.index('2022')],
                                    data[[j[header.index('Region-subregion-country-or-area')] for j in data].index(countries_regions[i])][header.index('2100')])) # computes the percentage growth for each country
    meanAll = mymean(population_increase) # uses mymean to compute the mean
    stdAll = mystd(population_increase) # uses mystd deviation to calculate the standard deviation
    print("\n8.The mean and standard deviation for the percentage growth rates for all counties (worldwide) are {}% and {}% respectively.".format(round(meanAll,2),round(stdAll,2)))
    
if __name__ == "__main__":main() # This line causes main() function to be executed if this module is executed without an import