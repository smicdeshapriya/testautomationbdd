import os, glob
import sys
import shutil 
import datetime
import subprocess
import sqlite3
import csv
import random, string
import re
import psycopg2
import csvdiff
from shutil import copyfile
#import cx_Oracle
import time
from time import time
import xml.etree.ElementTree as ET
import inspect


#from __future__ import print_function
def retryPointClick(x,y,container):
    xErr=16
    xList=[0,1,2,3,4,5,6]
    for i in xList:
        mouseClick(container, x+xErr+i, y-1, 0, Qt.LeftButton)
        if waitFor("object.exists(':titlebar.cbxPin_QCheckBox')", 1000) ==True:
            break
        
            
    
    

def copyingFile():    
#     src='C://Users//indikade//Desktop//testCopy//abc.csv'
#     dst='C://Users//indikade//Desktop//testCopy2//'
    src=getDictValue(varDict,'SurvFilePath')
    src=src+'tradesForSG.csv'
    #src='C://Users//indikade//Desktop//Release//Dump_Ver-4//qaTest//tradesForSG.csv'
    dst='C://Users//indikade//Desktop//git_product//src//Product//suite_Surveillance//shared//testdata//SpreadGraph//'
#     print src
#     print dst
    if os.path.exists(dst+'tradesForSG.csv'):
        os.remove(dst+'tradesForSG.csv')
    
    shutil.copy(src,dst)
    
        

def dragNdrop(item, loc):
    dragAndDrop(waitForObject(item), 31, 14, loc, 160, 678, Qt.CopyAction)
    
    
def findColumn(header,container):
    index=waitForObjectExists("{container='"+container+"' text?='"+header+"' type='HeaderViewItem' visible='true'}").visualIndex
    return index

def getRowCount(object):
    rowCount=str(waitForObject(object).text)
    rowCount=rowCount.partition(":")
    print rowCount
    #rowCount.replace("Row Count : ","")
    test.log(rowCount[2])
    r= str.strip(rowCount[2])
    
    if r == "0":
        test.warning("No records found ...!")
        return rowCount[2]
    else:
        return rowCount[2]
        #pass
        #test.verify(rowCount[2]>0, "Testing Row Count")

def checkEmpty(obj,value):
    if not value:
        return test.fail("ChekEmptyFail | Object value empty or null...", str(obj))
    
#registering AUT in localhost by using given port
def registerAUT(aut,server,port):
    cmd="squishserver --verbose --config addAttachableAUT "+aut+" "+server+":"+port+""
    print cmd
    result=os.system(cmd)
    print result
    
    

def startApplicationAttachable(cmd,path):
    os.system(""+path+""+"\\"+cmd+"")

def getAppPath(command):
     output = subprocess.check_output(command, shell=True)
     print output
     return output
      
def queryDB(testDatabase,sqlString):
#     for record in testData.dataset("EnvironmentDetails/variableMap.csv"):
#         if testData.field(record, "SymbolicVariable")==:
        
    conn = sqlite3.connect(testDatabase)
    print "Opened database successfully";
    cursor = conn.cursor()
    try: 
        cursor.execute(sqlString)
#         cursor.execute(sqlString)
#         cursor.execute("SELECT fieldSet FROM AC"+sqlString)
        conn.commit()
        return cursor 
    except Exception,err:
        test.fail("Unexpected error in database operation", str(err))
    finally:
        print "Print data";
        #conn.close()
    

def csv2DB(dataFile,myCSV,sql1,sql2,fields):
    try:
        db_filename = dataFile
        #'D:\\TestDIR\\csv2db\\todo.db'
        data_filename = myCSV
        #sys.argv[1]
        
        #SQL1='''CREATE TABLE task(details text,priority text,status text,deadline text,project text);'''
        
        SQL2 = """insert into task(details, priority, status, deadline, project)
                 values (:details, :priority, 'active', :deadline, :project)
              """
        queryDB(db_filename,sql1)
        
        with open(data_filename, 'rt') as csv_file:
            next(csv_file)
            csv_reader = csv.reader(csv_file)            
            #csv_reader = csv.DictReader(csv_file)
            test.log(str(csv_reader))
            
            with sqlite3.connect(db_filename) as conn:
                cursor = conn.cursor()
                cursor.executemany(sql2, csv_reader)
            
        conn.commit()
        #conn.close()
    except Exception,err:
        test.fail("CSV to Database Conversion Error", str(err)) 
   
