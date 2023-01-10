import sys
from qtpy import QtWidgets, QtWebEngineWidgets

class Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the web engine view
        self.view = QtWebEngineWidgets.QWebEngineView(self)

        # Set the web engine view as the central widget
        self.setCentralWidget(self.view)

        # Create the address bar
        self.address_bar = QtWidgets.QLineEdit(self)
        self.address_bar.returnPressed.connect(self.load_page)

        # Create the back and forward buttons
        self.back_button = QtWidgets.QPushButton("<", self)
        self.back_button.clicked.connect(self.view.back)
        self.forward_button = QtWidgets.QPushButton(">", self)
        self.forward_button.clicked.connect(self.view.forward)

        # Create the refresh button
        self.refresh_button = QtWidgets.QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self.view.reload)

        # Create the light and dark mode buttons
        self.light_button = QtWidgets.QPushButton("Light Mode", self)
        self.light_button.clicked.connect(self.set_light_mode)
        self.dark_button = QtWidgets.QPushButton("Dark Mode", self)
        self.dark_button.clicked.connect(self.set_dark_mode)

        # Create the layout and add the widgets
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.back_button)
        self.layout.addWidget(self.forward_button)
        self.layout.addWidget(self.refresh_button)
        self.layout.addWidget(self.address_bar)
        self.layout.addWidget(self.light_button)
        self.layout.addWidget(self.dark_button)

        # Set the layout as the main window's layout
        self.setLayout(self.layout)

        # Set the main window properties
        self.setWindowTitle("Web Browser")
        self.setGeometry(100,100,800,600)
        self.show()

    def load_page(self):
        # Get the URL from the address bar
        url = self.address_bar.text()

        # Load the URL into the web engine view
        self.view.load(QtWebEngineWidgets.QUrl(url))

    def set_light_mode(self):
        # Set the application's style sheet to light mode
        app.setStyleSheet("""
        QMainWindow {
            background-color: white;
            color: black;
        }
        """)

    def set_dark_mode(self):
        # Set the application's style sheet to dark mode
        app.setStyleSheet("""
       
