class Light:
    """Свет."""
    def turn_on(self):
        print('Включить свет')

    def turn_off(self):
        print('Выключить свет')


class CommandBase:
    """Базовая команда."""
    def execute(self):
        raise NotImplementedError()


class LightCommandBase(CommandBase):
    """Выключатель света."""
    def __init__(self, light):
        self.light = light


class TurnOnLightCommand(LightCommandBase):
    """Включить свет"""
    def execute(self):
        self.light.turn_on()


class TurnOffLightCommand(LightCommandBase):
    """Выключить свет"""
    def execute(self):
        self.light.turn_off()


class Switch:
    """Переключатель"""
    def __init__(self, on_command, off_command):
        self.on_command = on_command
        self.off_command = off_command

    def on(self):
        self.on_command.execute()

    def off(self):
        self.off_command.execute()


light = Light()
switch = Switch(on_command=TurnOnLightCommand(light),
                off_command=TurnOffLightCommand(light))
switch.on()  # Включить свет
switch.off()  # Выключить свет