def DB2csv(dataFile,myCSV,sqlSelect,fieldSet):
    try:
        db_filename = dataFile
        #'D:\\TestDIR\\csv2db\\todo.db'
        data_filename = myCSV +".csv"
        test.log(str(myCSV))
        data=queryDB(db_filename,sqlSelect)
        with open(data_filename, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(fieldSet)
            writer.writerows(data) 
    except Exception, Err:
        test.fail("Database to CSV Conversion Error", str(Err))          
              
def compareTable(tableA,tableB):
    for row in tableA:
        numOfCols = testData.fieldNames(tableA[row]).length
        for col in numOfCols:
            if(testData.field(tableA[row],col)==testData.field(tableB[row],col)):
                test.log(testData.fieldNames(tableA[row])[col]+" values matching!")
            else:
                return false   
        return true

    
def compareCSV(csv1,csv2,id,path):
    try:
        print csv1
        print csv2
        #print path
        os.system("C:") 
        
        #output= os.system("csvdiff --style=summary "+id+"  \""+csv1+"\"  \""+csv2+"\"")
        output= os.system("csvdiff --style=pretty --output=\""+path+"\" "+id+"  \""+csv1+"\"  \""+csv2+"\"")
        
        #output= os.system("csvdiff --style=summary "+id+" \""+csv1+"\" \""+csv2+"\"")
        if output == 1 or output ==0:
            return output
            print output
        else:
            return output 
            print output 
        #os.system("csvdiff --style=pretty --output="+path+"/diff.json transact_time "+csv1+" "+csv2+"")
        #output= os.system("csvdiff --style=summary transact_time "+csv1+" "+csv2+"")
        #print output 
   
    except Exception,err:
        test.fail("CSV Comparision Fail:", str(err))

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))    
    
    
def ExportToCSV(filename,folder):
    
   
#     if  waitFor("object.exists(':_QMenu')", 5000)==True:        
#         activateItem(waitForObjectItem(":_QMenu", "Export To CSV"))
#         
#     else:    
#         clickButton(waitForObject(":ftmTableTitlebar.btnExportTable_QPushButton"))
        
    
    snooze(5)
    if waitFor("object.exists(':No Data_QMessageBox')", 2000) == True:
        testSettings.logScreenshotOnFail = True
        test.fail("No data returned for the query...!")
        testSettings.logScreenshotOnFail = False    
    else:
        try:        
            snooze(5)
            if waitFor("object.exists(':stackedWidget.listView_QListView_3')", 2000) == True:
                doubleClick(waitForObject(":stackedWidget.listView_QListView_3"))
            else:
                mouseClick(waitForObject(":stackedWidget.treeView_QTreeView_2"), 104, 125, 0, Qt.LeftButton)
                snooze(1)  
            
        except Exception, e:
            snooze(1)
            raise(e)
            
        finally:    
            mouseDrag(waitForObject(":Save File_Edit"), 85, 8, -107, 3, 1, Qt.LeftButton)       
            sendEvent("QKeyEvent", waitForObject(":Save File_Edit"), QEvent.KeyPress, 16777248, 0, 0, "", False, 1)        
            type(waitForObject(":Save File_Edit"), filename)
            snooze(1)        
            clickButton(waitForObject(":Save File.Save_Button"))
            if object.exists(':Save File_QMessageBox') == True:
                waitFor("object.exists(':Save File_QMessageBox')", 20000)
                test.compare(findObject(":Save File_QMessageBox").enabled, True)
                clickButton(waitForObject(":sp2WindowsView.Yes_QPushButton"))

                        
            
def setOderID(orderid):
    global myOrderID
    myOrderID=[]
    myOrderID.append(orderid)
    
    
    

def userLogin(username,password,env,language,loginAttempt,appName):  
     
    currentApplicationContext().detach()  
    tempList=[] 
    
    try:
         
        startApplication(appName)
        
        
#Added to override the 12072016 release dll missing issue >>>>>>>>
        #clickButton(waitForObject(":Warning.Yes_QPushButton"))
        #clickButton(waitForObject(":Warning.Yes_QPushButton"))
        #lickButton(waitForObject(":Warning.Yes_QPushButton"))
