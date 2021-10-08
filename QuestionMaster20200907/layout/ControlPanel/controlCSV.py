from docxtpl import DocxTemplate
import jinja2
import pandas as pd
import csv
from csv import writer
import os
import time


# import tkinter as tk

# def onReturn(event):

#     value = entry1.get()
#     print(value)
#     entry1.delete(0, "end")

# root = tk.Tk()
# root.title("test")

# entry1=tk.Entry(root)
# entry1.bind("<Return>", onReturn)
# entry1.pack()

# root.mainloop()






newCSV="D:\\pythonworkspace\\QuestionMaster20200907\\template\\QuestionMasterCSV.csv"

def createWord(Qno):
    tpl=DocxTemplate("D:\\pythonworkspace\\QuestionMaster20200907\\template\\NormalQuestion.docx")
    context={"QID":str(Qno)}
    tpl.render(context)
    tpl.save("D:\\pythonworkspace\\QuestionMaster20200907\\Question\\%s.docx" %str(Qno))
    tpl.save("D:\\pythonworkspace\\QuestionMaster20200907\\Question\\%s.docx" %(str(Qno)+"E"))
    tpl.save("D:\\pythonworkspace\\QuestionMaster20200907\\Question\\%s.docx" %(str(Qno)+"C"))
    # print("created")

# createWord(5000002)

def openWord(Qno): #打開已有word
    FileName=str(Qno)
    try:
        os.startfile("D:\\pythonworkspace\\QuestionMaster20200907\\Question\\%s.docx" %FileName)
        print("opened")
    except:
        print("404 Word Doc NOT FOUND")
# openWord(5000003)

def chooseWord(Qno, B, E, C): #揀開邊個Language 既ex, 介面左下click lang open 用
    Sum=int(B)+int(E)+int(C)
    QnoB=str(Qno)
    QnoE=str(Qno)+"E"
    QnoC=str(Qno)+"C"
    # print(Sum)
    if (Sum==0):
        print("405 CHOICE NOT FOUND")
    if (Sum==3):
        print("all")
        openWord(QnoB)
        openWord(QnoE)
        openWord(QnoC)
    if (Sum==1):
        print("print 1")
        if (B==1):
            openWord(QnoB)
        if (E==1):
            openWord(QnoE)
        if (C==1):
            openWord(QnoC)
    if (Sum==2):
        print("print 2")
        if (B==0):
            openWord(QnoE)
            openWord(QnoC)
        if (E==0):
            openWord(QnoB)
            openWord(QnoC)
        if (C==0):
            openWord(QnoB)
            openWord(QnoE)
    # print(Qno, B, E, C)



        
# chooseWord(5000002, 0, 1, 0)

def pdReadCsv(csvFile): #讀CSV
    pdDataFrame=pd.read_csv(newCSV)
    # print(len(pdDataFrame))<-----直接就係個len
    # print(pdDataFrame.iloc[0,0])<-----UID
    # print(pdDataFrame[0:1])
    # print(pdDataFrame.iloc[0,1])<----QID
    # print(pdDataFrame.loc[0])<------特定print個row, 以table 表示
    
    return pdDataFrame

# pdReadCsv(newCSV)

# def pdLatestUID(csvFile): #好似無用了
#     pdDataFrame=pd.read_csv(newCSV)
#     newUID=pdDataFrame.iloc[-1,0]+1
#     print(str(newUID))
#     return (str(newUID))


# def addNewRow(csvFile, list_of_element): #好似無用了
#     pdDataFrame=pd.read_csv(newCSV)
#     pdDataFrame=pdDataFrame.append(list_of_element, ignore_index=False)
#     print(pdDataFrame)
#     return

