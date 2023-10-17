import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from DB.Migration import get_Data_DB
import pandas as pd

df = pd.read_excel("E:\PythonGUI-ManageEmployee\Pyqt5\DB\dataI.xlsx", header=None)
df = df.iloc[1:]
for index, row in df.iterrows():
    # get_Data_DB().save_Data(
    #     OrderNo=row.values[0],
    #     Weight=row.values[4],
    #     Volume=row.values[5],
    #     Qty=row.values[3],
    #     ShipToAddress=row.values[2],
    #     ShipTo=row.values[1],
    #     TripNo=row.values[6],
    #     PickUp="NHONTRACH",
    #     TripType="Normal",
    #     CreateUser="truongnguyen",
    # )
    # get_Data_DB().save_Data_One(
    #     TripNo=row.values[6],
    #     ETP="2023-10-13 9:00:12.000",
    #     ETA="2023-10-13 9:20:12.000",
    #     CreateUser="truongnguyen",
    # )
    print()