#<<<<<<<<                
        
        waitForObject("{name='editUserID' type='QLineEdit' visible='1' window=':LoginDialog_LoginDialog'}").clear()        
        mouseDrag(waitForObject(":LoginDialog.editUserID_QLineEdit"), 53, 14, -81, -2, 1, Qt.LeftButton)        
        type(waitForObject("{name='editUserID' type='QLineEdit' visible='1' window=':LoginDialog_LoginDialog'}"), username)        
        type(waitForObject(":LoginDialog.editUserID_QLineEdit"), "<Tab>")
        type(waitForObject(":LoginDialog.editPassword_QLineEdit"), password)        
        #looking for environment
        envCmb=waitForObject(":LoginDialog.cmbSystem_QComboBox")
        try:
            if envCmb.count <= 0:
                createNewEnv(env)
            else:                
                for index in range(envCmb.count):
                    #envCmb.itemText(index) != env:
                    envCmb.setCurrentIndex(index)
                    tempList.append(envCmb.currentText)                
                                                         
                if env not in tempList:
                    createNewEnv(env)
                    waitForObject("{name='editUserID' type='QLineEdit' visible='1' window=':LoginDialog_LoginDialog'}").clear()
                    type(waitForObject("{name='editUserID' type='QLineEdit' visible='1' window=':LoginDialog_LoginDialog'}"), username)
                #else:
                    #updateEnv(env)                    
                        
                                         
            mouseClick(waitForObject(":LoginDialog.cmbSystem_QComboBox"), 148, 8, 0, Qt.LeftButton)                                 
            mouseClick(waitForObjectItem(":LoginDialog.cmbSystem_QComboBox", env), 43, 5, 0, Qt.LeftButton)
            mouseClick(waitForObject(":LoginDialog.cmbLanguage_QComboBox"), 67, 13, 0, Qt.LeftButton)
            mouseClick(waitForObjectItem(":LoginDialog.cmbLanguage_QComboBox", language), 50, 9, 0, Qt.LeftButton)
            clickButton(waitForObject(":LoginDialog.btnLogin_QPushButton"))
    
    
            snooze(2)
            
            if waitFor("object.exists(':Pentagon_QMessageBox')", 3000) ==True:
                test.log("Login Failed for --"+username+"")
                return False         
            else:
                waitFor("object.exists(':frmStatusBarPanel.lbluser_QLabel')", 20000)
                test.compare(str(findObject(":frmStatusBarPanel.lbluser_QLabel").text), username)                          
                return True
        except Exception, err:
            test.fail("Exception in creating environment", str(err))                                 
                        
    except Exception, e:
        testSettings.logScreenshotOnFail = True
        test.fail("Exception in Login", str(e))
        testSettings.logScreenshotOnFail = False
        
        

#----------------------------------------------------------
def userLogin2(username,password,env,language,loginAttempt,appName):    
          
    try:        
         

        waitForObject("{name='editUserID' type='QLineEdit' visible='1' window=':LoginDialog_LoginDialog'}").clear()
        
        mouseDrag(waitForObject(":LoginDialog.editUserID_QLineEdit"), 53, 14, -81, -2, 1, Qt.LeftButton)
        
        type(waitForObject("{name='editUserID' type='QLineEdit' visible='1' window=':LoginDialog_LoginDialog'}"), username)        
        type(waitForObject(":LoginDialog.editUserID_QLineEdit"), "<Tab>")
        type(waitForObject(":LoginDialog.editPassword_QLineEdit"), password)        
        #looking for environment
        envCmb=waitForObject(":LoginDialog.cmbSystem_QComboBox")
        if envCmb.count <= 0:
            createNewEnv()
        elif envCmb.count > 0:                
            for index in range(envCmb.count):
                if envCmb.currentText != env:
                    createNewEnv()
                    waitForObject("{name='editUserID' type='QLineEdit' visible='1' window=':LoginDialog_LoginDialog'}").clear()
                    type(waitForObject("{name='editUserID' type='QLineEdit' visible='1' window=':LoginDialog_LoginDialog'}"), username)                    
                    break   
                
        mouseClick(waitForObject(":LoginDialog.cmbSystem_QComboBox"), 148, 8, 0, Qt.LeftButton)                                 
        mouseClick(waitForObjectItem(":LoginDialog.cmbSystem_QComboBox", env), 43, 5, 0, Qt.LeftButton)
        mouseClick(waitForObject(":LoginDialog.cmbLanguage_QComboBox"), 67, 13, 0, Qt.LeftButton)
        mouseClick(waitForObjectItem(":LoginDialog.cmbLanguage_QComboBox", language), 50, 9, 0, Qt.LeftButton)
        clickButton(waitForObject(":LoginDialog.btnLogin_QPushButton"))

        snooze(2)
        
        if waitFor("object.exists(':Pentagon_QMessageBox')", 3000) ==True:
            test.log("Login Failed for --"+username+"")
            return False           
         
        else:
            waitFor("object.exists(':frmStatusBarPanel.lbluser_QLabel')", 20000)
            test.compare(str(findObject(":frmStatusBarPanel.lbluser_QLabel").text), username)           
            return True                     
           
             
    except Exception, e:       
        raise Exception(e)
       
