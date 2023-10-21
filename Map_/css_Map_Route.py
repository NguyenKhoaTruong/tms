def type_cs():
    styles = """
    <style>
                .main-menu{
                    display: flex;
                }
                .container-main {
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    grid-gap: 10px;
                    position: absolute;
                    bottom:0px;
                    z-index: 1000;
                }
                .container{
                    height: 500px;
                    width: 350px;
                    background-color:#d7e3d4;
                    border-radius:25px;
                    margin:10px;
                    padding:10px;
                    overflow: auto;
                }
                .tripline {
                    position: relative;
                    margin: 10px auto;
                    width: 80%;
                }
                .title{
                    font-size:15px;
                    color:#3498db;
                    font-weight:bold
                }
                .event {
                    position: relative;
                    padding: 10px;
                    border-left: 1px solid #3498db;
                    margin: 10px 0;
                }

                .event-date {
                    font-weight: bold;
                    color: #3498db;
                    margin-bottom: 5px;
                }

                .event-description {
                    color: #666;
                }

                .event:before {
                    content: "";
                    position: absolute;
                    top: 0;
                    left: -10px;
                    width: 20px;
                    height: 20px;
                    background-color: #3498db;
                    border-radius: 50%;
                }

                .sub-events {
                    margin-left: 10px;
                    padding-left: 10px;
                    border-left: 1px solid #ccc;
                }

                .sub-event {
                    padding: 10px 0;
                }

                .sub-event-date {
                    font-weight: bold;
                    color: #3498db;
                    font-size:15px
                }

                .sub-event-description {
                    color: #e33232;
                    font-size:15px
                }
                
                .title-text{
                    font-size:20px;
                    color:red;
                    margin:10px;
                    padding:10px;
                }
            </style>
            """
    return styles


# css Map Clutter
def css_Map_Cluster():
    styles = """
    <style>
                .main-menu{
                    display: flex;
                    
                }
                .container-main {
                    display: flex;
                    top:0px;
                }
                .container{
                    height: 830px;
                    width: 400px;
                    background-color:#d7e3d4;
                    overflow: auto;
                }
                .route-main {
                    position: absolute;
                    right:0px;
                    bottom:0px;
                    z-index: 1000;
                }
                .route{
                    height: 200px;
                    width: 350px;
                    background-color:#d7e3d4;
                    border-radius:25px;
                    margin:10px;
                    padding:10px;
                }
                .tripline {
                    position: relative;
                    margin: 10px auto;
                    width: 80%;
                }
                .title{
                    font-size:15px;
                    color:#3498db;
                    font-weight:bold
                }
                .event {
                    position: relative;
                    padding: 10px;
                    border-left: 1px solid #3498db;
                    margin: 10px 0;
                }

                .event-date {
                    font-weight: bold;
                    color: #3498db;
                    margin-bottom: 5px;
                }

                .event-description {
                    color: #666;
                }

                .event:before {
                    content: "";
                    position: absolute;
                    top: 0;
                    left: -10px;
                    width: 20px;
                    height: 20px;
                    background-color: #3498db;
                    border-radius: 50%;
                }

                .sub-events {
                    margin-left: 10px;
                    padding-left: 10px;
                    border-left: 1px solid #ccc;
                }

                .sub-event {
                    padding: 10px 0;
                }

                .sub-event-date {
                    font-weight: bold;
                    color: #3498db;
                    font-size:15px
                }

                .sub-event-description {
                    color: #e33232;
                    font-size:15px
                }
                
                .title-text{
                    font-size:20px;
                    color:red;
                    margin:10px;
                    padding:10px;
                    font-weight:bold;
                }
                table, td, th {  
                    border: 1px solid #ddd;
                    text-align: left;
                    }

                table {
                    border-collapse: collapse;
                    width: 100%;
                    }

                th, td {
                    padding: 15px;
                    font-size:15px;
                    font-weight:bold;
                    }
            </style>
            """
    return styles


def type_Cs_Cluster():
    style = """
            <style>
                .container{
                    height: 400px; 
                    width: 500px;
                    position:absolute;
                    z-index:1000;
                    top:20px;
                    left:20px;
                    background-color:#d7e3d4;
                    border-radius:25px;
                    overflow: auto
                }
                .title-text{
                    font-size:20px;
                    font-weight:bold;
                    color:red;
                    margin:5px;
                    padding:5px;
                    letter-spacing:1px
                }
                .item-route{
                    margin-left:30px;
                    letter-spacing:3px;
                    font-size:20px;
                    font-weight:bold;
                    padding:5px;
                    margin:5px
                }
            </style>
    """
    return style


def css_DialogCompare():
    styles = """
    <style>
        .main{
            display: flex;
        }
        .tab-des{
            width:200px;
            height:200px;
            border-radius:5px;
            position:absolute;
            z-index:1000;
            right:0px;
            top:10px;
            font-size:15px;
            background-color:#fd9931;
            display: grid;
            grid-template-columns: repeat(1, 1fr);
            grid-gap: 10px;
        }
        .normal{
            display:flex
        }
        .icon-normal{
            background-color:#fd9931;
        }
        .text-normal{
            background-color:#fd9931;
            font-size:15px
        }
        .container{
            width:400px;
            height:400px;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            grid-gap: 10px;
            margin:5px;
        }
        .route-main {

        }
        .route{
            height: 140px;
            width: 255px;
            font-family: math;
            text-align: center;
            background-color:#fd9931;
            border-radius:5px;
            margin:5px;
            padding:5px;
        }
        .title-text{
            font-size:15px;
            font-weight:bold;
            color:white;
            margin:5px;
            padding:5px;
            letter-spacing:1px;
        }
        .route-min{
            height: 140px;
            width: 255px;
            font-family: math;
            text-align: center;
            background-color:red;
            border-radius:5px;
            margin:5px;
            padding:5px;
        }
    </style>
    """
    return styles


def type_CSS():
    styles = """
    <style>
                .test{
                    width:100px;
                    height:100px
                }
            </style>
            """
    return styles
