from manim import *

class PressureLine(Scene):
    def construct(self):
        # Single line with all conversions
        conv = MathTex(
            "101.3", "\\text{kPa}", "=", "1", "\\text{atm}", 
            "=", "760", "\\text{mmHg}", "=", "760", "\\text{torr}"
        ).scale(1.5)
        
        # Color coding
        colors = {
            "kPa": BLUE,
            "atm": RED,
            "mmHg": GREEN,
            "torr": PURPLE
        }
        
        # Apply colors
        for i, part in enumerate(conv):
            tex = part.get_tex_string()
            if "kPa" in tex:
                part.set_color(colors["kPa"])
            elif "atm" in tex:
                part.set_color(colors["atm"])
            elif "mmHg" in tex:
                part.set_color(colors["mmHg"])
            elif "torr" in tex:
                part.set_color(colors["torr"])
        
        # Simple animation
        self.play(Write(conv), run_time=3)
        self.wait(10)
