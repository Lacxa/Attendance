import json
from datetime import datetime
import os
from kivy import utils
from kivy import platform
from kivymd.uix.textfield import MDTextField
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.pickers import MDDatePicker

from database import Uzuri as Uz

import kivymd_extensions.akivymd



Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"
Clock.max_iteration = 250


if utils.platform != 'android':
    Window.size = [420, 740]
    #pass
else:
    from jnius import autoclass

class MainApp(MDApp):
    # APP
    screens = ['home']
    screens_size = NumericProperty(len(screens) - 1)
    current = StringProperty(screens[len(screens) - 1])
    month_name = StringProperty("")
    selected_date = StringProperty("")

    internet = StringProperty("asset/slide_three_img.png")
    nodata = StringProperty("asset/slide_three_img.png")

    def on_start(self):
        self.keyboard_hooker()
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Gray"
        #self.display()
        self.month()

    """ KEYBOARD INTEGRATION """

    def keyboard_hooker(self, *args):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        print(self.screens_size)
        if key == 27 and self.screens_size > 0:
            print(f"your were in {self.current}")
            last_screens = self.current
            self.screens.remove(last_screens)
            print(self.screens)
            self.screens_size = len(self.screens) - 1
            self.current = self.screens[len(self.screens) - 1]
            self.screen_capture(self.current)
            return True
        elif key == 27 and self.screens_size == 0:
            toast('Press Home button!')
            return True

    """ SCREEN FUNCTIONS """

    def screen_capture(self, screen):
        sm = self.root
        sm.current = screen
        if screen in self.screens:
            pass
        else:
            self.screens.append(screen)
        print(self.screens)
        self.screens_size = len(self.screens) - 1
        self.current = self.screens[len(self.screens) - 1]
        print(f'size {self.screens_size}')
        print(f'current screen {screen}')

    def screen_leave(self):
        print(f"your were in {self.current}")
        last_screens = self.current
        self.screens.remove(last_screens)
        print(self.screens)
        self.screens_size = len(self.screens) - 1
        self.current = self.screens[len(self.screens) - 1]
        self.screen_capture(self.current)

    """ DISPENSING FUNCTIONS """

    def update_graph(self):
        chart3 = self.root.ids.chart3
        chart3.x_labels =  ["Visitors", "Schools", "Students"]
        chart3.y_labels = ["45", "50", "65"]
        chart3.update()

    def display(self):
        self.root.ids.prt.data = {}
        self.root.ids.vis.data = {}
        self.root.ids.pvs.data = {}
        data = Uz.parent(Uz())
        data2 = Uz.vistor(Uz())


        self.root.ids.pvs.data.append(
            {
                "viewclass": "InfoCard",
                "name": "Parents",
            }
        )
        self.root.ids.pvs.data.append(
            {
                "viewclass": "InfoCard",
                "name": "Visitors / Guider / School teacher",
            }
        )

        if data:
            for i, y in data.items():
                for child in y["children"]:
                    self.root.ids.prt.data.append(
                        {
                            "viewclass": "StuCard",
                            "name": child["name"],
                            "pname": y["name"],
                            "pnumber": y["phone"],
                            "cage": child["age"],
                        }
                    )

        else:
            self.root.ids.prt.data.append(
                {
                    "viewclass": "StuCardx",
                    "name": "No data available yet!",
                }
            )

        if data2:
            for i, y  in data2.items():
                self.root.ids.vis.data.append(
                    {
                        "viewclass": "VisCard",
                        "name": y["company_name"],
                        "gname": y["guider_name"],
                        "total": y["number_of_visitors"],
                        "phone": y["phone_number"],
                    }
                )

        else:
            self.root.ids.vis.data.append(
                {
                    "viewclass": "StuCardx",
                    "name": "No data available yet!",
                }
            )

    def month(self):
        current_time = datetime.now()
        month_name = current_time.strftime("%B")
        date_str = current_time.strftime("%Y-%m-%d")
        self.root.ids.date_label.text = date_str

        self.month_name = month_name

    def show_date_picker(self):
        self.theme_cls.primary_palette = "Blue"
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.root.ids.date_label.text = f"Selected Date: {value}"
        self.get_date(value)

    def on_cancel(self, instance, value):
        # Handle the cancel event (optional)
        self.root.ids.date_label.text = "Selection Canceled"
        self.root.ids.date_label.text_color =  (1, 0, 0, .5)

    def choice(self, name):
        print("choice")
        if name == "Parents":
            # screen_manager.current = "parent"
            screen_manager = self.root.ids.screen_manager
            screen_manager.current = "student"

        else:
            screen_manager = self.root.ids.screen_manager
            screen_manager.current = "visitor"

    def search(self):
        search_text = self.root.ids.search_field.text
        print(f"Searching for: {search_text}")

    def student_choice(self, name, pname, pnumber, cage):

        self.root.ids.parent_name.text = pname
        self.root.ids.contact.text = pnumber
        self.root.ids.child.text = name
        self.root.ids.age.text = cage + "  Years old"


        screen_manager = self.root.ids.screen_manager
        screen_manager.current = "parinfo"

    def visitor_choice(self, name, gname, total , phone):
        self.root.ids.sname.text = name
        self.root.ids.gui.text = gname
        self.root.ids.no.text = phone
        self.root.ids.total.text = total

        screen_manager = self.root.ids.screen_manager
        screen_manager.current = "visinfo"

    def get_date(self, date):
        Uz.

    # def generate_pdf(self):
    #     now = datetime.now()
    #     timestamp = now.strftime("%Y%m%d_%H%M%S")
    #     filename = f"report_{timestamp}.pdf"
    #     filepath = os.path.join(self.user_data_dir, filename)  # saves file in app data directory
    #     try:
    #         c = canvas.Canvas(filepath, pagesize=letter)
    #         # Add content to the PDF (replace with your actual data)
    #         c.drawString(72, 750, "This is a simple report.")  # Example content
    #         c.save()
    #         self.root.ids.filename_label.text = filename
    #         print(f"Report saved to: {filepath}")
    #         return filepath
    #     except Exception as e:
    #         print(f"Error generating report: {e}")
    #         return None

    def share_whatsapp(self):
        filepath = self.generate_pdf()
        if filepath and platform == "android":
            try:
                PythonActivity = autoclass("org.kivy.android.PythonActivity")
                Intent = autoclass("android.content.Intent")
                Uri = autoclass("android.net.Uri")
                File = autoclass("java.io.File")

                intent = Intent(Intent.ACTION_SEND)
                intent.setType("application/pdf")

                file = File(filepath)
                uri = Uri.fromFile(file)
                intent.putExtra(Intent.EXTRA_STREAM, uri)
                intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)

                chooser = Intent.createChooser(intent, "Share PDF")
                PythonActivity.mActivity.startActivity(chooser)
            except Exception as e:
                print(f"Error sharing: {e}")
        elif filepath:
            print("Sharing is only available on Android devices")
        else:
            print("No file was created")

    def permition(self):

        if platform == "android":
            from android.permissions import request_permissions, Permission
        if platform == "android":
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])


    def register_caller(self, ):
        with open("parent.json", "w") as file:
            data = ["Uz.vistor(Uz())"]
            data_dump = json.dumps(data, indent=2)
            file.write(data_dump)
            file.close()

# add aa def in database forparent.json to have the full parent data then when searching easy


    def load(self, data_file_name):
        with open(data_file_name, "r") as file:
            initial_data = json.load(file)
        return initial_data


MainApp().run()