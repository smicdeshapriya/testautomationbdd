# -*- coding: utf-8 -*-
import __builtin__
import os
import sys
from os import listdir
from os.path import join
import csv

source(findFile("scripts", "commonMethods.py")) 
source(findFile("scripts", "winSquishServer.py"))

# @Step("user click on 'Trades' menu Item")
# def step(context):
#     clickButton(waitForObject(":titlebar.btnMainMenu_QPushButton"))
#     activateItem(waitForObjectItem(":mainMenu_QMenu", "Trades"))
    
@Given("user click on Trades icon")
def step(context):
    mouseClick(waitForObject(":graphicsView_QGraphicsItem_2"), 118, 67, 0, Qt.LeftButton)

@Then("user should navigate to 'Trades' tab window")
def step(context):
    waitFor("object.exists(':Trades_TabItem')", 20000)
    test.compare(findObject(":Trades_TabItem").type, "TabItem")
    test.compare(findObject(":Trades_TabItem").text, "Trades")
    

@Then("trade filter fields should be located in left vertical pane")
def step(context):
    waitFor("object.exists(':scrollAreaWidget.frmFilterHolder_QFrame')", 20000)
    test.compare(findObject(":scrollAreaWidget.frmFilterHolder_QFrame").enabled, True)
    test.compare(findObject(":scrollAreaWidget.frmFilterHolder_QFrame").visible, True)
    sendEvent("QMouseEvent", waitForObject(":scrollAreaWidget.frmFilterHolder_QFrame"), QEvent.MouseMove, 833, 261, Qt.NoButton, 1, 0)

@Then("trade generic display pane should be in right upper pane")
def step(context):
    waitFor("object.exists(':splitTableAndGraph.Trades_sp2::SpatialTableView')", 20000)
    test.compare(findObject(":splitTableAndGraph.Trades_sp2::SpatialTableView").visible, True)
    test.compare(findObject(":splitTableAndGraph.Trades_sp2::SpatialTableView").enabled, True)

@Then("trade graphs pane should be in right lower pane")
def step(context):
    waitFor("object.exists(':frmLineChartView.frmLineChartPH_QFrame')", 20000)
    test.compare(findObject(":frmLineChartView.frmLineChartPH_QFrame").visible, True)
    test.compare(findObject(":frmLineChartView.frmLineChartPH_QFrame").enabled, True)
    sendEvent("QMouseEvent", waitForObject(":frmLineChartView.frmLineChartPH_QFrame"), QEvent.MouseMove, 530, -570, Qt.NoButton, 1, 0)
    
    


@When("user right click on Trades tab and select dockable")
def step(context):
    openContextMenu(waitForObject(":sp2WindowsView_QTabBar"), 27, 14, 0)
    activateItem(waitForObjectItem(":_QMenu", "Dockable"))



@Step("user click on trade filter Clear button")
def step(context):
    clickButton(waitForObject(":frmBtnPanel.btnClear_QPushButton"))

@When("user fill trade filters using '|any|'")
def step(context, filters):
         for record in testData.dataset(filters):
             instrument = testData.field(record, "Instrument")
             exectype = testData.field(record, "ExecType")
             tradetype = testData.field(record, "TradeType")
             tradesubtype = testData.field(record, "TradeSubType")
             buytrader = testData.field(record, "BuyTrader")
             tradeoperator = testData.field(record, "TradeOperator")
             selltrader = testData.field(record, "SellTrader")
             buyfirm = testData.field(record, "BuyFirm")
             firmoperator = testData.field(record, "FirmOperator")
             sellfirm = testData.field(record, "SellFirm")
             buyclient = testData.field(record, "BuyClient")
             clientoperator = testData.field(record, "ClientOperator")
             sellclient = testData.field(record, "SellClient")
             tradeprice_from = testData.field(record, "TradePrice:From")
             tradeprice_to = testData.field(record, "TradePrice:To")
             tradesize_from = testData.field(record, "TradeSize:From")
             tradesize_to = testData.field(record, "TradeSize:To")
             customfilter = testData.field(record, "CustomFilter")
             tradelinkid = testData.field(record, "TradeLinkId")
             tradereportid = testData.field(record, "TradeReportId")
             date_from = testData.field(record, "Date:From")
             date_to = testData.field(record, "Date:To")
             time_from = testData.field(record, "Time:From")
             time_to = testData.field(record, "Time:To")
          
              
         mouseClick(waitForObject(":frmFilterHolder.txtInstrumentID_QLineEdit"), 83, 12, 0, Qt.LeftButton)
         type(waitForObject(":frmFilterHolder.txtInstrumentID_QLineEdit"), instrument)
         mouseClick(waitForObject(":frmFilterHolder.cmbExecType_QComboBox"), 59, 10, 0, Qt.LeftButton)
         mouseClick(waitForObjectItem(":frmFilterHolder.cmbExecType_QComboBox", str(exectype)), 23, 10, 0, Qt.LeftButton)
         mouseClick(waitForObject(":frmFilterHolder.cmbTradeType_QComboBox"), 89, 8, 0, Qt.LeftButton)
         mouseClick(waitForObjectItem(":frmFilterHolder.cmbTradeType_QComboBox", str(tradetype)), 49, 10, 0, Qt.LeftButton)
         mouseClick(waitForObject(":frmFilterHolder.cmbTradeSubType_QComboBox"), 79, 16, 0, Qt.LeftButton)
         mouseClick(waitForObjectItem(":frmFilterHolder.cmbTradeSubType_QComboBox", str(tradesubtype)), 27, 14, 0, Qt.LeftButton)
              
         mouseClick(waitForObject(":gbxTraderID.txtBuyTrader_QLineEdit"), 69, 13, 0, Qt.LeftButton)
         clickButton(waitForObject(":gbxTraderID.btnBuyTraderSelector_QPushButton"))
         mouseClick(waitForObject(":gbxTraderID.txtBuyTrader_QLineEdit"), 114, 8, 0, Qt.LeftButton)
         type(waitForObject(":gbxTraderID.txtBuyTrader_QLineEdit"), buytrader)
         mouseClick(waitForObject(":gbxTraderID.cmbTraderOperator_QComboBox"), 117, 13, 0, Qt.LeftButton)
         mouseClick(waitForObject(":gbxTraderID.txtSellTrader_QLineEdit"), 86, 14, 0, Qt.LeftButton)
         type(waitForObject(":gbxTraderID.txtSellTrader_QLineEdit"), selltrader)
         
         mouseClick(waitForObject(":gbxFirmID.txtBuyFirm_QLineEdit"), 39, 23, 0, Qt.LeftButton)
         type(waitForObject(":gbxFirmID.txtBuyFirm_QLineEdit"), buyfirm)
         mouseClick(waitForObject(":gbxFirmID.txtBuyFirm_QLineEdit"), 119, 9, 0, Qt.LeftButton)
         mouseClick(waitForObject(":gbxFirmID.txtSellFirm_QLineEdit"), 28, 12, 0, Qt.LeftButton)
         mouseClick(waitForObject(":gbxFirmID.cmbFirmOperator_QComboBox"), 30, 15, 0, Qt.LeftButton)
         mouseClick(waitForObject(":gbxFirmID.txtSellFirm_QLineEdit"), 67, 15, 0, Qt.LeftButton)
         type(waitForObject(":gbxFirmID.txtSellFirm_QLineEdit"), sellfirm)
         
         mouseClick(waitForObject(":gbxClientID.txtBuyClient_QLineEdit"), 60, 14, 0, Qt.LeftButton)
         type(waitForObject(":gbxClientID.txtBuyClient_QLineEdit"), buyclient)
         mouseClick(waitForObject(":gbxClientID.cmbClientOperator_QComboBox"), 47, 18, 0, Qt.LeftButton)
         mouseClick(waitForObject(":gbxClientID.txtSellClient_QLineEdit"), 48, 20, 0, Qt.LeftButton)
         type(waitForObject(":gbxClientID.txtSellClient_QLineEdit"), sellclient)
         
         mouseClick(waitForObject(":gbxTradePrice.txtTradePriceFrom_QLineEdit"), 76, 10, 0, Qt.LeftButton)
         type(waitForObject(":gbxTradePrice.txtTradePriceFrom_QLineEdit"), tradeprice_from)    
         mouseClick(waitForObject(":gbxTradePrice.txtTradePriceTo_QLineEdit"), 87, 9, 0, Qt.LeftButton)
         type(waitForObject(":gbxTradePrice.txtTradePriceTo_QLineEdit"), tradeprice_to)  
           
         mouseClick(waitForObject(":gbxTradeSize.txtTradeSizeFrom_QLineEdit"), 86, 12, 0, Qt.LeftButton)
         type(waitForObject(":gbxTradeSize.txtTradeSizeFrom_QLineEdit"), tradesize_from)    
         mouseClick(waitForObject(":gbxTradeSize.txtTradeSizeTo_QLineEdit"), 56, 14, 0, Qt.LeftButton)
         type(waitForObject(":gbxTradeSize.txtTradeSizeTo_QLineEdit"), tradesize_to)
         
         mouseClick(waitForObject(":frmFilterHolder.cmbCustomFilter_QComboBox_2"), 94, 12, 0, Qt.LeftButton)
         mouseClick(waitForObject(":frmFilterHolder.txtTradeReportLinkID_QLineEdit"), 29, 21, 0, Qt.LeftButton)
         type(waitForObject(":frmFilterHolder.txtTradeReportLinkID_QLineEdit"), tradelinkid)
         mouseClick(waitForObject(":frmFilterHolder.txtTradeReportID_QLineEdit_2"), 38, 11, 0, Qt.LeftButton)
         type(waitForObject(":frmFilterHolder.txtTradeReportID_QLineEdit_2"), tradereportid)
         
         mouseClick(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_5"), 65, 14, 0, Qt.LeftButton)
         sendEvent("QMouseEvent", waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_5"), QEvent.MouseButtonPress, 13, 17, Qt.LeftButton, 1, 0)
         sendEvent("QMouseEvent", waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_5"), QEvent.MouseButtonRelease, 8, 15, Qt.LeftButton, 0, 0)
         mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_5"), 18, 13, -20, 0, 1, Qt.LeftButton)
         type(waitForObject(":gbxDuration.dtFromDurationDate_QDateEdit_2"), date_from)    
         mouseClick(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_6"), 14, 17, 0, Qt.LeftButton)
         type(waitForObject(":gbxDuration.dtFromDurationTime_QTimeEdit_2"), time_from)    
         mouseClick(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_7"), 12, 9, 0, Qt.LeftButton)
         mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_7"), 19, 8, -40, -1, 1, Qt.LeftButton)
         type(waitForObject(":gbxDuration.dtToDurationDate_QDateEdit_2"), date_to)    
         mouseClick(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_8"), 7, 8, 0, Qt.LeftButton)   
         type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), time_to)
         clickButton(waitForObject(":frmBtnPanel.btnApply_QPushButton"))
     

@Step ("user apply instrument filter values of '([^']*)','([^']*)','([^']*)','([^']*)'", regexp=True)
def step(context, Instrument, ExecTypes,TradeTypes,TradeSubTypes):
    if(Instrument !=""):
        Instrument=Instrument.replace(",","|")
        Instrument=multipleFilterProccessor(varDict,Instrument,'|')  
        mouseClick(waitForObject(":frmFilterHolder.txtInstrumentID_QLineEdit"), 34, 6, 0, Qt.LeftButton)
        type(waitForObject(":frmFilterHolder.txtInstrumentID_QLineEdit"), Instrument)
    if(ExecTypes !=""):    
        ExecTypes=ExecTypes.split(",")
        for ExecType in ExecTypes:
            mouseClick(waitForObject(":frmFilterHolder.cmbExecType_QComboBox"), 55, 14, 0, Qt.LeftButton)
            mouseClick(waitForObjectItem(":frmFilterHolder.cmbExecType_QComboBox", ExecType), 16, 9, 0, Qt.LeftButton)
    if(TradeTypes !=""):
        TradeTypes=TradeTypes.split(",")
        for TradeType in TradeTypes:    
            #mouseClick(waitForObject(":splitTableAndGraph.Trades_sp2::SpatialTableView"), 25, 92, 0, Qt.LeftButton)
            mouseClick(waitForObject(":frmFilterHolder.cmbTradeType_QComboBox"), 158, 6, 0, Qt.LeftButton)
            mouseClick(waitForObjectItem(":frmFilterHolder.cmbTradeType_QComboBox", TradeType), 11, 7, 0, Qt.LeftButton)
    if(TradeSubTypes !=""):
        TradeSubTypes=TradeSubTypes.split(",")
        for TradeSubType in TradeSubTypes:        
            #mouseClick(waitForObject(":splitTableAndGraph.Trades_sp2::SpatialTableView"), 25, 97, 0, Qt.LeftButton)
            mouseClick(waitForObject(":frmFilterHolder.cmbTradeSubType_QComboBox"), 179, 12, 0, Qt.LeftButton)
            mouseClick(waitForObjectItem(":frmFilterHolder.cmbTradeSubType_QComboBox", TradeSubType), 16, 11, 0, Qt.LeftButton)
    
@When("user apply trader filter values of '([^']*)','([^']*)','([^']*)'", regexp=True)
def step(context, BuyTrader, TradeOperator, SellTrader):
                           
    mouseClick(waitForObject(":gbxTraderID.txtBuyTrader_QLineEdit"), 69, 13, 0, Qt.LeftButton)
    #clickButton(waitForObject(":gbxTraderID.btnBuyTraderSelector_QPushButton"))
    if(BuyTrader !=""):
        BuyTrader=BuyTrader.replace(",","|")  
        BuyTrader=multipleFilterProccessor(varDict,BuyTrader,'|') 
        mouseClick(waitForObject(":gbxTraderID.txtBuyTrader_QLineEdit"), 114, 8, 0, Qt.LeftButton)
        type(waitForObject(":gbxTraderID.txtBuyTrader_QLineEdit"), BuyTrader)
        
    if(TradeOperator !=""):
        mouseClick(waitForObject(":gbxTraderID.cmbTraderOperator_QComboBox"), 251, 7, 0, Qt.LeftButton)
        mouseClick(waitForObjectItem(":gbxTraderID.cmbTraderOperator_QComboBox", TradeOperator), 83, 9, 0, Qt.LeftButton)

    if(SellTrader !=""):
        SellTrader=SellTrader.replace(",","|") 
        SellTrader=multipleFilterProccessor(varDict,SellTrader,'|') 
        mouseClick(waitForObject(":gbxTraderID.txtSellTrader_QLineEdit"), 86, 14, 0, Qt.LeftButton)
        type(waitForObject(":gbxTraderID.txtSellTrader_QLineEdit"), SellTrader)

@When("user apply firm filter values of '([^']*)','([^']*)','([^']*)'", regexp=True)
def step(context, BuyFirm, FirmOperator, SellFirm):
    if(BuyFirm !=""):
        BuyFirm=BuyFirm.replace(",","|")
        BuyFirm=multipleFilterProccessor(varDict,BuyFirm,'|')  
        mouseClick(waitForObject(":gbxFirmID.txtBuyFirm_QLineEdit"), 39, 23, 0, Qt.LeftButton)
        type(waitForObject(":gbxFirmID.txtBuyFirm_QLineEdit"), BuyFirm)
    
    if(FirmOperator !=""):
        mouseClick(waitForObject(":gbxFirmID.cmbFirmOperator_QComboBox"), 247, 8, 0, Qt.LeftButton)
        mouseClick(waitForObjectItem(":gbxFirmID.cmbFirmOperator_QComboBox", FirmOperator), 23, 11, 0, Qt.LeftButton)     
    
    if(SellFirm !=""):
        SellFirm=SellFirm.replace(",","|")
        SellFirm=multipleFilterProccessor(varDict,SellFirm,'|')
        mouseClick(waitForObject(":gbxFirmID.txtSellFirm_QLineEdit"), 67, 15, 0, Qt.LeftButton)
        type(waitForObject(":gbxFirmID.txtSellFirm_QLineEdit"), SellFirm)


@When("user apply client filter values of '([^']*)','([^']*)','([^']*)'", regexp=True)
def step(context, BuyClient, ClientOperator, SellClient):
    if(BuyClient !=""):
        BuyClient=BuyClient.replace(",","|")
        BuyClient=multipleFilterProccessor(varDict,BuyClient,'|')
        mouseClick(waitForObject(":gbxClientID.txtBuyClient_QLineEdit"), 60, 14, 0, Qt.LeftButton)
        type(waitForObject(":gbxClientID.txtBuyClient_QLineEdit"), BuyClient)
        
    if(ClientOperator !=""):        
        mouseClick(waitForObject(":gbxClientID.cmbClientOperator_QComboBox"), 248, 6, 0, Qt.LeftButton)
        mouseClick(waitForObjectItem(":gbxClientID.cmbClientOperator_QComboBox", ClientOperator), 54, 8, 0, Qt.LeftButton)
                
    if(SellClient !=""):
        SellClient=SellClient.replace(",","|")
        SellClient=multipleFilterProccessor(varDict,SellClient,'|')        
        mouseClick(waitForObject(":gbxClientID.txtSellClient_QLineEdit"), 48, 20, 0, Qt.LeftButton)
        type(waitForObject(":gbxClientID.txtSellClient_QLineEdit"), SellClient)   

@When("user apply trade price filter values of '(\w*)','(\w*)'", regexp=True)
def step(context, TradePrice_From, TradePrice_To):
    mouseClick(waitForObject(":gbxTradePrice.txtTradePriceFrom_QLineEdit"), 76, 10, 0, Qt.LeftButton)
    type(waitForObject(":gbxTradePrice.txtTradePriceFrom_QLineEdit"), TradePrice_From)    
    mouseClick(waitForObject(":gbxTradePrice.txtTradePriceTo_QLineEdit"), 87, 9, 0, Qt.LeftButton)
    type(waitForObject(":gbxTradePrice.txtTradePriceTo_QLineEdit"), TradePrice_To)  
           

@When("user apply trade size filter values of '(\w*)','(\w*)'", regexp=True)
def step(context, TradeSize_From, TradeSize_To):
 
    mouseClick(waitForObject(":gbxTradeSize.txtTradeSizeFrom_QLineEdit"), 86, 12, 0, Qt.LeftButton)
    type(waitForObject(":gbxTradeSize.txtTradeSizeFrom_QLineEdit"), TradeSize_From)    
    mouseClick(waitForObject(":gbxTradeSize.txtTradeSizeTo_QLineEdit"), 56, 14, 0, Qt.LeftButton)
    type(waitForObject(":gbxTradeSize.txtTradeSizeTo_QLineEdit"), TradeSize_To)


@When("user apply custom filter values of '(\w*)','(\w*)'", regexp=True)
def step(context, TradeLinkId, TradeReportId):
    #mouseClick(waitForObject(":frmFilterHolder.cmbCustomFilter_QComboBox_2"), 94, 12, 0, Qt.LeftButton)
    mouseClick(waitForObject(":frmFilterHolder.txtTradeReportLinkID_QLineEdit"), 29, 21, 0, Qt.LeftButton)
    type(waitForObject(":frmFilterHolder.txtTradeReportLinkID_QLineEdit"), TradeLinkId)
    mouseClick(waitForObject(":frmFilterHolder.txtTradeReportID_QLineEdit_2"), 38, 11, 0, Qt.LeftButton)
    type(waitForObject(":frmFilterHolder.txtTradeReportID_QLineEdit_2"), TradeReportId)

@Step("user apply duration filter values of '(\w*)','(\w*)','(\w*)','(\w*)'", regexp=True)
def step(context, Date_From, Time_From, Date_To, Time_To):
    
    i = datetime.datetime.now() - datetime.timedelta(hours=0)
    j = datetime.datetime.now()
    dateFrom = i.strftime('%d%m%Y')
    timeFrom = i.strftime('%H%M')
    test.log(str(dateFrom))
    test.log(str(timeFrom))    
    dateTo = j.strftime('%d%m%Y')
    timeTo = j.strftime('%H%M')
    
    if(Date_From !=""):
        Date_From=Date_From.replace(",","|")
        Date_From=multipleFilterProccessor(varDict,Date_From,'|')    
        mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_5"), 16, 7, -13, 3, 1, Qt.LeftButton)
        type(waitForObject(":gbxDuration.dtFromDurationDate_QDateEdit_2"), Date_From)
    else:
        mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_5"), 16, 7, -13, 3, 1, Qt.LeftButton)
        type(waitForObject(":gbxDuration.dtFromDurationDate_QDateEdit_2"), dateFrom)
    if(Time_From !=""):
        Time_From=Date_From.replace(",","|")
        Time_From=multipleFilterProccessor(varDict,Time_From,'|')  
        mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_6"), 18, 7, -18, 0, 1, Qt.LeftButton)
        type(waitForObject(":gbxDuration.dtFromDurationTime_QTimeEdit_2"), Time_From)
    else:
        pass
        #mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_6"), 18, 7, -18, 0, 1, Qt.LeftButton)
        #type(waitForObject(":gbxDuration.dtFromDurationTime_QTimeEdit_2"), timeFrom)    
    if(Date_To !=""):
        Date_To=Date_To.replace(",","|")
        Date_To=multipleFilterProccessor(varDict,Date_To,'|')   
        mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_7"), 16, 6, -12, 2, 1, Qt.LeftButton)
        type(waitForObject(":gbxDuration.dtToDurationDate_QDateEdit_2"), Date_To)        
    else:
        mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_7"), 16, 6, -12, 2, 1, Qt.LeftButton)
        type(waitForObject(":gbxDuration.dtToDurationDate_QDateEdit_2"), dateTo) 
    if(Time_To !=""):
        Time_To=Time_To.replace(",","|")
        Time_To=multipleFilterProccessor(varDict,Time_To,'|') 
        mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_8"), 16, 10, -18, -5, 1, Qt.LeftButton)
        type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), Time_To)
    else:
        mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_8"), 16, 10, -18, -5, 1, Qt.LeftButton)
        type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), timeTo)
      
      

    
