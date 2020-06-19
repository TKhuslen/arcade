import arcade

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Gradients Example"
SPEED = 50
BALL_SCALE = 0.02

class MenuView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """
        Set up the application.
        """

        super().__init__()

        self.shapes = arcade.ShapeElementList()

        # This is a large rectangle that fills the whole
        # background. The gradient goes between the two colors
        # top to bottom.
        color1 = (6, 90, 182)
        color2 = (72, 177, 191)
        points = (0, 0), (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), (0, SCREEN_HEIGHT)
        colors = (color1, color1, color2, color2)
        rect = arcade.create_rectangle_filled_with_colors(points, colors)
        self.shapes.append(rect)
        self.alexander_image = arcade.Sprite(":resources:images/hamilton.png", 0.3)
        self.alexander_image.center_x = 80
        self.alexander_image.center_y = 200
        self.welcome_image = arcade.Sprite(":resources:images/wel.png", 1)
        self.welcome_image.center_x = 200
        self.welcome_image.center_y = 500


    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()
        self.shapes.draw()
        arcade.draw_text("Instructions:", 150, 400, arcade.color.BLACK, 20)
        # arcade.draw_rectangle_filled(500, 500, 50, 50, (255, 0, 0, 127))
        arcade.draw_text("WASD controls red", 150, 320, arcade.color.BLACK, 15)
        arcade.draw_text("Arrows controls blue", 150, 220, arcade.color.BLACK, 15)
        arcade.draw_text("Click to start->", 200, 120, arcade.color.BLACK, 15)
        self.alexander_image.draw()
        self.welcome_image.draw()

    def on_mouse_press(self, x, y, button, mod):
        """ If the user presses the mouse button, changes the dialogue. """
        game_view = FirstMiniGame()
        game_view.setup()
        self.window.show_view(game_view)

class FirstMiniGame(arcade.View):
    def __init__(self):
        super().__init__()

        self.player_num = 0
        self.cur_player = None
        self.player_list = arcade.SpriteList()
        self.shooting_circles_list = []

        arcade.set_background_color(arcade.color.WHITE)
        self.background_image = arcade.Sprite(":resources:images/logo.png", 0.3)
        self.background_image.center_x = 165
        self.background_image.center_y = 300
        self.ball = arcade.Sprite(":resources:images/gray.png", BALL_SCALE)
        self.ball.center_x = 165
        self.ball.center_y = 300

        self.hoops = arcade.SpriteList()

        self.x_speed = 80
        self.y_speed = 80
        self.score1 = 0
        self.score2 = 0

        self.player_1_scoring = False
        self.player_2_scoring = False

    def setup(self):

        self.player1 = arcade.Sprite(":resources:images/bluepad.png", 1)
        self.player2 = arcade.Sprite(":resources:images/redpad.png", 1)
        self.player1.center_x= 165
        self.player1.center_y= 75
        self.player2.center_x= 165
        self.player2.center_y= 525
        self.player_list.append(self.player1)
        self.player_list.append(self.player2)
        self.physics_engine = arcade.PhysicsEngineSimple(self.ball, self.player_list)

        self.hoop1 = arcade.Sprite(":resources:images/rectangle.jpg", 1)
        self.hoop1.center_x = 165
        self.hoop1.center_y = 600

        self.hoop2 = arcade.Sprite(":resources:images/rectangle.jpg", 1)
        self.hoop2.center_x = 165
        self.hoop2.center_y = 0

        self.hoops.append(self.hoop1)
        self.hoops.append(self.hoop2)

    def on_draw(self):

        arcade.start_render()

        self.border = arcade.draw_rectangle_outline(165, 300, 310, 580, arcade.color.GRAY, border_width=3)
        self.center_line = arcade.draw_line(10, 300, 320, 300, arcade.color.GRAY)
        self.background_image.draw()
        self.shooting_circle1 = arcade.draw_circle_outline(165,10,55,arcade.color.BLUE,border_width=3)
        self.shooting_circle2 = arcade.draw_circle_outline(165,590,55,arcade.color.RED,border_width=3)
        self.shooting_circles_list.append(self.shooting_circle1)
        self.shooting_circles_list.append(self.shooting_circle2)
        self.hoops.draw()
        self.ball.draw()
        self.player_list.draw()

        player1_scored = arcade.check_for_collision(self.hoop1, self.ball)
        if not self.player_1_scoring:
            if player1_scored:
                self.player_1_scoring = True
                self.score1 += 1
                arcade.draw_text("Player 1 Won!", 100, 400, arcade.color.BLUE, 20, font_name='comicsansms')

        player2_scored = arcade.check_for_collision(self.hoop2, self.ball)
        if not self.player_2_scoring:
            if player2_scored:
                self.player_2_scoring = True
                self.score1 += 1
                arcade.draw_text("Player 2 Won!", 100, 200, arcade.color.RED, 20, font_name='comicsansms')

    def on_key_press(self, key, mod):

        if key == arcade.key.RIGHT:
            self.player_list[0].change_x = 8
        if key == arcade.key.LEFT:
            self.player_list[0].change_x = -8
        if key == arcade.key.UP:
            self.player_list[0].change_y = 8
        if key == arcade.key.DOWN:
            self.player_list[0].change_y = -8

        if key == arcade.key.D:
            self.player_list[1].change_x = 8
        if key == arcade.key.A:
            self.player_list[1].change_x = -8
        if key == arcade.key.W:
            self.player_list[1].change_y = 8
        if key == arcade.key.S:
            self.player_list[1].change_y = -8

    def on_key_release(self, key, mod):
        if (key == arcade.key.LEFT) or (key == arcade.key.RIGHT):
            self.player_list[0].change_x = 0
        elif (key == arcade.key.DOWN) or (key == arcade.key.UP):
            self.player_list[0] .change_y = 0
        if (key == arcade.key.A) or (key == arcade.key.D):
            self.player_list[1].change_x = 0
        elif (key == arcade.key.W) or (key == arcade.key.S):
            self.player_list[1].change_y = 0

    def on_update(self, delta_time: float):

        if self.player_list[0].center_x > 320 or self.player_list[0].center_x < 10:
            self.player_list[0].center_x -= 10
        if self.player_list[0].center_y > 295 or self.player_list[0].center_y < 10:
            self.player_list[0].center_y -= 10
        if self.player_list[1].center_x > 320 or self.player_list[1].center_x < 10:
            self.player_list[1].center_x -= 10
        if self.player_list[1].center_y > 590 or self.player_list[1].center_y < 295:
            self.player_list[1].center_y -= 10
        self.player_list[0].update()
        self.player_list[1].update()
        # Keeps the ball moving
        self.ball.center_x += self.x_speed * delta_time
        self.ball.center_y += self.y_speed * delta_time
        if self.ball.center_x > 310 or self.ball.center_x < 20:
            self.x_speed *= -1
        if self.ball.center_y > 580 or self.ball.center_y < 20:
            self.y_speed *= -1

        first_player_collision = arcade.check_for_collision(self.player_list[0], self.ball)
        if first_player_collision:
            self.x_speed *= -1
            self.y_speed *= -1

        second_player_collision = arcade.check_for_collision(self.player_list[1], self.ball)
        if second_player_collision:
            self.x_speed *= -1
            self.y_speed *= -1


def main():
    window = arcade.Window(330,600, "Air Hockey", resizable=True)
    first_view = MenuView()
    window.show_view(first_view)
    arcade.run()
if __name__ == '__main__':
    main()