#----------------------------------------------------------        
            
       
def createEnv(env,fed,ipselmethod,certfile,ip,port):
    
      
    test.log("Details"+env+","+fed+","+ipselmethod+","+certfile+","+ip+","+port)
    
    currentApplicationContext().detach()
        
    
    startApplication("SurveillancePentagon")
    clickButton(waitForObject(":LoginDialog.btnSettings_QPushButton"))
    clickButton(waitForObject(":Settings.pushButton_2_QPushButton"))
    type(waitForObject(":Environment Name_QLineEdit"), env)
    clickButton(waitForObject(": .OK_QPushButton"))
    waitForObjectItem(":frame_2_QTreeWidget", "FED")
    clickItem(":frame_2_QTreeWidget", "FED", 54, 3, 0, Qt.LeftButton)
    type(waitForObject(":_QLineEdit"), fed)
    waitForObjectItem(":frame_2_QTreeWidget", "Sequential")
    clickItem(":frame_2_QTreeWidget", "Sequential", 93, 11, 0, Qt.LeftButton)
    mouseClick(waitForObject(":_QComboBox"), 75, 5, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":_QComboBox", ipselmethod), 82, 4, 0, Qt.LeftButton)
    waitForObjectItem(":frame_2_QTreeWidget", "_1")
    clickItem(":frame_2_QTreeWidget", "_1", 77, 9, 0, Qt.LeftButton)
    type(waitForObject(":_sp2::BrowseWidget"), certfile)   
    mouseClick(waitForObject(":_QLineEdit_2"), 76, 8, 0, Qt.LeftButton)
    type(waitForObject(":_QLineEdit_2"), certfile)
    waitForObjectItem(":frame_2_QTreeWidget", "IPs")
    clickItem(":frame_2_QTreeWidget", "IPs", -9, 17, 0, Qt.LeftButton)
    waitForObjectItem(":frame_2_QTreeWidget", "IPs.IP1")
    clickItem(":frame_2_QTreeWidget", "IPs.IP1", -9, 14, 0, Qt.LeftButton)
    waitForObjectItem(":frame_2_QTreeWidget", "IPs.IP1.")
    clickItem(":frame_2_QTreeWidget", "IPs.IP1.", 42, 9, 0, Qt.LeftButton)
    type(waitForObject(":_QLineEdit_2"), ip)   
    waitForObjectItem(":frame_2_QTreeWidget", "IPs.IP1.0")
    clickItem(":frame_2_QTreeWidget", "IPs.IP1.0", 38, 13, 0, Qt.LeftButton)
    sendEvent("QMouseEvent", waitForObject(":qt_spinbox_lineedit_QLineEdit"), QEvent.MouseButtonDblClick, 39, 12, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(":qt_spinbox_lineedit_QLineEdit"), QEvent.MouseButtonRelease, 39, 12, Qt.LeftButton, 0, 0)
    type(waitForObject(":_QSpinBox"), port)    
    clickButton(waitForObject(":Settings.pushButton_QPushButton"))
    clickButton(waitForObject(":Are you sure?.Yes_QPushButton"))
    clickButton(waitForObject(":LoginDialog.btnCancel_QPushButton"))            
            
def setDateTime():
    i = datetime.datetime.now()
    #dateFrom=str("%s%s%s"%(i.day, i.month, i.year))
    #print dateFrom
    #print (time.strftime("%H:%M:%S"))
    dateFrom= i.strftime('%d%m%Y')
    timeFrom= i.strftime('%H%M%S%f')
    print("date:"+dateFrom)
    print ("time:"+timeFrom)
    
    
    
def save_screenshot(obj_name, filename):
    widget = waitForObject(obj_name)
    # Create remote screenshot of the widget:
    img = grabWidget(widget)
    img.save(filename, "PNG")

    # Copy remote file to computer that is executing
    # this script/squishrunner:
    testData.get(filename)
    
 
