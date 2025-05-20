from manim import *

class IdealGasLawSimpleText(Scene):
    def construct(self):
        # Part 1: PV = nRT with Text objects
        p = Text("P", color=BLUE, font_size=72)
        v = Text("V", color=RED, font_size=72)
        eq = Text("=", font_size=72)
        n = Text("n", color=GREEN, font_size=72)
        r = Text("R", color=GOLD, font_size=72)
        t = Text("T", color=PURPLE, font_size=72)
        
        # Arrange the equation
        equation = VGroup(p, v, eq, n, r, t).arrange(RIGHT, buff=0.3)
        equation.center()
        
        self.play(Write(equation), run_time=2)
        
        # Add labels
        n_label = Text("Moles", color=GREEN, font_size=36).next_to(n, DOWN, buff=0.5)
        t_label = Text("Kelvin", color=PURPLE, font_size=36).next_to(t, DOWN, buff=0.5)
        
        n_arrow = Arrow(n_label.get_top(), n.get_bottom(), color=GREEN)
        t_arrow = Arrow(t_label.get_top(), t.get_bottom(), color=PURPLE)
        
        self.play(
            Write(n_label),
            GrowArrow(n_arrow),
            Write(t_label),
            GrowArrow(t_arrow),
            run_time=2
        )
        self.wait(3)
        
        # Part 2: R value with Text
        r_text = Text("R = 0.0821 ", color=GOLD, font_size=48)
        fraction_line = Line(LEFT, RIGHT, color=WHITE).scale(0.5)
        
        # Numerator (L·atm)
        l = Text("L", color=RED, font_size=36)
        dot1 = Text("·", font_size=36)
        atm = Text("atm", color=BLUE, font_size=36)
        numerator = VGroup(l, dot1, atm).arrange(RIGHT, buff=0.1)
        
        # Denominator (mol·K)
        mol = Text("mol", color=GREEN, font_size=36)
        dot2 = Text("·", font_size=36)
        k = Text("K", color=PURPLE, font_size=36)
        denominator = VGroup(mol, dot2, k).arrange(RIGHT, buff=0.1)
        
        # Build the fraction
        fraction = VGroup(
            numerator,
            Line(numerator.get_left()+DOWN*0.2, numerator.get_right()+DOWN*0.2),
            denominator
        ).arrange(DOWN, buff=0.2)
        
        r_value = VGroup(r_text, fraction).arrange(RIGHT, buff=0.2)
        r_value.next_to(equation, DOWN, buff=1)
        
        self.play(
            Write(r_text),
            FadeIn(fraction),
            run_time=3
        )
        self.wait(5)
        
        # Part 3: Connections
        l_conn = Line(l.get_top(), v.get_bottom(), color=RED)
        atm_conn = Line(atm.get_top(), p.get_bottom(), color=BLUE)
        
        self.play(
            Create(l_conn),
            Create(atm_conn),
            run_time=2
        )
        self.wait(12)
