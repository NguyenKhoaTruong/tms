import sys

sys.path.append("E:\PythonGUI-ManageEmployee\Pyqt5")
from Compare_Algorithm.PyQT5_Content_Compare import Content_Compare
import re


class Data_Compare:
    def __init__(self):
        print("Data Compare")

    def show_(web_View, dataLayout, distance, weight, data_center):
        content_Title = [
            "Brute Force",
            "Branch Bound",
            "Greedy Algorithms",
            "Hill Climbing",
            "Lin Kernighan Heuristic",
            "Nearest Neighbor",
            "2 - OPT",
            "Randomized Tour",
        ]
        content_Data = [
            Content_Compare().content_Brute(distance, weight),
            Content_Compare().content_Branch(distance, weight),
            Content_Compare().content_Greedy(distance, weight),
            Content_Compare().content_Hill(distance, weight),
            Content_Compare().content_Lin(distance, weight),
            Content_Compare().content_Nearest(distance, weight),
            Content_Compare().content_OPT(distance, weight),
            Content_Compare().content_Random(distance, weight),
        ]

        def clean_Data(data):
            cleaned_data = []
            for item in data:
                # Xóa ký tự '\n' và khoảng trắng không cần thiết sử dụng regular expressions
                cleaned_item = re.sub(r"\s+", " ", item)
                cleaned_data.append(cleaned_item)
            return cleaned_data

        data__ = clean_Data(content_Data)

        def show_Content_HTML(data_center, title, content):
            data = ""
            for index, value in enumerate(title):
                data += f"""
                <div class="container"> 
                <div class="tripline">
                <div class="title">
                {value}
                <div class="event">
                <div class="event-date">Trip: {len(data_center)}</div>
                <ul class="sub-events">
                <li class="sub-event">
                {content[index]}
                </li></ul></div></div></div></div>
                """
            return data

        html_content = f"""
       <!DOCTYPE html>
        <html>
        <head>
            <title>Google Maps</title>
            <style>
                .main-menu{{
                    display: flex;
                }}
                .container-main {{
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    grid-gap: 10px;
                    position: absolute;
                    top:0px;
                    z-index: 1000;

                }}
                .container{{
                    height: 400px; 
                    width: 415px;
                    background-color:#d7e3d4;
                    border-radius:25px;
                    margin:10px;
                    padding:10px
                }}
                .tripline {{
                    position: relative;
                    margin: 10px auto;
                    width: 80%;
                }}
                .title{{
                    font-size:15px;
                    color:#3498db;
                    font-weight:bold
                }}
                .event {{
                    position: relative;
                    padding: 10px;
                    border-left: 1px solid #3498db;
                    margin: 10px 0;
                }}

                .event-date {{
                    font-weight: bold;
                    color: #3498db;
                    margin-bottom: 5px;
                }}

                .event-description {{
                    color: #666;
                }}

                .event:before {{
                    content: "";
                    position: absolute;
                    top: 0;
                    left: -10px;
                    width: 20px;
                    height: 20px;
                    background-color: #3498db;
                    border-radius: 50%;
                }}

                .sub-events {{
                    margin-left: 10px;
                    padding-left: 10px;
                    border-left: 1px solid #ccc;
                }}

                .sub-event {{
                    padding: 10px 0;
                }}

                .sub-event-date {{
                    font-weight: bold;
                    color: #3498db;
                    font-size:15px
                }}

                .sub-event-description {{
                    color: #e33232;
                    font-size:15px
                }}
            </style>
        </head>
            <body>
            <div class="main-menu">
                <div class="container-main">
                    {show_Content_HTML(data_center,content_Title,data__)}
                </div>
                <div style="height: 2000px; width: 100%;">
                </div>
            </div>
            </body>
        </html>
        """
        web_View.setHtml(html_content)
        dataLayout.addWidget(web_View)
