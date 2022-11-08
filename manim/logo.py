from manim import *

class ManimCELogo(Scene):
    def construct(self):
        #self.camera.background_color = "#ece6e2" #pyright: ignore
        self.camera.background_color = BLACK #pyright: ignore
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{SEPTIC}", fill_color=WHITE).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=PINK, fill_opacity=1).shift(2*LEFT)
        square = Square(color=GREEN, fill_opacity=1).shift(3*UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)