@Step("user click on Trade filter Apply button")
def step(context):
    #Array to pass step data
    context.userData=[]
    #Setting config timeout for Order query  
    timeout=0
    for record in testData.dataset("EnvironmentDetails/systemDeyals.csv"):
        property = testData.field(record, "property")
        delay = testData.field(record, "delay")
        if property=='trade_apply':
            timeout=float(delay)
            break  
    #saveDesktopScreenshot("screen.png")  
    t1 = float(0)
    clickButton(waitForObject(":frmBtnPanel.btnApply_QPushButton"))
    
    #Waiting for query to respond
   #Looking for error messages
    while t1 <= timeout: 
        try:
            if waitFor("object.exists(':Warning_QMessageBox')", 2000) == True:
                raise Exception
            elif waitFor("object.exists(':Error_QMessageBox')", 2000) == True:
                raise Exception                      
            
            elif waitFor("object.exists(':No Data_QMessageBox')", 2000) == True:
                raise Exception
                    # test.compare(findObject(":No Data_QMessageBox").enabled, True)  
            
            elif waitFor("object.exists(':ftmTableTitlebar.lblQuerySummary_QLabel_2')",2000) == True:
                if waitForObject(":ftmTableTitlebar.lblQuerySummary_QLabel_2").text == "Executing Query, Please Wait..":        
                    snooze(1)
                    t1 = t1 + 1   
                    test.log(str(t1)) 
                    if t1==timeout:
                        test.fail("Query takes too long to respond! - current delay: "+str(t1)+"")
                else:
                    break                         
            else:
                break
            
        except Exception, e:
            if waitFor("object.exists(':Warning_QMessageBox')", 2000) == True:
                #test.compare(str(waitForObjectExists(":sp2WindowsView.qt_msgbox_label_QLabel").text), "To Order Price cannot exceed From Order Price")
                context.userData.append(str(waitForObjectExists(":sp2WindowsView.qt_msgbox_label_QLabel").text))
                clickButton(waitForObject(":sp2WindowsView.OK_QPushButton"))
                
            elif waitFor("object.exists(':Error_QMessageBox')", 2000) == True:
                context.userData.append(str(waitForObjectExists(":Error.qt_msgbox_label_QLabel").text))
                clickButton(waitForObject(":Error.OK_QPushButton"))
            elif waitFor("object.exists(':No Data_QMessageBox')", 2000) == True:
                #test.compare(str(waitForObjectExists(":sp2WindowsView.qt_msgbox_label_QLabel").text), "No Matching Records Found for Query Criteria")
                context.userData.append(str(waitForObjectExists(":No Data.qt_msgbox_label_QLabel").text))
                clickButton(waitForObject(":No Data.OK_QPushButton"))
                
            else:
                break
                       
#         except LookupError, err:
#             if str(err) == "LookupError: Object ':ftmTableTitlebar.lblQuerySummary_QLabel_2' not ready. ":
#                 pass
#             else:
#                 test.fail("Unexpected error in Query", str(err))
#                 
        
    #Logging the response time
    test.log("Response time: "+str(t1)+"")
    #snooze(timeout)
    
       
         
@Then("system should return query result in the trades pane")
def step(context):
    rowCount=str(waitForObject(":ftmTableTitlebar.lblQuerySummary_QLabel_2").text)
    rowCount=rowCount.partition(":")
    print rowCount
    #rowCount.replace("Row Count : ","")
    test.log(rowCount[2])
    if rowCount[2]=="" or rowCount[2]==0:
        test.fail("No records...")
    else:
        pass
    #test.verify(rowCount[2] > 0, "Testing Row Count")  
      
@Then("user export queried result into '|any|' csv file in the '|any|' folder")
def step(context,filename,folder):

    sendEvent("QMouseEvent", waitForObject(":ftmTableTitlebar.btnExportTable_QPushButton"), QEvent.MouseButtonPress, 7, 9, Qt.LeftButton, 1, 0)
    activateItem(waitForObjectItem(":_QMenu", "Export To CSV"))
    sendEvent("QKeyEvent", waitForObject(":Save File_Edit"), QEvent.KeyPress, 16777251, 0, 0, "", False, 1)
    #clickButton(waitForObject(":ftmTableTitlebar.btnExportTable_QPushButton"))
    snooze(5)
    if waitFor("object.exists(':No Data_QMessageBox')", 2000)== True:
        testSettings.logScreenshotOnFail = True
        test.fail("No data returned for the query...!")
        testSettings.logScreenshotOnFail = False    
    else:
        snooze(5)        
        waitForObjectItem(":stackedWidget.listView_QListView", folder)        
        doubleClickItem(":stackedWidget.listView_QListView", folder, 35, 5, 0, Qt.LeftButton)       
        mouseDrag(waitForObject(":Save File_Edit"), 85, 8, -107, 3, 1, Qt.LeftButton)       
        sendEvent("QKeyEvent", waitForObject(":Save File_Edit"), QEvent.KeyPress, 16777248, 0, 0, "", False, 1)        
        type(waitForObject(":Save File_Edit"), filename)
        snooze(1)
        clickButton(waitForObject(":Save File.Save_Button"))
        
# def step(context,csvFilePath):
#     clickButton(waitForObject(":ftmTableTitlebar.btnExportTable_QPushButton"))
#     #type(waitForObject(":sp2WindowsView.lookInCombo_QComboBox"),csvFilePath)
#     type(waitForObject(":Save File_Edit"), "actualTrades")
#     clickButton(waitForObject(":Save File.Save_Button"))

