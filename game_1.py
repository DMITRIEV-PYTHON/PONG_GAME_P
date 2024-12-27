import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PONG GAME"

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.1)  # Масштаб 0.1
        self.change_x = 3  # Начальная скорость по оси X
        self.change_y = 3  # Начальная скорость по оси Y

    def update(self):
        # Обновление позиции мяча
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Отражение мяча от верхней и нижней границы экрана
        if self.top >= SCREEN_HEIGHT or self.bottom <= 0:
            self.change_y *= -1

        # Отражение мяча от левой и правой границы экрана
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x *= -1

    def check_collision_with_bar(self, bar):
        # Проверка столкновения с платформой
        if arcade.check_for_collision(self, bar):
            self.change_y *= -1  # Отражение мяча

class Bar(arcade.Sprite):
    def __init__(self):
        # Убедитесь, что bar.png существует в том же каталоге
        super().__init__('bar.png', 0.1)  # Масштаб 0.1
        self.speed = 5  # Скорость движения платформы
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 5

    def update(self, keys_pressed):
        # Управление движением платформы
        if arcade.key.LEFT in keys_pressed and self.left > 0:
            self.center_x -= self.speed
        if arcade.key.RIGHT in keys_pressed and self.right < SCREEN_WIDTH:
            self.center_x += self.speed

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.keys_pressed = set()  # Множество нажатых клавиш
        self.setup()

    def setup(self):
        # Инициализация начальных позиций
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        # Очистка экрана
        self.clear((255, 255, 255))  # Белый фон
        # Рисуем платформу и мяч
        self.bar.draw()
        self.ball.draw()

    def on_update(self, delta_time):
        # Обновление состояния игры
        self.ball.update()  # Обновляем мяч
        self.bar.update(self.keys_pressed)  # Обновляем платформу
        self.ball.check_collision_with_bar(self.bar)  # Проверка столкновений

    def on_key_press(self, symbol, modifiers):
        # Добавление клавиши в множество нажатых
        self.keys_pressed.add(symbol)

    def on_key_release(self, symbol, modifiers):
        # Удаление клавиши из множества нажатых
        self.keys_pressed.discard(symbol)


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
