# import modules
import csv
from statistics import mean

# path of the input file
PyBank_input_file=r"PyBank\Resources\budget_data.csv"

# create an empty list of months
number_months=[]

# create an empty list for the number of profits/losses
profits_losses=[]

# open the input file in a read mode
with open(PyBank_input_file, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    # skip the header
    next(csvreader)

    # loop through the file
    for row in csvreader:

        # append the list of months
        number_months.append(row[0])
        
        # append the list of profits_losses
        profits_losses.append(int(row[1]))

    # create a list of comprehensions for the difference between profits_losses between 2 months
    difference=[profits_losses[i+1]-profits_losses[i] for i in range(len(profits_losses)-1)]
    
    # calculate the average of profits_losses
    average_profits_losses=mean(difference)

    # calculate the increase and decrease of the profits_losses
    greatest_increase=max(difference)
    greatest_decrease=min(difference)

    # return the months with the greatest incread and decrease
    date_greatest_increase=number_months[difference.index(max(difference))+1]
    date_greatest_decrease=number_months[difference.index(min(difference))+1]

# path of the output file  
PyBank_output_file=r"PyBank\Analysis\PyBank Analysis.txt"

# open the output file in write mode
with open(PyBank_output_file,'w') as analysis:

    # write the results on the output file
    analysis.write("Financial Analysis")
    analysis.write("\n----------------------------")
    analysis.write(f"\nTotal Months: {len(number_months)}")
    analysis.write(f"\nTotal: ${sum(profits_losses)}")
    analysis.write(f"\nAverage Change: ${round(average_profits_losses,2)}")
    analysis.write(f"\nGreatest Increase: {date_greatest_increase} (${greatest_increase})")
    analysis.write(f"\nGreatest Decrease: {date_greatest_decrease} (${greatest_decrease})")