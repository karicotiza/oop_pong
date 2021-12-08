import turtle
import tkinter


# Игровое окно
class GamingWindow:
    """
    В классе есть проблема со свойством "canvas", это
    свойство создаёт и держит окрытым пустое окно. Если
    подразумевалось, что вся программа будет выполняться
    в одном окне, то это свойство нужно передавать в
    другие классы.
    """
    def __init__(self):
        self.__game_state = StateOfTheGame
        # self.__canvas = tkinter.Tk()

    @staticmethod
    def main():
        window = NicknameInputMenu()
        window.display()


class Menu:
    """
    Та же проблема со свойством "canvas", что и в классе "Игровое окно"
    """
    def __init__(self):
        self.__next = 0
        # self.__canvas = tkinter.Tk()

    def set_next(self, menu):
        self.__next = menu
        return self.__next

    def display(self):
        pass

    def execute(self):
        pass


# Меню ввода никнеймов
class NicknameInputMenu(Menu):
    def __init__(self):
        super().__init__()
        self.__canvas = tkinter.Tk()
        self.__nickname_input_1 = tkinter.Entry(self.__canvas, width=40)
        self.__nickname_input_2 = tkinter.Entry(self.__canvas, width=40)
        self.__submit_button = tkinter.Button(
            self.__canvas, text="Подтвердить", width=33, bg="red", fg="white", command=self.execute
        )
        self.__next = 0

    def set_next(self, menu):
        self.__next = menu
        return self.__next

    def display(self):
        self.__canvas.title("Меню ввода никнеймов")
        self.__nickname_input_1.grid(row=0, pady=(20, 5), padx=20)
        self.__nickname_input_2.grid(row=1, pady=(5, 5), padx=20)
        self.__submit_button.grid(row=2, pady=(5, 20), padx=20)
        self.__canvas.mainloop()

    def execute(self):
        check = NicknameCheckCommand()
        check.execute(self.__nickname_input_1.get(), self.__nickname_input_2.get())
        self.__canvas.destroy()
        self.set_next(MainMenu())
        self.__next.display()


# Комманда
class Command:
    """
    Зачем создавать класс с одним методом, который постоянно переопределяется ?
    """

    def execute(self, string_array):
        pass


# Команда проверки никнейма
class NicknameCheckCommand(Command):
    def __init__(self):
        self.__forbidden_chars = str()

    def execute(self, *args):
        pass


# Команда установки формата матча
class SetMatchFormatCommand(Command):
    def __init__(self):
        self.__match_format = 0

    def execute(self, string_array):
        pass


# Формат матча
class MatchFormat:
    """
    Кажется этот класс должен взаимодействовать с другими - на диаграмме не взаимодействует
    """

    def __init__(self):
        self.__tie_break_score = str()
        self.__games_total = 0

    def is_tie_break(self, score):
        if score > self.__tie_break_score:
            boolean = True
        else:
            boolean = False
        return boolean


# Настройки матча
class MatchSettings:
    """
    В свойствах, класс создаёт сам себя по рекурсии ?
    """

    def __init__(self):
        self.__game_pre_settings = MatchSettings()
        self.__match_format = MatchFormat()
        self.__game_mode = str()

    def get_game_pre_settings(self):
        return self.__game_pre_settings

    def set_match_format(self):
        pass

    def get_match_format(self):
        return self.__match_format

    def set_game_mode(self):
        pass

    def get_game_mode(self):
        return self.__game_mode


# Главное меню
class MainMenu(Menu):
    """
    1. В диаграмме у класса 3 свойства типа "кнопка",
    в набросках интерфейса 4 кнопки

    2. У класса один метод "execute" и результат нажатия
    на кнопку, может быть только один
    """
    def __init__(self):
        super().__init__()
        self.__canvas = tkinter.Tk()
        self.__select_match_format_button = tkinter.Button(
            self.__canvas, text="Формат", width=33, bg="white", fg="black", command=self.execute
        )
        self.__settings_button = tkinter.Button(
            self.__canvas, text="Настройки", width=33, bg="white", fg="black", command=self.execute
        )
        self.__exit_button = tkinter.Button(
            self.__canvas, text="Выход", width=33, bg="red", fg="white", command=self.execute
        )
        self.__next = 0

    def set_next(self, menu):
        self.__next = menu
        return self.__next

    def display(self):
        self.__canvas.title("Главное меню")
        self.__select_match_format_button.grid(row=0, pady=(20, 5), padx=20)
        self.__settings_button.grid(row=1, pady=(5, 5), padx=20)
        self.__exit_button.grid(row=2, pady=(5, 20), padx=20)
        self.__canvas.mainloop()

    def execute(self):
        self.__canvas.destroy()
        self.set_next(MatchFormatSelectionMenu())
        self.__next.display()


