#imports
import wx
import requests
from bs4 import BeautifulSoup

#price scraping
#27
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
}
URL = 'https://www.amazon.nl/iiyama-GB2730HSU-B1-1920x1080-DisplayPort-HDMI-VGA-USB-verstelbaar/dp/B07CZG35VV/ref=sr_1_16?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=iiyama&qid=1603039574&sr=8-16'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
price = soup.find(id="price_inside_buybox")
print(price.text)
#24
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
}
URL = 'https://www.amazon.nl/iiyama-GB2530HSU-B1-1920x1080-DisplayPort-HDMI-VGA-USB-verstelbaar/dp/B07CZG3GHQ/ref=sr_1_6?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=iiyama&qid=1603135668&sr=8-6'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
price2 = soup.find(id="price_inside_buybox")
print(price2.text)
#34
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'
}
URL = 'https://www.amazon.nl/iiyama-XUB3493WQSU-B1-3440x1440-DisplayPort-HDMI-USB3-0-verstelbaar/dp/B07XHLG8G3/ref=sr_1_1?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=iiyama&qid=1603135614&refinements=p_n_size_browse-bin%3A16365476031&rnid=16365040031&s=electronics&sr=1-1'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
price3 = soup.find(id="price_inside_buybox")
print(price3.text)

#graphical results
class Example(wx.Frame):
    
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)

        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, label='iiyama monitoren',
                                pos=(25, 15), size=(200, -1))
        heading.SetFont(font)

        wx.StaticLine(self, pos=(25, 50), size=(300,1))

        wx.StaticText(self, label='27 inch', pos=(25, 80))
        wx.StaticText(self, label='24inch', pos=(25, 100))
        wx.StaticText(self, label='144hz', pos=(25, 120))

        wx.StaticText(self, label= price.text, pos=(250, 80))
        wx.StaticText(self, label=price2.text, pos=(250, 100))
        wx.StaticText(self, label=price3.text, pos=(250, 120))

        wx.StaticLine(self, pos=(25, 260), size=(300,1))


        btn = wx.Button(self, label='sluiten', pos=(140, 310))

        btn.Bind(wx.EVT_BUTTON, self.OnClose)

        self.SetSize((360, 380))
        self.SetTitle('wx.StaticLine')
        self.Centre()

    def OnClose(self, e):

        self.Close(True)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