@Then("user writes '([^']*)' data into the database '([^']*)'", regexp=True)
def step(context,csvFile,dbFile):
    snooze(5)
#substring csv file name
    tableName=csvFile.replace(".csv","")
    test.log('TableName:'+tableName)
    
    #Setting file path using global variables defined in bdd_hooks.py
    dbFile=getDictValue(varDict,'SurvFilePath')+dbFile
    csvFile=getDictValue(varDict,'SurvFilePath')+csvFile
    test.log('DBpath='+dbFile)
    test.log('CSVpath='+csvFile)
    
    #Reading the Column Names of the CSV
    with open(csvFile, "rb") as f:
        reader = csv.reader(f)
        columns = reader.next()
        rest = [row for row in reader]
        test.log(str(columns))
        
    #sql commands to insert table & data into the database  
    fields=""
    values=""
    for header in columns:
        print header
        fields= fields + header + "' text,'"
        values=values+"?,"
    print fields
    values=values[:-1]
    print values
    
    #remove last ,
    #values=values[:-1]
    #rempve last ,    
    fields=fields[:-2]    
    print fields
    #add first ' 
    fields="'"+fields
    print fields
    #pass field names of csv
    fields1=fields
    fields1=fields1.replace("'","")
    fields1=fields1.split(",")
    print fields1
        
    sql1='CREATE TABLE IF NOT EXISTS '+tableName+' (id INTEGER PRIMARY KEY AUTOINCREMENT,'+fields+');'
    test.log(sql1)
    fields=fields.replace("text","")
    fields_x=fields.replace(",",", :")
    #fields_x=fields_x.replace("'","|")
    print fields_x    
    context.userdata=[]
    context.userdata.append(fields)
    #sql2='INSERT INTO '+tableName+' ('+fields+') VALUES(:'+fields_x+');'
    sql2='INSERT INTO '+tableName+' ('+fields+') VALUES('+values+');'
    test.log(sql2)
    #Writes into the db using common methods    
    csv2DB(dbFile,csvFile,sql1,sql2,fields1)
    
@Then("user compare fields of '|any|' with '|any|' and '|any|' data tables in '|any|'")
def step(context,columnList,actualResult,expectedResult,db):
    test.warning("TODO implement user compare ")
    fieldSet=[]
    test.log(columnList)
    for record in testData.dataset(""+columnList+""):
        fieldname = testData.field(record, "FieldName")
        fieldSet.append(fieldname)
    
    sqlFields=','.join(fieldSet)
    test.log(sqlFields)
       
        
#     sqlUnion = '''  SELECT COUNT() FROM (SELECT symbol,trade_status,execution_type,executed_qty,executed_value,buy_broker_id,sell_broker_id,buy_trader_id,sell_trader_id
#                 FROM
#                 (
#                   SELECT symbol,trade_status,execution_type,executed_qty,executed_value,buy_broker_id,sell_broker_id,buy_trader_id,sell_trader_id
#                   FROM expectedTradeResult
#                   UNION ALL
#                   SELECT symbol,trade_status,execution_type,executed_qty,executed_value,buy_broker_id,sell_broker_id,buy_trader_id,sell_trader_id
#                   FROM actualTradeResult
#                 ) tmp
#                 GROUP BY symbol
#                 HAVING COUNT(*) = 1 
#                 ORDER BY sell_trader_id) '''
                
    sqlUnion = "SELECT COUNT() FROM (SELECT "+sqlFields+" FROM(SELECT "+sqlFields+" FROM "+expectedResult+" UNION SELECT "+sqlFields+" FROM "+actualResult+") tmp GROUP BY symbol HAVING COUNT(*) = 1 ORDER BY transact_time)"     
    test.log(sqlUnion)                    
   #sqlUnion='SELECT Symbol,Firm_ID,Owner_ID,Side FROM tradeResult UNION SELECT Symbol,Firm_ID,Owner_ID,Side FROM expectedTradeResult;'
   
    db=SurvFilePath+db
    result=queryDB(db,sqlUnion).fetchone()[0]
    test.log("UnionResult: "+str(result)) 
    test.compare(0, result, "Expected & Actual Table Verification")  
     
    #######---UNDER CONSTURCTION----########
#     selectQuery="SELECT "+sqlFields+" FROM "+actualResult+""
#     DB2csv(db,"testCsv",selectQuery,fieldSet)
    
#    for row in result:
#        test.log(row.count)
#        print "Symbol = ", row[0] +  "|Firm_ID = ", row[1] + "|Owner_ID = ", row[2] + "|Side = ", row[3], "\n"
#         print "Firm_ID = ", row[1]
#         print "Owner_ID = ", row[2]
#         print "Side = ", row[3], "\n"
#                 
    
    
@Step("user deletes '([^']*)' and '([^']*)' data tables from '([^']*)'", regexp=True)
def step(context, table1,table2,db):
    
    
    #Delete previously generated json files
#     dir=getDictValue(varDict,'SurvFilePath')   
#     ListDir=os.listdir(dir)
# 
#     for item in ListDir:
#         if item.endswith(".json"):
#             os.remove(join(dir, item))   
#         
      
#    #get application path of squish 
#     
#     appPath=getAppPath("squishrunner --info applications")   
#     test.log(str(appPath))     
#     path=appPath.replace("mapped","")
#     path=path.replace("SurveillanceWorkstation","")
#     path=path.strip()
#     test.log(str(path))
#     
#     #changing the survFile path using new value
#     setDictValue(varDict,'SurvFilePath','')
#     test.log(getDictValue(varDict,'SurvFilePath'))
#     snooze(1)
#     setDictValue(varDict,'SurvFilePath',path+'\\qaTest\\')
#     test.log(getDictValue(varDict,'SurvFilePath'))
#     snooze(1)
#     
#     #Create file path
#     if not os.path.exists(getDictValue(varDict,'SurvFilePath')):
#         os.makedirs(getDictValue(varDict,'SurvFilePath'))  
    

    sqlDeleteTable1='DROP TABLE IF EXISTS '+table1+''
    sqlDeleteTable2='DROP TABLE IF EXISTS '+table2+''
    
#     sqlDeleteTable1='DELETE FROM '+table1+';'
#     sqlDeleteTable2='DELETE FROM '+table2+';'
    
    #db=SurvFilePath+db
    
    db=getDictValue(varDict,'SurvFilePath')+db
    test.log(db)
    queryDB(db,sqlDeleteTable1)
    queryDB(db,sqlDeleteTable2)
    
    #Remove previously generated json files
    #absFilePath(getDictValue(varDict,file_path))
    
    
@Then("system should return '|any|' rows in Trade query result in the pane")
def step(context,rows):
    #test.warning("TODO implement system should return query result in the orders pane")
    rowCount=str(waitForObject(":ftmTableTitlebar.lblQuerySummary_QLabel_2").text)
    rowCount=rowCount.partition(":")
    print rowCount
    #rowCount.replace("Row Count : ","")
    test.log(rowCount[2])
    r= str.strip(rowCount[2])
    
    if r == "0":
        test.fail("No records found ...!")
    else:
        #pass
        test.verify(rowCount[2]>0, "Testing Row Count")
        #test.verify(rows == str.strip(rowCount[2]), "Comparing row Count")
    
    
@Then("the system should return available trades whithin the given period of '|any|' to '|any|'")
def step(context, timeFrom,timeTo):
      
    mouseClick(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_6"), 14, 17, 0, Qt.LeftButton)
    type(waitForObject(":gbxDuration.dtFromDurationTime_QTimeEdit_2"), timeFrom)    
    
    mouseClick(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_8"), 7, 8, 0, Qt.LeftButton)   
    type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), timeTo)
    clickButton(waitForObject(":frmBtnPanel.btnApply_QPushButton"))   
    
    snooze(5)
        
    rowCount=str(waitForObject(":ftmTableTitlebar.lblQuerySummary_QLabel_2").text)
    rowCount=rowCount.partition(":")
    print rowCount
    #rowCount.replace("Row Count : ","")
    test.log(rowCount[2])
    test.verify(rowCount[2]>0, "Testing Row Count")    
    
    
    
# @Then("user look for default filter fields of '|any|'")
# def step(context,filterFeilds):    
#     pass


@When("user resize coulmns using drag and drop")
def step(context):
    dragItemBy(waitForObject(":Trades_QHeaderView"), 101, 9, 322, 36, 1, Qt.LeftButton)
    dragItemBy(waitForObject(":Trades_QHeaderView"), 523, 8, 215, 0, 1, Qt.LeftButton)
    dragItemBy(waitForObject(":Trades_QHeaderView"), 834, 9, 212, 7, 1, Qt.LeftButton)
    #type(waitForObject(":splitTableAndGraph.Trades_sp2::SpatialTableView"), "<Alt>")

@Then("coulmns should be resized acordingly")
def step(context):
    pass



@Then("system prompt save trade filter dialog box")
def step(context):
    waitFor("object.exists(':FileNameInputDialog_FileNameInputDialog')", 20000)
    test.compare(findObject(":FileNameInputDialog_FileNameInputDialog").enabled, True)

@When("user type filter name & click on save button")
def step(context):
    mouseClick(waitForObject(":FileNameInputDialog.txtText_QLineEdit"), 27, 11, 0, Qt.LeftButton)
    type(waitForObject(":FileNameInputDialog.txtText_QLineEdit"), "myTestFilter")
    clickButton(waitForObject(":FileNameInputDialog.btnSave_QPushButton"))

@Then("trade filter saved & displayed on custom pane")
def step(context):
    waitFor("object.exists(':lstFiltersList.myTestFilter - Trades Window_QModelIndex')", 20000)
    test.compare(findObject(":lstFiltersList.myTestFilter - Trades Window_QModelIndex").text, "myTestFilter - Trades Window")
    mouseClick(waitForObject(":frmSidePanle_2.lstFiltersList_QListWidget"), -429, 619, 0, Qt.LeftButton)
    clickButton(waitForObject(":frame.btnClose_QPushButton"))


@When("user click on save trade filter button")
def step(context):
    sendEvent("QMouseEvent", waitForObject(":titlebar.btnDumpToFile_QPushButton"), QEvent.MouseButtonPress, 21, 20, Qt.LeftButton, 1, 0)
    activateItem(waitForObjectItem(":_QMenu", "Save Filter")) 

@Then("user selects '|any|' option in dialogbox")
def step(context, saveOption):
    if(saveOption=="SaveFilter" or saveOption==""):
        clickButton(waitForObject(":Save Filter_QPushButton"))
    elif(saveOption=="SaveWatchList"):
        clickButton(waitForObject(":Save Watch List_QPushButton"))
@When("user drag '|any|' and drop into trade filter pane")
def step(context,anyCol):
    try:
        col=findColumn(anyCol,":Trades_QHeaderView")  
        checkEmpty(waitForObject("{column?='"+str(col)+"' container=':vSplitterTableAndGraph.Trades_sp2::SpatialTableView' row='0' type='QModelIndex'}"),str(findObject("{column?='"+str(col)+"' container=':vSplitterTableAndGraph.Trades_sp2::SpatialTableView' row='0' type='QModelIndex'}").text))
        dragAndDrop(waitForObject("{column?='"+str(col)+"' container=':vSplitterTableAndGraph.Trades_sp2::SpatialTableView' row='0' type='QModelIndex'}"), 47, 12, ":scrollAreaWidget.frmFilterHolder_QFrame", 94, 916, Qt.CopyAction)
        global tradeReportID 
        tradeReportID = waitForObjectExists(":Trades.0_10_QModelIndex_3").text
    except Exception,e:
        test.fail("Failed to find Cell", str(e))
        
@Then("Instrument filter should be filled with the selected Instrument value")
def step(context):
    waitFor("object.exists(':frmFilterHolder.txtInstrument_LineEditEx')", 20000)
    test.compare(str(findObject("::frmFilterHolder.txtInstrument_LineEditEx").text), str(findObject(":Trades.0_0_QModelIndex_2").text))

