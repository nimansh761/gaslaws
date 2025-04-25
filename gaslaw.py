from manim import *

class GasLawDerivation(Scene):
    def construct(self):
        
        original = MathTex("P", "V", "=", "n", "R", "T")
        original.scale(1.5)
        colors = [BLUE, RED, WHITE, GREEN, GOLD, PURPLE]
        for i, color in enumerate(colors):
            original[i].set_color(color)
        
        self.play(Write(original))
        self.wait(2)

        
        sub1 = MathTex("n", "=", r"\frac{m}{M}").next_to(original, DOWN)
        sub1[0].set_color(GREEN)
        self.play(Write(sub1))
        self.wait(1)

        
        eq1 = MathTex("P", "V", "=", r"\frac{m}{M}", "R", "T")
        eq1.scale(1.5)
        for i, color in [(0, BLUE), (1, RED), (4, GOLD), (5, PURPLE)]:
            eq1[i].set_color(color)
        
        self.play(
            Transform(original, eq1),
            FadeOut(sub1),
            run_time=2
        )
        self.wait(1)

        
        eq2 = MathTex("P", "=", r"\frac{m}{M \cdot V}", "R", "T")
        eq2.scale(1.5)
        for i, color in [(0, BLUE), (3, GOLD), (4, PURPLE)]:
            eq2[i].set_color(color)
        
        self.play(Transform(original, eq2), run_time=2)
        self.wait(1)

        
        sub2 = MathTex(r"\rho", "=", r"\frac{m}{V}").next_to(original, DOWN)
        sub2[0].set_color(ORANGE)
        self.play(Write(sub2))
        

        
        final = MathTex("P", "=", r"\frac{\rho}{M}", "R", "T")
        final.scale(1.5)
        for i, color in [(0, BLUE), (2, ORANGE), (3, GOLD), (4, PURPLE)]:
            final[i].set_color(color)
        
        self.play(
            Transform(original, final),
            FadeOut(sub2),
            run_time=2
        )
        self.wait(3)
