from manim import *

class FinalIdealGasLawSimplified(Scene):
    def construct(self):
        
        equation = MathTex("P", "V", "=", "n", "R", "T")
        
        
        equation[0].set_color(BLUE)    # P (blue)
        equation[1].set_color(RED)     # V (red)
        equation[3].set_color(GREEN)   # n (green)
        equation[4].set_color(GOLD)    # R (gold)
        equation[5].set_color(PURPLE)  # T (purple)
        
        equation.scale(2)
        self.play(Write(equation), run_time=2)
        
        
        n_label = Tex("moles").next_to(equation[3], DOWN, buff=0.7).set_color(GREEN)
        t_label = Tex("Kelvin").next_to(equation[5], DOWN, buff=0.7).set_color(PURPLE)
        n_arrow = Arrow(n_label.get_top(), equation[3].get_bottom(), color=GREEN, buff=0.2)
        t_arrow = Arrow(t_label.get_top(), equation[5].get_bottom(), color=PURPLE, buff=0.2)
        
        self.play(
            Write(n_label),
            GrowArrow(n_arrow),
            Write(t_label),
            GrowArrow(t_arrow),
            run_time=2
        )
        self.wait(3)  
        
       
        r_value = MathTex("R", "=", "0.0821", r"\frac{L \cdot atm}{mol \cdot K}")
        r_value.scale(1.5)
        r_value.next_to(equation, DOWN, buff=1.5)
        
        # Color coding
        r_value[0].set_color(GOLD)    # R (gold)
        r_value[3][0].set_color(RED)   # L (red)
        r_value[3][2:4].set_color(BLUE)  # atm (blue)
        r_value[3][5:7].set_color(GREEN) # mol (green)
        r_value[3][8:].set_color(PURPLE) # K (purple)
        
        self.play(Write(r_value), run_time=3)
        self.wait(5)  
        
        
        connections = VGroup(
            Line(r_value[3][0].get_top(), equation[1].get_bottom(), color=RED),    # L → V
            Line(r_value[3][2].get_top(), equation[0].get_bottom(), color=BLUE),    # atm → P
        )
        
        self.play(
            Create(connections[0]),  # L → V
            Create(connections[1]),  # atm → P
            run_time=2
        )
        self.wait(12) 
