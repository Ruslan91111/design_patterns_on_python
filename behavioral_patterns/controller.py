from abc import ABC, abstractmethod


class WindowBase(ABC):
    @abstractmethod
    def show(self):
        raise NotImplementedError()

    @abstractmethod
    def hide(self):
        raise NotImplementedError()


class MainWindow(WindowBase):
    def show(self):
        print('Show MainWindow')

    def hide(self):
        print('Hide MainWindow')


class SettingWindow(WindowBase):
    def show(self):
        print('Show SettingWindow')

    def hide(self):
        print('Hide SettingWindow')


class HelpWindow(WindowBase):
    def show(self):
        print('Show HelpWindow')

    def hide(self):
        print('Hide HelpWindow')


class WindowController:
    # Посредник для работы с окнами.
    def __init__(self):
        self.windows = dict.fromkeys(['main', 'setting', 'help'])

    def show(self, win):
        # Показываем только запрашиваемое окно, остальные скрываем.
        for window in self.windows.values():
            if window is not win:
                window.hide()
        win.show()

    def set_main(self, win):
        self.windows['main'] = win

    def set_setting(self, win):
        self.windows['setting'] = win

    def set_help(self, win):
        self.windows['help'] = win

# Инициализируем разные окна.
main_win = MainWindow()
setting_win = SettingWindow()
help_win = HelpWindow()

# Инициализируем контроллер и передаем в него наши окна.
controller = WindowController()
controller.set_main(main_win)
controller.set_setting(setting_win)
controller.set_help(help_win)

main_win.show()  # Show MainWindow

controller.show(setting_win)
# Hide MainWindow
# Hide HelpWindow
# Show SettingWindow

controller.show(help_win)
# Hide MainWindow
# Hide SettingWindow
# Show HelpWindow