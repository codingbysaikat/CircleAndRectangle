from manim import *

class CircleAndRectangle(Scene):
    def construct(self):
        self.camera.frame_width = 9
        self.camera.frame_height = 16

        text1 = Text("Learning mathematics")
        text2 = Text("is a style of life")

        text1.to_edge(UP)
        text1.shift(UP*2)
        text2.next_to(text1,DOWN)

        circle = Circle(radius=1.5)
        center = circle.get_center()

        # Center of circle
        center = circle.get_center()
        line1 = Line(
            center + LEFT * 1.5,
            center + RIGHT * 1.5,
            color=YELLOW
        )
        # Text animation
        self.play(Write(text1))
        self.play(Write(text2))

        self.play(Create(circle))
        self.play(Create(line1))

         # 2. Duplicate line
        line2 = Line(
            center + DOWN * 1.5,
            center + UP * 1.5,
            color=YELLOW
        )
        self.play(Create(line2))

        self.play(line1.animate.move_to(DOWN * 1.5),line2.animate.move_to(RIGHT * 1.5))
        line3 = line1.copy()
        line4 = line2.copy()
        self.play(line3.animate.move_to(UP *1.5),line4.animate.move_to(LEFT *1.5))
        self.wait()


        group = VGroup(line1,line2,line3, line4)
        group.move_to(ORIGIN)
        self.play(group.animate.rotate(PI, about_point=group.get_center()),run_time=2) 
        self.play(Rotate(group, angle=PI), run_time=2)

        self.play(circle.animate.shift(UP*2),group.animate.shift(DOWN*2))
        self.wait()
















