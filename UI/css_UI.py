def css_Clsuter():
    css = """
        QTextEdit {
            height: 100px;
            color: green;
            font-weight: bold;
        }

        QPushButton {
            font-size: 15px;
        }

        QLabel {
            font-size: 15px;
            /* margin: 10px; */
            margin-left: 5px;
        }

        QLineEdit {
            height: 30px;
            margin: 10px;
            font-size: 15px
        }

        QDialogButtonBox {
            font-size: 15px;
            height: 30px
        }
        QComboBox {
            font-size: 15px;
        }
        QCheckBox{
            font-size: 15px;
            margin-right:10px;
        }
        """
    return css
def css_DataTable():
    css="""
     #customers {
        font-family: Arial, Helvetica, sans-serif;
        border-collapse: collapse;
        width: 50%;
    }
    #customers td,
    #customers th {
        border: 1px solid #181818;
        padding: 8px;
        text-align: center;
    }

    #customers tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    #customers tr:hover {
        background-color: #ddd;
    }

    #customers th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
    }
    .container{
        display: grid;
        grid-template-columns: repeat(1, 1fr);
        grid-gap: 10px;
        position: absolute;
    }
    .p{
        font-weight: bold;
        font-size: 20px;
        padding-left: 20px;
    }
    """
    return css
