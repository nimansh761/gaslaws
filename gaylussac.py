from manim import *

class GayLussacsLaw(Scene):
    def construct(self):
        
        left_frac = MathTex(r"\frac{P_1}{T_1}")
        equals = MathTex("=")
        right_frac = MathTex(r"\frac{P_2}{T_2}")
        
        
        equation = VGroup(left_frac, equals, right_frac).arrange(RIGHT, buff=0.5)
        
        
        equation.set_width(config.frame_width * 0.9)
        
       
        self.play(Write(left_frac), run_time=1.0)
        self.play(Write(equals), run_time=0.5)
        self.play(Write(right_frac), run_time=1.0)
        
       
        self.wait(5.5)
        
       
        self.play(FadeOut(equation), run_time=1.0)
