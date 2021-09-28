import csv

from statistics import mean

PyBank_input_file=r"PyBank\Resources\budget_data.csv"
number_months=[]
profits_losses=[]

with open(PyBank_input_file, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader)

    for row in csvreader:
        number_months.append(row[0])
        profits_losses.append(int(row[1]))
    difference=[profits_losses[i+1]-profits_losses[i] for i in range(len(profits_losses)-1)]
    average_profits_losses=mean(difference)
    greatest_increase=max(difference)
    greatest_decrease=min(difference)
    date_greatest_increase=number_months[difference.index(max(difference))+1]
    date_greatest_decrease=number_months[difference.index(min(difference))+1]
   
PyBank_output_file=r"PyBank\Analysis\PyBank Analysis.txt"
with open(PyBank_output_file,'w') as analysis:
    analysis.write("Financial Analysis")
    analysis.write("\n----------------------------")
    analysis.write(f"\nTotal Months: {len(number_months)}")
    analysis.write(f"\nTotal: ${sum(profits_losses)}")
    analysis.write(f"\nAverage Change: ${round(average_profits_losses,2)}")
    analysis.write(f"\nGreatest Increase: {date_greatest_increase} (${greatest_increase})")
    analysis.write(f"\nGreatest Decrease: {date_greatest_decrease} (${greatest_decrease})")