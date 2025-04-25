from manim import *

class BoylesLawFormula(Scene):
    def construct(self):
        
        left_p1 = MathTex("(")
        p1 = MathTex("P_1")
        right_p1 = MathTex(")")
        left_v1 = MathTex("(")
        v1 = MathTex("V_1")
        right_v1 = MathTex(")")
        
        equals = MathTex("=")
        
        left_p2 = MathTex("(")
        p2 = MathTex("P_2")
        right_p2 = MathTex(")")
        left_v2 = MathTex("(")
        v2 = MathTex("V_2")
        right_v2 = MathTex(")")
        
       
        left_side = VGroup(left_p1, p1, right_p1, left_v1, v1, right_v1).arrange(RIGHT, buff=0.1)
        right_side = VGroup(left_p2, p2, right_p2, left_v2, v2, right_v2).arrange(RIGHT, buff=0.1)
        equation = VGroup(left_side, equals, right_side).arrange(RIGHT, buff=0.3)
        
      
        equation.set_width(config.frame_width * 0.9)
        
       
        self.play(
            Write(left_p1), Write(p1), Write(right_p1),
            Write(left_v1), Write(v1), Write(right_v1),
            run_time=1.2
        )
        self.play(Write(equals), run_time=0.4)
        self.play(
            Write(left_p2), Write(p2), Write(right_p2),
            Write(left_v2), Write(v2), Write(right_v2),
            run_time=1.2
        )
        
        
        self.wait(4.8)