def createPdNewRowContent(csvFile, NameQID, Qtype): #呢個直接加特定Q, 再開埋
        
    oldDataFrame=pd.read_csv(newCSV)
    newUID = oldDataFrame.iloc[-1,0]+1
    newRow=[{"UID":newUID,"QID":NameQID, "QID_E":NameQID+"E", "QID_C":NameQID+"C", "QType":Qtype, "Difficulty":"Nan", "BiSpace":"Nan", "EnSpace":"Nan", "TcSpace":"Nan", "ExamPt1":"Nan", "ExamPt2":"Nan", "ExamPt3":"Nan"}]   
    oldDataFrame=oldDataFrame.append(newRow, sort=False , ignore_index=True)
    oldDataFrame.to_csv(csvFile,index=False)  

    createWord(NameQID)
    openWord(str(NameQID))
    time.sleep(2)
    openWord(str(NameQID)+"E")
    time.sleep(2)
    openWord(str(NameQID)+"C")
    return

# createPdNewRowContent(newCSV, "IB1990P1Q1", "LQ")



def AutoNewQ(csvFile): #UID+1 加Q, 再開埋
    DataFrame=pd.read_csv(csvFile)
    newUID = DataFrame.iloc[-1,0]+1
    newRow=[{"UID":newUID,"QID":str(newUID), "QID_E":str(newUID)+"E", "QID_C":str(newUID)+"C", "QType":"Normal", "Difficulty":"Nan", "BiSpace":"Nan", "EnSpace":"Nan", "TcSpace":"Nan", "ExamPt1":"Nan", "ExamPt2":"Nan", "ExamPt3":"Nan"}]   
    DataFrame=DataFrame.append(newRow, sort=False , ignore_index=True)
    DataFrame.to_csv(csvFile,index=False)  

    createWord(newUID)
    openWord(str(newUID))
    time.sleep(2)
    openWord(str(newUID)+"E")
    time.sleep(2)
    openWord(str(newUID)+"C")
    return

# AutoNewQ(newCSV)

def DelQ(csvFile,QNo): #Del Q, 特登唔del 條題目，必要時搵到
    DataFrame=pd.read_csv(csvFile)
    DataFrame = DataFrame[DataFrame.QID != QNo]
    DataFrame.to_csv(csvFile,index=False)  
    # 下面果段無用
    # for i in range(int(len(DataFrame))):
    #     if (DataFrame.iloc[i,1] != QID):
    #         print("Not Equal")

    #     else:
    #         print("Equal")
    return
# DelQ(newCSV, "5000009")


def searchQ(csvFile, Qno): # 利用非unique id search
    try:
        DataFrame=pd.read_csv(csvFile)
        target=DataFrame.loc[DataFrame['QID'] == Qno]

        #print(target)
        # print(target.iloc[0,0])
        # print(target.iloc[0,1])
        # print(target.iloc[:1,0:2])
        return [target.iloc[0,0], target.iloc[0,1]] # return 該題UID QID
    except IndexError: # 若搜尋出現ERROR, return 0 去 main 出error msg
        
        return 0

def searchQprop(csvFile, Qno):
    try:
        DataFrame=pd.read_csv(csvFile)
        target=DataFrame.loc[DataFrame['QID'] == Qno]
        print("searchQprop:")
        print(target)
        #print(target.iloc[0, 0])
        # print(target.iloc[0,0])
        # print(target.iloc[0,1])
        # print(target.iloc[:1,0:2])
        return [target.iloc[0]]
    except IndexError:
        
        print("404 index error")
    

    
# print(searchQ(newCSV, "5000002"))

def editQ(csvFile, Qno, Qtype, Difficulty, Bi, En, Tc):
    DataFrame=pd.read_csv(csvFile)
    DataFrame.loc[DataFrame['QID'] == Qno, 'QType']=Qtype
    DataFrame.loc[DataFrame['QID'] == Qno, 'Difficulty']=Difficulty
    DataFrame.loc[DataFrame['QID'] == Qno, 'BiSpace']=Bi
    DataFrame.loc[DataFrame['QID'] == Qno, 'EnSpace']=En
    DataFrame.loc[DataFrame['QID'] == Qno, 'TcSpace']=Tc
    DataFrame.to_csv(csvFile,index=False) 
    return

