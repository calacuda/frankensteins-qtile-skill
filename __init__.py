from mycroft import MycroftSkill, intent_handler


class FrankensteinsQtile(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('qtile.frankensteins.intent')
    def handle_qtile_frankensteins(self, message):
        self.speak_dialog('qtile.frankensteins')


def create_skill():
    return FrankensteinsQtile()

