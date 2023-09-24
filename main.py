from win10toast import ToastNotifier


toast = ToastNotifier()
while True:
    toast.show_toast(
        # Title
        "Remainder",
        # Description
        "Hey Man, Drink Water",
        # Duration in seconds
        duration=20,
        icon_path="Bottle_of_Water_icon-icons.com_68778.ico",
        threaded=True,
    )
