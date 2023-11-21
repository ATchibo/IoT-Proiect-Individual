from kivy.clock import Clock
from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.scrollview import MDScrollView
from matplotlib import pyplot as plt


Builder.load_file("components/homepage/watering_history_view.kv")


class WateringHistoryView(MDBoxLayout):
    def __init__(self, **kwargs):
        super(WateringHistoryView, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = 1
        Clock.schedule_once(self.init, 0.1)

    def init(self, *args):
        ml = self.ids.watering_history_list

        contacts = ["Paula", "John", "Kate", "Vlad"]
        for c in contacts:
            ml.add_widget(
                OneLineListItem(
                    text=c
                )
            )