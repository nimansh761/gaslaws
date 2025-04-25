from manim import *

class GayLussacsLaw(Scene):
    def construct(self):
        # Create the equation with proper fractions
        left_frac = MathTex(r"\frac{P_1}{T_1}")
        equals = MathTex("=")
        right_frac = MathTex(r"\frac{P_2}{T_2}")
        
        # Combine and arrange
        equation = VGroup(left_frac, equals, right_frac).arrange(RIGHT, buff=0.5)
        
        # Scale to 90% width (big and clear)
        equation.set_width(config.frame_width * 0.9)
        
        # Animation sequence (total 8 seconds)
        self.play(Write(left_frac), run_time=1.0)
        self.play(Write(equals), run_time=0.5)
        self.play(Write(right_frac), run_time=1.0)
        
        # Hold for 5.5s (total 8s)
        self.wait(5.5)
        
        # Fade out
        self.play(FadeOut(equation), run_time=1.0)