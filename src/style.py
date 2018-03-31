def setStyleSheet(app, theme):
    
    if theme == 'light':

        app.setStyleSheet("""
            QTableWidget {
                font-family: "Consolas";
                font-size: 10pt;
                gridline-color: #e4e4e4;
            }
            QLineEdit {
                border: 1px solid #c1c1c1;
                font-size: 12px;
                border-radius: 2px;
                margin-top: 2px;
                margin-bottom: 2px;
                padding-left: 5px;
            }
            QTextEdit {
                font-family: "Consolas";
                font-size: 10pt;
            }
            QPlainTextEdit {
                font-family: "Consolas";
                font-size: 10pt;
            }
            QGroupBox {
                font-weight: bold;
                color: #111
            }
            QTabBar::tab:selected {
            }
    """)

    elif theme == 'dark':
        pass