from manim import *

class CombinedGasLawDerivation(Scene):
    def construct(self):
        # Set up layout parameters
        title = Tex("Combined Gas Law Derivation", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Initialize all equation parts
        boyles = MathTex(r"P_1V_1 = P_2V_2").shift(UP)
        charles = MathTex(r"\frac{V_1}{T_1} = \frac{V_2}{T_2}")
        gaylussac = MathTex(r"\frac{P_1}{T_1} = \frac{P_2}{T_2}").shift(DOWN)
        
        # Animate each law appearing
        self.play(Write(boyles), run_time=1.5)
        self.wait(0.5)
        self.play(Write(charles), run_time=1.5)
        self.wait(0.5)
        self.play(Write(gaylussac), run_time=1.5)
        self.wait(1)
        
        # Transform into combined forms
        boyles_combined = MathTex(r"\frac{P_1V_1}{T_1} = \frac{P_2V_2}{T_2}")
        self.play(
            Transform(boyles, boyles_combined),
            Transform(charles, boyles_combined.copy()),
            Transform(gaylussac, boyles_combined.copy()),
            run_time=2
        )
        self.wait(2)
        
        # Final combined law
        combined_law = MathTex(r"\frac{PV}{T} = \text{constant}", font_size=42)
        self.play(
            FadeOut(boyles),
            FadeOut(charles),
            FadeOut(gaylussac),
            Write(combined_law),
            run_time=1.5
        )
        self.wait(3)
        
        # Clean up
        self.play(
            FadeOut(combined_law),
            FadeOut(title)
        )

    def scale(self):
        return super().scale()
    
from manim import *

class CombinedGasLawImage(Scene):
    def construct(self):
        # Combined gas law with professional formatting
        law = MathTex(
            r"\frac{P_1 V_1}{T_1} = \frac{P_2 V_2}{T_2}",
            font_size=96,
            color=BLUE
        )
        
        
        
        # Render both forms
        self.add(law)
        self.wait(5)  # Display for 5 seconds