import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "MITUNA'S DABBLE"

CHARACTER_SCALING = 0.3
PIANO_SCALING = 0.7
COIN_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 10
PLAYER_JUMP_SPEED = 20
GRAVITY = 1

class MyAnimation(arcade.Window):
    """ Main Application Class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_list = None
        self.item_list = None
        self.physics_engine = None

        self.already_playing = False
        self.time = 0
        # Load Sounds
        self.jump_sound = arcade.load_sound(":resources:sounds/move.wav")
        self.dabble_sound = arcade.load_sound(":resources:sounds/gallop.mp3")
        arcade.set_background_color(arcade.csscolor.TEAL)
    def setup(self):
        """Set up the game here. Call this function to restart the game. """
        self.player_list = arcade.SpriteList()
        self.item_list = arcade.SpriteList()

        self.mituna_sprite = arcade.Sprite(":resources:images/animated_characters/mituna/Mituna_sprite.png", CHARACTER_SCALING)
        self.mituna_sprite.center_x = 64
        self.mituna_sprite.center_y = 128

        self.piano_sprite = arcade.Sprite(":resources:images/animated_characters/mituna/piano.png", PIANO_SCALING)
        self.piano_sprite.center_x = 900
        self.piano_sprite.center_y = 128

        self.player_list.append(self.mituna_sprite)
        self.item_list.append(self.piano_sprite)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.mituna_sprite, GRAVITY)

    def on_draw(self):
        """Render the screen. """
        arcade.start_render()
        self.player_list.draw()
        self.item_list.draw()
        # Code to draw the screen goes here

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.W or key == arcade.key.UP:
            self.mituna_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.mituna_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.mituna_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.mituna_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if (key == arcade.key.W) or (key == arcade.key.S):
            self.mituna_sprite.change_y = 0
        elif (key == arcade.key.A) or (key == arcade.key.D):
            self.mituna_sprite.change_x = 0

    def on_update(self, time):
        self.mituna_sprite.update()
        self.time += time
        self.piano_playing = arcade.check_for_collision(self.mituna_sprite, self.piano_sprite)

        if not self.already_playing:
            if self.piano_playing:
                arcade.play_sound(self.dabble_sound)
                self.already_playing = True

def main():
    """ Main method """
    window = MyAnimation()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
