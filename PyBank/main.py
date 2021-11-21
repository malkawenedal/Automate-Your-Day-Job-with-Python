{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 186,
   "id": "61aef79c-d5c7-41cf-adca-8ba1ff95f23f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the pathlib and csv library\n",
    "from pathlib import Path\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "3bc886ed-01cd-42e7-87dc-a857c70b6a21",
   "metadata": {},
   "outputs": [],
   "source": [
    "#set the file path \n",
    "csvpath=Path('../../unit 2 homework/PyBank/Resources/budget_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "id": "0e3e7b10-d1a6-4b87-85fe-cd0b90436dcf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class '_io.TextIOWrapper'>\n",
      "<class '_csv.reader'>\n",
      "May-2010\n",
      "Jul-2010\n",
      "Oct-2010\n",
      "Jan-2011\n",
      "Mar-2011\n",
      "Feb-2012\n",
      "[116771, -662642, -391430, 379920, 212354, 510239, -428211, -821271, 693918, 416278, -974163, 860159, -1115009, 1033048, 95318, -308093, 99052, -521393, 605450, 231727, -65187, -702716, 177975, -1065544, 1926159, -917805, 898730, -334262, -246499, -64055, -1529236, 1497596, 304914, -635801, 398319, -183161, -37864, -253689, 403655, 94168, 306877, -83000, 210462, -2196167, 1465222, -956983, 1838447, -468003, -64602, 206242, -242155, -449079, 315198, 241099, 111540, 365942, -219310, -368665, 409837, 151210, -110244, -341938, -1212159, 683246, -70825, 335594, 417334, -272194, -236462, 657432, -211262, -128237, -1750387, 925441, 932089, -311434, 267252, -1876758, 1733696, 198551, -665765, 693229, -734926, 77242, 532869]\n"
     ]
    }
   ],
   "source": [
    "with open(csvpath, 'r') as csvfile:\n",
    "    print(type(csvfile))\n",
    "    \n",
    "    csvreader=csv.reader(csvfile,delimiter=',')\n",
    "    print(type(csvreader))\n",
    "    \n",
    "   \n",
    "\n",
    " # read each row of data after the header\n",
    "    month=0\n",
    "    total_pl =0\n",
    "    delta=[]\n",
    "    prev_month=0\n",
    "    max_up_month=0\n",
    "    max_up_date=\"\"\n",
    "    for row in csvreader:\n",
    "        if row[0]==\"Date\":\n",
    "            pass \n",
    "        elif row[0] == \"Jan-2010\":\n",
    "            prev_month = int(row[1])\n",
    "            month=month+1\n",
    "            total_pl += int(row[1])\n",
    "            max_up_month=0\n",
    "            max_up_date=row[0]\n",
    "        elif row[0] == \"Feb-2010\":\n",
    "            max_up_month = int(row[1]) - prev_month\n",
    "            month=month +1\n",
    "            total_pl += int(row[1])\n",
    "            max_up_date= row[0]\n",
    "            delta.append(int(row[1]) - prev_month)\n",
    "            prev_month= int(row[1])\n",
    "        else:\n",
    "            month =month+1\n",
    "            total_pl += int(row[1])\n",
    "            delta.append(int(row[1]) - prev_month)\n",
    "            if (int(row[1]) - prev_month) > max_up_month:\n",
    "                max_up_month= int(row[1]) - prev_month\n",
    "                print(row[0])\n",
    "                max_up_date=row[0]\n",
    "            prev_month=int(row[1])\n",
    "            \n",
    "             \n",
    "    \n",
    "    print (delta)\n",
    "    \n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "id": "ac9bb4ba-5ea7-4667-aa79-08fa2c7b3b98",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Total MONTHS 86\n",
      " Total $ 38382578\n",
      "Average Change  -2315.1176470588234\n"
     ]
    }
   ],
   "source": [
    "   #The total number of months included in the dataset.\n",
    "print(f\" Total MONTHS {month}\")\n",
    "  \n",
    "    #The net total amount of Profit/Losses over the entire period.\n",
    "print(f\" Total $ {total_pl}\")    \n",
    "    \n",
    "    #The average of the changes in Profit/Losses over the entire period.\n",
    "print (\"Average Change \"+ \" \"+ str((sum(delta)/len(delta))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "id": "209dc1e7-be96-4a75-85e2-5cd0bcc5f256",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " The greatest increase in profit is  (Feb-2012), (1926159)\n"
     ]
    }
   ],
   "source": [
    " #The greatest increase in profits (date and amount) over the entire period.\n",
    "print(f\" The greatest increase in profit is  ({max_up_date}), ({max_up_month})\")\n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "756addbd-83ac-434e-982b-89fe9bda8c28",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