@When("user select an Exec type and drop into trade filter pane")
def step(context):
    checkEmpty(waitForObject(":Trades.0_3_QModelIndex_2"),str(findObject(":Trades.0_3_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_3_QModelIndex_2"), 38, 12, ":scrollAreaWidget.frmFilterHolder_QFrame", 81, 845, Qt.CopyAction)    
  
@Then("Exec type filter should be filled with the selected Exec type value")
def step(context):
    waitFor("object.exists(':frmFilterHolder.cmbExecType_QComboBox')", 20000)
    test.compare(str(findObject(":frmFilterHolder.cmbExecType_QComboBox").currentText), str(findObject(":Trades.0_3_QModelIndex_2").text))

@When("user select an Trade type and drop into trade filter pane")
def step(context):
   scrollTo(waitForObject(":Trades_QScrollBar_2"), 8)
   checkEmpty(waitForObject(":Trades.0_18_QModelIndex_2"),str(findObject(":Trades.0_18_QModelIndex_2").text))
   dragAndDrop(waitForObject(":Trades.0_18_QModelIndex_2"), 30, 13, ":scrollAreaWidget.frmFilterHolder_QFrame", 66, 884, Qt.CopyAction)
       
@Then("Trade type filter should be filled with the selected Trade type value")
def step(context):
    waitFor("object.exists(':frmFilterHolder.cmbTradeType_QComboBox')", 20000)
    test.compare(str(findObject(":frmFilterHolder.cmbTradeType_QComboBox").currentText), str(findObject(":Trades.0_18_QModelIndex_2").text))

@When("user select an Trade Sub type and drop into trade filter pane")
def step(context):
    checkEmpty(waitForObject(":Trades.0_17_QModelIndex_2"),str(findObject(":Trades.0_17_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_17_QModelIndex_2"), 21, 8, ":scrollAreaWidget.frmFilterHolder_QFrame", 233, 889, Qt.CopyAction)

@Then("Trade Sub type filter should be filled with the selected Trade Sub type value")
def step(context):
    waitFor("object.exists(':frmFilterHolder.cmbTradeSubType_QComboBox')", 20000)
    test.compare(str(findObject(":frmFilterHolder.cmbTradeSubType_QComboBox").currentText), str(findObject(":Trades.0_17_QModelIndex_2").text))
    
@When("user select Buy Trader and drop into trade filter pane")
def step(context):
    checkEmpty(waitForObject(":Trades.0_8_QModelIndex_2"),str(findObject(":Trades.0_8_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_8_QModelIndex_2"), 47, 11, ":scrollAreaWidget.frmFilterHolder_QFrame", 161, 732, Qt.CopyAction)

@Then("Buy Trader filter should be filled with the selected Buy Trader value")
def step(context):
    test.compare(str(waitForObjectExists(":gbxTraderID.txtBuyTrader_LineEditEx").text), str(findObject(":Trades.0_8_QModelIndex_2").text))

@When("user select Sell Trader and drop into trade filter pane")
def step(context):
    checkEmpty(waitForObject(":Trades.0_9_QModelIndex_2"),str(findObject(":Trades.0_9_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_9_QModelIndex_2"), 33, 13, ":scrollAreaWidget.frmFilterHolder_QFrame", 184, 808, Qt.CopyAction)

@Then("Sell Trader filter should be filled with the selected Sell Trader value")
def step(context):
    test.compare(str(waitForObjectExists(":gbxTraderID.txtSellTrader_LineEditEx").text), str(findObject(":Trades.0_9_QModelIndex_2").text))

@When("user select Buy Firm and drop into trade filter pane")
def step(context):
    checkEmpty(waitForObject(":Trades.0_6_QModelIndex_2"),str(findObject(":Trades.0_6_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_6_QModelIndex_2"), 40, 14, ":scrollAreaWidget.frmFilterHolder_QFrame", 241, 739, Qt.CopyAction)

@Then("Buy Firm filter should be filled with the selected Buy Firm value")
def step(context):
    test.compare(str(waitForObjectExists(":gbxFirmID.txtBuyFirm_LineEditEx").text), str(findObject(":Trades.0_6_QModelIndex_2").text))

@When("user select Sell Firm and drop into trade filter pane")
def step(context):
    checkEmpty(waitForObject(":Trades.0_7_QModelIndex_2"),str(findObject(":Trades.0_7_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_7_QModelIndex_2"), 42, 12, ":scrollAreaWidget.frmFilterHolder_QFrame", 79, 893, Qt.CopyAction)

@Then("Sell Firm filter should be filled with the selected Sell Firm value")
def step(context):
    test.compare(str(waitForObjectExists(":gbxFirmID.txtSellFirm_LineEditEx").text), str(findObject(":Trades.0_7_QModelIndex_2").text))

@When("user select Buy Client and drop into trade filter pane")
def step(context):
    #checkEmpty(waitForObject(":Trades.0_10_QModelIndex_2"),str(findObject(":Trades.0_10_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_10_QModelIndex_2"), 42, 13, ":scrollAreaWidget.frmFilterHolder_QFrame", 100, 863, Qt.CopyAction)

@Then("Buy Client filter should be filled with the selected Buy Client value")
def step(context):
    test.compare(str(waitForObjectExists(":gbxClientID.txtBuyClient_LineEditEx").text), str(findObject(":Trades.0_10_QModelIndex_2").text))

@When("user select Sell Client and drop into trade filter pane")
def step(context):
    #checkEmpty(waitForObject(":Trades.0_11_QModelIndex_2"),str(findObject(":Trades.0_11_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_11_QModelIndex_2"), 33, 12, ":scrollAreaWidget.frmFilterHolder_QFrame", 50, 816, Qt.CopyAction)

@Then("Sell Client filter should be filled with the selected Sell Client value")
def step(context):
    test.compare(str(waitForObjectExists(":gbxClientID.txtSellClient_LineEditEx").text), str(findObject(":Trades.0_11_QModelIndex_2").text))

@When("user select an Trade Report Link ID and drop into trade filter pane")
def step(context):
    checkEmpty(waitForObject(":Trades.0_16_QModelIndex_2"),str(findObject(":Trades.0_16_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_16_QModelIndex_2"), 42, 14, ":scrollAreaWidget.frmFilterHolder_QFrame", 203, 867, Qt.CopyAction)

    #dragAndDrop(waitForObject(":Trades.0_18_QModelIndex_2"), 80, 11, ":scrollAreaWidget.frmFilterHolder_QFrame", 47, 768, Qt.CopyAction)

@Then("Trade Report Link ID filter should be filled with the selected Trade Report Link ID value")
def step(context):
    test.compare(str(waitForObjectExists(":frmFilterHolder.txtTradeReportLinkID_QLineEdit").text), str(findObject(":Trades.0_16_QModelIndex_2").text))    

@When("user select second Instrument and drop into trade filter pane")
def step(context):
    scrollTo(waitForObject(":Trades_QScrollBar"), 0)
    checkEmpty(waitForObject(":Trades.8_0_QModelIndex_2"),str(findObject(":Trades.8_0_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.8_0_QModelIndex_2"), 33, 18, ":scrollAreaWidget.frmFilterHolder_QFrame", 142, 810, Qt.CopyAction)

@Then("Instrument filter should be filled with the selected second Instrument value")
def step(context):
    test.compare(str(waitForObjectExists(":frmFilterHolder.txtInstrument_LineEditEx").text), str(findObject(":Trades.8_0_QModelIndex_2").text))

@When("user select second Exec type and drop into trade filter pane")
def step(context):
    checkEmpty(waitForObject(":Trades.8_3_QModelIndex_2"),str(findObject(":Trades.8_3_QModelIndex_2").text))   
    dragAndDrop(waitForObject(":Trades.8_3_QModelIndex_2"), 52, 8, ":scrollAreaWidget.frmFilterHolder_QFrame", 148, 785, Qt.CopyAction)

@Then("Exec type filter should be filled with the selected second Exec type value")
def step(context):
    test.compare(str(waitForObjectExists(":frmFilterHolder.cmbExecType_QComboBox").currentText), str(findObject(":Trades.8_3_QModelIndex_2").text))
    

@When("user select second Trade type and drop into trade filter pane")
def step(context):
    checkEmpty(waitForObject(":Trades.8_7_QModelIndex_2"),str(findObject(":Trades.8_7_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.8_7_QModelIndex_2"), 31, 15, ":scrollAreaWidget.frmFilterHolder_QFrame", 139, 825, Qt.CopyAction)

@Then("Trade type filter should be filled with the selected second Trade type value")
def step(context):
    test.compare(str(waitForObjectExists(":frmFilterHolder.cmbTradeType_QComboBox").currentText), str(findObject(":Trades.8_7_QModelIndex_2").text))
    mouseClick(waitForObject(":sp2WindowsView.Trades_sp2::MDISubEx"), 777, 18, 0, Qt.LeftButton)


@When("user select an Trade Report ID and drop into trade filter pane")
def step(context):
    checkEmpty(waitForObject(":Trades.0_1_QModelIndex_2"),str(findObject(":Trades.0_1_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_1_QModelIndex_2"), 41, 12, ":scrollAreaWidget.frmFilterHolder_QFrame", 175, 868, Qt.CopyAction)    

@Then("Trade Report ID filter should be filled with the selected Trade Report ID value")
def step(context):
    waitFor("object.exists(':frmFilterHolder.txtTradeReportID_QLineEdit_2')", 20000)
    test.compare(str(findObject(":frmFilterHolder.txtTradeReportID_QLineEdit_2").text), str(findObject(":Trades.0_1_QModelIndex_2").text))

@When("user drag '|any|' and drop into 'InstrumentID' trade filter property")
def step(context,column):       
    try:
#         fieldName = ("{name='"+filName+"' type='LineEditEx' visible='1'}")
#         field = waitForObject(fieldName)
        col=findColumn(column,":Trades_QHeaderView")  
        checkEmpty(waitForObject("{column?='"+str(col)+"' container=':vSplitterTableAndGraph.Trades_sp2::SpatialTableView' row='0' type='QModelIndex'}"),str(findObject("{column?='"+str(col)+"' container=':vSplitterTableAndGraph.Trades_sp2::SpatialTableView' row='0' type='QModelIndex'}").text))
        dragAndDrop(waitForObject("{column='"+str(col)+"' container=':vSplitterTableAndGraph.Trades_sp2::SpatialTableView' row='0' type='QModelIndex'}"), 36, 18, "{name='txtInstrumentID' type='LineEditEx' visible='1'}", 115, 5, Qt.CopyAction)
        #dragAndDrop(waitForObject("{column='"+str(col)+"' container=':vSplitterTableAndGraph.Trades_sp2::SpatialTableView' row='0' type='QModelIndex'}"), 36, 18, "{name='txtInstrumentID' type='LineEditEx' visible='1'}", 115, 5, Qt.CopyAction)
    except Exception,e:
        test.fail("Failed to find Cell", str(e))
    
@When("user select an Exec type and drop into trade filter property")
def step(context):
    checkEmpty(waitForObject(":Trades.0_3_QModelIndex_2"),str(findObject(":Trades.0_3_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_3_QModelIndex_2"), 45, 19, ":scrollAreaWidget.frmFilterHolder_QFrame", 248, 41, Qt.CopyAction)

@When("user select an Trade type and drop into trade filter property")
def step(context):
    scrollTo(waitForObject(":Trades_QScrollBar"), 4)
    checkEmpty(waitForObject(":Trades.0_18_QModelIndex_2"),str(findObject(":Trades.0_18_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_18_QModelIndex_2"), 34, 11, ":scrollAreaWidget.frmFilterHolder_QFrame", 174, 68, Qt.CopyAction)
    #test.warning("TODO FROM HERE")

@When("user select an Trade Sub type and drop into trade filter property")
def step(context):
    checkEmpty(waitForObject(":Trades.0_17_QModelIndex_2"),str(findObject(":Trades.0_17_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_17_QModelIndex_2"), 24, 13, ":scrollAreaWidget.frmFilterHolder_QFrame", 212, 96, Qt.CopyAction)

@When("user select Buy Trader and drop into trade filter property")
def step(context):
    scrollTo(waitForObject(":Trades_QScrollBar"), 0)
    checkEmpty(waitForObject(":Trades.0_8_QModelIndex_2"),str(findObject(":Trades.0_8_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_8_QModelIndex_2"), 35, 14, ":gbxTraderID.txtBuyTrader_LineEditEx", 52, 11, Qt.CopyAction)

@When("user select Sell Trader and drop into trade filter property")
def step(context):
    checkEmpty(waitForObject(":Trades.0_9_QModelIndex_2"),str(findObject(":Trades.0_9_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_9_QModelIndex_2"), 60, 10, ":gbxTraderID.txtSellTrader_LineEditEx", 22, 11, Qt.CopyAction)

@When("user select Buy Firm and drop into trade filter property")
def step(context):
    checkEmpty(waitForObject(":Trades.0_6_QModelIndex_2"),str(findObject(":Trades.0_6_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_6_QModelIndex_2"), 41, 15, ":gbxFirmID.txtBuyFirm_LineEditEx", 94, 9, Qt.CopyAction)

@When("user select Sell Firm and drop into trade filter property")
def step(context):
    checkEmpty(waitForObject(":Trades.0_7_QModelIndex_2"),str(findObject(":Trades.0_7_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_7_QModelIndex_2"), 55, 10, ":gbxFirmID.txtSellFirm_LineEditEx", 68, 18, Qt.CopyAction)
    #type(waitForObject(":splitTableAndGraph.Trades_sp2::SpatialTableView"), "<Tab>")

@When("user select Buy Client and drop into trade filter property")
def step(context):
    #checkEmpty(waitForObject(":Trades.0_10_QModelIndex_2"),str(findObject(":Trades.0_10_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_10_QModelIndex_2"), 39, 14, ":gbxClientID.txtBuyClient_LineEditEx", 75, 6, Qt.CopyAction)

@When("user select Sell Client and drop into trade filter property")
def step(context):
    #checkEmpty(waitForObject(":Trades.0_11_QModelIndex_2"),str(findObject(":Trades.0_11_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_11_QModelIndex_2"), 54, 12, ":gbxClientID.txtSellClient_LineEditEx", 103, 16, Qt.CopyAction)

@When("user select an Trade Report ID and drop into trade filter property")
def step(context):
    context.userData=[]
    dragItemBy(waitForObject(":Trades_QHeaderView"), 198, 13, 71, 1, 1, Qt.LeftButton)
    checkEmpty(waitForObject(":Trades.0_1_QModelIndex_3"),str(findObject(":Trades.0_1_QModelIndex_3").text))
    dragAndDrop(waitForObject(":Trades.0_10_QModelIndex_3"), 66, 11, ":frmFilterHolder.txtTradeReportID_QLineEdit_2", 40, 7, Qt.CopyAction)
   # test.compare(waitForObjectExists(":Trades.0_1_QModelIndex_3").enabled, True)
    sendEvent("QKeyEvent", waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), QEvent.KeyPress, 16777251, 0, 0, "", False, 1)  
    
    context.userData.append(str(findObject(":frmFilterHolder.txtTradeReportID_QLineEdit_2").text))

@When("user select an Trade Report Link ID and drop into trade filter property")
def step(context):          
    checkEmpty(waitForObject(":Trades.0_16_QModelIndex_2"),str(findObject(":Trades.0_16_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.0_16_QModelIndex_2"), 22, 6, ":frmFilterHolder.txtTradeReportLinkID_QLineEdit", 86, 5, Qt.CopyAction)
    #dragAndDrop(waitForObject(":Trades.0_16_QModelIndex_2"), 94, 12, ":frmFilterHolder.txtTradeReportLinkID_QLineEdit", 70, 8, Qt.CopyAction)

@When("user select second Instrument and drop into trade filter property")
def step(context):
    scrollTo(waitForObject(":Trades_QScrollBar"), 0)
    checkEmpty(waitForObject(":Trades.8_0_QModelIndex_2"),str(findObject(":Trades.8_0_QModelIndex_2").text))
    dragAndDrop(waitForObject(":Trades.8_0_QModelIndex_2"), 49, 16, ":frmFilterHolder.txtInstrument_LineEditEx", 76, 2, Qt.CopyAction)

@Then("Instrument filter should be filled  by appending the Instrument value")
def step(context):
    test.warning("this should append with a | ")
    test.xcompare(str(waitForObjectExists(":frmFilterHolder.txtInstrument_LineEditEx").text), "CP1INSCR87_01")



@When("user right click on record and select 'View History'")
def step(context):
    #waitForObjectItem(":vSplitterTableAndGraph.Trades_sp2::SpatialTableView", "0/1")
    clickItem(":vSplitterTableAndGraph.Trades_sp2::SpatialTableView", "0/1", 47, 19, 0, Qt.LeftButton)
    openItemContextMenu(waitForObject(":vSplitterTableAndGraph.Trades_sp2::SpatialTableView"), "0/1", 47, 16, 0)
    activateItem(waitForObjectItem(":_QMenu", "View History"))
# 
#     openItemContextMenu(waitForObject(":splitTableAndGraph.Trades_sp2::SpatialTableView"), "0/1", 53, 5, 0)
#     activateItem(waitForObjectItem(":_QMenu", "View History"))

@Then("trade history tab should open with the name of '|any|'")
def step(context,header):    
   
    
    #test.compare(waitForObjectExists("{container=':Trades_QHeaderView' text='Transact Time' type='HeaderViewItem' visible='true'}").type, "HeaderViewItem")
                              # Object '{container='Trades_QHeaderView' text?='Trade Report ID' type='HeaderViewItem' visible='true'}' not found: Object 'Trades_QHeaderView' not found. 


    #test.compare(waitForObjectExists("{container=':Trades_QHeaderView' text='Trade Report ID' type='HeaderViewItem' visible='true'}").text, "Trade Report ID")



   # test.compare(waitForObjectExists("{container=':frmPieChartPH.qt_tabwidget_tabbar_QTabBar_4' text='History : WXX3T6ZLTF' type='TabItem'}").text, "History : WXX3T6ZLTF")

    
    
    try:
        col=findColumn("Trade Report ID",":Trades_QHeaderView")
        tradeRepLnkId = waitForObjectExists("{column='"+str(col)+"' container=':splitter.Trades_sp2::SpatialTableView_2' row='0' type='QModelIndex'}").text
        #test.compare(waitForObjectExists("{container=':frmPieChartPH.qt_tabwidget_tabbar_QTabBar_4' text?=' History : *' type='TabItem'}").text, " History : "+tradeRepLnkId+"")
        test.compare(waitForObjectExists("{container=':frmPieChartPH.qt_tabwidget_tabbar_QTabBar_4' text='History : "+tradeRepLnkId+"' type='TabItem'}").text, "History : "+tradeRepLnkId+"")
    except Exception,e:
        test.fail("Error on column", str(e))
            

@Then("history tab should contain history results")
def step(context):
    pass

@Then("user export queried Trade history result into '|any|' csv file in the '|any|' folder")
def step(context,filename,folder):
    clickButton(waitForObject(":ftmAnalicticsTitlebar.btnExportHistoryTable_QPushButton"))    
    ExportToCSV(filename,folder)

@Then("Colour code '|any|' should map for each Execution type '|any|'")
def step(context, ColourCode, ExecType):
    col=findColumn(ExecType,":Trades_QHeaderView")
    waitFor("object.exists(':Trades.0_3_QModelIndex')", 20000)
    #test.compare(findObject(":Trades.0_3_QModelIndex").foregroundColor, "#FF00A038")
    if ColourCode !="" and test.compare(waitForObjectExists(":Trades.0_3_QModelIndex").text, ExecType)==True :
        ColourCode=ColourCode.replace("$","#")   
        testSettings.logScreenshotOnFail = True     
        test.compare(findObject("{column='"+str(col)+"' container=':vSplitterTableAndGraph.Trades_sp2::SpatialTableView' row='0' type='QModelIndex'}").foregroundColor, ColourCode)
        testSettings.logScreenshotOnFail = False


@When("user types Instrument '|any|'")
def step(context,ins):
    mouseClick(waitForObject(":frmFilterHolder.txtInstrumentID_QLineEdit"), 42, 14, 0, Qt.LeftButton)
    type(waitForObject(":frmFilterHolder.txtInstrumentID_QLineEdit"), "A")  
    
    waitForObjectItem(":_QListView", "AA\\_01")
    clickItem(":_QListView", "AA\\_01", 25, 7, 0, Qt.LeftButton)
    
#     listview = waitForObject(":_QListView")
#     item = listview.firstChild()
#     test.compare(item.text(0), "A0Q4R0")
#     child = item.firstChild()
#     test.compare(child.text(0), "Orange")
#     sibling = item.nextSibling()
#     test.compare(sibling.text(0), "Banana")

@Then("sugession list which starts from '|any|' should return")
def step(context,inst):

    #waitFor("object.exists(':A0Q4R0_QModelIndex')", 20000)
    #test.compare(findObject("{container?=':_QListView_?*' text='"+inst+"?*' type='QModelIndex'}").text, inst+"?*")

    pass


@When("user right click on order and select 'Veiw Orders' option")
def step(context):
    #here this should populate all trade related orders -- todo 

    openItemContextMenu(waitForObject(":vSplitterTableAndGraph.Trades_sp2::SpatialTableView"), "0/0", 68, 13, 0)
    activateItem(waitForObjectItem(":_QMenu", "View Orders"))
# 
#     openItemContextMenu(waitForObject(":splitTableAndGraph.Trades_sp2::SpatialTableView"), "0/0", 42, 3, 0)
#     activateItem(waitForObjectItem(":_QMenu", "View Orders"))

@Then("system should return respective orders for the trade")
def step(context):
#     trid=str(context.userData[0])
    testSettings.logScreenshotOnFail = True
    #waitFor("object.exists('{container=':sp2WindowsView_QTabBar' text?=' Orders for Trade Report ID : "+trid+"' type='TabItem'}')", 20000)
    
    
    
    test.compare(findObject("{container=':sp2WindowsView_QTabBar' text?=' Orders for Trade Report ID : "+trRepId+"' type='TabItem'}").text, " Orders for Trade Report ID : "+trRepId+"")
    #TODO compare query count 
    #waitFor("object.exists(':ftmTableTitlebar.lblQuerySummary_QLabel_3')", 20000)
    #test.compare(str(findObject(":ftmTableTitlebar.lblQuerySummary_QLabel_3").text), "Query Count : 1 ")
    testSettings.logScreenshotOnFail = False


@Then("user select record and copy Trade Report ID")
def step(context):
    try:
        waitForObjectItem(":splitTableAndGraph.Trades_sp2::SpatialTableView", "0/0")
        clickItem(":splitTableAndGraph.Trades_sp2::SpatialTableView", "0/0", 53, 13, 0, Qt.LeftButton)
        type(waitForObject(":splitTableAndGraph.Trades_sp2::SpatialTableView"), "<Right>")
        #dragAndDrop(waitForObject(":Trades.0_1_QModelIndex"), 39, 10, ":scrollAreaWidget.frmFilterHolder_QFrame", 97, 789, Qt.CopyAction)
        waitFor("object.exists(':Trades.0_0_QModelIndex')", 5000)
        #test.compare(findObject(":Trades.0_1_QModelIndex").text, "UIG0JGSWLE")
        
        context.userData.append(str(findObject(":Trades.0_0_QModelIndex").text))
    except Exception,e:
        test.fail("Failed to capture ID", str(e))

@Then("new tab should open with '|any|'")
def step(context,trid):
    global trRepId
    trRepId = context.userData[0]
    
#     col=findColumn("Trade Report ID",":Trades_QHeaderView")   
#     trRepId=findObject("{column='"+str(col)+"' container=':vSplitterTableAndGraph.Trades_sp2::SpatialTableView' row='0' type='QModelIndex'}").text
#     testSettings.logScreenshotOnFail = True    
#     #test.compare(findObject("{container=':sp2WindowsView_QTabBar' text?=' Orders for Trade Report ID : "+trRepId+"' type='TabItem'}").text," Orders for Trade Report ID : "+trRepId+"")
#     #test.compare(findObject(":Orders.0_12_QModelIndex_2").text, context.userData[0] )
#     testSettings.logScreenshotOnFail = False
#     snooze(5)
    

    col=findColumn("Trade Report ID",":Orders_QHeaderView") 
    #test.compare(waitForObjectExists("{container=':Orders_QHeaderView' text='Trade Report ID' type='HeaderViewItem' visible='true'}").text, "Trade Report ID")
    
    
    
    test.compare(waitForObjectExists("{column='"+str(col)+"' container=':vSplitterTableAndGraph.Orders_sp2::SpatialTableView' row='0' type='QModelIndex'}").text, trRepId)

    
    

@When("user clicks on multiple insturment selector")
def step(context):
    sendEvent("QMouseEvent", waitForObject(":frmFilterHolder.btnInstrumentSelector_QPushButton"), QEvent.MouseButtonPress, 19, 9, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(":frmFilterHolder.btnInstrumentSelector_QPushButton"), QEvent.MouseButtonRelease, 19, 9, Qt.LeftButton, 0, 0)

# @Then("system prompts an insturment selector window")
# def step(context):
#     waitFor("object.exists(':frmSelectorHeader.lblWindowTitle_QLabel')", 20000)
#     test.compare(str(findObject(":frmSelectorHeader.lblWindowTitle_QLabel").text), "Instrument Selector")
#     sendEvent("QMouseEvent", waitForObject(":CustomSelectorWnd.frmSelectorHeader_QFrame"), QEvent.MouseMove, 164, 311, Qt.NoButton, 1, 0)
# 
# @Then("window lists currently available instruments")
# def step(context):
#     sendEvent("QMouseEvent", waitForObject(":CustomSelectorWnd.frmSelectorHeader_QFrame"), QEvent.MouseButtonPress, 367, 24, Qt.LeftButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject(":CustomSelectorWnd_CustomSelectorWnd"), 519, 267, 893, 298)
#     mouseDrag(waitForObject(":CustomSelectorWnd.frmSelectorHeader_QFrame"), 367, 24, -7, -7, 1, Qt.LeftButton)
#     waitFor("object.exists(':frmTablePlaceHolderWidget.tableView_QTableView')", 20000)
#     test.compare(findObject(":frmTablePlaceHolderWidget.tableView_QTableView").enabled, True)
# 
# @When("user types required instruments on instrument field with wildcard selects them")
# def step(context):
#     context.userData="" 
#     pipe="|"
#     table = context.table
#      # Drop initial row with column headers
#     table.pop(0)
#  
#     for (expression,instrument) in table:
#         #context.userData.append(instrument)
#         context.userData += instrument+pipe
#         mouseClick(waitForObject(":scrollArea.txtInstrumentID_QLineEdit"), 46, 8, 0, Qt.LeftButton)
#         lineEdit=waitForObject(":scrollArea.txtInstrumentID_QLineEdit")
#         lineEdit.text=""
#         type(waitForObject(":scrollArea.txtInstrumentID_QLineEdit"), expression.replace("^","*"))
#         type(waitForObject(":scrollArea.txtInstrumentID_QLineEdit"), "<Keypad_Enter>")
#         clickButton(waitForObject("{container=':frmTablePlaceHolderWidget.tableView_QTableView' name?='"+instrument+"' type='QCheckBox' visible='1'}"))
#                    
#     test.log(context.userData)   
# 
# @When("user clicks on instrument selector ok button")
# def step(context):
#     clickButton(waitForObject(":frame.btnSelectOkay_QPushButton"))


@Then("Trades tab should detach from the main workstation")
def step(context):
    #waitFor("object.exists(':TradesWindow.1461912807667_sp2::QDockWidgetEx')", 20000)
    test.compare(str(findObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}").windowTitle), "Trades Window")
    test.compare(findObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}").floating, True)

@Then("Trades window dockable to top of the main workstation")
def step(context):
    #snooze(5)TODO
       
    test.compare(str(findObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}").windowTitle), "Trades Window")
    #test.compare(findObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}").floating, False)

@Then("Trades window dockable to bottom of the main workstation")
def step(context):
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseButtonPress, 834, 3, Qt.LeftButton, 1, 0)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 834, 5, Qt.NoButton, 1, 0)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 834, 7, Qt.NoButton, 1, 0)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 834, 9, Qt.NoButton, 1, 0)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 834, 11, Qt.NoButton, 1, 0)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 834, 13, Qt.NoButton, 1, 0)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 834, 16, Qt.NoButton, 1, 0)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 825, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -9, -11, 833, 18)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 825, -12, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -10, 0, 830, 35)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 824, -17, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 6, 830, 35)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, 17, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 46, 830, 75)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -12, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 57, 830, 86)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -13, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 67, 830, 96)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -12, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 78, 830, 107)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -12, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 89, 830, 130)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, 2, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 114, 830, 143)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -11, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 126, 830, 167)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -11, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 138, 830, 190)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, 0, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 161, 830, 190)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -12, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 172, 830, 201)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -11, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 184, 830, 225)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -11, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 196, 830, 240)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, 5, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -11, 224, 831, 284)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, 8, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -11, 255, 831, 299)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, 23, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -11, 270, 831, 299)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -9, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -11, 284, 831, 338)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, 2, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -11, 309, 831, 364)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, 3, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -11, 335, 831, 392)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, 5, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -11, 363, 831, 423)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, 8, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -11, 394, 831, 423)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -4, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -11, 413, 836, 488)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 831, 23, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -6, 459, 837, 501)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -10, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -5, 472, 837, 501)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -10, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -5, 485, 837, 529)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -8, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -5, 500, 837, 529)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -10, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -5, 513, 837, 542)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -8, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -5, 528, 837, 557)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -10, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -5, 541, 841, 586)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 830, -7, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -1, 557, 841, 586)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -10, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 0, 570, 842, 599)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -12, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 1, 581, 843, 610)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 831, -11, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 6, 593, 848, 622)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 830, -9, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 10, 607, 852, 636)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -14, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 616, 853, 645)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -14, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 625, 853, 654)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -15, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 633, 853, 662)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -14, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 642, 853, 671)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -12, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 653, 853, 682)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -14, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 662, 853, 691)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -12, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 673, 853, 702)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -12, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 684, 853, 713)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 824, -11, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 9, 696, 851, 725)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 825, -13, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 8, 706, 850, 735)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -15, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 8, 714, 850, 743)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -17, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 8, 720, 850, 749)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -18, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 8, 725, 850, 754)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -9, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 9, 739, 851, 768)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 828, -15, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 747, 853, 776)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 750, 853, 779)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -18, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 755, 853, 784)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -18, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 760, 853, 789)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -16, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 767, 853, 796)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -16, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 774, 853, 803)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -15, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 782, 853, 811)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 825, -15, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 10, 790, 852, 819)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -17, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 10, 796, 852, 825)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -18, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 10, 801, 852, 830)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 10, 803, 852, 832)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 10, 806, 852, 835)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 10, 808, 852, 837)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 11, 812, 853, 841)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 828, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 13, 816, 855, 845)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 828, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 15, 819, 857, 848)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 16, 823, 858, 852)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 829, -16, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 19, 830, 861, 859)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -17, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 20, 836, 862, 865)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 20, 839, 862, 868)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 20, 842, 862, 871)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 20, 844, 862, 873)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 21, 847, 863, 876)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 828, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 23, 849, 865, 878)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 23, 850, 865, 879)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 23, 851, 865, 880)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 23, 852, 865, 881)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 23, 854, 865, 883)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 24, 858, 866, 887)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 24, 861, 866, 890)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 24, 865, 866, 894)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 24, 869, 866, 898)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 24, 873, 866, 902)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -18, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 24, 878, 866, 907)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -15, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 25, 886, 867, 915)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 828, -15, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 894, 869, 923)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -17, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 900, 869, 929)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -17, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 906, 869, 935)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 910, 869, 939)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -18, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 915, 869, 944)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 918, 869, 947)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -16, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 925, 869, 954)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -18, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 930, 869, 959)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -17, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 936, 869, 965)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 940, 869, 969)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 944, 869, 973)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 947, 869, 976)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -17, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 27, 953, 869, 982)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 824, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 25, 957, 867, 986)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 822, -18, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 21, 962, 863, 991)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 819, -15, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 14, 970, 856, 999)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 819, -15, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 7, 978, 849, 1007)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 820, -16, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 1, 985, 843, 1014)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 820, -17, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -5, 991, 837, 1020)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 819, -16, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -12, 998, 830, 1027)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 820, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -18, 1002, 824, 1031)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 821, -18, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -23, 1007, 819, 1036)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 821, -18, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -28, 1012, 814, 1041)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 821, -19, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -33, 1016, 809, 1045)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 820, -18, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -39, 1021, 803, 1050)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 824, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -41, 1024, 801, 1053)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 824, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -43, 1025, 799, 1054)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 824, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -45, 1028, 795, 1060)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 824, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -47, 1031, 795, 1062)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -47, 1033, 795, 1062)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 824, -20, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -49, 1036, 793, 1067)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -49, 1038, 793, 1067)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 825, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -50, 1040, 791, 1070)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 825, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -51, 1041, 790, 1071)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 825, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -52, 1042, 790, 1071)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -52, 1043, 790, 1072)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 824, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -54, 1045, 788, 1074)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 824, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -56, 1047, 786, 1076)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 825, -23, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -57, 1047, 785, 1076)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -21, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -57, 1049, 785, 1078)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -57, 1050, 785, 1079)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -57, 1051, 785, 1080)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -57, 1052, 785, 1081)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -57, 1053, 785, 1082)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 826, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -57, 1054, 785, 1083)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 828, -22, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -55, 1055, 787, 1084)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -23, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -54, 1055, 788, 1084)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 828, -23, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -52, 1055, 790, 1084)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 827, -23, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -51, 1055, 791, 1084)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseMove, 828, -23, Qt.NoButton, 1, 0)
#     sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -49, 1055, 793, 1084)
#     sendEvent("QMouseEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), QEvent.MouseButtonRelease, 826, -23, Qt.LeftButton, 0, 0)
    sendEvent("QMoveEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), -16, 560, 795, 1086)
    #waitFor("object.exists('{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}')", 20000)
    test.compare(str(findObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}").windowTitle), "Trades Window")
    #Todo
    #test.compare(findObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}").floating, False)

@When("user select tabbed menu in the trades window right click menu item")
def step(context):
    mouseClick(waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 258, 14, 0, Qt.LeftButton)
    mouseClick(waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='1'}"), 258, 14, 0, Qt.RightButton)
    activateItem(waitForObjectItem("{type='QMenu' unnamed='1' visible='1'}", "Tabbed"))
    sendEvent("QContextMenuEvent", waitForObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='0' window=':SurveillanceWorkstationClass_MainWnd'}"), QContextMenuEvent.Mouse, 258, 14, 0)
    
    test.compare(findObject("{name?='TradesWindow.*' type='sp2::QDockWidgetEx' visible='0' window=':SurveillanceWorkstationClass_MainWnd'}").floating, False)

@Then("trades window should attached to main workstaion as tab window")
def step(context):
    waitFor("object.exists(':Trades_TabItem')", 20000)
    test.compare(findObject(":Trades_TabItem").enabled, True)
    test.compare(findObject(":Trades_TabItem").type, "TabItem")
    test.compare(findObject(":Trades_TabItem").text, "Trades")


@Step("user adds required filter fields from table settings")
def step(context):
    clickButton(waitForObject(":ftmTableTitlebar.btnTableOptions_QPushButton"))
    waitForObjectItem(":frame.lstAllColumns_QTableWidget", "0/0")
    clickItem(":frame.lstAllColumns_QTableWidget", "0/0", 166, 8, 0, Qt.LeftButton)
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    type(waitForObject(":frame.lstAllColumns_QTableWidget"), "<Down>")
    waitForObjectItem(":frame.lstAllColumns_QTableWidget", "24/0")
    doubleClickItem(":frame.lstAllColumns_QTableWidget", "24/0", 71, 11, 0, Qt.LeftButton)
    scrollTo(waitForObject(":lstAllColumns_QScrollBar"), 55)
    waitForObjectItem(":frame.lstAllColumns_QTableWidget", "64/0")
    doubleClickItem(":frame.lstAllColumns_QTableWidget", "64/0", 85, 10, 0, Qt.LeftButton)
    scrollTo(waitForObject(":lstAllColumns_QScrollBar"), 61)
    waitForObjectItem(":frame.lstAllColumns_QTableWidget", "69/0")
    doubleClickItem(":frame.lstAllColumns_QTableWidget", "69/0", 64, 10, 0, Qt.LeftButton)
    waitForObjectItem(":frame.lstAllColumns_QTableWidget", "70/0")
    doubleClickItem(":frame.lstAllColumns_QTableWidget", "70/0", 66, 10, 0, Qt.LeftButton)
    clickButton(waitForObject(":frame_3.btnOK_QPushButton"))
    
    

@When("user right click on Trade and select 'Live Order Book' option")
def step(context):
    openItemContextMenu(waitForObject(":vSplitterTableAndGraph.Trades_sp2::SpatialTableView"), "0/0", 41, 11, 0)
    activateItem(waitForObjectItem(":_QMenu", "View Live Order Book"))
# 
#     openItemContextMenu(waitForObject(":splitTableAndGraph.Trades_sp2::SpatialTableView"), "0/0", 40, 13, 0)
#     activateItem(waitForObjectItem(":_QMenu", "View Live Order Book"))

@Then("new tab should open with Live Orders For '([^']*)'", regexp=True)
def step(context, Instrument):
    Instrument=multipleFilterProccessor(varDict,Instrument,'|')
    waitFor("object.exists(': Order Book for Instrument ID : STAF1002_TabItem')", 20000)
    #test.compare(findObject("{container=':sp2WindowsView_QTabBar' text?=' Order Book for Instrument ID : "+Instrument+"' type='TabItem'}").text, " Order Book for Instrument ID : "+Instrument+"")
    test.compare(str(waitForObjectExists(":frmOBCtrlTitle.lblOBInstrumentID_QLabel_11").text), Instrument)


@Then("system should return respective Live Orders for the '|any|'")
def step(context, Instrument):
    
    Instrument=multipleFilterProccessor(varDict,Instrument,'|') 
    waitFor("object.exists(':frmOBCtrlTitle.lblOBInstrumentID_QLabel_7')", 20000)
    test.compare(str(findObject(":frmOBCtrlTitle.lblOBInstrumentID_QLabel_7").text), Instrument)
      
    
@Then("system should return an error message of '|any|' in the trades pane")
def step(context, error):
    try:
        if len(context.userData) !=0:
            test.compare(str(context.userData[0]), error)
        else:
            raise Exception
    except Exception, err:
        test.fail("Exception in error message comparison", str(err))
#     
#     
#     
#     waitFor("object.exists(':No Data_QMessageBox')", 20000)
#     test.compare(findObject(":No Data_QMessageBox").visible, True)
#     test.compare(str(findObject(":No Data_QMessageBox").windowTitle), "No Data")
#     test.compare(findObject(":No Data_QMessageBox").enabled, True)
#     waitFor("object.exists(':sp2WindowsView.qt_msgbox_label_QLabel')", 20000)
#     test.compare(str(findObject(":sp2WindowsView.qt_msgbox_label_QLabel").text), ErrorMessage)
#     sendEvent("QMouseEvent", waitForObject(":No Data_QMessageBox"), QEvent.MouseMove, 306, 32, Qt.NoButton, 1, 0)
#     clickButton(waitForObject(":sp2WindowsView.OK_QPushButton"))


@Then("user look for default filter fields of 'TradesWindow/defaultFilterFields.csv'")
def step(context):
    waitFor("object.exists(':frmFilterHolder.lblInstrument_QLabel_2')", 20000)
    test.compare(findObject(":frmFilterHolder.lblInstrument_QLabel_2").enabled, True)
    waitFor("object.exists(':frmFilterHolder.lblExecType_QLabel')", 20000)
    test.compare(findObject(":frmFilterHolder.lblExecType_QLabel").enabled, True)
    waitFor("object.exists(':frmFilterHolder.cmbExecType_QComboBox')", 20000)
    test.compare(findObject(":frmFilterHolder.cmbExecType_QComboBox").enabled, True)
    test.compare(findObject(":frmFilterHolder.cmbExecType_QComboBox").editable, False)
    waitFor("object.exists(':frmFilterHolder.lblTadeType_QLabel')", 20000)
    test.compare(findObject(":frmFilterHolder.lblTadeType_QLabel").enabled, True)
    waitFor("object.exists(':frmFilterHolder.cmbTradeType_QComboBox')", 20000)
    test.compare(findObject(":frmFilterHolder.cmbTradeType_QComboBox").editable, False)
    test.compare(findObject(":frmFilterHolder.cmbTradeType_QComboBox").enabled, True)
    waitFor("object.exists(':frmFilterHolder.lblTradeSubType_QLabel')", 20000)
    test.compare(findObject(":frmFilterHolder.lblTradeSubType_QLabel").enabled, True)
    waitFor("object.exists(':frmFilterHolder.cmbTradeSubType_QComboBox')", 20000)
    test.compare(findObject(":frmFilterHolder.cmbTradeSubType_QComboBox").enabled, True)
    test.compare(findObject(":frmFilterHolder.cmbTradeSubType_QComboBox").editable, False)
    waitFor("object.exists(':gbxTraderID.lblBuyTrader_QLabel')", 20000)
    test.compare(findObject(":gbxTraderID.lblBuyTrader_QLabel").enabled, True)
    waitFor("object.exists(':gbxTraderID.btnBuyTraderSelector_QPushButton')", 20000)
    test.compare(findObject(":gbxTraderID.btnBuyTraderSelector_QPushButton").enabled, True)
    waitFor("object.exists(':gbxTraderID.lblTraderIDOperator_QLabel')", 20000)
    test.compare(findObject(":gbxTraderID.lblTraderIDOperator_QLabel").enabled, True)
    waitFor("object.exists(':gbxTraderID.cmbTraderOperator_QComboBox')", 20000)
    test.compare(findObject(":gbxTraderID.cmbTraderOperator_QComboBox").enabled, True)
    test.compare(findObject(":gbxTraderID.cmbTraderOperator_QComboBox").editable, False)
    waitFor("object.exists(':gbxTraderID.lblSellTrader_QLabel')", 20000)
    test.compare(findObject(":gbxTraderID.lblSellTrader_QLabel").enabled, True)
    waitFor("object.exists(':gbxTraderID.btnSellTraderSelector_QPushButton')", 20000)
    test.compare(findObject(":gbxTraderID.btnSellTraderSelector_QPushButton").enabled, True)
    waitFor("object.exists(':gbxTraderID.txtBuyTrader_LineEditEx')", 20000)
    test.compare(findObject(":gbxTraderID.txtBuyTrader_LineEditEx").enabled, True)
    waitFor("object.exists(':gbxTraderID.txtSellTrader_LineEditEx')", 20000)
    test.compare(findObject(":gbxTraderID.txtSellTrader_LineEditEx").enabled, True)
    waitFor("object.exists(':gbxFirmID.txtSellFirm_LineEditEx')", 20000)
    test.compare(findObject(":gbxFirmID.txtSellFirm_LineEditEx").enabled, True)
    waitFor("object.exists(':gbxFirmID.txtBuyFirm_LineEditEx')", 20000)
    test.compare(findObject(":gbxFirmID.txtBuyFirm_LineEditEx").enabled, True)
    waitFor("object.exists(':gbxFirmID.btnSellFirmSelector_QPushButton')", 20000)
    test.compare(findObject(":gbxFirmID.btnSellFirmSelector_QPushButton").enabled, True)
    waitFor("object.exists(':gbxFirmID.lblSellFirm_QLabel')", 20000)
    test.compare(findObject(":gbxFirmID.lblSellFirm_QLabel").enabled, True)
    waitFor("object.exists(':gbxFirmID.cmbFirmOperator_QComboBox')", 20000)
    test.compare(findObject(":gbxFirmID.cmbFirmOperator_QComboBox").enabled, True)
    test.compare(findObject(":gbxFirmID.cmbFirmOperator_QComboBox").editable, False)
    waitFor("object.exists(':gbxFirmID.lblFirmOperator_QLabel')", 20000)
    test.compare(findObject(":gbxFirmID.lblFirmOperator_QLabel").enabled, True)
    waitFor("object.exists(':gbxFirmID.btnBuyFirmSelector_QPushButton')", 20000)
    test.compare(findObject(":gbxFirmID.btnBuyFirmSelector_QPushButton").enabled, True)
    waitFor("object.exists(':gbxFirmID.lblBuyFirm_QLabel')", 20000)
    test.compare(findObject(":gbxFirmID.lblBuyFirm_QLabel").enabled, True)
    waitFor("object.exists(':gbxClientID.lblBuyClient_QLabel')", 20000)
    test.compare(findObject(":gbxClientID.lblBuyClient_QLabel").enabled, True)
    waitFor("object.exists(':gbxClientID.cmbClientOperator_QComboBox')", 20000)
    test.compare(findObject(":gbxClientID.cmbClientOperator_QComboBox").editable, False)
    test.compare(findObject(":gbxClientID.cmbClientOperator_QComboBox").enabled, True)
    waitFor("object.exists(':gbxClientID.lblClientOperator_QLabel')", 20000)
    test.compare(findObject(":gbxClientID.lblClientOperator_QLabel").enabled, True)
    waitFor("object.exists(':gbxClientID.txtBuyClient_LineEditEx')", 20000)
    test.compare(findObject(":gbxClientID.txtBuyClient_LineEditEx").enabled, True)
    waitFor("object.exists(':gbxClientID.txtSellClient_LineEditEx')", 20000)
    test.compare(findObject(":gbxClientID.txtSellClient_LineEditEx").enabled, True)
    waitFor("object.exists(':gbxTradePrice.lblTradePriceFrom_QLabel')", 20000)
    test.compare(findObject(":gbxTradePrice.lblTradePriceFrom_QLabel").enabled, True)
    waitFor("object.exists(':gbxTradePrice.txtTradePriceFrom_QLineEdit')", 20000)
    test.compare(findObject(":gbxTradePrice.txtTradePriceFrom_QLineEdit").enabled, True)
    waitFor("object.exists(':gbxTradePrice.lblTradePriceTo_QLabel')", 20000)
    test.compare(findObject(":gbxTradePrice.lblTradePriceTo_QLabel").enabled, True)
    waitFor("object.exists(':gbxTradePrice.txtTradePriceTo_QLineEdit')", 20000)
    test.compare(findObject(":gbxTradePrice.txtTradePriceTo_QLineEdit").enabled, True)
    waitFor("object.exists(':gbxTradeSize.txtTradeSizeFrom_QLineEdit')", 20000)
    test.compare(findObject(":gbxTradeSize.txtTradeSizeFrom_QLineEdit").enabled, True)
    waitFor("object.exists(':gbxTradeSize.lblTradeSizeTo_QLabel')", 20000)
    test.compare(findObject(":gbxTradeSize.lblTradeSizeTo_QLabel").enabled, True)
    waitFor("object.exists(':gbxTradeSize.txtTradeSizeTo_QLineEdit')", 20000)
    test.compare(findObject(":gbxTradeSize.txtTradeSizeTo_QLineEdit").enabled, True)
    waitFor("object.exists(':gbxTradeSize.lblTradeSizeFrom_QLabel')", 20000)
    test.compare(findObject(":gbxTradeSize.lblTradeSizeFrom_QLabel").enabled, True)
    waitFor("object.exists(':frmFilterHolder.lblTradeReportLInkID_QLabel')", 20000)
    test.compare(findObject(":frmFilterHolder.lblTradeReportLInkID_QLabel").enabled, True)
    waitFor("object.exists(':frmFilterHolder.txtTradeReportLinkID_QLineEdit')", 20000)
    test.compare(findObject(":frmFilterHolder.txtTradeReportLinkID_QLineEdit").enabled, True)
    waitFor("object.exists(':frmFilterHolder.lblTradeReportID_QLabel_2')", 20000)
    test.compare(findObject(":frmFilterHolder.lblTradeReportID_QLabel_2").enabled, True)
    waitFor("object.exists(':frmFilterHolder.txtTradeReportID_QLineEdit_2')", 20000)
    test.compare(findObject(":frmFilterHolder.txtTradeReportID_QLineEdit_2").enabled, True)
    waitFor("object.exists(':gbxDuration.lblFromDuration_QLabel')", 20000)
    test.compare(findObject(":gbxDuration.lblFromDuration_QLabel").enabled, True)
    waitFor("object.exists(':gbxDuration.dtFromDurationTime_QTimeEdit_2')", 20000)
    test.compare(str(findObject(":gbxDuration.dtFromDurationTime_QTimeEdit_2").displayFormat), "HH:mm:ss.zzz")
    test.compare(findObject(":gbxDuration.dtFromDurationTime_QTimeEdit_2").enabled, True)
    waitFor("object.exists(':gbxDuration.lblToDuration_QLabel')", 20000)
    test.compare(findObject(":gbxDuration.lblToDuration_QLabel").enabled, True)
    waitFor("object.exists(':gbxDuration.dtToDurationDate_QDateEdit_2')", 20000)
    test.compare(str(findObject(":gbxDuration.dtToDurationDate_QDateEdit_2").displayFormat), "dd/MM/yyyy")
    test.compare(findObject(":gbxDuration.dtToDurationDate_QDateEdit_2").enabled, True)
    waitFor("object.exists(':gbxDuration.dtToDurationDateTime_QTimeEdit_2')", 20000)
    test.compare(str(findObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2").displayFormat), "HH:mm:ss.zzz")
    test.compare(findObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2").enabled, True)
    waitFor("object.exists(':gbxDuration.dtFromDurationDate_QDateEdit_2')", 20000)
    test.compare(findObject(":gbxDuration.dtFromDurationDate_QDateEdit_2").enabled, True)
    test.compare(str(findObject(":gbxDuration.dtFromDurationDate_QDateEdit_2").displayFormat), "dd/MM/yyyy")
    waitFor("object.exists('::frmFilterHolder.txtInstrument_LineEditEx')", 20000)
    test.compare(findObject("::frmFilterHolder.txtInstrument_LineEditEx").enabled, True)



@When("user types '|any|' value in Trades View-InstrumentId then respective list which start with these values should return")
def step(context,word):
    try:
        word=multipleFilterProccessor(varDict,word,'|') 
        #test.warning("TODO implement user types 'INSD' value in Trades View-InstrumentId then respective list which start with these values should return")
        mouseClick(waitForObject("::frmFilterHolder.txtInstrument_LineEditEx"), 25, 14, 0, Qt.LeftButton)
        type(waitForObject("::frmFilterHolder.txtInstrument_LineEditEx"), word)
        type(waitForObject(":_QListView"), "<Down>")
        type(waitForObject(":_QListView"), "<Down>")
        type(waitForObject(":_QListView"), "<Down>")
        type(waitForObject(":_QListView"), "<Down>")
        type(waitForObject(":_QListView"), "<Down>")
        type(waitForObject(":_QListView"), "<Enter>")
        
        if searchSome(word,str(findObject("::frmFilterHolder.txtInstrument_LineEditEx").displayText))==True:
            pass
        else:
            test.fail("String not found in Autocomplete List")
    except Exception,err:
        test.fail("Unexpected error in Autocomplete", str(err))
        
@Then("user look for default Table fields of 'TradesWindow/defaultTableFields.csv'")
def step(context):
    for record in testData.dataset("TradesWindow/defaultTableFields.csv"):
        column1 = testData.field(record, "column1")
        column2 = testData.field(record, "column2")
        column3 = testData.field(record, "column3")
        column4 = testData.field(record, "column4")
        column5 = testData.field(record, "column5")
        column6 = testData.field(record, "column6")
        column7 = testData.field(record, "column7")
        column8 = testData.field(record, "column8")
        column9 = testData.field(record, "column9")
        column10 = testData.field(record, "column10")
        column11 = testData.field(record, "column11")
        column12 = testData.field(record, "column12")
        column13 = testData.field(record, "column13")
        column14 = testData.field(record, "column14")
        column15 = testData.field(record, "column15")
        column16 = testData.field(record, "column16")
    
        
    test.compare(waitForObjectExists(":Symbol_HeaderViewItem_2").text, column1)
    test.compare(waitForObjectExists(":Trade Report ID_HeaderViewItem_2").text, column2)
    test.compare(waitForObjectExists(":Trade Status_HeaderViewItem").text, column3)
    test.compare(waitForObjectExists(":Execution Type_HeaderViewItem_2").text, column4)
    test.compare(waitForObjectExists(":Executed Qty_HeaderViewItem").text, column5)
    test.compare(waitForObjectExists(":Executed Value_HeaderViewItem").text, column6)    
    test.compare(waitForObjectExists(":Buy Broker ID_HeaderViewItem").text, column7)
    test.compare(waitForObjectExists(":Sell Broker ID_HeaderViewItem").text, column8)
    test.compare(waitForObjectExists(":Buy Trader ID_HeaderViewItem").text, column9)
    test.compare(waitForObjectExists(":Sell Trader ID_HeaderViewItem").text, column10)    
    test.compare(waitForObjectExists(":Buy Client ID_HeaderViewItem").text, column11)
    test.compare(waitForObjectExists(":Sell Client ID_HeaderViewItem").text, column12)
    test.compare(waitForObjectExists(":Buy Order ID_HeaderViewItem").text, column13)
    test.compare(waitForObjectExists(":Sell Order ID_HeaderViewItem").text, column14)
    test.compare(waitForObjectExists(":Aggressor Side_HeaderViewItem").text, column15)
    test.compare(waitForObjectExists(":Transact Time_HeaderViewItem_2").text, column16)   
  

@Given("user clean mismatch json files in 'TradesWindow' expected results")
def step(context):
    #test.warning("TODO implement user clean mismatch json files in 'TradesWindow' expected results")  
    test.log(getDictValue(varDict,'tradesExResFiles'))
    jsonFilePath=getDictValue(varDict,'tradesExResFiles')
    test.log(str(removeFiles(jsonFilePath,"*.json")))
        

@Then("user pick '|any|' of first & fifth record")
def step(context,TransactTime):
    context.userData=[]
    col=findColumn(TransactTime,":Trades_QHeaderView") 
    scrollTo(waitForObject(":Trades_QScrollBar"), 1)
    #context.userData.append(waitForObjectExists(":Trades.0_15_QModelIndex").text)
    #context.userData.append(waitForObjectExists(":Trades.5_15_QModelIndex").text)
    
    startTime=waitForObjectExists("{column='"+str(col)+"' container=':vSplitterTableAndGraph.Trades_sp2::SpatialTableView' row='0' type='QModelIndex'}").text
    endTime=waitForObjectExists("{column='"+str(col)+"' container=':vSplitterTableAndGraph.Trades_sp2::SpatialTableView' row='4' type='QModelIndex'}").text
    
    context.userData=extractDateTime(startTime,endTime)
    test.log(str(context.userData))
    snooze(2)


@Then("user apply duration filter values at millisecond precision")
def step(context):
    dateFrom=str(context.userData[0])
    timeFrom=str(context.userData[1])
    dateTo=str(context.userData[2])
    timeTo=str(context.userData[3])
    
    mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_DateFrom"), 16, 7, -13, 3, 1, Qt.LeftButton)
    type(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_DateFrom"), dateFrom)

    mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_6"), 16, 10, -18, -4, 1, Qt.LeftButton)
    type(waitForObject(":gbxDuration.dtFromDurationTime_QTimeEdit_2"), timeFrom)
    

    mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_7"), 16, 6, -12, 2, 1, Qt.LeftButton)
    type(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_7"), dateTo) 



    mouseDrag(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_8"), 13, 9, -23, 0, 1, Qt.LeftButton)
    type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), timeTo)
#     type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), "<Keypad_1>")
#     type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), "<Keypad_4>")
#     type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), "<Keypad_4>")
#     type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), "<Keypad_2>")
#     type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), "<Keypad_1>")
#     type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), "<Keypad_7>")
#     type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), "<Keypad_8>")
#     type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), "<Keypad_1>")
# 
#     mouseClick(waitForObject(":gbxDuration.qt_spinbox_lineedit_QLineEdit_8"), 6, 9, 0, Qt.LeftButton)
#     type(waitForObject(":gbxDuration.dtToDurationDateTime_QTimeEdit_2"), )


@Then("user adds required trades filter fields from table settings")
def step(context):
    clickButton(waitForObject(":frmSubTitleBar.btnTableOptions_QPushButton_2"))
    waitForObjectItem(":frame.lstAllColumns_QTableWidget", "0/0")
    clickItem(":frame.lstAllColumns_QTableWidget", "0/0", 142, 5, 0, Qt.LeftButton)
    waitForObjectItem(":frame.lstAllColumns_QTableWidget", "70/0")
    doubleClickItem(":frame.lstAllColumns_QTableWidget", "70/0", 71, 11, 0, Qt.LeftButton)
    waitForObjectItem(":frame.lstAllColumns_QTableWidget", "69/0")
    doubleClickItem(":frame.lstAllColumns_QTableWidget", "69/0", 109, 8, 0, Qt.LeftButton)    
    clickButton(waitForObject(":frame_3.btnOK_QPushButton"))



@Then("new trades tab window should open with saved values")
def step(context):
    test.compare(waitForObjectExists(":Trades_TabItem_2").text, "Trades")
    test.compare(waitForObjectExists(":Trades_TabItem_2").type, "TabItem")
    test.compare(waitForObjectExists(":Trades_TabItem_2").enabled, True)
    
@When("user clicks ascending on '|any|' column")
def step(context,colName):
   
    mouseClick(waitForObject("{container=':Trades_QHeaderView' text?='"+colName+"' type='HeaderViewItem' visible='true'}"), 42, 10, 0, Qt.LeftButton)
#     mouseClick(waitForObject(":Executed Value_HeaderViewItem_2"), 42, 10, 0, Qt.LeftButton)
#     sendEvent("QWheelEvent", waitForObject(":vSplitterTableAndGraph.Trades_sp2::SpatialTableView"), 583, 15, 120, 0, 2)
#     sendEvent("QWheelEvent", waitForObject(":vSplitterTableAndGraph.Trades_sp2::SpatialTableView"), 581, 15, 120, 0, 2)
#     sendEvent("QWheelEvent", waitForObject(":vSplitterTableAndGraph.Trades_sp2::SpatialTableView"), 577, 13, 120, 0, 2)
#     mouseClick(waitForObject(":Executed Value_HeaderViewItem_2"), 72, 9, 0, Qt.LeftButton)
#     mouseClick(waitForObject(":Executed Value_HeaderViewItem_2"), 73, 9, 0, Qt.LeftButton)
# 
#     mouseClick(waitForObject("{container=':Trades_QHeaderView' text='"+colName+"' type='HeaderViewItem' visible='true'}"), 74, 12, 0, Qt.LeftButton)
    #mouseClick(waitForObject("{text='"+colName+"' type='HeaderViewItem' visible='true'}"), 74, 12, 0, Qt.LeftButton)

def step(context):
    test.vp("AssendingTradesTable")

@When("user clicks descending on 'Value' column")
def step(context):
    mouseClick(waitForObject(":Executed Value_HeaderViewItem"), 84, 11, 0, Qt.LeftButton)

@Then("trades should reorder in descending order by value")
def step(context):
    test.vp("decendingTradesTable")

@When("user clicks on Show Table Only button")
def step(context):
    clickButton(waitForObject(":frmSubTitleBar.btnShowOnlyTable_QPushButton"))

@Then("only the result table & analytics pane should be fully visible")
def step(context):
    test.compare(waitForObjectExists(":_QGraphicsRectItem_3").enabled, True)
    test.compare(waitForObjectExists(":_QGraphicsRectItem_3").visible, True)
    test.compare(waitForObjectExists(":vSplitterTableAndGraph.Orders_sp2::SpatialTableView").enabled, True)
    test.compare(waitForObjectExists(":vSplitterTableAndGraph.Orders_sp2::SpatialTableView").visible, True)


@When("there are no system errors")
def step(context):
    
    if waitFor("object.exists(':No Data_QMessageBox')", 2000) == True:
        testSettings.logScreenshotOnFail = True
        test.fail("Unexpected Error")
        testSettings.logScreenshotOnFail = False
                #test.compare(findObject(":No Data_QMessageBox").enabled, True)
    elif waitFor("object.exists(':Warning_QMessageBox')",2000) ==True:
        testSettings.logScreenshotOnFail = True
        test.fail("Unexpected Error")
        testSettings.logScreenshotOnFail = False
        
    elif waitFor("object.exists(':Data Unavailable_QMessageBox')", 2000) == True:
        testSettings.logScreenshotOnFail = True
        test.fail("Unexpected Error")
        testSettings.logScreenshotOnFail = False
        #test.compare(findObject(":Warning_QMessageBox").enabled, True)
    else:
        try:
            if len(context.userData) !=0:
                #Look for System Errors
                for record in testData.dataset("EnvironmentDetails/systemErrors.csv"):
                    error = testData.field(record, "error")
                    if error in context.userData:   
                        raise Exception                   
            else:
                pass
        except Exception, err:
            
            test.log(str(context.userData[0]))
            test.fail("System Error..!!!", str(err))

        
        

@When("user selects 'Actively Participated Instruments' from Analytics")
def step(context):
    sendEvent("QMouseEvent", waitForObject(":frmSubTitleBar.btnAnalytics_QPushButton"), QEvent.MouseButtonPress, 14, 12, Qt.LeftButton, 1, 0)
    activateItem(waitForObjectItem(":AnalyticsMenu_QMenu", "Actively Participated Instruments"))



@When("user clicks on save filter button on second view")
def step(context):
    sendEvent("QMouseEvent", waitForObject(":frame.btnDumpToFile_QPushButton_4"), QEvent.MouseButtonPress, 55, 21, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(":frame.btnDumpToFile_QPushButton_4"), QEvent.MouseButtonRelease, 55, 21, Qt.LeftButton, 0, 0)


@When("user clicks on Orders multiple Firm selector")
def step(context):
    test.warning("TODO implement user clicks on Orders multiple Firm selector")
    test.fail("Not Implemented")


@When("user clicks on Orders multiple Trader selector")
def step(context):
    pass


@When("user clicks on 'Custom Sort' button")
def step(context):
    sendEvent("QMouseEvent", waitForObject(":frmSubTitleBar.btnMultipleColumnSort_QPushButton"), QEvent.MouseButtonPress, 9, 15, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(":frmSubTitleBar.btnMultipleColumnSort_QPushButton"), QEvent.MouseButtonRelease, 9, 15, Qt.LeftButton, 0, 0)
    #mouseClick(waitForObject(":frmSubTitleBar.btnMultipleColumnSort_QPushButton"), QEvent.MouseButtonPress, 9, 15, Qt.LeftButton, 1, 0)

@Then("'Custom Sort' Window should appear")
def step(context):
    test.compare(waitForObjectExists(":spMultipleColumnSortDlg_sp2::MultipleColumnSortDlg").enabled, True)
    sendEvent("QMouseEvent", waitForObject(":spMultipleColumnSortDlg_sp2::MultipleColumnSortDlg"), QEvent.MouseMove, 128, 105, Qt.NoButton, 1, 0)    



#@Then("user selects 'executed_value','executed_qty','instrument_id' in 'Ascending' order")
@Then("user selects multiple values in 'Ascending' order")
def step(context):
    
    context.userData="" 
    pipe="|"
    table = context.table
    # Drop initial row with column headers
    table.pop(0)
    mouseClick(waitForObject(":Trades.cmbColumn_QComboBox"), 168, 14, 0, Qt.LeftButton)
    colCmb=waitForObject(":Trades.cmbColumn_QComboBox")
 
    for (value,sort_in) in table:
#         for index in range(colCmb.count):
#             if colCmb.currentText == value:
#                 colCmb.setCurrentIndex(index)
        mouseClick(waitForObjectItem(":Trades.cmbColumn_QComboBox", value.replace("_","\\_")), 84, 3, 0, Qt.LeftButton)
        mouseClick(waitForObject(":Trades.cmbOrder_QComboBox"), 104, 10, 0, Qt.LeftButton)
        mouseClick(waitForObjectItem(":Trades.cmbOrder_QComboBox", sort_in), 59, 10, 0, Qt.LeftButton)
        clickButton(waitForObject(":Trades.btnAdd_QToolButton"))
   
                        
          
@Then("clicks on 'Sort' button")
def step(context):
    clickButton(waitForObject(":Trades.pushButton_6_QPushButton"))

@When("user Select draw tracker toggle option")
def step(context):
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 773, 82, 0, Qt.LeftButton)
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 1241, 76, 0, Qt.LeftButton)
    sendEvent("QMouseEvent", waitForObject(":ftmGraphTitlebar.btnGraphOptions_QPushButton"), QEvent.MouseButtonPress, 4, 19, Qt.LeftButton, 1, 0)
    clickButton(waitForObject(":ftmGraphTitlebar.chxDrawGrahpTracker_QCheckBox"))
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 940, 172, 0, Qt.LeftButton)
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 877, 213, 0, Qt.LeftButton)
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 449, 152, 0, Qt.LeftButton)
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 469, 59, 0, Qt.LeftButton)
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 1054, 68, 0, Qt.LeftButton)
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 1411, 379, 0, Qt.LeftButton)

    

