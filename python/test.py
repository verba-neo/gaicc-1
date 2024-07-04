from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast('하이요', '짜잔!', duration=10, threaded=True)