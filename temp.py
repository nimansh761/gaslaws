from manim import *

class CelsiusToKelvin(Scene):
    def construct(self):
        # Create the conversion equation with colored text
        equation = MathTex(
            r"\text{Degrees Celsius}", "+", "273", "=", r"\text{Kelvin Temperature}"
        ).scale(1.3)
        
        # Color coding
        equation[0].set_color(BLUE)    # "Degrees Celsius" in blue
        equation[2].set_color(YELLOW)  # "273" in yellow
        equation[4].set_color(RED)     # "Kelvin Temperature" in red
        
        # Center the equation
        equation.move_to(ORIGIN)
        
        # Simple animation - write all at once
        self.play(Write(equation), run_time=2)
        self.wait(5)  # Display for 5 seconds