@Then("tracker should be available")
def step(context):
    testSettings.logScreenshotOnPass= True
    test.compare("1", "1", "Get the ss to compare the Alert View tile" )
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 915, 126, 0, Qt.LeftButton)
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 708, 142, 0, Qt.LeftButton)


@When("user select Draw points option")
def step(context):
    sendEvent("QKeyEvent", waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), QEvent.KeyPress, 16777251, 0, 0, "", False, 1)
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 812, 104, 0, Qt.LeftButton)
    sendEvent("QMouseEvent", waitForObject(":ftmGraphTitlebar.btnGraphOptions_QPushButton"), QEvent.MouseButtonPress, 7, 12, Qt.LeftButton, 1, 0)
    clickButton(waitForObject(":ftmGraphTitlebar.cbxDrawPoints_QCheckBox"))
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 797, 383, 0, Qt.LeftButton)
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 54, 387, 0, Qt.LeftButton)
    mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 1467, 387, 0, Qt.LeftButton)
    testSettings.logScreenshotOnPass= True
    test.compare("1", "1", "Get the ss to compare the Alert View tile" )
    

@Then("points should be available in the graph")
def step(context):
    testSettings.logScreenshotOnPass= True
    test.compare("1", "1", "Get the ss to compare the Alert View tile" )
    

