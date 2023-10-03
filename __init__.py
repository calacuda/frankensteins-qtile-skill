from mycroft import MycroftSkill, intent_handler
import requests


class FrankensteinsQtile(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def mk_url(self, path: str):
        """used to make urls for the API calls"""
        path = ("/" + path).replace("//", "/")
        ip = self.settings.get("nebula_ip") 
        return f"http://{ip}{path}"

    def is_group(self, group) -> bool:
        if not group:
            self.speak("sorry, but, could not find a group name in the utterance.")
        
        return bool(group)

    @intent_handler("qtile.frankensteins.focus-on.intent")
    def handle_focus_on(self, message):
        group = message.data.get("group")

        if not self.is_group(group): return

        self.log.info(f"switching qtile focus to group {group}", wait=True)
        res = requests.get(self.mk_url(f"focus-on/{group}"))

        if res.body.startswith("no group"):
            spelling = ", ".join(group)
            self.log.info(f"focus shifting failed")
            self.speak(f"{group.title()} spelled {spelling} is not a group name. Failed to switch focus.")
        else:
            self.log.info(f"focus shifting success")
            self.speak_dialog('qtile.frankensteins.focus-on')

    @intent_handler("qtile.frankensteins.move-to.intent")
    def handle_move_to(self, message):
        group = message.data.get("group")

        if not self.is_group(group): return

        self.log.info(f"moving window to the group called {group}", wait=True)
        res = requests.get(self.mk_url(f"move-to/{group}"))
        
        if res.body.startswith("no group"):
            spelling = ", ".join(group)
            self.log.info(f"moving of window failed")
            self.speak(f"{group.title()} spelled {spelling} is not a group name. Failed to move window.")
        else:
            self.log.info(f"moving of window success")
            self.speak_dialog('qtile.frankensteins.move-to')

    @intent_handler("qtile.frankensteins.auto-desk-layout.intent")
    def handle_auto_desk_layout(self, message):
        group = message.data.get("layout")

        if not self.is_group(group): return

        res = requests.get(self.mk_url(f"/auto-desk/layout/{layout}"))

        spelling = ", ".join(layout)
        self.speak(f"setting up layout {layout.title()} spelled {spelling}.")
        # self.log.info(f"moving of window success")
        self.speak_dialog('qtile.frankensteins.auto-desk-layout')


def create_skill():
    return FrankensteinsQtile()

