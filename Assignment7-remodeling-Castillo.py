#Jonathan Castillo
#Section 10
#On my honor, I have neither given nor received unauthorized assistance on this assignment.
import math
#part 1 of the project.
print("<<<<<< Painting the house rooms >>>>>>")
print()
#ask the user for number of rooms.
numRoom=int(input("How many rooms there are?:"))
#assign the balue of the cost per room.
costOneRoom=int(300)
print()
#ask the user if they want an extra layer of paint.
paint=str(input("Do you want a third layer of paint? (yes/no):"))
#calculate the cost of paint
costRoom=costOneRoom*numRoom
#define the variable for extra cost.
extraCost=0
print()
#use of if statement to decide if the user wants the extra layer.
if paint=="yes":
  extraCost=costRoom*0.30
else:
  extracost=0
#calculate the total cost.
totalPaintCost=math.ceil(costRoom+extraCost)
print("The total cost of the rooms paiting is: "+str(totalPaintCost))
print()
#part 2 of the project
print("<<<<<< Heater and Ductwork in the living room >>>>>>")
print()
#define the variable and assign the value of the cost of the job.
jobCost=400
#ask user for length and width of living room.
length=int((input("The Length of the living room is:")))
print()
width=int((input("The width of the living room is:")))
#calculate the cost of the ductwork.
ductworkCost=math.ceil((length+width)*10)
print()
#ask the user if they want to cut corners.
cuttingCorners=str(input("Do you consent to cut corners in Ductwork? (yes/no):"))
#calculate the diagonal of the room.
diagonal=(math.sqrt(length**2+width**2))
print()
#printing the diagonal.
print("The living room is "+str(diagonal)+" feet in diagonal")
#if statement to  determind if the user want to cut corners.
if cuttingCorners=="yes" and int(diagonal)<20:
  ductworkCost=math.ceil(diagonal*10)
print()
#printing  the total cost of the job.
print("The total cost of the ductwork and job is:"+str(ductworkCost+jobCost))
print()
#part 3 of the project
print("<<<<<< Flooring Work >>>>>>")
print()
#assigning and defining variables
floorCost=0
floorJobCost=int(9600)
#asking user for square feet.
floorSquareFt=int(input("How many square feet is the floor?:"))
print()
#using nested if statement to determine the cost of the flooring.
if floorSquareFt<1000:
  floorCost=int(floorSquareFt*8)
else:
  if 1000<=floorSquareFt<3000:
    floorCost=int(floorSquareFt*6)
  else:
    floorCost=int(floorSquareFt*4)
#printing the total cost and calculating it.
totalfloorCost=int(floorCost+floorJobCost)
print("The total cost for the flooring is:"+str(totalfloorCost))
print()
#printing the total cost of part 1,2 and 3 of the project.
print("<<<<<< The total cost for all the house work is: $"+str(totalPaintCost+ductworkCost+totalfloorCost+jobCost)+" >>>>>>")
  