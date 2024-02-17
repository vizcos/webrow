import sys
import pyfiglet
import requests
from rich.console import Console
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class XOBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(XOBrowser, self).__init__(*args, **kwargs)
        self.setStyleSheet("background-color: #36393f; color: #ffffff;")

        self.browser = QWebEngineView()
        self.func876()
        self.browser.urlChanged.connect(self.func543)
        self.browser.loadFinished.connect(self.func298)
        self.browser.loadStarted.connect(self.func789)
        self.browser.page().profile().downloadRequested.connect(self.func654)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.status.setStyleSheet("background-color: #202225; color: #ffffff;")
        self.setStatusBar(self.status)

        self.func122()

        self.show()

    def func876(self):
        default_url = self.func333()
        if default_url:
            self.browser.setUrl(QUrl(default_url))
        else:
            print("Failed to fetch default URL from def.txt")

    def func333(self):
        url = "https://xo-dl.vercel.app/def.txt"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            print("Failed to fetch default URL from:", url)
            return None

    def func122(self):
        navtb = QToolBar("Navigation")
        navtb.setStyleSheet("background-color: #202225; color: #ffffff;")
        self.addToolBar(navtb)

        back_btn = QAction("<-", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction("->", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction("↻", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction("⌂", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.func432)
        navtb.addAction(home_btn)

        abt_btn = QAction("?", self)
        abt_btn.setStatusTip("About xo")
        abt_btn.triggered.connect(self.func555)
        navtb.addAction(abt_btn)

        navtb.addSeparator()

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.func234)
        self.urlbar.setStyleSheet("background-color: #202225; color: #ffffff;")
        navtb.addWidget(self.urlbar)

        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

    def func298(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - xo browser [the unhackable browser]" % title)

    def func432(self):
        default_url = self.func333()
        if default_url:
            self.browser.setUrl(QUrl(default_url))
        else:
            print("Failed to fetch default URL from def.txt")

    def func234(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)

    def func543(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def func789(self):
        url = self.browser.url().toString()
        console.print(f"[URL]: Opened URL: {url}", style="bold red")

    def func654(self, itm):
        dlpth, _ = QFileDialog.getSaveFileName(self, "Save File", itm.path(),
                                                       "All Files (*)")
        if dlpth:
            itm.setPath(dlpth)
            itm.accept()

    def func555(self):
        self.browser.setUrl(QUrl("https://xo-dl.vercel.app/about.html"))


app = QApplication(sys.argv)
app.setApplicationName("xo browser - The Unhackable Browser")
console = Console()
console.print(pyfiglet.figlet_format("xo\ndev logs", font="slant"), style="bold purple")
window = XOBrowser()
app.exec_()
