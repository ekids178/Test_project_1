from manim import *

class demo1(Scene):
	def construct(self):	#construct a showcase
		circle = Circle()	#build a circle
		self.play(Create(circle))	#create a video of a circle
		square = Square()
		self.play(Transform(circle, square), run_time = 1)	#transform circle into square
		self.wait()
		self.play(ApplyMethod(circle.shift, UL))	#ApplyMethod(smooth transition)
		self.play(ApplyMethod(circle.rotate, 0.5))
		self.play(ApplyMethod(circle.scale, 2))
		self.wait()

class Counting(Scene):
	def construct(self):
		numb = Text("0")
		for i in range(10):
			self.play(Transform(numb, Text(str(i))))


class demo9(Scene):
    def construct(self):
        ax = (
            Axes(x_range=[-4, 4, 1], x_length=10, y_range=[0, 16, 2], y_length=6)
        .to_edge(DOWN)
        .add_coordinates()
        ).set_color(WHITE)

        k = ValueTracker(-3)
        func = ax.get_graph(lambda x : x**2 , x_range=[-4, 4], color = RED)
        pt = always_redraw(
            lambda: Dot().move_to(
                ax.c2p(k.get_value(), func.underlying_function(k.get_value()))
                )
            )
        slope = always_redraw(
            lambda: ax.get_secant_slope_group(
            x = k.get_value(), 
            graph = func, 
            dx = 0.1,
            secant_line_color = BLUE,
            secant_line_length = 3
            )
        )

        self.add(ax, func, pt, slope)
        self.play(k.animate.set_value(3), run_time = 3)
        self.wait()
