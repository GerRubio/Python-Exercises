# Example of OOPP.

class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.status = 0
        self.apps = []

    def power_on(self):
        self.status = 1

    def power_off(self):
        self.status = 0

    def install_app(self, app):
        self.apps.append(app)

    def uninstall_app(self, app):
        self.apps.remove(app)

google = MobilePhone('Google', 6.0, 8)

google.apps = ['Instagram', 'Twitter', 'Telegram', 'WhatsApp']

google.power_on()
print(f'Phone status: {google.status}')

google.install_app(google.apps)
print(f'App installed: {google.apps}')

google.uninstall_app(google.apps[1])
print(f'App uninstalled: {google.apps}')

google.power_off()
print(f'Phone status: {google.status}')