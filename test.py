from datetime import datetime

data_string = "2023-12-04T06:30:38.941Z"
data_datetime = datetime.fromisoformat(data_string.replace('Z', '+00:00'))

# Lấy ra chỉ phần giờ, phút và giây
time_only = data_datetime.time()

# Định dạng thành chuỗi chỉ với giờ, phút và giây
formatted_time = time_only.strftime("%H:%M:%S")

time_object = datetime.strptime(formatted_time, "%H:%M:%S").time()

print(time_object,type(time_object))
