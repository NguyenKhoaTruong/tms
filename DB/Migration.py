from __future__ import generators
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy import join
from sqlalchemy.sql import text
from sqlalchemy import desc
import csv
from dotenv import load_dotenv


class get_Data_DB:
    def __init__(self):
        load_dotenv()
        # connect db server S1
        SERVER = "192.168.70.131"
        DATABASE = "S1"
        DRIVER = "SQL Server"
        USERNAME = "SQLPythol"
        PASSWORD = "MPL331tstb"
        DATABASE_CONNECTION = (
            f"mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}"
        )
        engine = create_engine(DATABASE_CONNECTION)
        self.connection = engine.connect()

    def showDataContact(self):
        query = text("Select ContactName from MA_Contact")
        data = []
        contactCode = self.connection.execute(query)
        for value in contactCode:
            data.append(value)
        return data

    def showDataTableEquipment(self):
        query = text(
            """
            Select me.EquipmentDesc,me.EquipTypeNo,
            ms.StaffUserId,me.DefaultStaffId
            from MA_Staff ms , MA_Equipment me
            where ms.StaffUserId=me.DefaultStaffId
            """
        )
        data = []
        dataEquipment = self.connection.execute(query)
        for value in dataEquipment:
            data.append(value)
        return data

    def showDataEquipType(self):
        query = text("Select EquipTypeNo from MA_Equipment")
        dataEquipType = self.connection.execute(query).all()
        return dataEquipType

    def showDataTripPickUpAndShipTo(self):
        query = text("Select CompanyName from MA_Companys")
        dataQuery = self.connection.execute(query).all()
        return dataQuery

    def showDataTripType(self):
        query = text(
            """
            Select CodeDesc from MA_StdCodes where CodeType='TESIMORDTRIPTYPE'
            """
        )
        dataQuery = self.connection.execute(query).all()
        return dataQuery

    def showDataEquimentGroup(self):
        query = text(
            """
                Select met.EquipTypeNo
                from MA_Equipment me, MA_EquipmentType met
                where me.EquipTypeNo=met.EquipTypeNo
                """
        )
        data = []
        dataQuery = self.connection.execute(query)
        for value in dataQuery:
            data.append(value)
        return data

    def showDataEquipmentGroupTrip(self):
        query = text(
            """
                Select met.EquipTypeNo
                from  MA_EquipmentType met
                """
        )
        data = []
        dataQuery = self.connection.execute(query)
        for value in dataQuery:
            data.append(value)
        return data

    def addTripSimpleDL(
        self,
        TripNo,
        ETP,
        ETA,
        CreateDate,
        CreateUser,
        IsUse,
        EquipmentCode,
        EquipmentDesc,
        DriverId,
        TripStatus,
        DCCode,
        EquipTypeNo,
        CODAmount,
    ):
        try:
            query = """Insert into TE_SimpleTrip(TripNo,ETP,ETA,CreateDate,
            CreateUser,IsUse,EquipmentCode,EquipmentDesc,DriverId,TripStatus,
            DCCode,EquipTypeNo,CODAmount)
            values('{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}',{})
            """.format(
                TripNo,
                ETP,
                ETA,
                CreateDate,
                CreateUser,
                IsUse,
                EquipmentCode,
                EquipmentDesc,
                DriverId,
                TripStatus,
                DCCode,
                EquipTypeNo,
                CODAmount,
            )
            self.connection.execute(query)
            print("Add Data Success")
        except ValueError as error:
            print("Log Error", error)

    def addOrderSimple(
        self,
        OrderNo,
        Weight,
        Volume,
        ShipTo,
        ShipToAddress,
        DeliveryDate,
        Priority,
        CreateDate,
        TripNo,
        DCCode,
        ContactCode,
        CODAmount,
        CreateUser,
        IsUse,
        SplitOrderIndex,
        TripType,
        Qty,
        PickUp,
        COD,
        ItemNote,
    ):
        try:
            query = """
            Insert into TE_SimpleOrder(OrderNo,Weight,Volume,ShipTo,ShipToAddress,
            DeliveryDate,Priority,CreateDate,TripNo,DCCode,ContactCode,CODAmount,
            CreateUser,IsUse,SplitOrderIndex,TripType,Qty,PickUp,COD,ItemNote)
            values('{}',{},{},'{}','{}','{}',{},'{}','{}','{}',
            '{}',{},'{}',{},{},'{}',{},'{}',{},'{}')
            """.format(
                OrderNo,
                Weight,
                Volume,
                ShipTo,
                ShipToAddress,
                DeliveryDate,
                Priority,
                CreateDate,
                TripNo,
                DCCode,
                ContactCode,
                CODAmount,
                CreateUser,
                IsUse,
                SplitOrderIndex,
                TripType,
                Qty,
                PickUp,
                COD,
                ItemNote,
            )
            self.connection.execute(query)
            print("Add Data Success")
        except ValueError as error:
            print("Log Error", error)

    def showDataTripSimple(self):
        try:
            query = text(
                """
                    Select st.TripNo,st.BatchGroupNo,st.BatchGroupNo,st.EquipTypeNo,st.ETP,
                    me.Ownership,st.Porter,st.DriverDesc,so.OrderNo,so.Qty,so.Weight,so.Volume,
                    so.OrderId,so.CreateDate,so.CreateUser,st.ETA,st.TripStatus
                    from  TE_SimpleOrder so,TE_SimpleTrip st,MA_Equipment me
                    where so.TripNo=st.TripNo and st.EquipmentCode=me.EquipmentCode
                    """
            )
            data = []
            dataQuery = self.connection.execute(query)
            for value in dataQuery:
                data.append(value)
            return data
        except ValueError as error:
            print("Log Error", error)

    def findDataTripOrder(self, dataSearch):
        try:
            query = text(
                """
                    Select Top 1 st.TripNo,st.BatchGroupNo,st.BatchGroupNo,
                    st.EquipTypeNo,st.ETP,me.Ownership,st.Porter,
                    st.DriverDesc,st.EquipmentCode,st.EquipmentDesc,
                    so.OrderNo,so.Qty,so.Weight,so.Volume,so.OrderId,
                    so.CreateDate,so.CreateUser,st.ETA,st.TripStatus,
                    st.TripMemo,st.LinkUpTripNo,st.CreateDate,st.CreateUser
                    from  MA_Equipment me,TE_SimpleOrder so, TE_SimpleTrip st, 
                    MA_Companys mc,MA_Staff ms
                    where so.TripNo=st.TripNo and ms.StaffUserId=me.DefaultStaffId
                    and me.EquipmentCode=st.EquipmentCode or st.TripNo='{}' or so.OrderNo='{}'
                    """.format(
                    dataSearch, dataSearch
                )
            )
            dataQuery = self.connection.execute(query).all()
            return dataQuery
        except ValueError as error:
            print("Log Error", error)

    def showDataTripOrder(self):
        query = text(
            """
                Select top 100 st.TripNo,st.BatchGroupNo,st.BatchGroupNo,st.EquipTypeNo,st.ETP,
                me.Ownership,st.Porter,st.DriverDesc,st.EquipmentCode,st.EquipmentDesc,st.TripMemo,
                so.OrderNo,so.Qty,so.Weight,so.Volume,so.OrderId,so.CreateDate,so.CreateUser,st.ETA,
                st.TripStatus
                from  TE_SimpleOrder so,TE_SimpleTrip st,MA_Equipment me
                where me.EquipmentCode=st.EquipmentCode and so.TripNo=st.TripNo
                order by st.TripNo desc
                """
        )
        data = []
        dataQuery = self.connection.execute(query)
        for value in dataQuery:
            data.append(value)
        return data

    def dataTableTripOrder(self):
        query = text(
            """
                Select st.TripNo,st.BatchGroupNo,st.BatchGroupNo,st.EquipTypeNo,st.ETP,
                me.Ownership,st.Porter,st.DriverDesc,st.EquipmentCode,st.EquipmentDesc,
                so.OrderNo,so.Qty,so.Weight,so.Volume,so.OrderId,so.CreateDate,so.CreateUser,st.ETA,
                st.TripStatus
                from  TE_SimpleOrder so,TE_SimpleTrip st,MA_Equipment me
                where me.EquipmentCode=st.EquipmentCode and so.TripNo=st.TripNo or
                so.TripNo=st.TripNo or so.OrderNo=so.OrderNo
                """
        )
        data = []
        dataQuery = self.connection.execute(query)
        for value in dataQuery:
            data.append(value)
        return data

    def dataTableTripEquiment(self):
        query = text(
            """
                Select st.TripNo,st.DriverDesc,st.EquipmentCode,
                so.OrderNo,st.TripMemo,me.EquipTypeNo
                from  TE_SimpleOrder so,TE_SimpleTrip st,MA_Equipment me
                where me.EquipmentCode=st.EquipmentCode and so.TripNo=st.TripNo
                """
        )
        data = []
        dataQuery = self.connection.execute(query)
        for value in dataQuery:
            data.append(value)
        return data

    def dataExpressOrder(self):
        try:
            query = text(
                """
                    Select Top 10 so.OrderNo,so.DeliveryDate,so.TripNo,so.ShipTo,ms.StaffName,
                    so.Weight,so.Volume,so.Qty,so.ArrivalTime,so.ItemNote,so.PickUp,
                    so.OtherRefNo3,so.TripType,so.ShipToAddress,so.OtherRefNo2,so.OtherRefNo1,
                    ms.Remark,ms.Remark,ms.Remark,st.EquipmentCode,st.EquipmentCode,ms.StaffName,
                    ms.MobileNo,me.Ownership,so.CODAmount,mc.WavePriority,so.RequestGroup,so.RequestTruckType,
                    so.CreateDate,so.CreateUser,st.TripStatus,st.TripStatus,ms.Remark,ms.Remark,
                    st.Vendor,st.EquipmentDesc,st.DriverDesc,mc.Addr1,mc.Province
                    from  TE_SimpleOrder so,TE_SimpleTrip st,MA_Equipment me,MA_Staff ms, MA_Companys mc
                    where me.EquipmentCode=st.EquipmentCode and so.TripNo=st.TripNo
                    and ms.StaffUserId=me.DefaultStaffId and me.EquipmentCode=st.EquipmentCode
                    and mc.ContactCode=so.ContactCode    
                    """
            )
            data = []
            dataQuery = self.connection.execute(query)
            for value in dataQuery:
                data.append(value)
            return data
        except ValueError as error:
            print("Log Error", error)

    def showDataEquipment(self):
        query = text(
            """
                Select me.EquipmentCode, me.DefaultStaffId
                from  MA_Equipment me
                """
        )
        data = []
        dataQuery = self.connection.execute(query).all()
        for value in dataQuery:
            data.append(value)
        return data

    def dataExpressOrderDetail(self):
        query = text(
            """
                Select so.OrderNo,so.PickUp,so.ShipToArea,so.TripType,so.Weight,so.Volume,
                so.ItemNote,so.Qty,so.CODAmount,st.CompleteTime,so.RequestGroup,so.RequestTruckType,
                mc.WavePriority
                from  MA_Equipment me,TE_SimpleOrder so, TE_SimpleTrip st, MA_Companys mc
                where so.TripNo=st.TripNo
                """
        )
        data = []
        dataQuery = self.connection.execute(query).all()
        for value in dataQuery:
            data.append(value)
        return data

    def addAutoCheckGenerated(
        self,
        OrderNo,
        ShipTo,
        Weight,
        Volume,
        Qty,
        ShipToArea,
        ShipToAddress,
        ItemNote,
        PickUp,
        TripType,
        RequestGroup,
        RequestTruckType,
        OtherRefNo1,
        COD,
        CODAmount,
        CreateDate,
        CreateUser,
        UpdateDate,
        UpdateUser,
        IsUse,
        SplitOrderIndex,
        ContactCode,
        DeliveryDate,
        Priority,
        TripNo,
        ETP,
        ETA,
        EquipmentCode,
        EquipmentDesc,
        DriverId,
        TripStatus,
        EquipTypeNo,
        DriverDesc,
        Vendor,
        DCCode,
    ):
        try:
            queryOrderTrip = """
            Insert into TE_SimpleOrder(OrderNo,ShipTo,Weight,Volume,Qty,
            ShipToArea,ShipToAddress,ItemNote,PickUp,TripType,RequestGroup,
            RequestTruckType,OtherRefNo1,COD,CODAmount,CreateDate,CreateUser,
            UpdateDate,UpdateUser,IsUse,SplitOrderIndex,ContactCode,
            DeliveryDate,Priority,TripNo,DCCode)
            values('{}','{}',{},{},{},'{}','{}','{}','{}','{}',
            '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',
            '{}','{}','{}','{}','{}','{}')
            """.format(
                OrderNo,
                ShipTo,
                Weight,
                Volume,
                Qty,
                ShipToArea,
                ShipToAddress,
                ItemNote,
                PickUp,
                TripType,
                RequestGroup,
                RequestTruckType,
                OtherRefNo1,
                COD,
                CODAmount,
                CreateDate,
                CreateUser,
                UpdateDate,
                UpdateUser,
                IsUse,
                SplitOrderIndex,
                ContactCode,
                DeliveryDate,
                Priority,
                TripNo,
                DCCode,
            )
            self.connection.execute(queryOrderTrip)
            queryGeneratedSimpleTrip = """
            Insert into TE_SimpleTrip(TripNo,ETP,ETA,CreateDate,CreateUser,
            UpdateDate,UpdateUser,IsUse,EquipmentCode,EquipmentDesc,DriverId,
            DriverDesc,TripStatus,Vendor,DCCode,EquipTypeNo,CODAmount)
            values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',
            '{}','{}','{}','{}','{}','{}','{}')
            """.format(
                TripNo,
                ETP,
                ETA,
                CreateDate,
                CreateUser,
                UpdateDate,
                UpdateUser,
                IsUse,
                EquipmentCode,
                EquipmentDesc,
                DriverId,
                DriverDesc,
                TripStatus,
                Vendor,
                DCCode,
                EquipTypeNo,
                CODAmount,
            )
            self.connection.execute(queryGeneratedSimpleTrip)
        except ValueError as error:
            print("Log Error", error)

    def searchTripSimple(self, dataSearch, dataTimeLeft, dataTimeRight):
        try:
            query = text(
                """
                    Select DISTINCT st.TripNo,st.BatchGroupNo,st.BatchGroupNo,
                    st.EquipTypeNo,st.ETP,me.Ownership,st.Porter,
                    st.DriverDesc,st.EquipmentCode,st.EquipmentDesc,
                    so.OrderNo,so.Qty,so.Weight,so.Volume,st.TripMemo,
                    so.CreateDate,so.CreateDate,so.CreateUser,st.TripStatus,
                    st.TripMemo,st.SecurityCode,st.CreateDate,st.CreateUser
                    from  MA_Equipment me,TE_SimpleOrder so, TE_SimpleTrip st, 
                    MA_Companys mc,MA_Staff ms,MA_Contact mct
                    where so.TripNo=st.TripNo and ms.StaffUserId=me.DefaultStaffId
                    and me.EquipmentCode=st.EquipmentCode and mct.ContactName='{}' 
                    and st.ETP>='{}' and st.ETP<='{}'
                    order by TripNo
                    """.format(
                    dataSearch, dataTimeLeft, dataTimeRight
                )
            )
            dataQuery = self.connection.execute(query).all()
            return dataQuery
        except ValueError as error:
            print("Log Error", error)

    def searchDataOrder(
        self, nameContact, timeLeft, timeRight, status, textNote, otherNo
    ):
        try:
            query = text(
                """
                    Select so.OrderNo,so.DeliveryDate,st.TripNo,
                    so.ShipTo,ms.StaffName,so.Weight,so.Volume,so.Qty,
                    so.ArrivalTime,so.ItemNote,so.PickUp,so.OtherRefNo3,so.TripType,
                    so.ShipToAddress,so.OtherRefNo2,so.OtherRefNo1,ms.Remark,
                    ms.Remark,ms.Remark,st.EquipmentCode,st.EquipmentCode,
                    ms.StaffName,ms.MobileNo,me.Ownership,so.CODAmount,
                    mc.WavePriority,so.RequestGroup,so.RequestTruckType,
                    so.CreateDate,so.CreateUser,st.TripStatus,st.TripStatus,
                    ms.Remark,ms.Remark,st.Vendor,st.EquipmentDesc,st.DriverDesc,
                    mc.Addr1,mc.Province
                    from  MA_Equipment me,TE_SimpleOrder so, TE_SimpleTrip st, 
                    MA_Companys mc,MA_Staff ms,MA_Contact mct
                    where so.TripNo=st.TripNo and ms.StaffUserId=me.DefaultStaffId
                    and me.EquipmentCode=st.EquipmentCode and mct.ContactName='{}' 
                    and so.DeliveryDate>='{}' and so.DeliveryDate<='{}'  
                    and st.TripStatus='{}' or so.ItemNote='{}' or so.OrderNo='{}'
                    """.format(
                    nameContact, timeLeft, timeRight, status, textNote, otherNo
                )
            )
            dataQuery = self.connection.execute(query).all()
            return dataQuery
        except ValueError as error:
            print("Log Error", error)

    def saveDataFromFile(
        self,
        OrderNo,
        PickUp,
        ShipTo,
        ShipToAddress,
        TripType,
        Weight,
        Volume,
        ItemNote,
        Qty,
        Priority,
        CODAmount,
        CompleteTime,
        RequestGroup,
        RequestTruckType,
        OtherRefNo1,
        EquipmentCode,
        DriverId,
        ETP,
        ETA,
        ATP,
        ETD,
        ATD,
        TripNo,
        COD,
        ActualAmount,
        CreateUser,
        CreateDate,
        DCCode,
        ContactCode,
        DeliveryDate,
        EquipmentDesc,
        TripStatus,
        EquipTypeNo,
    ):
        querySaveDataToOder = text(
            """
            Insert into TE_SimpleOrder(OrderNo,PickUp,ShipTo,ShipToAddress,TripType,
            Weight,Volume,ItemNote,Qty,Priority,CODAmount,RequestGroup,RequestTruckType,
            OtherRefNo1,TripNo,COD,ActualAmount,CreateUser,CreateDate,DCCode,ContactCode,
            DeliveryDate)
            values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',
            '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
            """.format(
                OrderNo,
                PickUp,
                ShipTo,
                ShipToAddress,
                TripType,
                Weight,
                Volume,
                ItemNote,
                Qty,
                Priority,
                CODAmount,
                RequestGroup,
                RequestTruckType,
                OtherRefNo1,
                TripNo,
                COD,
                ActualAmount,
                CreateUser,
                CreateDate,
                DCCode,
                ContactCode,
                DeliveryDate,
            )
        )
        self.connection.execute(querySaveDataToOder)
        querySaveDataSimple = text(
            """
            Insert into TE_SimpleTrip(TripNo,EquipmentCode,DriverId,ETP,
            ETA,ATP,ETD,ATD,CompleteTime,CreateUser,CreateDate,DCCode,
            EquipmentDesc,TripStatus,EquipTypeNo,CODAmount)
            values('{}','{}','{}','{}','{}','{}','{}','{}',
            '{}','{}','{}','{}','{}','{}','{}','{}')
            """.format(
                TripNo,
                EquipmentCode,
                DriverId,
                ETP,
                ETA,
                ATP,
                ETD,
                ATD,
                CompleteTime,
                CreateUser,
                CreateDate,
                DCCode,
                EquipmentDesc,
                TripStatus,
                EquipTypeNo,
                CODAmount,
            )
        )
        self.connection.execute(querySaveDataSimple)

    def showInfoOrderNo(self, dataSearch):
        try:
            query = text(
                """
                        Select so.OrderNo,so.DeliveryDate,so.TripNo
                    ,so.ShipTo,ms.StaffName,so.Qty,so.ArrivalTime,so.ItemNote,so.PickUp,
                    so.OtherRefNo3,so.TripType,so.ShipToAddress,so.OtherRefNo2,so.OtherRefNo1,
                    ms.Remark,ms.Remark,ms.Remark,me.EquipmentCode,st.EquipmentCode,
                    ms.StaffName,ms.MobileNo,me.Ownership,so.CODAmount,mc.WavePriority,
                    so.RequestGroup,so.RequestTruckType,so.CreateDate,so.CreateUser,
                    st.TripStatus,st.TripStatus,ms.Remark,ms.Remark,
                    st.Vendor,st.EquipmentDesc,st.DriverDesc,mc.Addr1,mc.Province
                    from  MA_Equipment me,TE_SimpleOrder so, TE_SimpleTrip st, 
                    MA_Companys mc,MA_Staff ms
                    where so.TripNo=st.TripNo and ms.StaffUserId=me.DefaultStaffId
                    and me.EquipmentCode=st.EquipmentCode and so.OrderNo='{}'
                    order by so.OrderId desc
                    """.format(
                    dataSearch
                )
            )
            dataQuery = self.connection.execute(query).scalar()
            return dataQuery
        except ValueError as error:
            print("Log Error", error)

    def searchStatusOrder(self, contactCode, status):
        try:
            query = text(
                """
                    Select so.OrderNo,so.DeliveryDate,so.TripNo
                    ,so.ShipTo,ms.StaffName,so.Qty,so.ArrivalTime,so.ItemNote,so.PickUp,
                    so.OtherRefNo3,so.TripType,so.ShipToAddress,so.OtherRefNo2,so.OtherRefNo1,
                    ms.Remark,ms.Remark,ms.Remark,st.EquipmentCode,st.EquipmentCode,
                    ms.StaffName,ms.MobileNo,me.Ownership,so.CODAmount,mc.WavePriority,
                    so.RequestGroup,so.RequestTruckType,so.CreateDate,so.CreateUser,
                    st.TripStatus,st.TripStatus,ms.Remark,ms.Remark,
                    st.Vendor,st.EquipmentDesc,st.DriverDesc,mc.Addr1,mc.Province
                    from  MA_Equipment me,TE_SimpleOrder so, TE_SimpleTrip st, 
                    MA_Companys mc,MA_Staff ms,MA_Contact mct
                    where so.TripNo=st.TripNo and so.ContactCode=mct.ContactCode
                    and so.ContactCode='{}' and st.TripStatus='{}'
                    order by so.OrderId desc
                    """.format(
                    contactCode, status
                )
            )
            data = []
            dataQuery = self.connection.execute(query).all()
            for value in dataQuery:
                data.append(value)
            return data
        except ValueError as error:
            print("Log Error", error)

    def checkOrder(self, orderNo):
        query = text(
            """
                Select so.OrderNo
                from  TE_SimpleOrder so
                where so.OrderNo='{}'
                """.format(
                orderNo
            )
        )
        dataQuery = self.connection.execute(query).scalar()
        return dataQuery

    def checkTrip(self, tripNo):
        query = text(
            """
                Select st.TripNo
                from  TE_SimpleTrip st
                where st.TripNo='{}'
                """.format(
                tripNo
            )
        )
        dataQuery = self.connection.execute(query).scalar()
        return dataQuery

    def showDataImportFile(self):
        query = text(
            """
                Select DISTINCT so.OrderId,so.OrderNo,so.ShipTo,so.ShipToAddress,so.TripType,so.Weight,so.Volume,
                so.ItemNote,so.Qty,so.CODAmount,so.Priority,st.CompleteTime,so.RequestGroup,
                so.RequestTruckType,so.OtherRefNo1,st.DriverId,st.ETP,st.ETA,st.ATP,st.ATD,
                st.ATP
                from  MA_Equipment me,TE_SimpleOrder so, TE_SimpleTrip st, MA_Companys mc
                where so.TripNo=st.TripNo
                order by so.OrderId desc
                OFFSET 11 ROWS
				FETCH NEXT 100 ROWS ONLY;
                """
        )
        data = []
        dataQuery = self.connection.execute(query).all()
        for value in dataQuery:
            data.append(value)
        return data

    def showDataImportFileLib(self):
        query = text(
            """
                Select DISTINCT top 11 so.OrderId,so.OrderNo,so.ShipTo,so.ShipToAddress,so.TripType,so.Weight,so.Volume,
                so.ItemNote,so.Qty,so.CODAmount,so.Priority,st.CompleteTime,so.RequestGroup,
                so.RequestTruckType,so.OtherRefNo1,st.DriverId,st.ETP,st.ETA,st.ATP,st.ATD,
                st.ATP
                from  MA_Equipment me,TE_SimpleOrder so, TE_SimpleTrip st, MA_Companys mc
                where so.TripNo=st.TripNo
                order by so.OrderId desc
                """
        )
        data = []
        dataQuery = self.connection.execute(query).all()
        for value in dataQuery:
            data.append(value)
        return data

    def checkTripNo(self):
        try:
            query = text(
                """
                Select top 1 TripNo
                from TE_SimpleTrip
                order by TripNo desc
                """
            )
            dataQuery = self.connection.execute(query).scalar()
            return dataQuery
        except ValueError as error:
            print("Log Error", error)

    def checkOrderNo(self, orderNo):
        try:
            query = text(
                """
                Select  OrderNo
                from TE_SimpleOrder
                where OrderNo='{}'
                """.format(
                    orderNo
                )
            )
            dataQuery = self.connection.execute(query).all()
            return dataQuery
        except ValueError as error:
            print("Log Error", error)

    # test data phân cụm: khi có data hiện tại chưa có có

    # def checkDataCluster(orderID):
    #     try:
    #         query=text(
    #             """
    #             select top 100 lat,lon,weight,volume
    #             from TE_SimpleOrder ts, OM_OrderOrg om
    #             where ts.OrderId=om.OrdeId and ts.OrderId=''
    #             """.format(orderID)
    #             )
    #         dataQuery=self.connection.execute(query).all()
    #         return dataQuery
    #     except ValueError as error:
    #         print('Log Error',error)

    # data test chưa có data:
    def checkDataCluster(self):
        try:
            query = text(
                """
                select top 20 OrdeId,ItemNo,OrgName,OrgAddr1,OrgAddr2,OrgAddr3,Lat,Lon
                from OM_OrderOrg
                order by OrdeId desc
                """
            )
            dataQuery = self.connection.execute(query).all()
            return dataQuery
        except ValueError as error:
            print("Log Error", error)

    # process data leck
    def dataSource(self):
        try:
            query = text(
                """
                select OrdeId,ItemNo,OrgName,OrgAddr1,OrgAddr2,OrgAddr3,Lat,Lon
                from OM_OrderOrg
                order by OrdeId desc
                """
            )
            dataQuery = self.connection.execute(query).all()
            fileSave = "DataSoucrce.csv"
            with open(fileSave, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                header = [
                    "OrderId",
                    "ItemNo",
                    "Address1",
                    "Address2",
                    "Address3",
                    "Latitude",
                    "Longitude",
                ]
                writer.writerow(header)
                for row in dataQuery:
                    writer.writerow(row)
                print("Lưu dữ liệu vào file thành công.")
            return dataQuery
        except ValueError as error:
            print("Log Error", error)

    # Test data select :
    # def data_Select(self,data):
    #     try:
    #         value_ = ', '.join("'" + value + "'" for value in data)
    #         query=text(
    #             """
    #             SELECT CompanyId,so.OrderNo,so.Weight,so.Volume,so.RequestTruckType,Lat,Lon
    #             FROM MA_Companys,TE_SimpleOrder so
    #             WHERE CompanyId=so.ShipTo and CompanyId IN ({})
    #             """.format(value_)
    #             )
    #         dataQuery=self.connection.execute(query).all()
    #         return dataQuery
    #     except ValueError as error:
    #         print('Log Error',error)
    def data_Select(self, data):
        try:
            value_ = ", ".join("'" + value + "'" for value in data)
            query = text(
                """
                SELECT CompanyId,so.OrderNo,so.Weight,so.Volume,so.RequestTruckType,Lat,Lon,Addr1,Addr2,Addr3 
                FROM MA_Companys,TE_SimpleOrder so 
                WHERE CompanyId=so.ShipTo and CompanyId IN ({})
                """.format(
                    value_
                )
            )
            dataQuery = self.connection.execute(query).all()
            return dataQuery
        except ValueError as error:
            print("Log Error", error)

    def data_Select_Lib(self, data):
        try:
            query = text(
                """
                SELECT CompanyId,so.OrderNo,so.Weight,so.Volume,so.RequestTruckType,Lat,Lon,Addr1,Addr2,Addr3 
                FROM MA_Companys,TE_SimpleOrder so 
                WHERE CompanyId=so.ShipTo and CompanyId='{}'
                """.format(
                    data
                )
            )
            dataQuery = self.connection.execute(query).all()
            return dataQuery
        except ValueError as error:
            print("Log Error", error)

    def data_lake(self):
        try:
            query = text(
                """
                SELECT CompanyId,so.OrderNo,so.Weight,so.Volume,so.RequestTruckType,Addr1,Addr2,Addr3,Lat,Lon 
                FROM MA_Companys,TE_SimpleOrder so 
                WHERE CompanyId=so.ShipTo 
                """
            )
            dataQuery = self.connection.execute(query).all()
            return dataQuery
        except ValueError as error:
            print("Log Error", error)

    # test import file data order
    def save_Data(
        self,
        OrderNo,
        Weight,
        Volume,
        Qty,
        ShipToAddress,
        ShipTo,
        TripNo,
        PickUp,
        TripType,
        CreateUser,
    ):
        sqlQuery = text(
            """
            Insert into TE_SimpleOrder(OrderNo,Weight,Volume,Qty,
            ShipToAddress,ShipTo,TripNo,PickUp,TripType,CreateUser)
            values('{}',{},{},{},'{}','{}','{}','{}','{}','{}')
            """.format(
                OrderNo,
                Weight,
                Volume,
                Qty,
                ShipToAddress,
                ShipTo,
                TripNo,
                PickUp,
                TripType,
                CreateUser,
            )
        )
        self.connection.execute(sqlQuery)
        self.connection.commit()

    def save_Data_One(self, TripNo, ETP, ETA, CreateUser):
        sqlQuery = text(
            """
            Insert into TE_SimpleTrip(TripNo,ETP,ETA,CreateUser)
            values('{}','{}','{}','{}')
            """.format(
                TripNo, ETP, ETA, CreateUser
            )
        )
        self.connection.execute(sqlQuery)
        self.connection.commit()


get_Data_DB().showDataImportFile()
