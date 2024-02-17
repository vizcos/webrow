import sys
import pyfiglet
from rich.console import Console
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class SoulzBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(SoulzBrowser, self).__init__(*args, **kwargs)
        self.setStyleSheet("background-color: #36393f; color: #ffffff;")
        
        # Ask for audio permission with a popup message
        permission = QMessageBox.question(self, "Audio Permission", "Allow audio playback?", QMessageBox.Yes | QMessageBox.No)
        self.allow_audio = permission == QMessageBox.Yes
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)
        self.browser.loadStarted.connect(self.print_opened_url)
        self.browser.page().profile().downloadRequested.connect(self.handle_download)
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.status.setStyleSheet("background-color: #202225; color: #ffffff;")
        self.setStatusBar(self.status)
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
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
        abt_btn = QAction("!", self)
        abt_btn.setStatusTip("download xo browser")
        abt_btn.triggered.connect(self.about)
        navtb.addAction(abt_btn)
        navtb.addSeparator()
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.urlbar.setStyleSheet("background-color: #202225; color: #ffffff;")
        navtb.addWidget(self.urlbar)
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)
        self.show()

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - soulz rowser [the hub browser]" % title)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def print_opened_url(self):
        url = self.browser.url().toString()
        console.print(f"[URL]: Opened URL: {url}", style="bold red")

    def handle_download(self, download_item):
        download_path, _ = QFileDialog.getSaveFileName(self, "Save File", download_item.path(),
                                                       "All Files (*);;Text Files (*.txt)")
        if download_path:
            download_item.setPath(download_path)
            download_item.accept()

    def about(self, url):
        self.browser.setUrl(QUrl("https://xo-dl.vercel.app/xobrowser.zip"))
        
    def closeEvent(self, event):
        if self.allow_audio:
            event.accept()
        else:
            event.ignore()

app = QApplication(sys.argv)
app.setApplicationName("Soulz Browser - the hub browser")
console = Console()
console.print(pyfiglet.figlet_format("soulz browser \ndev logs", font="slant"), style="bold purple")
window = SoulzBrowser()
app.exec_()
