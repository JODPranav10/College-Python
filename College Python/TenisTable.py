from manim import *
import numpy as np
import random
class Pong(Scene):
    def construct(self):
        rect1 = Rectangle(height=2, width=0.2, color=BLUE)
        rect2 = Rectangle(height=2, width=0.2, color=BLUE)
        rect1.move_to(LEFT * 9)
        rect2.move_to(RIGHT * 9)
        self.add(rect1, rect2)
        def leftupdate(mob, dt):
            mob.move_to(
                LEFT * 5 + UP * np.sin(self.time * 2) * 2.2
            )
        def rightupdate(mob, dt):
            mob.move_to(
                RIGHT * 5 + UP * np.sin(self.time * 2 + PI) * 2.2
            )
        rect1.add_updater(leftupdate)
        rect2.add_updater(rightupdate)
        ball = Circle(radius=0.2, color=RED)
        ball.move_to(ORIGIN)
        self.add(ball)
        velocity = RIGHT * 3 + UP * 2
        reset_cooldown = 0
        def reset_ball():
            nonlocal velocity, reset_cooldown
            ball.move_to(ORIGIN)
            angle = random.uniform(-PI/3, PI/3)
            direction = random.choice([LEFT, RIGHT])
            speed = 4
            velocity = (
                direction * np.cos(angle) * speed
                + UP * np.sin(angle) * speed
            )
            reset_cooldown = 0.2   
        def ballupdate(mob, dt):
            nonlocal velocity, reset_cooldown
            if reset_cooldown > 0:
                reset_cooldown -= dt
                return
            mob.shift(velocity * dt)
            if mob.get_top()[1] >= 3.5:
                velocity[1] *= -1
            if mob.get_bottom()[1] <= -3.5:
                velocity[1] *= -1
            if (
                mob.get_right()[0] >= rect2.get_left()[0]
                and rect2.get_bottom()[1] <= mob.get_y() <= rect2.get_top()[1]
            ):
                velocity[0] *= -1
                mob.set_x(rect2.get_left()[0] - mob.radius)

            if (
                mob.get_left()[0] <= rect1.get_right()[0]
                and rect1.get_bottom()[1] <= mob.get_y() <= rect1.get_top()[1]
            ):
                velocity[0] *= -1
                mob.set_x(rect1.get_right()[0] + mob.radius)
            if mob.get_right()[0] > 10 or mob.get_left()[0] < -10:
                reset_ball()
        ball.add_updater(ballupdate)
        self.wait(20)