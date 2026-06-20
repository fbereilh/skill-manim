from manim import *


class DogEating(Scene):
    def construct(self):
        self.camera.background_color = "#aee2ff"

        # ground
        ground = Rectangle(width=16, height=4, fill_color="#8fcf6b",
                           fill_opacity=1, stroke_width=0)
        ground.to_edge(DOWN, buff=0)
        self.add(ground)

        # --- bowl on the right ---
        bowl = Arc(radius=1.0, start_angle=PI, angle=PI, color="#3b6ea5")
        bowl.set_stroke(width=10)
        bowl_base = Line(bowl.get_start(), bowl.get_end(), color="#3b6ea5",
                         stroke_width=10)
        bowl_grp = VGroup(bowl, bowl_base).move_to(RIGHT * 3.2 + DOWN * 1.2)

        # kibble inside the bowl
        kibble = VGroup(*[
            Dot(radius=0.13, color="#6b4423")
            for _ in range(4)
        ]).arrange(RIGHT, buff=0.18)
        kibble.move_to(bowl_grp.get_center() + UP * 0.15)

        self.play(FadeIn(bowl_grp), FadeIn(kibble), run_time=0.6)

        # --- dog built from shapes ---
        body = Ellipse(width=1.6, height=0.95, color="#c8862f",
                       fill_opacity=1, stroke_width=0)
        head = Circle(radius=0.5, color="#c8862f", fill_opacity=1,
                      stroke_width=0).next_to(body, RIGHT, buff=-0.15).shift(UP * 0.25)
        ear = Ellipse(width=0.25, height=0.5, color="#9c6420",
                      fill_opacity=1, stroke_width=0).move_to(head.get_top() + LEFT * 0.05)
        eye = Dot(radius=0.06, color=BLACK).move_to(head.get_center() + RIGHT * 0.2 + UP * 0.1)
        snout = Dot(radius=0.09, color="#5a3a18").move_to(head.get_right() + LEFT * 0.05)
        tail = Line(body.get_left(), body.get_left() + LEFT * 0.45 + UP * 0.35,
                    color="#c8862f", stroke_width=10)
        legs = VGroup(*[
            Line(ORIGIN, DOWN * 0.5, color="#9c6420", stroke_width=10)
            for _ in range(2)
        ])
        legs[0].move_to(body.get_bottom() + LEFT * 0.4 + DOWN * 0.2)
        legs[1].move_to(body.get_bottom() + RIGHT * 0.4 + DOWN * 0.2)

        dog = VGroup(tail, legs, body, ear, head, eye, snout)
        dog.move_to(LEFT * 6 + DOWN * 0.9)

        # walk in from the left
        self.play(dog.animate.move_to(LEFT * 0.6 + DOWN * 0.9),
                  rate_func=linear, run_time=1.6)

        # eat: dog dips toward bowl, kibble disappears one by one, hearts pop
        for k in kibble:
            self.play(dog.animate.shift(DOWN * 0.2 + RIGHT * 0.1),
                      rate_func=there_and_back, run_time=0.35)
            self.play(FadeOut(k, shift=UP * 0.3), run_time=0.25)

        # happy hearts float up
        hearts = VGroup(*[
            Text("♥", color="#e23b3b", font_size=54)
            for _ in range(3)
        ])
        for i, h in enumerate(hearts):
            h.move_to(dog.get_top() + UP * 0.3 + RIGHT * (i - 1) * 0.7)

        self.play(
            LaggedStart(*[
                h.animate.shift(UP * 1.6).set_opacity(0)
                for h in hearts
            ], lag_ratio=0.3),
            dog.animate.shift(UP * 0.25),
            run_time=1.6,
        )
        self.wait(0.4)