# print(editQ(newCSV, "5000003", "MC", "2", "5", "7", "11"))




# addNewRow(newCSV, createPdNewRowContent(newCSV, "MOMC9999", "MC"))

# def appendNewRow(csvFile):
#     pdDataFrame=pd.read_csv(newCSV)
#     pdDataFrame=pdDataFrame.append([{"UID":"newUID", "QID":"NewQID", "QID_E":"NewQIDE", "QID_C":"NewQIDC", "QType":"Qtype", "Difficulty":"Nan", "BiSpace":"Nan", "TcSpace":"Nan", "EnSpace":"Nan", "ExamPt1":"Nan", "ExamPt2":"Nan", "ExamPt3":"Nan"}], sort=False , ignore_index=True)
#     pdDataFrame.to_csv(newCSV, index=False)
#     return

# appendNewRow(newCSV)
# print(pdReadCsv(newCSV))
#----------------------------------------------------------

# def Readcsv(csvFile):
#     with open (csvFile, 'r')as csv_file:
#         csvReader=csv.reader(csv_file)
#         csvList=[]
#         for line in csvReader:
#             csvList.append(line)
#         return csvList #output 個list 出去
#         print(len(csvList))
#         # print(csvList[1][4])
#         # for line in csvReader:
#         #     print(line)

# def LatestUID(csvFile):
#     newUID=int(Readcsv(csvFile)[-1][0])+1
#     return (str(newUID))

# def addNewRow(csvFile, list_of_element):
#     with open (csvFile, 'a', newline="")as csv_file:
#         csvWriter = writer(csv_file)
#         csvWriter.writerow(list_of_element)
#         return

# def createNewRowContent(csvFile, NameQID, Qtype):
#     newUID = LatestUID(csvFile)
#     newRow=[newUID, NameQID, NameQID+"E", NameQID+"C", Qtype, "Nan", "Nan", "Nan", "Nan", "Nan", "Nan", "Nan"]
#     return newRow


# def autoNewRowContent(csvFile, Qtype):
#     newUID = LatestUID(csvFile)
#     newRow=[newUID, newUID, newUID+"E", newUID+"C", Qtype, "Nan", "Nan", "Nan", "Nan", "Nan", "Nan", "Nan"]
#     return newRow

# def QuestionRowContent(QID, Qtype, Difficulty, BiSpace, EnSpace, TcSpace, ExamPt1, ExamPt2, ExamPt3):
#     RowContent_woutUID=[QID, QID+"E", QID+"C", Qtype, Difficulty, BiSpace, EnSpace, TcSpace, ExamPt1, ExamPt2, ExamPt3]
#     return RowContent_woutUID



# def editRowContent(uid, rowContent):
#     uniqueID=[uid]
#     updatedRow=uniqueID+rowContent
#     return updatedRow

# def updatecsv(csvFile, newRow):
#     Qlist = Readcsv(csvFile)
#     print(Qlist)
#     for i in Qlist:
#         print(i)
#         print(i[0])
#         print(newRow[0])
#         print(i[0] == newRow[0])
#         if (i[0] == newRow[0]) :
#             i=newRow
#             print(i)
#             return print(Qlist)
           
            
    # print("No such data")
    # return Qlist



    






# print(updatecsv(newCSV, editRowContent("5000001", QuestionRowContent("test", "LQ", "2", "5", "7", "11", 123, 321, 1234567))))


# print(editRowContent("5000012", QuestionRowContent("test", "LQ", "2", "5", "7", "11", 123, 321, 1234567)))




# print(addNewRow(newCSV,autoNewRowContent(newCSV, "LQ")))

# addNewRow(newCSV,createNewRowContent(newCSV, "MO1234", "LQ"))

# print(LatestUID(newCSV))

# print(Readcsv(newCSV))

# print(addNewRow("D:\\pythonworkspace\\QuestionMaster20200907\\template\\QuestionMasterCSV.csv", "MO1234", "LQ"))


print("controlCSV is ready.")

# chooseWord("5000001", 1, 1, 1)