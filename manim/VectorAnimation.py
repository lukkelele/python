from manim import *

class VectorAnimation(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY # pyright: ignore
        end_loc = [3,2,0]
        v_org = Arrow(ORIGIN, ORIGIN, buff=6, max_stroke_width_to_length_ratio=10)
        v_end = Arrow(ORIGIN, end_loc, buff=6, max_stroke_width_to_length_ratio=10)
        #v_org.set_stroke(width=2, color=BLACK)
        dot = Dot(ORIGIN, radius=DEFAULT_DOT_RADIUS, color=WHITE)
        dot_end = Dot(end_loc, radius=DEFAULT_DOT_RADIUS, color=WHITE)
        numberplane = NumberPlane()
        numberplane.set_color_by_gradient(WHITE)
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        #origin_text.set_stroke(width=4, color=BLACK)
        tip_text = Text('(3, 2)').next_to(v_end.get_end(), RIGHT)
        origin_text.font_size = DEFAULT_FONT_SIZE + 2
        tip_text.font_size = DEFAULT_FONT_SIZE + 2
        A = Text('AMADEUS $').move_to([-3,3,0])
        A.color = PINK
        A.set_stroke(width=2, color=WHITE)
        Anew = A.move_to([3,-3,0])
        Anew = A.copy().move_to([3,-3,0])


        self.play(FadeIn(numberplane))
        self.play(FadeIn(dot))
        self.wait(0.2)
        self.play(FadeIn(dot_end))

        self.play(FadeIn(origin_text))
        self.play(FadeIn(tip_text))
        self.wait(1)
        self.play(FadeOut(dot_end))
        self.play(Transform(v_org, v_end))
        #self.play(FadeIn(A))
        self.wait(2)
        #Anew = A.move_to([3,-3,0])
        self.play(Transform(A, Anew))
        self.wait(0.5)
        

        self.add(numberplane, dot, v_end, origin_text, tip_text)
        self.wait(3)


