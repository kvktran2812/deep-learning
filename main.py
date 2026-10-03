from manim import *
import numpy as np


class IntroDemo(Scene):
    def construct(self):
        # --- 1. Text appears, then shrinks to the top ---
        title = Text("Hello, Manim!", font_size=56)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate.scale(0.6).to_edge(UP))

        # --- 2. Morph a square into a circle ---
        square = Square(color=BLUE, fill_opacity=0.6)
        self.play(Create(square))
        self.play(Transform(square, Circle(color=RED, fill_opacity=0.6)))
        self.play(square.animate.shift(RIGHT * 2).rotate(PI / 2))
        self.play(FadeOut(square))

        # --- 3. Plot a sine wave with a dot that traces it ---
        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 1],
            x_length=9,
            y_length=4,
            tips=False,
        )
        graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
        label = Text("y = sin(x)", font_size=30, color=YELLOW).next_to(axes, DOWN)

        self.play(Create(axes))
        self.play(Create(graph), FadeIn(label))

        # A ValueTracker drives the dot's position via an updater
        t = ValueTracker(0)
        dot = always_redraw(
            lambda: Dot(
                axes.c2p(t.get_value(), np.sin(t.get_value())),
                color=RED,
            )
        )
        self.add(dot)
        self.play(t.animate.set_value(2 * PI), run_time=4, rate_func=linear)
        self.wait(1)