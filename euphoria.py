import arcade

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
SCREEN_TITLE = "WELCOME"



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        """
        Initializer for the game
        """

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.WHITE_SMOKE)
        self._current_view: Optional[View] = None

    def setup(self):
        self.char_list = arcade.SpriteList()
        self.cat = arcade.Sprite(":resources:images/animated_characters/image/welc_1.png")
        self.cat.center_x = 700
        self.cat.center_y = 350
        self.char_list.append(self.cat)
        self.current_mouse_x = 0
        self.current_mouse_y = 0
        self.bg_switch = False
        self.draw_timer = 0
        self.bg_x_timer = 0
        self.bg_x = []
        self.backgrounds = []
        # self.main_menu_open = True
        path = "image/backgrounds"


    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()
        # Draw our sprites
        self.char_list.draw()
        if self.main_menu_open:
            for i in range(len(self.backgrounds)):
                arcade.draw_texture_rectangle(self.bg_x[i], int(SCREEN_HEIGHT / 2), SCREEN_WIDTH, SCREEN_HEIGHT,
                                              self.backgrounds[i])
        if self.draw_timer > self.bg_x_timer:
            for k in range(len(self.bg_x)):
                if self.bg_x[k] <= -720:
                    self.bg_x[k] = max(self.bg_x) + SCREEN_WIDTH
                self.bg_x[k] -= 1

        if max(self.bg_x) % 720 == 0:
            self.bg_switch = not self.bg_switch
            if not self.bg_switch:
                self.bg_x_timer = self.draw_timer + 200

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.x = range(700, 750)
        self.y = range(350, 400)
        self.button = arcade.MOUSE_BUTTON_LEFT
        MyGame.on_update(self, 1)

    def on_update(self, delta_time: float):

        # if self._current_view is not None:
        #     self._current_view.on_update(0.1)
        try:
            self.textbox_time += 0.1
            seconds = self.textbox_time % 60
            if seconds >= 0.115:
                if self.textbox_list:
                    for textbox in self.textbox_list:
                        textbox.update(1, self.key)
                    self.textbox_time = 0.0
        except AttributeError:
            pass
def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