# Меню выбора формата матча
class MatchFormatSelectionMenu(Menu):
    def __init__(self):
        super().__init__()
        self.__canvas = tkinter.Tk()
        self.__three_games_button = tkinter.Button(
            self.__canvas, text="Три тайма", width=33, bg="white", fg="black", command=self.execute
        )
        self.__five_game_button = tkinter.Button(
            self.__canvas, text="Пять таймов", width=33, bg="white", fg="black", command=self.execute
        )
        self.__next = 0

    def set_next(self, menu):
        self.__next = menu
        return self.__next

    def display(self):
        self.__canvas.title("Главное меню")
        self.__three_games_button.grid(row=0, pady=(20, 5), padx=20)
        self.__five_game_button.grid(row=1, pady=(5, 20), padx=20)
        self.__canvas.mainloop()

    def execute(self):
        self.__canvas.destroy()
        self.set_next(GameModeSelectionMenu())
        self.__next.display()


# Меню выбора режима игры
class GameModeSelectionMenu(Menu):
    def __init__(self):
        super().__init__()
        self.__canvas = tkinter.Tk()
        self.__vs_computer_button = tkinter.Button(
            self.__canvas, text="Против компьютера", width=33, bg="white", fg="black", command=self.execute
        )
        self.__one_vs_one_button = tkinter.Button(
            self.__canvas, text="На двоих", width=33, bg="white", fg="black", command=self.execute
        )
        self.__couple_button = tkinter.Button(
            self.__canvas, text="Двое против компьютера", width=33, bg="white", fg="black", command=self.execute
        )
        self.__next = 0

    def set_next(self, menu):
        self.__next = menu
        return self.__next

    def display(self):
        self.__canvas.title("Меню выбора режима матча")
        self.__vs_computer_button.grid(row=0, pady=(20, 5), padx=20)
        self.__one_vs_one_button.grid(row=1, pady=(5, 5), padx=20)
        self.__couple_button.grid(row=2, pady=(5, 20), padx=20)
        self.__canvas.mainloop()

    def execute(self):
        self.__canvas.destroy()
        self.set_next(PlayingField())
        self.__next.display()


# Игровое поле
class PlayingField(Menu):
    def __init__(self):
        super().__init__()
        self.__canvas = turtle.Screen()
        self.__ball_controller = BallController()
        self.__paddle_controller = RacketModel()
        self.__game_state = StateOfTheGame()
        self.__next = 0

    def set_next(self, menu):
        self.__next = menu
        return self.__next

    def display(self):
        self.__canvas.title("Теннис")
        self.__canvas.bgcolor("black")
        self.__canvas.setup(width=1000, height=600)

        left_pad = turtle.Turtle()
        left_pad.speed(0)
        left_pad.shape("square")
        left_pad.color("white")
        left_pad.shapesize(stretch_wid=6, stretch_len=2)
        left_pad.penup()
        left_pad.goto(-400, 0)

        right_pad = turtle.Turtle()
        right_pad.speed(0)
        right_pad.shape("square")
        right_pad.color("white")
        right_pad.shapesize(stretch_wid=6, stretch_len=2)
        right_pad.penup()
        right_pad.goto(400, 0)

        middle_line = turtle.Turtle()
        middle_line.speed(0)
        middle_line.shape("square")
        middle_line.color("white")
        middle_line.shapesize(stretch_wid=30, stretch_len=0.1)
        middle_line.penup()
        middle_line.goto(0, 0)

        hit_ball = turtle.Turtle()
        hit_ball.speed(40)
        hit_ball.shape("circle")
        hit_ball.color("white")
        hit_ball.penup()
        hit_ball.goto(0, 0)
        hit_ball.dx = 5
        hit_ball.dy = -5

        sketch = turtle.Turtle()
        sketch.speed(0)
        sketch.color("white")
        sketch.penup()
        sketch.hideturtle()
        sketch.goto(0, 260)
        sketch.write("0    0", align="center", font=("Courier", 24, "normal"))

    def execute(self):
        pass


# Послеигровое поле
class PostGameMenu(Menu):
    def __init__(self):
        super().__init__()
        self.__canvas = tkinter.Tk()
        self.__start_again_button = tkinter.Button(self.__canvas)
        self.__quit_game_button = tkinter.Button(self.__canvas)
        self.__next = None

    def set_next(self, menu):
        self.__next = menu
        return self.__next

    def display(self):
        pass

    def execute(self):
        pass


