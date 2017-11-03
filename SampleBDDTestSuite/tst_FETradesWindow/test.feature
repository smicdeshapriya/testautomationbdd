# This is a sample .feature file
# You can find a more extensive introduction to the Gherkin format at
# https://github.com/cucumber/cucumber/wiki/Gherkin

Feature: Trades Window

    #------------------[Querying and Filtering Trades]------------------------------------------------

    ################-------------------------------Instrument Filter-----------------------------------------------------------

    # @SendTrades
    # Scenario: OWTS_000-Send Trades to the exchange
    #  Given user send orders to the exchange by 'iteCompleteTest.cmd' in 'sikulixPath' using 'iteTrades_Fil_PFill.sikuli'

    #@Cleanup
    #Scenario: OWTS_000-Clean dynamiclally generated objects & files
    #Given user clean mismatch json files in 'TradesWindow' expected results


    @Regression
    @Positive
    @Seatrial
    @Smoke
    Scenario: TWTS_001-Layout of Trades window

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button


    @Regression
    @Positive
    @Seatrial
    @Smoke
    Scenario Outline: TWTS_002-Querying and Filtering Trades for single instrument-positive

        #Given user send new buy Trades to the exchange using sikulix -platformtheme none
        Given user deletes '<ActualResult>' and '<ExpectedResult>' data tables from 'STAF.db'
        Given user clean mismatch json files in 'TradesWindow' expected results
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user close all open tabs
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        #When user enter filter values
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        #And user adds required trades filter fields from table settings
        And user export result into '<ActualResult>' csv file in the 'qaTest' folder
        #Then user writes '<ExpectedResult>.csv' data into the database 'STAF.db'
        Then user writes '<ActualResult>' data into the database 'STAF.db'
        When DB 'STAF.db' writes selected 'tradeSqlFieldSet' values back to '<ActualResult>' after reordering by 'id'
        Then user compare '<ExpectedResult>.csv' in 'tradesExResFiles' and '<ActualResult>.csv' order by 'id'
        #Then user compare fields of 'TradesWindow/compareTradeColumns.csv' with '<ActualResult>' and '<ExpectedResult>' data tables in 'STAF.db'
        #Then user deletes 'actualTradeResult' and 'expectedTradeResult' data tables from 'STAF.db'
        #Then user logout from the appliaction


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            #|INS005|Fill|On Book|AT|TRD001|AND|TRD002|FRM003|AND|FRM001||||200|1000|1000|5000|||||||25|actualTradeResult|expectedTrades_INSCR87_01|
            #||||||||||||||||||||||110000000|235959999|25|actualTradeResult|expectedTrades_INSCR87_01|
            #|INS005|||||||||||||||||||SDATE|STIME|EDATE|ETIME|50|actualTradeResult|expectedTrades_INSCR87_01|
            |INS005|Fill||||||||||||||||||||||50|actualTradeResult|INS005_ALL|
            |INS005|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|50|actualTradeResult|INS005_ALL|
            |INS005|Fill|On Book|||||||||||||||||SDATE|STIME|EDATE|ETIME|50|actualTradeResult|INS005_ALL|
            |INS005|Fill|On Book|AT||||||||||||||||SDATE|STIME|EDATE|ETIME|50|actualTradeResult|INS005_ALL|
            |INS005|Fill|On Book|AT|TRD001|AND|TRD002|||||||||||||SDATE|STIME|EDATE|ETIME|50|actualTradeResult|INS005_ALL|
            |INS005|Fill|On Book|AT|TRD001|AND|TRD002|FRM003|AND|FRM001||||||||||SDATE|STIME|EDATE|ETIME|50|actualTradeResult|INS005_ALL|
            |INS005|Fill|On Book|AT|TRD001|AND|TRD002|FRM003|AND|FRM001||||100|1000|||||SDATE|STIME|EDATE|ETIME|50|actualTradeResult|INS005_ALL|
            |INS005|Fill|On Book|AT|TRD001|AND|TRD002|FRM003|AND|FRM001||||100|1000|1000|5000|||SDATE|STIME|EDATE|ETIME|50|actualTradeResult|INS005_ALL|





        @Regression
        @Negative
        @Seatrial
        @Smoke
        Scenario Outline: TWTS_003-Querying and Filtering Trades for single instrument-negative

        #Given user send new buy Trades to the exchange using sikulix
        Given user deletes 'actualTradeResult' and 'expectedTradeResult' data tables from 'STAF.db'
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        #When user enter filter values
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        Then system should return an error message of '<ErrorMessage>' in the trades pane

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|CustomFilter|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|ErrorMessage|
            |DUMMY||||||||||||||||||||SDATE|STIME|EDATE|ETIME|No Matching Records Found for Query Criteria|
            |||||||||||||||||||||SDATE|STIME|EDATE|ETIME|There must be at least one Instrument ID, Buy/Sell Firm ID, Trader ID or Client ID selected.|
            |INS005|||||||||||||1000|100|100|1000||||SDATE|STIME|EDATE|ETIME|'From' Trade Price cannot exceed 'To' Trade Price|
            |INS005|||||||||||||1|100|1000|100||||SDATE|STIME|EDATE|ETIME|'From' Trade Size cannot exceed 'To' Trade Size|
            |INS005||||||||||||||||||||01012099|STIME|01012050|ETIME|'From' Duration cannot exceed 'To' Duration|
            |INS005||||||||||||||||||||SDATE|101010111|EDATE|080808888|'From' Duration cannot exceed 'To' Duration|
      
      
      
        @Regression
        @Positive
        @Seatrial
        @Smoke
        Scenario Outline: TWTS_004-Querying and Filtering Trades for multiple instruments,Traders,Firms

        Given user deletes 'actualTradeResult' and 'expectedTradeResult' data tables from 'STAF.db'
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            |INS005,INS006,INS007,INS008|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|100|actualTradeResult|expectedTradeResult|

        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_004_01-Querying and Filtering Trades by applying all fields

        Given user deletes 'actualTradeResult' and 'expectedTradeResult' data tables from 'STAF.db'
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        #When user enter filter values
        Then user opens table settings view
        #When user double clicks on an item in the Selected Columns
        Then user double clicks on all items in the available column and verify they are selected in selected column
        Then user clicks on table settings OK button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            |INS005,INS006,INS007,INS008|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|100|actualTradeResult|expectedTradeResult|




        @Regression
        @Negative
        @Seatrial
        Scenario Outline: TWTS_005-Querying and Filtering Trades for multiple instruments-negative

        Given user deletes 'actualTradeResult' and 'expectedTradeResult' data tables from 'STAF.db'
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        #When user enter filter values
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        Then system should return an error message of '<ErrorMessage>' in the trades pane

        Examples:
            |ErrorMessage|Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            |No Matching Records Found for Query Criteria|INS005,INS006,INS007,INS008|New|||PTQA33921|AND|PTQA33921|||||||||||||SDATE|STIME|EDATE|ETIME|10|actualTradeResult|expectedTradeResult|


        @Regression
        @Positive
        @Seatrial
        @Smoke
        Scenario: TWTS_006-Querying and Filtering Trades - Multiple Instruments Selector

        #Given user send new buy Trades to the exchange using sikulix
        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user clicks on multiple insturment selector
        Then system prompts an insturment selector window
        And window lists currently available instruments
        When user types required instruments on instrument field with wildcard
            |expression|instrument|
            |EXPRE2 |INS005|
            |EXPRE2 |INS006|
            |EXPRE2 |INS007|
            |EXPRE2 |INS008|

        And user clicks on instrument selector ok button
        Then selected instruments should populate in the Trdes Window separated by pipe lines
        And user click on Trade filter Apply button
        Then there are no system errors


    @Regression
    @Positive
    @Seatrial
    Scenario: TWTS_007-Querying and Filtering Trades - tooltip for multiple instruments

        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user clicks on multiple insturment selector
        Then system prompts an insturment selector window
        And window lists currently available instruments
        When user types required instruments on instrument field with wildcard
            |expression|instrument|
            |INSDRP_^ |INS001|
            |INSDRP_^ |INS002|
            |INSDRP_^ |INS003|
            |INSDRP_^ |INS004|
        And user clicks on instrument selector ok button
        Then selected instruments should populate in the Trdes Window separated by pipe lines
        And tootip available for multiple instruments


    @Regression
    @Positive
    @Seatrial
    Scenario Outline: TWTS_008-Querying and Filtering Trades - resize and reorder column using drag and drop
        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        When user click on Trade filter Apply button
        #Then the system should return available trades whithin the given period of '10:30:00:000' to '12:30:00:000'
        When user resize coulmns using drag and drop
        Then coulmns should be resized acordingly

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            |INS005,INS006,INS007,INS008|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|100|actualTradeResult|expectedTradeResult|

        #If the number of rows or columns exceed the size of the pane, horizontal and vertical scroll bars should be enabled for the pane. -OutOfScope
        #In instances where query result is empty, an error message should be displayed as 'No Matching Records Found for Query Criteria'. -Coverd
        #The maximum number of records loaded into the trades pane is 20,000. - TODO
        #If the query result exceeds the record limit, the first (earliest in transact time) 20,000 records of the result should be displayed.
        @Regression
        @Positive-TODO
        @Seatrial

        Scenario Outline: TWTS_009-Querying and Filtering Trades - save a set of filter criteria of the window via 'Save Filter' option

        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        #And user apply custom filter values of '<CustomFilter>','<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        Then system should return query result in the trades pane
        And user deletes previously created filter 'myFilter1'
        When user click on save trade filter button
        Then system prompt save filter dialog box
        #there will be a change in save filter option.
        #And user selects '<SaveOption>' option in dialogbox
        And user enters filter name as 'myFilter1'
        When user click on filter Save button
        Then saved 'myFilter1.trdf' should be added to Filter pane
        When user double click on saved filter
        Then new trades tab window should open with saved values
        And user deletes previously created filter 'myFilter1'


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            |INS005,INS006,INS007,INS008|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|100|actualTradeResult|expectedTradeResult|

        #The user should be able to save any changes done to the layout of the window/tables via 'Save Profile' option. (drop 2)-OutOfScope

        @Positive-TODO
        @Seatrial
        Scenario: TWTS_010-Configurable Filter Fields-default filter fields should be available in the Filter pane

        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        Then user look for default filter fields of 'TradesWindow/defaultFilterFields.csv'

    @Regression
    @Positive
    @Seatrial
    Scenario: TWTS_011-Auto Complete Enabled Filters- Instrument,Traders,Firms (clientId no,case sensitive )
        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user types 'INS005' value in Trades View-InstrumentId then respective list which start with these values should return


    #When user types Instrument 'A'
    #Then sugession list which starts from 'A' should return

    @Positive-TODO
    @Seatrial
    Scenario: TWTS_012-Configurable Table Fields - Table Settings (add & remove)
        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        Then user look for default Table fields of 'TradesWindow/defaultTableFields.csv'

    #The main window should be dock-able in the main workstation as a tab
    @Regression
    @Positive
    @Seatrial
    Scenario: TWTS_013-Dockable Trades window (Analytic, Graphs pane)
        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        #When user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        Then user should navigate to 'Trades' tab window
        When user right click on Trades tab and select dockable
        Then Trades tab should detach from the main workstation
    #And Trades window dockable to right of the main workstation
    #And Trades window dockable to left of the main workstation
    #And Trades window dockable to top of the main workstation
    #And Trades window dockable to bottom of the main workstation
    #When user select tabbed menu in the trades window right click menu item
    #Then trades window should attached to main workstaion as tab window


    #BUG- return all when user query with trdreport ID
    @Regression
    @Positive
    @Seatrial
    @Smoke
    Scenario: TWTS_014-Drag and drop data cell values to filter pane -TODO after default table fields set
        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of 'OB_INS26','','',''
        And user apply duration filter values of 'SDATE','STIME','EDATE','ETIME'
        When user click on Trade filter Apply button
        When there are no system errors
        Then user opens table settings view
        Then user add 'Trade Report ID' filter from table settings
        And user adds required filter fields from table settings
        When user drag 'Symbol' and drop into trade filter pane
        Then Instrument filter should be filled with the selected Instrument value
        When user drag 'Exec type' and drop into trade filter pane
        Then Exec type filter should be filled with the selected Exec type value
        When user drag 'Trade type' and drop into trade filter pane
        Then Trade type filter should be filled with the selected Trade type value
        When user drag 'Trade Sub type' and drop into trade filter pane
        Then Trade Sub type filter should be filled with the selected Trade Sub type value
        When user drag 'Buy Trader' and drop into trade filter pane
        Then Buy Trader filter should be filled with the selected Buy Trader value
        When user drag 'Sell Trader' and drop into trade filter pane
        Then Sell Trader filter should be filled with the selected Sell Trader value
        When user drag 'Buy Firm' and drop into trade filter pane
        Then Buy Firm filter should be filled with the selected Buy Firm value
        When user drag 'Sell Firm' and drop into trade filter pane
        Then Sell Firm filter should be filled with the selected Sell Firm value
        When user drag 'Buy Client' and drop into trade filter pane
        Then Buy Client filter should be filled with the selected Buy Client value
        When user drag 'Sell Client' and drop into trade filter pane
        Then Sell Client filter should be filled with the selected Sell Client value
        When user drag 'Trade Report ID' and drop into trade filter pane
        Then Trade Report ID filter should be filled with the selected Trade Report ID value
        When user drag 'Trade Report Link ID' and drop into trade filter pane
        Then Trade Report Link ID filter should be filled with the selected Trade Report Link ID value
        When user click on Trade filter Apply button
        Then system should return query result in the trades pane

    @Regression
    @Positive
    @Seatrial
    Scenario: TWTS_015-Drag and drop second value to the filter pane-TODO after default table fields set
        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of 'INS005','','',''
        And user apply duration filter values of 'SDATE','STIME','EDATE','ETIME'
        When user click on Trade filter Apply button
        When there are no system errors
        Then system should return query result in the trades pane
        Then user opens table settings view
        Then user add 'Trade Report ID' filter from table settings
        When user drag 'Symbol' and drop into trade filter pane
        Then Instrument filter should be filled with the selected Instrument value
        When user drag 'Exec type' and drop into trade filter pane
        Then Exec type filter should be filled with the selected Exec type value
        When user drag 'Trade type' and drop into trade filter pane
        Then Trade type filter should be filled with the selected Trade type value
        When user drag 'Trade Sub type' and drop into trade filter pane
        Then Trade Sub type filter should be filled with the selected Trade Sub type value
        When user drag 'Buy Trader' and drop into trade filter pane
        Then Buy Trader filter should be filled with the selected Buy Trader value
        When user drag 'Sell Trader' and drop into trade filter pane
        Then Sell Trader filter should be filled with the selected Sell Trader value
        When user drag 'Buy Firm' and drop into trade filter pane
        Then Buy Firm filter should be filled with the selected Buy Firm value
        #Second drag & drop
        When user drag 'Symbol' and drop into trade filter pane
        Then Instrument filter should be filled with the selected Instrument value
        When user drag 'Exec type' and drop into trade filter pane
        Then Exec type filter should be filled with the selected Exec type value
        When user drag 'Trade type' and drop into trade filter pane
        Then Trade type filter should be filled with the selected Trade type value
        When user drag 'Trade Sub type' and drop into trade filter pane
        Then Trade Sub type filter should be filled with the selected Trade Sub type value
        When user drag 'Buy Trader' and drop into trade filter pane
        Then Buy Trader filter should be filled with the selected Buy Trader value
        When user drag 'Sell Trader' and drop into trade filter pane
        Then Sell Trader filter should be filled with the selected Sell Trader value
        When user drag 'Buy Firm' and drop into trade filter pane
        Then Buy Firm filter should be filled with the selected Buy Firm value



    @Regression
    @Seatrial
    Scenario: TWTS_016-Drag and drop data cell values to filter property- copy paste -TODO after default table fields set
        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of 'INS005','','',''
        And user apply duration filter values of 'SDATE','STIME','EDATE','ETIME'
        When user click on Trade filter Apply button
        When there are no system errors
        Then system should return query result in the trades pane
        Then user opens table settings view
        Then user add 'Trade Report ID' filter from table settings
        When user drag 'Symbol' and drop into 'InstrumentID' trade filter property
        #Then Instrument filter should be filled with the selected Instrument value
        When user select an Exec type and drop into trade filter property
        Then Exec type filter should be filled with the selected Exec type value
        When user select an Trade type and drop into trade filter property
        Then Trade type filter should be filled with the selected Trade type value
        When user select an Trade Sub type and drop into trade filter property
        Then Trade Sub type filter should be filled with the selected Trade Sub type value
        When user select Buy Trader and drop into trade filter property
        Then Buy Trader filter should be filled with the selected Buy Trader value
        When user select Sell Trader and drop into trade filter property
        Then Sell Trader filter should be filled with the selected Sell Trader value
        When user select Buy Firm and drop into trade filter property
        Then Buy Firm filter should be filled with the selected Buy Firm value
        When user select Sell Firm and drop into trade filter property
        Then Sell Firm filter should be filled with the selected Sell Firm value
        When user select Buy Client and drop into trade filter property
        Then Buy Client filter should be filled with the selected Buy Client value
        When user select Sell Client and drop into trade filter property
        Then Sell Client filter should be filled with the selected Sell Client value
        When user select an Trade Report ID and drop into trade filter property
        Then Trade Report ID filter should be filled with the selected Trade Report ID value
        When user select an Trade Report Link ID and drop into trade filter property
        Then Trade Report Link ID filter should be filled with the selected Trade Report Link ID value
        When user click on Trade filter Apply button
        Then system should return query result in the trades pane

    @Regression
    @Seatrial
    Scenario: TWTS_017-Drag and drop second value to the filter property -TODO after default table fields set
        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of 'INS005','','',''
        And user apply duration filter values of 'SDATE','STIME','EDATE','ETIME'
        When user click on Trade filter Apply button
        When there are no system errors
        Then system should return query result in the trades pane
        Then user opens table settings view
        Then user add 'Trade Report ID' filter from table settings
        When user drag 'Symbol' and drop into 'InstrumentID' trade filter property
        #Then Instrument filter should be filled with the selected Instrument value
        When user select an Exec type and drop into trade filter property
        Then Exec type filter should be filled with the selected Exec type value
        When user select an Trade type and drop into trade filter property
        Then Trade type filter should be filled with the selected Trade type value
        When user select an Trade Sub type and drop into trade filter property
        Then Trade Sub type filter should be filled with the selected Trade Sub type value
        When user select Buy Trader and drop into trade filter property
        Then Buy Trader filter should be filled with the selected Buy Trader value
        When user select Sell Trader and drop into trade filter property
        Then Sell Trader filter should be filled with the selected Sell Trader value
        When user select Buy Firm and drop into trade filter property
        Then Buy Firm filter should be filled with the selected Buy Firm value
        When user select Sell Firm and drop into trade filter property
        Then Sell Firm filter should be filled with the selected Sell Firm value
        When user select Buy Client and drop into trade filter property
        Then Buy Client filter should be filled with the selected Buy Client value
        When user select Sell Client and drop into trade filter property
        Then Sell Client filter should be filled with the selected Sell Client value
        When user select an Trade Report ID and drop into trade filter property
        Then Trade Report ID filter should be filled with the selected Trade Report ID value
        When user select an Trade Report Link ID and drop into trade filter property
        Then Trade Report Link ID filter should be filled with the selected Trade Report Link ID value
        #drag & drop second value
        When user select second Instrument and drop into trade filter property
        Then Instrument filter should be filled  by appending the Instrument value
        When user click on Trade filter Apply button
        Then system should return query result in the trades pane

    # @Positive-TODO
    #Scenario: Querying at Millisecond Precision
    #Covered in Scenario TWTS_001

    @Regression
    @Smoke
    Scenario Outline: TWTS_018-Viewing Trade History
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<CustomFilter>','<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return query result in the trades pane
        #And user adds required filter fields from table settings
        Then user opens table settings view
        Then user add 'Trade Report Link ID' filter from table settings
        #And user find 'Trade Report ID' column index
        When user right click on record and select 'View History'
        And user wait until history invokes
        When user drag 'Trade Report Link ID' and drop into trade filter pane
        Then trade history tab should open with the name of 'Trade Report Link ID'
        When user points cursor to tab name tooltip should appear with full tab name
        Then history tab should contain history results
        And user export queried Trade history result into 'tradeHistoryResult' csv file in the 'qaTest' folder

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|CustomFilter|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|
            |INS005|Fill|||||||||||||||||||SDATE|STIME|EDATE|ETIME|100|


        @Regression
        @Seatrial
        @Smoke
        Scenario Outline: TWTS_019-Execution Type Color Coding -TODO with default field update

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<CustomFilter>','<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return query result in the trades pane
        And Colour code '<ColourCode>' should map for each Execution type 'Execution Type'



        Examples:
            |ColourCode|Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|CustomFilter|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|
            |$FF00A038|INS005|Fill|||||||||||||||||||SDATE|STIME|EDATE|ETIME|5|
            |$FF008890|INS010|Trade Correct|||||||||||||||||||SDATE|STIME|EDATE|ETIME|5|
            |$FF8E8E8E|INS015|Trade Cancel|||||||||||||||||||SDATE|STIME|EDATE|ETIME|5|


        @Regression
        @Seatrial
        @Smoke
        Scenario Outline: TWTS_020-Viewing Orders
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<CustomFilter>','<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return query result in the trades pane
        Then user opens table settings view
        Then user add 'Trade Report ID' filter from table settings
        #When user select an Trade Report ID and drop into trade filter property
        When user right click on order and select 'Veiw Orders' option
        When there are no system errors
        Then new tab should open with 'Trade Report ID'
        And system should return respective orders for the trade


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|CustomFilter|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|
            |INS005|Fill|||||||||||||||||||SDATE|STIME|EDATE|ETIME|2|
        #|INS005|Trade Correct|||||||||||||||||||SDATE|STIME|EDATE|ETIME|5|
        #|INS005|Trade Cancel|||||||||||||||||||SDATE|STIME|EDATE|ETIME|5|
        #|STAF1000|Trade Correct|||||||||||||||||||26042016|19042016|100000000|235959999|5|
        #|STAF1000|Trade Cancel|||||||||||||||||||26042016|19042016|100000000|235959999|5|


        # 10	Viewing Live Order Book View


        @Regression
        @Seatrial
        @Smoke
        Scenario Outline: TWTS_021-Viewing Live Order Book
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<CustomFilter>','<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        Then system should return query result in the trades pane
        When user right click on Trade and select 'Live Order Book' option
        Then new tab should open with Live Orders For '<Instrument>'
        And system should return respective Live Orders for the '<Instrument>'


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|CustomFilter|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|
            |INS005|Fill|||||||||||||||||||SDATE|STIME|EDATE|ETIME|5|

        #11	Plot Trade History Trail

        #12	Highlighting Option
        #Todo


        # 15 Trade Price and Volume Graph-- TODO
        Scenario Outline: TWTS_022-Trade Price and Volume Graph
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        #When user enter filter values
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        Then system should return query result in the trades pane
        #This should do a screenshot verification for an exact execution report (row)
        #When user clicks on a row
        #Then grahp should be drawn for the '<Instrument>' with respective 'Trade Price' & 'Volume'

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            |INS005|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|5|actualTradeResult|expectedTradeResult|





        @Positive
        Scenario: TWTS_023-Plot Trade History Trail- TODO

        #Bid Offer graph for the relevant instrument will be invoked.
        #The BOG will display trade history for the relevant instrument and for the given time period.

        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        When user clicks on multiple firm selector


    @Positive
    Scenario: TWTS_024-Querying and Filtering Trades - Multiple Trader Selector - TODO

        #Given user send new buy Trades to the exchange using sikulix
        Given user login to the 'SurveillanceWorkstation'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        When user clicks on multiple trader selector

   
    @Positive
    @Seatrial
    Scenario Outline: TWTS_025-Sorting Feature

        Given user deletes 'Result' and 'ascendingResult' data tables from 'STAF.db'
        Given user deletes 'defaultResult' and 'ascendingDBResult' data tables from 'STAF.db'
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        #When user enter filter values
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        #And user adds required trades filter fields from table settings
        And user export result into 'Result.csv' csv file in the 'qaTest' folder
        Then user writes 'Result.csv' data into the database 'STAF.db'
        When DB 'STAF.db' writes selected 'tradeSqlFieldSetSort' values back to 'Result' after reordering by 'Executed Value'
        Given user deletes 'Result' and 'ascendingResult' data tables from 'STAF.db'
        Then user writes 'Result.csv' data into the database 'STAF.db'
        When DB 'STAF.db' writes selected 'tradeSqlFieldSet' values back to 'Result' after reordering by 'id'
        When user clicks ascending on '<SortBy>' column
        And user export result into 'ascendingResult.csv' csv file in the 'qaTest' folder
        Then user writes 'ascendingResult.csv' data into the database 'STAF.db'
        When DB 'STAF.db' writes selected 'tradeSqlFieldSet' values back to 'ascendingResult' after reordering by 'id'
        Then user compare 'ascendingResult.csv' in 'SurvFilePath' and 'Result.csv' order by 'id'



        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|SortBy|
            |INS005,INS006,INS007,INS008,INS0010|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|5|Executed Value|


              
        Scenario Outline: TWTS_025_01-Sorting Feature - Custom Sort

        Given user deletes 'Result' and 'ascendingResult' data tables from 'STAF.db'
        Given user deletes 'defaultResult' and 'ascendingDBResult' data tables from 'STAF.db'
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        #When user enter filter values
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        Then user opens table settings view
        Then user add 'Trade Report ID,Trade Type,Trade Sub Type' filter from table settings
        And user export result into 'Result.csv' csv file in the 'qaTest' folder
        Then user writes 'Result.csv' data into the database 'STAF.db'
        When DB 'STAF.db' writes selected 'tradeSqlFieldSetSort' values back to 'Result' after reordering by 'Executed Value,Executed Qty,Symbol'
        Given user deletes 'Result' and 'ascendingResult' data tables from 'STAF.db'
        Then user writes 'Result.csv' data into the database 'STAF.db'
        When DB 'STAF.db' writes selected 'tradeSqlFieldSet' values back to 'Result' after reordering by 'id'
        When user clicks on 'Custom Sort' button
        Then 'Custom Sort' Window should appear
        #And user selects 'executed_value','executed_qty','instrument_id' in 'Ascending' order
        And user selects multiple values in 'Ascending' order
            |value|sort_in|
            |Executed Value|Ascending|
            |Executed Qty|Ascending|
            |Symbol|Ascending|


        And clicks on 'Sort' button
        And user export result into 'ascendingResult.csv' csv file in the 'qaTest' folder
        Then user writes 'ascendingResult.csv' data into the database 'STAF.db'
        When DB 'STAF.db' writes selected 'tradeSqlFieldSet' values back to 'ascendingResult' after reordering by 'id'
        Then user compare 'ascendingResult.csv' in 'SurvFilePath' and 'Result.csv' order by 'id'


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            |INS005,INS006,INS007,INS008|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|5|actualTradeResult|expectedTradeResult|



        @Regression
        @Positive
        @Seatrial
        @Smoke
        Scenario Outline: TWTS_026-Exporting Data as csv & excel

        #Given user send new buy Trades to the exchange using sikulix -platformtheme none
        Given user deletes '<ActualResult>' and '<ExpectedResult>' data tables from 'STAF.db'
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        #When user enter filter values
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        And user export result into '<ActualResult>' csv file in the 'qaTest' folder
        #Then user export Orders queried result into '<ActualResult>' xls file in the 'qaTest' folder



        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            |INS005|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|


        @Regression
        @Positive
        @Seatrial
        @Smoke
        Scenario Outline: TWTS_027-Querying at Millisecond Precision


        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        #When user enter filter values
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        Then user pick 'Transact Time' of first & fifth record
        And user apply duration filter values at millisecond precision
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '5' rows in Trade query result in the pane


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            |INS005,INS006|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|5|||


        @Positive
        @Regression
        Scenario Outline: TWTS_028-Table Settings View-Add/Remove fileds to default view

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        Then user opens table settings view
        When user double clicks on an item in the Selected Columns
        #Then no column should left in the Selected side
        Then user double clicks on all items in the available column and verify they are selected in selected column
        Then it should be added to the trail of Selected Columns and bold in Table Columns
        Then user clicks on table settings OK button
        And click on save config
        Then close the window and open another trade window
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then user reset to default 
        #Then verify all selected columns available
        
        
        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            |INS005,INS006|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|5|||
    


    @Positive
    Scenario Outline: TWTS_029-Trade Price & Volume Graph - default graph which will be drawn for the queried criteria

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item	
        And user click on trade filter Clear button

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|ActualResult|ExpectedResult|
            |INS005|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|

        @Regression
        @Positive
        Scenario Outline: TWTS_030-Trade Price & Volume Graph - default graph which will be drawn for the queried criteria - TODO

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        



        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |INS005|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|

        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_031-Trade Price & Volume Graph functuionalities

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        When user Select draw tracker toggle option
        Then tracker should be available
        When user select Draw points option
        Then points should be available in the graph
        When user invoke Show/Hide  Alert News
        Then alerts/news should be available
        When user inovoke Show/Hide price series
        Then price series should be disbale
        When user inovoke Show/Hide volume series
        Then volume series should be disbale
        When user invoke color by Aggressor Side option
        Then aggressor sides should get solored acccording to the spec

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP71|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|

        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_032-Trade Price & Volume Graph functuionalities (Panning)

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        When user pane price axis of trade price graph

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP71|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|

        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_033-Trade Price & Volume Graph functuionalities (Draw static line)

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        When user creates static lines in price axis
        Then created lines should be available
        When user creates static lines in volume axis
        Then created lines should be available

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP71|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|


        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_034-Trade Price & Volume Graph functuionalities (context menu)

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        When user inovke trade price graph context menu option
        And user view standard Deviation option
        And user view Median Absolute Deviation option


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP71|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|

        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_035-Trade Price & Volume Graph functuionalities (context menu view orders)

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        When user inovke trade price graph context menu option
        And user view order window from context menu for 'CP71'
        And order window for relevant instrument should be available


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP71|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|

        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_036-Trade Price & Volume Graph functuionalities (context menu view trades)

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        When user inovke trade price graph context menu option
        And user view trade window from context menu for 'CP71'
        And trade window for relevant instrument should be available


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP71|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|

        @Positive
        @Seatrial
        Scenario Outline: TWTS_037-Analytic (Invoking and drill down)

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        And User invoke 'Actively Participated Instruments' analytic
        Then analytic should be available in analytic pane
        When user right click on analytic pane
        Then analytic should drill down to its second level


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP71|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|


        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_038-Invokig other charts and Trade Map

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        And User invoke 'Actively Participated Instruments' analytic
        Then analytic should be available in analytic pane
        When user click on veiw type as bar chart
        Then analytic should be available as bar chart
        When user click on view type as stack chart
        Then analytic would be available as stack chart
        When user invoke Trade Map
        Then Trade Map should be available

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP71|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|


        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_039 - user close trade winodw while query is executing

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button and cancels the window while query is executing

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP71|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|


        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_040- Invoke multiple windows through save filter and close all the tabs before gets loaded

        Given User connect to backend
        When user update sysgurad processing thread count to '1'
        And restart SurveillanceseManager process
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user save above filter in name 'defaultTradeFilter'
        And user invoke multiple windows through save 'filter'
        Then user cancels all the invoked windows
        Given User connect to backend
        When user update sysgurad processing thread count to '10'
        And restart SurveillanceseManager process

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP71|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|




        @Regression
        @Positive
        @Seatrial
        @Smoke
        Scenario Outline: TWTS_041-Save as default
        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        And user click on 'Trades' menu Item
        #And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<CustomFilter>','<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return query result in the trades pane
        And user adds required filter fields from table settings
        Then user save config from save as default

        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|CustomFilter|TradeLinkId|TradeReportId|Date:From|Time:From|Date:To|Time:To|RowCount|
            |CP70|Fill|||||||||||||||||||SDATE|STIME|EDATE|ETIME|100|

        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_042-Trade Price & Volume Graph functuionalities (Draw static line)

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        When user change the range as '10000' to '1000'
        Then range should be available as '10000' to '1000'


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP70|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|

        @Regression
        @Positive
        @Seatrial
        Scenario Outline: TWTS_043-Trade Price & Volume Graph functuionalities (change range of volume axis)

        Given user login to the 'SurveillanceWorkstation -platformtheme none'
        And user navigated to Surveillance main window
        # And user click on 'Trades' menu Item
        And user click on 'Trades' menu Item
        And user click on trade filter Clear button
        When user apply instrument filter values of '<Instrument>','<ExecType>','<TradeType>','<TradeSubType>'
        And user apply trader filter values of '<BuyTrader>','<TradeOperator>','<SellTrader>'
        And user apply firm filter values of '<BuyFirm>','<FirmOperator>','<SellFirm>'
        And user apply client filter values of '<BuyClient>','<ClientOperator>','<SellClient>'
        And user apply trade price filter values of '<TradePrice:From>','<TradePrice:To>'
        And user apply trade size filter values of '<TradeSize:From>','<TradeSize:To>'
        And user apply custom filter values of '<TradeLinkId>','<TradeReportId>'
        And user apply duration filter values of '<Date:From>','<Time:From>','<Date:To>','<Time:To>'
        And user click on Trade filter Apply button
        When there are no system errors
        Then system should return '<RowCount>' rows in Trade query result in the pane
        When user change the range of volume axis as '10000' to '1000'
        Then range should be available as '10000' to '1000'


        Examples:
            |Instrument|ExecType|TradeType|TradeSubType|BuyTrader|TradeOperator|SellTrader|BuyFirm|FirmOperator|SellFirm|BuyClient|ClientOperator|SellClient|TradePrice:From|TradePrice:To|TradeSize:From|TradeSize:To|TradeLinkId|TradeReportId|Date:From|Date:To|Time:From|Time:To|RowCount|ActualResult|ExpectedResult|
            |CP70|Fill||||||||||||||||||SDATE|STIME|EDATE|ETIME|25|actualTradeResult|expectedTrades_INSCR87_01|