def get_pids_for_title(window_title_excerpt):
    p = subprocess.Popen(
        #args=squishinfo.testCase + "/../windowlist",
        args="windowlist",
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    stdout = p.communicate()[0]
    last_pid = None
    pids = []
    for l in stdout.split("\r\n"):
        if l.startswith("PID: "):
            last_pid = l[5:]
            continue
        elif window_title_excerpt in l and not last_pid in pids:
            pids.append(last_pid)
    return pids                
            
#def send_orders():
    
#     import paramiko
#      
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(
#         paramiko.AutoAddPolicy())
#     client.connect('172.25.76.93', username='lseqa2', password='slse!!123')
#     stdin, stdout, stderr = client.exec_command('cd ~/ICON/bin;ls -a;./ITEStarter')
#     for line in stdout:
#           print '... ' + line.strip('\n')
#     client.close()
#         

def runITEScript(loc,cmdFile,filepath,sikuliScript):
   
    print "==================="
    print loc 
    print cmdFile 
    print filepath
    print sikuliScript
    print "==================="
    
    currentLocation=loc
    sikulixPath=filepath+"\\sikulix"
    javaPath= """C:\Program Files\Java\jdk1.7.0_79\\bin"""
    scriptPath=""+filepath+""+"\\"+sikuliScript+""
    space=" "
    print "**********************"
    print currentLocation
    print sikulixPath
    print javaPath
    print scriptPath
    
    
    print "testPath=" + ""+filepath+""+"\\"+cmdFile+""+space+""+currentLocation+""+space+""+sikulixPath+""+space+"\""+javaPath+"\""+space+""+scriptPath+""
    print "**********************"
    
    #os.system("D:\\Projects\\STAF\\GIT\\functional_automation\\Product\\Drop1\\suite_Surveillance_v1.0\\shared\\scripts\\global\\sikulix_scrpts\\iteTrades.cmd")
    os.system(""+filepath+""+"\\"+cmdFile+""+space+""+currentLocation+""+space+""+sikulixPath+""+space+"\""+javaPath+"\""+space+""+scriptPath+"")
    #snooze(10)
    return True
    #os.system("D:\\Projects\\STAF\\suite_SurveillanceWS5i3\\shared\\scripts\\global\\iteTest1.cmd")
    #javaPath="set path=C:\Program Files\Java\jdk1.7.0_79\bin"
    #sikulixPath="D:\Projects\STAF\GIT\functional_automation\Product\Drop1\suite_Surveillance_v1.0\shared\scripts\global\sikulix_scrpts\sikulix"
#     os.system(javaPath)
#     os.system("d:")
#     os.system("cd D:\Projects\STAF\GIT\functional_automation\Product\Drop1\suite_Surveillance_v1.0\shared\scripts\global\sikulix_scrpts\sikulix")
#     os.system("runsikulix.cmd -r "+filePath+"\\"+sikuliScript)
#     snooze(10)
#     
    
def setDifValue(original,custom):
    if original=="":
        original=custom
        return original    
    
def variableDict(source):
    #varDict={} 
    for record in testData.dataset(source):
        
        symbolicVar = testData.field(record, "SymbolicVariable")
        realVar = testData.field(record, "RealVariable")        
        varDict[symbolicVar]=realVar
    
def getDictValue(dictionary,x):
    #return dictionary[''+value+'']
    #a = adict.get('dogname', default)
    return dictionary.get(''+x+'',x)

def setDictValue(dictionary,item,value):
    dic={''+item+'':''+value+''}
    dictionary.update(dic)
    #snooze(1)

def multipleFilterProccessor(dict,filterVal,s):
    #print filterVal.split(separator)
    tempArray1=filterVal.split(s)
    tempArray2=[]
    print tempArray1
    #s=separator    
    for key in tempArray1:
        print key
        tempArray2.append(getDictValue(dict, key))
    print tempArray2
    return s.join(tempArray2)

def multipleFilterProccessorDecode(dict,filterVal,s):
    #print filterVal.split(separator)
    tempArray1=filterVal.split(s)
    tempArray2=[]
    print tempArray1
    #s=separator    
    for key in tempArray1:
        print key
        tempArray2.append(getDictValue(dict, key))
    return tempArray2
    #return s.join(tempArray2)

def createNewEnv(env):
    for record in testData.dataset("EnvironmentDetails/EnvDetails.csv"):
        
        envname = testData.field(record, "EnvName")
        if envname == env:
            fed = testData.field(record, "FED")
            ipselmethod = testData.field(record, "IPSelMethod")
            certfile = testData.field(record, "CertFile")
            ip = testData.field(record, "IP")
            port = testData.field(record, "Port")             
                
            clickButton(waitForObject(":LoginDialog.btnSettings_QPushButton"))
            clickButton(waitForObject(":Settings.pushButton_2_QPushButton"))
            type(waitForObject(":Environment Name_QLineEdit"), envname)
            clickButton(waitForObject(": .OK_QPushButton"))
            waitForObjectItem(":frame_2_QTreeWidget", "FED")
            clickItem(":frame_2_QTreeWidget", "FED", 38, 8, 0, Qt.LeftButton)
            type(waitForObject(":_QLineEdit_2"), fed)  
            waitForObjectItem(":frame_2_QTreeWidget", "_1")
            clickItem(":frame_2_QTreeWidget", "_1", 36, 17, 0, Qt.LeftButton)
            clickButton(waitForObject(":..._QPushButton"))
            try:        
                snooze(5)
                if waitFor("object.exists(':stackedWidget.treeView_QTreeView_3')", 2000) == True:
                    mouseClick(waitForObject("{column='0' container=':stackedWidget.treeView_QTreeView_3' text='Spatial2.cer' type='QModelIndex'}"))
                else:
                    mouseClick(waitForObject(":stackedWidget.listView_QListView_2"), 104, 125, 0, Qt.LeftButton)
                    snooze(1)  
                
            except Exception, e:            
                test.fail("Exception in certificate file", str(e))
    #         scrollTo(waitForObject(":_QScrollBar"), 2)
    #         waitForObjectItem(":stackedWidget.treeView_QTreeView_3", "Spatial2\\.cer")
    #         clickItem(":stackedWidget.treeView_QTreeView_3", "Spatial2\\.cer", 90, 9, 0, Qt.LeftButton)
    #         clickButton(waitForObject(":Open_QPushButton"))
    # 
    #         waitForObjectItem(":stackedWidget.listView_QListView_2", "Spatial2\\.cer")
    #         clickItem(":stackedWidget.listView_QListView_2", "Spatial2\\.cer", 41, 8, 0, Qt.LeftButton)
            sendEvent("QMouseEvent", waitForObject(":Open_QPushButton"), QEvent.MouseButtonPress, 16, 8, Qt.LeftButton, 1, 0)
            sendEvent("QMouseEvent", waitForObject(":Open_QPushButton"), QEvent.MouseButtonRelease, 16, 8, Qt.LeftButton, 0, 0)
            waitForObjectItem(":frame_2_QTreeWidget", "IPs")
            clickItem(":frame_2_QTreeWidget", "IPs", -11, 7, 0, Qt.LeftButton)
            waitForObjectItem(":frame_2_QTreeWidget", "IPs.IP1")
            clickItem(":frame_2_QTreeWidget", "IPs.IP1", -12, 7, 0, Qt.LeftButton)
            waitForObjectItem(":frame_2_QTreeWidget", "IPs.IP1.")
            clickItem(":frame_2_QTreeWidget", "IPs.IP1.", 19, 12, 0, Qt.LeftButton)
            type(waitForObject(":_QLineEdit_2"), ip)    
            waitForObjectItem(":frame_2_QTreeWidget", "IPs.IP1.0")
            clickItem(":frame_2_QTreeWidget", "IPs.IP1.0", 26, 17, 0, Qt.LeftButton)
            type(waitForObject(":_QSpinBox"), port)   
            waitForObjectItem(":frame_2_QTreeWidget", "Secure Communication")
            clickItem(":frame_2_QTreeWidget", "Secure Communication", -12, 11, 0, Qt.LeftButton)
            waitForObjectItem(":frame_2_QTreeWidget", "Secure Communication.Enable")
            clickItem(":frame_2_QTreeWidget", "Secure Communication.Enable", 9, 14, 0, Qt.LeftButton)
            waitForObjectItem(":frame_2_QTreeWidget", "Secure Communication.false_1")
            clickItem(":frame_2_QTreeWidget", "Secure Communication.false_1", 46, 9, 0, Qt.LeftButton)
            clickButton(waitForObject(":_QCheckBox"))
            sendEvent("QWheelEvent", waitForObject(":_QCheckBox"), 118, 2, -120, 0, 2)
            sendEvent("QWheelEvent", waitForObject(":frame_2_QTreeWidget"), 252, 327, -120, 0, 2)
            clickButton(waitForObject(":Settings.pushButton_QPushButton"))
            clickButton(waitForObject(":Are you sure?.Yes_QPushButton"))
            break
        else:
            continue
        
            
def  updateEnv(env):
#enabling secure communication option
    clickButton(waitForObject(":LoginDialog.btnSettings_QPushButton"))
    waitForObjectItem(":frame.treeWidget_QTreeWidget", env)
    clickItem(":frame.treeWidget_QTreeWidget", env, 20, 11, 0, Qt.LeftButton)
    waitForObjectItem(":frame_2_QTreeWidget", "Secure Communication")
    clickItem(":frame_2_QTreeWidget", "Secure Communication", -12, 15, 0, Qt.LeftButton)
    waitForObjectItem(":frame_2_QTreeWidget", "Secure Communication.Enable")
    clickItem(":frame_2_QTreeWidget", "Secure Communication.Enable", 48, 13, 0, Qt.LeftButton)

    if  waitFor("object.exists(':Secure Communication.true_QModelIndex_2')", 5000)==True:
        if waitForObject(":Secure Communication.true_QModelIndex_2").text=="true":
            test.log("Communication Secure")
        elif  waitForObject(":Secure Communication.true_QModelIndex_2").text=="false":           
            waitForObjectItem(":frame_2_QTreeWidget", "Secure Communication.false_1")
            clickItem(":frame_2_QTreeWidget", "Secure Communication.false_1", 87, 15, 0, Qt.LeftButton)
            clickButton(waitForObject(":_QCheckBox"))

#     waitForObjectItem(":frame_2_QTreeWidget", "Secure Communication.true")
#     clickItem(":frame_2_QTreeWidget", "Secure Communication.true", 22, 15, 0, Qt.LeftButton)    
#     clickButton(waitForObject(":_QCheckBox"))
    clickButton(waitForObject(":Settings.pushButton_QPushButton"))
    clickButton(waitForObject(":Are you sure?.Yes_QPushButton"))

    

def searchSome(something,line):
    
    searchObj = re.search( r''+something+'', line, re.M|re.I)
    if searchObj:
       print "search --> searchObj.group() : ", searchObj.group()
       return True
    else:
       print "Nothing found!!"
       return False

def absFilePath(relPath):
    path= os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', relPath))
    #print path
    #print os.getcwd()
    return path

def createFile(path):
    if not os.path.exists('SurvFilePath'):
       os.makedirs('SurvFilePath')

def removeFiles(path,fileType):
    myPath=absFilePath(path)
    files=myPath+"\\"+fileType
    #os.chdir(myPath)
    filelist = glob.glob(files)
    if not filelist:
        errorMsg = "Info: %s files not found in %s path" % (fileType,myPath)   
        return errorMsg
    else:
        for f in filelist:
            os.remove(f)
   
def extractDateTime(sdate,edate):
    
    myList=[]
    
    sdate=sdate.split("-")
    print sdate
    s1= ''.join(sdate[0])
    sd=s1.split("/")
    sd= ''.join(reversed(sd)) 
    print sd 
    myList.append(sd) 
   
    s2= ''.join(sdate[1])
    st=s2.split(":")
    st= ''.join(st) 
    st=st.split(".")
    st= ''.join(st) 
    print st
    myList.append(st)
    
    edate=edate.split("-")
    print edate
    e1= ''.join(edate[0])
    ed=e1.split("/")
    ed= ''.join(reversed(ed)) 
    print ed    
    myList.append(ed)
    
    e2= ''.join(edate[1])
    et=e2.split(":")
    et= ''.join(et) 
    et=et.split(".")
    et= ''.join(et) 
    print et
    myList.append(et)
    
    return myList
    

#connect to postgreSql

def connectPostgreSQL(sql): 
    
    envDetails=setEnvDetailsBGTest()     
    host=str(envDetails[0])
    username=str(envDetails[2])
    password='mit_0987'
    port='10999'
    
     
    # Try to connect
    conn=""
    try:
        conn=psycopg2.connect(database=username, user=username, password=password, host=host, port=port, sslmode='disable')
        print conn
    except:
        print "I am unable to connect to the database."
         
    try:
        
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Exception,err:
        test.log("psql execution failed... ",err)
        
      
#     rows = cur.fetchall()
#     print "\nRows: \n"
#     for row in rows:
#         print " ",row[0],"  ",row[1],"  ",row[2] 

def os_capture(args, cwd=None):
    if cwd is None:
        cwd = os.getcwd()
    proc = subprocess.Popen(
        args=args,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    stdout = proc.communicate()[0]
  
    return stdout, proc.returncode

def filterIntegerFromString(text):
     rowcount     = __builtin__.int(''.join(x for x in text if x.isdigit()))
     #return rowcount
     print rowcount
     
     
def connectToOracle():
    
    # connect via SQL*Net string or by each segment in a separate argument
    #connection = cx_Oracle.connect("user/password@TNS")
    connection = cx_Oracle.connect("s5surv22surv", "s5surv22surv", "172.25.83.134:1521/ora12c")
    
    cursor = connection.cursor()
    cursor.execute(""" select * from alert_reports """)
    
    for row in cursor:
        print row[0], "-", row[1]
        
    connection.close()
    
def connectToOracleUpdated(envName):
    
    for record in testData.dataset("EnvironmentDetails/DatabaseConnectionDetails.csv"):
        environment = testData.field(record, "Environment")
        databasename = testData.field(record, "DatabaseName")
        databasepwd = testData.field(record, "DatabasePWD")
        databaseip = testData.field(record, "DatabaseIP")
    
        if environment == envName:
             connection = cx_Oracle.connect(databasename, databasepwd, databaseip+":1521/ora12c")
             print "Database connected"
             break
         
def databaseQuery(envName,qeury):
            
        for record in testData.dataset("EnvironmentDetails/DatabaseConnectionDetails.csv"):
             environment = testData.field(record, "Environment")
             databasename = testData.field(record, "DatabaseName")
             databasepwd = testData.field(record, "DatabasePWD")
             databaseip = testData.field(record, "DatabaseIP")
     
             if environment == envName:
                  connection = cx_Oracle.connect(databasename, databasepwd, databaseip+":1521/ora12c")
                  print "Database connected"
                  #time.sleep(5)
                  break
              
        #connection = cx_Oracle.connect("s5surv5surv", "s5surv5surv", "172.25.83.134:1521/ora12c")    
        #connectToOracleUpdated("s5surv5")
        cursor = connection.cursor()
        sql=qeury
        #sql="select * from alert_reports"
        cursor.execute(sql)
        
        #outputList = {}
        outputList = []
        
        for row in cursor:
             outputList.append(row)
             #outputList.update(row)
             print row
        
        return outputList
        
        connection.close()
    
def setOrderFilterValuesToDict(dict):
    clientId=waitForObjectExists(":frmFilterHolder.txtClientID_QLineEdit_2").displayText
    firmId=waitForObjectExists(":frmFilterHolder.txtFirmID_QLineEdit").displayText
    Trader=waitForObjectExists(":frmFilterHolder.txtTraderID_QLineEdit").displayText
    Side=waitForObjectExists(":frmFilterHolder.cmbSide_QComboBox_2").currentText
    OrderType=waitForObjectExists(":frmFilterHolder.cmbOrderType_QComboBox").currentText
    orderId=waitForObjectExists(":frmFilterHolder.txtOrderID_QLineEdit_2").displayText      
    orderStatus=waitForObjectExists(":frmFilterHolder.cmbOrderStatus_QComboBox_2").currentText   
    tradeRepId=waitForObjectExists(":frmFilterHolder.txtTradeReportID_QLineEdit").displayText
    setDictValue(dict,'firmId',str(firmId))
    setDictValue(dict,'clientId',str(clientId))
    setDictValue(dict,'Trader',str(Trader))
    setDictValue(dict,'Side',str(Side))
    setDictValue(dict,'OrderType',str(OrderType))
    setDictValue(dict,'orderId',str(orderId))
    setDictValue(dict,'orderStatus',str(orderStatus))
    setDictValue(dict,'tradeRepId',str(tradeRepId))
   
def setEnvDetailsBGTest():
    
    for record in testData.dataset("EnvironmentDetails/LoginDetails.csv"):
        password = testData.field(record, "password")
        environment = testData.field(record, "environment")  
    
        host = ''
        portEnv = ''
        loggedEnv = environment
        pwd = password
        envDetails=[]
        
        for record in testData.dataset("EnvironmentDetails/EnvDetails.csv"):
            envname = testData.field(record, "EnvName")
            ip = testData.field(record, "IP")
            port = testData.field(record, "Port")
            
            if envname == loggedEnv:
                host = ip
                portEnv = port
                
                print host, portEnv, loggedEnv, pwd
                #break
        
        if environment == ' ':
             pass
        else:
            envDetails.append(host)
            envDetails.append(portEnv)
            envDetails.append(loggedEnv)
            envDetails.append(pwd)
            return envDetails
            break
        
        
        #print host, portEnv, username, pwd
       

def xmlUpdater(newsfile,element,value,atrib,atribProp,atribValue):
#     dir = os.path.abspath(inspect.stack()[0][1])
#     dir=dir.replace('scripts\commonMethods.py','')
#     print dir    
#     filename = dir+'testdata\\NewsData\\'+newsfile+''  
#     print filename   
#     i = datetime.datetime.now()
#     idate = i.strftime('%Y%m%d')
#     itime = i.strftime('%H%M')
#     print idate
#     print itime
#     
#     DateAndTime=idate+'T'+itime
    
    tree = ET.parse(newsfile)
    root = tree.getroot()
    for node in root.iter(element):
            #if atrib != '' and element == 'FormalName':
            if atrib != '':
                if node.attrib[atrib]==atribProp:
                    node.text=atribValue                           
            else:
                node.text = str(value)    

    tree.write(newsfile,xml_declaration=True, method='xml', encoding='UTF-8')

def copyNewsFile(newsfile,filePath,remoteNewsPath):
    
    try:
        
        #get news file & path for local
        #newsFile=context.userData[0]
        #localPath=context.userData[1]
        #test.log(localPath)
        
        
        #alter news file name
        newsfile=newsfile.replace('.xml','_'+randomword(3)+'.xml')
        #context.userData[0]=newsfile
            
        #get news file path for remote server
        remoteNewsPath=multipleFilterProccessor(varDict,remoteNewsPath,'|')
        #append file
        remoteNewsPath=remoteNewsPath+newsfile
        test.log(remoteNewsPath)
        
        
        #Transfer News File
        #file='C:\\Users\\indikade\\Desktop\\git_product\\src\\Product\\suite_Surveillance\\shared\\testdata\\NewsData\\28_01_01_both.xml'
        #fileTransfer(file,"/x01/s5surv23/data/NewsData/28_01_01_both.xml")
        fileTransfer(filePath,remoteNewsPath)
        fileTransfer2Surv4(filePath,newsfile)
        
    #     dir = os.path.abspath(inspect.stack()[0][1])
    #     dir=dir.replace('scripts\commonMethods.py','')
    #     print dir    
    #     filename = dir+'testdata\\NewsData\\'+newsfile+''  
    #     print filename 
    except Exception,err:
        test.fail("News upload to remote location Fails", str(err))
   
   
def main():
    print "Main Running..."
    file="28_01_both.xml"
    #xmlUpdater(file,'FormalName','xxxx')
    xmlUpdater(file,'FormalName','00000','Scheme','ISIN','ppgggppp')
    #connectToOracle()
    #connectToOracle2("s5surv5")
    #setEnvDetailsBGTest()
    #copyingFile()
    #fileCopy()
    #connectToOracle()
    #printLogToFile()
    #filterIntegerFromString('Haaziq : 123')
    #connectPostgreSQL()
#     stdout, exit_code = os_capture("pip")
#     print stdout, exit_code
    #test.compare(exit_code, 0, "Expected exit code: 0")
    #test.verify(stdout.find("some expected substring") != -1, "Expected to find: 'some expected substring'")
    
    #connectPostgreSQL()
    #searchSome("abc","aaaabcddd")
    #extractDateTime("2016/08/12-10:32:49.896","2016/08/13-11:33:49.996")
#     duration="2016/08/12-10:32:49.896"    
#     duration=duration.split("-")    
#     print duration  
#     
#     s= ''.join(duration[0])
#     k=s.split("/")
#     print k
#     k= ''.join(k) 
#     print k 
   
   
         
if __name__ == "__main__": main()    