# Биндер кнопок
class KeyBinder:
    def bind_keys(self, paddle_controllers):
        pass


# Вид ракетки
class RacketType:
    def draw(self, canvas):
        pass


# Модель ракетки
class RacketModel:
    def __init__(self):
        self.__x = float()
        self.__y = float()
        self.__x_acceleration = float()
        self.__y_acceleration = float()
        self.__height = float()
        self.__width = float()

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x_acceleration(self, new_acceleration):
        pass

    def set_y_acceleration(self, new_acceleration):
        pass

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


# Контроллер ракетки
class RacketController:
    def __init__(self):
        self.__paddle_model = RacketModel()
        self.__paddle_view = RacketType()

    def move_paddle(self, canvas):
        pass

    def get_paddle(self):
        return self.__paddle_model


# Вид мяча
class BallType:
    def draw(self, canvas):
        pass


# Модель мяча
class BallModel:
    def __init__(self):
        self.__x = float()
        self.__y = float()
        self.__x_acceleration = float()
        self.__y_acceleration = float()
        self.__radius = float()

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x_acceleration(self, new_acceleration):
        self.__x_acceleration = new_acceleration

    def set_y_acceleration(self, new_acceleration):
        self.__y_acceleration = new_acceleration

    def get_radius(self):
        return self.__radius


# Контроллер мяча
class BallController:
    def __init__(self):
        self.__ball_model = BallModel()
        self.__ball_view = BallType()

    def move_ball(self, canvas):
        pass

    def get_ball_model(self):
        return self.__ball_model

    def change_direction(self):
        pass


# Инжектор контроллеров
class ControllerInjector:
    """
    Как методы должны получать данные о том, что им нужно возвращать ?
    """

    @staticmethod
    def get_paddle_controller():
        return RacketController

    @staticmethod
    def get_ball_controller():
        return BallController


# Детектор столкновений
class CollisionDetector:
    @staticmethod
    def is_colliding(ball_model, racket_model):
        if ball_model == racket_model:
            return True
        else:
            return False


# Состояние игры
class StateOfTheGame:
    def __init__(self):
        self.__current_score = str()

    def get_current_score(self):
        return self.__current_score

    def set_current_score(self, left, right):
        pass


# Меню настроек
class SettingsMenu(Menu):
    """
    На диаграмме, класс ни кем не вызвается, а вроде должен вызываться из класса "Главное меню"
    """

    def __init__(self):
        super().__init__()
        self.__canvas = tkinter.Tk()
        self.__up_key_input_1 = tkinter.Entry(self.__canvas)
        self.__up_key_input_2 = tkinter.Entry(self.__canvas)
        self.__up_key_input_3 = tkinter.Entry(self.__canvas)
        self.__up_key_input_4 = tkinter.Entry(self.__canvas)
        self.__down_key_input_1 = tkinter.Entry(self.__canvas)
        self.__down_key_input_2 = tkinter.Entry(self.__canvas)
        self.__down_key_input_3 = tkinter.Entry(self.__canvas)
        self.__down_key_input_4 = tkinter.Entry(self.__canvas)
        self.__next = MainMenu()

    def set_next(self, menu):
        self.__next = menu
        return self.__next

    def display(self):
        pass

    def execute(self):
        pass


# Команда установки настроек
class SetupCommand:
    def __init__(self):
        self.__settings = Settings

    def execute(self, string_array):
        pass


# Настройки
class Settings:
    """
    В свойствах, класс создаёт сам себя по рекурсии ?
    """

    def __init__(self):
        self.__settings = Settings
        self.__player_keys = PlayerButtons

    def __get_player_keys(self):
        return self.__player_keys

    def __set_player_keys(self, player_keys):
        self.__player_keys = player_keys

    def get_settings(self):
        return self.__settings


# Кнопки игрока
class PlayerButtons:
    """
    В диаграмме нету типа данных "кнопка", но переменные в этом классе должны быть этого типа
    """

    def __init__(self):
        self.__key_up = str()
        self.__key_down = str()

    def get_key_up(self):
        return self.__key_up

    def set_key_up(self, button):
        self.__key_up = button

    def get_key_down(self):
        return self.__key_down

    def set_key_down(self, button):
        self.__key_down = button


if __name__ == "__main__":
    game = GamingWindow()
    game.main()
