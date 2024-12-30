import webview
from webview.errors import JavascriptException

webview.create_window(title="Яндекс Музыка", url='https://passport.yandex.ru/auth/list?origin=music_button-header&retpath=https%3A%2F%2Fmusic.yandex.ru%2Fsettings%3Freqid%3D30447626117300506896817380499798786%26from-passport', width=1366, height=768, resizable=False)
webview.start(private_mode=False)
