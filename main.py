__version__ = "1.0.3"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from wakeonlan import send_magic_packet

DEVICES = {"pc": "ff.ff.ff.ff.ff.ff",
           "raspi": "ff.ff.ff.ff.ff.ff"}


class ButtonApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")

        """for device in DEVICES:
            device = Button(
                text=device,
                pos_hint={"center_x": 0.5, "center_y": 0.5})
            device.bind(on_press=self.magic)
            main_layout.add_widget(device)"""

        pc_button = Button(
            text="PC",
            pos_hint={"center_x": 0.5, "center_y": 0.5})
        pc_button.bind(on_press=self.pc_func)
        main_layout.add_widget(pc_button)

        raspi_button = Button(
            text="Raspberry Pi",
            pos_hint={"center_x": 0.5, "center_y": 0.5})
        raspi_button.bind(on_press=self.raspi_func)
        main_layout.add_widget(raspi_button)

        return main_layout

    def pc_func(self, instance):
        send_magic_packet(DEVICES["pc"])
        print("Sent packet to PC!")

    def raspi_func(self, instance):
        send_magic_packet(DEVICES["raspi"])
        print("Sent packet to Raspberry Pi!")


if __name__ == '__main__':
    app = ButtonApp()
    app.run()
