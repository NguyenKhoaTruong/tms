import pandas as pd
from collections import defaultdict

# Đọc dữ liệu từ file CSV
file_path = "DataSoucrce.csv"  # Thay đổi đường dẫn tới file CSV của bạn
df = pd.read_csv(file_path)
# Chuyển cột từ DataFrame thành danh sách các từ
input_data = df[
    ["Latitude", "Longitude"]
].values.tolist()  # Thay đổi 'ten_cot_chua_tu' thành tên cột chứa từ trong file CSV của bạn
print("check value input data", input_data)


# Giai đoạn Map: Hàm map tạo ra các cặp (key, value) tương ứng với từng từ trong danh sách
def mapper(data):
    for row in data:
        for word in row:
            print("check value word", word)
            yield (word, 1)


# Giai đoạn Reduce: Hàm reduce tổng hợp các cặp (key, value) và đếm số lần xuất hiện của mỗi từ
def reducer(mapped_data):
    print("check value mapped_data", mapped_data)
    reduced_data = {}
    for key, values in mapped_data.items():
        reduced_data[key] = sum(values)
    return reduced_data


# Hàm chạy MapReduce
def run_mapreduce(input_data):
    print("check value input data", input_data)
    # Giai đoạn Map: Áp dụng hàm map cho dữ liệu đầu vào và gom nhóm các cặp (key, value) theo key
    mapped_data = {}
    for key, value in mapper(input_data):
        mapped_data.setdefault(key, []).append(value)

    # Giai đoạn Reduce: Áp dụng hàm reduce cho các cặp (key, value) đã gom nhóm
    reduced_data = reducer(mapped_data)

    return reduced_data


# Chạy MapReduce với dữ liệu đầu vào và in kết quả
result = run_mapreduce(input_data)
print("check value result kkkkk", result)
