import pico2d
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    def __init__(self):
        self.x, self.y = 400, 500
        self.frame = 0
        self.dir = 1
        self.image = pico2d.load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 15
        PIXEL_PER_METER = (10.0 / 0.3)
        RUN_SPEED_KMPH = 35.0
        RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        if self.x >= 780 or self.x <= 20:
            self.dir *= -1

    def draw(self):
        if self.dir == 1:
            if int(self.frame) < 5:
                self.image.clip_draw(
                    int(self.frame) * 183, 338, 183, 169,
                    self.x, self.y
                )
            elif int(self.frame) >= 5 and int(self.frame) < 10:
                self.image.clip_draw(
                    (int(self.frame) - 5) * 183, 169, 183, 169,
                    self.x, self.y
                )
            else:
                self.image.clip_draw(
                    (int (self.frame) - 10) * 183, 0, 183, 169,
                    self.x, self.y
                )
        elif self.dir == -1:
            if int(self.frame) < 5:
                self.image.clip_composite_draw(
                    int(self.frame) * 183, 0, 183, 169,
                    0, 'h', self.x, self.y
                )
            elif int(self.frame) >= 5 and int(self.frame) < 10:
                self.image.clip_composite_draw(
                    int(self.frame) * 183, 169, 183, 169,
                    0, 'h', self.x, self.y
                )
            else:
                self.image.clip_composite_draw(
                    int(self.frame) * 183, 338, 183, 169,
                    0, 'h', self.x, self.y
                )