@Then("price series should be disbale")
def step(context):
    testSettings.logScreenshotOnPass= True
    test.compare("1", "1", "Get the ss to compare the Alert View tile" )

@When("user right click on analytic pane")
def step(context):
    snooze(5)
    mouseClick(waitForObject(":_QtCharts::PieChartItem_5"), 349, 69, 0, Qt.LeftButton)
    openContextMenu(waitForObject(":_QtCharts::LegendScroller"), 103, 109, 0)

@Then("analytic should drill down to its second level")
def step(context):
    snooze(10)
    mouseClick(waitForObject(":_QtCharts::LegendScroller"), 60, 52, 0, Qt.LeftButton)

@When("user change the range as '|any|' to '|any|'")
def step(context,max_value,min_value):
    #mouseClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 27, 89, 0, Qt.LeftButton)
    #doubleClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 23, 18, 67108864, Qt.LeftButton)
    type(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), "<Ctrl>")
    #keyPress("<Ctrl>")
    sendEvent("QKeyEvent", waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), QEvent.KeyPress, 16777249, 0, 0, "", False, 1)
    doubleClick(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer", 23, 18, 67108864, Qt.LeftButton)
    #keyRelease("<Ctrl>")
    mouseDrag(waitForObject(":BoundryChange.txtFrom_QLineEdit"), 43, 10, -56, -4, 1, Qt.LeftButton)
    type(waitForObject(":BoundryChange.txtFrom_QLineEdit"), min_value)
    type(waitForObject(":BoundryChange.txtFrom_QLineEdit"), "<Tab>")
    type(waitForObject(":BoundryChange.txtTo_QLineEdit"), max_value)
    clickButton(waitForObject(":BoundryChange.btnOk_QPushButton"))

@Then("range should be available as '10000' to '1000'")
def step(context):
    testSettings.logScreenshotOnPass= True
    test.compare("1", "1", "Get the ss to compare the Alert View tile" )


@When("user change the range of volume axis as '|any|' to '|any|'")
def step(context,max_value,min_value):
    sendEvent("QKeyEvent", waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), QEvent.KeyPress, 16777249, 0, 0, "", False, 1)
    doubleClick(waitForObject(":frmLineChartPH.TradePriceGraph_ssgraph::GraphContainer"), 1489, 17, 67108864, Qt.LeftButton)
    mouseDrag(waitForObject(":BoundryChange.txtFrom_QLineEdit"), 42, 6, -53, -5, 1, Qt.LeftButton)
    type(waitForObject(":BoundryChange.txtFrom_QLineEdit"), min_value)
    type(waitForObject(":BoundryChange.txtFrom_QLineEdit"), "<Tab>")
    type(waitForObject(":BoundryChange.txtTo_QLineEdit"), max_value)
    clickButton(waitForObject(":BoundryChange.btnOk_QPushButton"))
