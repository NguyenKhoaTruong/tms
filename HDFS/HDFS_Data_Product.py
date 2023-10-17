import pandas as pd
import schedule
import time
import datetime
import matplotlib.pyplot as plt

# Hàm thực hiện data pipeline
def run_data_pipeline():
    try:
        print('ahahahha')
        # ...
        # Các bước xử lý dữ liệu và trực quan hóa tại đây
        # ...
    except Exception as e:
        print("An error occurred:", str(e))

# Hàm trả về trạng thái hoạt động của quá trình lập lịch
def is_scheduling_active():
    current_time = datetime.datetime.now().time()
    end_time = datetime.time(17, 5, 0)  # Thời gian kết thúc là 17:00:00
    return current_time < end_time

# Lập lịch chạy data pipeline cứ mỗi 5 giây
schedule.every(5).seconds.do(run_data_pipeline)

# Vòng lặp để duy trì việc chạy lập lịch
while is_scheduling_active():
    schedule.run_pending()
    time.sleep(1)
