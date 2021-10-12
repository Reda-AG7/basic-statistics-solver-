import tkinter as tk
from tkinter import font
from tkinter.constants import HORIZONTAL
from tkinter.ttk import *
from PIL import Image, ImageTk
import math
#The main window
root = tk.Tk()
root.title("iStat")
v1 = tk.DoubleVar()
#root.geometry('500x300')
def getOutliers(outliersList):
    s=''
    for i in outliersList:
        s+= str(i) + ' '
    return s
def calculate():
    text = txt_box.get("1.0","end")
    myData=[]
    print(type(text))
    i=0
    #split the data
    while i < len(text):
        if text[i].isnumeric():
            j=i+1
            while (text[j].isnumeric() or text[j] == '.') and j < len(text):
                j+=1
            myData.append(float(text[i:j]))
            i=j
        i+=1
    print(myData)

    #get the mean
    mean = 0
    size = len(myData)
    for i in myData:
        mean+=i
    mean/=size

    #get the variance
    sVariance = 0
    for i in myData:
        sVariance+=(i-mean)**2
    sVariance/=size-1

    #get the standard deviation
    sDeviation = math.sqrt(sVariance)

    #get the median and the quartiles
    myData.sort()
    median = 0
    q1=0
    q3=0
    index = size // 2
    if size%2 != 0:
        median = myData[index]
        q1 = myData[index // 2]
        q3 = myData[(index + size) // 2]
    else:
        median = (myData[(size//2)-1]+myData[size//2])/2
        if ((size - 1 - index) % 2 == 0):
            newIndex = (size + index) // 2
            q3 = (myData[newIndex] + myData[newIndex + 1]) / 2
            q1 = (myData[index // 2] + myData[index // 2 - 1]) / 2
        else:
            q3 = myData[(size + index) // 2]
            q1 = myData[(index // 2) - 1]
    iqr = q3-q1
    wiskerMax = q3 + 1.5*iqr
    wiskerMin = q1 - 1.5*iqr

    #outliers
    outliersList=[]
    for i in myData:
        if i < wiskerMin or i > wiskerMax  and i not in outliersList:
            outliersList.append(i)
    print("outliers list : ",outliersList)
    print(getOutliers(outliersList))
    #present results:
    
    roundDec = int(v1.get())
    print(roundDec)
    lbl_sMeanData = Label(root,text=str(round(mean,roundDec)), font=12).grid(row=4,column=0,pady=5,padx=5)
    lbl_sVarianceData = Label(root,text=str(round(sVariance,roundDec)),font=12).grid(row=4,column=1,pady=5,padx=5)
    lbl_sDeviationData = Label(root,text=str(round(sDeviation,roundDec)),font=12).grid(row=4,column=2,pady=5,padx=5)

    lbl_medianData = Label(root,text=str(round(median,roundDec)),font=12).grid(row=6,column=0,pady=5,padx=5)
    lbl_q1Data = Label(root,text=str(round(q1,roundDec)),font=12).grid(row=6,column=1,pady=5,padx=5)
    lbl_q3Data = Label(root,text=str(round(q3,roundDec)),font=12).grid(row=6,column=2,pady=5,padx=5)

    lbl_maxWiskerData = Label(root,text=str(round(wiskerMax,roundDec)),font=12).grid(row=8,column=0,pady=5,padx=5)
    lbl_minWiskerData = Label(root,text=str(round(wiskerMin,roundDec)),font=12).grid(row=8,column=1,pady=5,padx=5)
    lbl_outliersData = Label(root,text=getOutliers(outliersList)  ,font=12).grid(row=8,column=2,pady=5,padx=5)

for k in range(3):
    root.columnconfigure(k, weight=1, minsize=75)
    root.rowconfigure(k, weight=1, minsize=50)

lbl_logo = Label(master=root,text="iStat", font = "Helvetica 16 bold italic", foreground='#000000').grid(row=0,column=1,pady=5,padx=5)


txt_box = tk.Text(master=root) 
txt_box.grid(row=1,column=0,columnspan=3,pady=5,padx=5)

btn_calculate = Button(master=root, text='calculate', command=calculate)
btn_calculate.grid(row=2,column=0,pady=5,padx=10)
lbl_round = Label(root,text='Decimal round :',font=12, foreground='#BD4B4B').grid(row=2,column=1,pady=5,padx=5)
scale = tk.Scale(root, orient=HORIZONTAL,from_=0,to=6,variable = v1).grid(row=2,column=2,pady=5,padx=5)

lbl_sMean = Label(root,text='Simple mean :',font=12, foreground='#BD4B4B').grid(row=3,column=0,pady=5,padx=5)
lbl_sVariance = Label(root,text='Simple Variance :',font=12, foreground='#BD4B4B').grid(row=3,column=1,pady=5,padx=5)
lbl_sDeviation = Label(root,text='Standard Deviation :',font=12, foreground='#BD4B4B').grid(row=3,column=2,pady=5,padx=5)


lbl_median = Label(root,text='Median :',font=12, foreground='#BD4B4B').grid(row=5,column=0,pady=5,padx=5)
lbl_q1 = Label(root,text='q1 :',font=12, foreground='#BD4B4B').grid(row=5,column=1,pady=5,padx=5)
lbl_q3 = Label(root,text='q3 :',font=12, foreground='#BD4B4B').grid(row=5,column=2,pady=5,padx=5)

lbl_maxWisker = Label(root,text='max_wisker :',font=12, foreground='#BD4B4B').grid(row=7,column=0,pady=5,padx=5)
lbl_minWisker = Label(root,text='min_wisker :',font=12, foreground='#BD4B4B').grid(row=7,column=1,pady=5,padx=5)
lbl_outliers = Label(root,text='outliers :',font=12, foreground='#BD4B4B').grid(row=7,column=2,pady=5,padx=5)
root.mainloop()
