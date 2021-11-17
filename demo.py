from manim import *


class demo2(Scene):
    def construct(self):
        text1 = Text("This is Write(str)")
        text2 = Text("This is Create(str)")
        logo_blue = "#525893"
        cir1 = Circle(color=logo_blue)
        cir2 = Circle(color=logo_blue)

        self.play(
            Write(text1), Write(cir1),
            run_time = 2
            )
        self.play(
            text1.animate.shift(UP*3), cir1.animate.shift(UP*3)
            )
        self.play(
            Create(text2), Create(cir2),
            run_time = 2
            )
        

class demo3(Scene):
    def construct(self):
        logo_blue = "#525893"
        cir = Circle(color=logo_blue)
        sq = Square()
        self.play(
            cir.animate.shift(UP*3).scale(0.5), 
            sq.animate.rotate(1.57), 
            run_time = 3
            )


class demo4(Scene):
    def construct(self):
        eq1 = MathTex(
            r"\sum_{n=0}^{\infty}\sin(n)\\", 
            r"\vec{v} = \begin{bmatrix} 1 \\2 \\3 \end{bmatrix}\\",
            r"A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\\",
            r"e^{i\pi}+1=0"
            )
        eq1[3].set_color(RED)
        self.play(Write(eq1))


class demo5(Scene):
    def construct(self):
        circ = Circle(color = BLUE)
        rect = Rectangle(height = 1.5, width = 1).to_edge(UL)
        arrow = always_redraw(
            lambda: Line(start = rect.get_right(), end = circ.get_left()).add_tip()
            )
        
        set1 = VGroup(circ, rect, arrow)

        self.play(Write(set1))
        self.wait()
        self.play(
            rect.animate.to_edge(DL),
            circ.animate.scale(0.5)
        )
        self.play(
            rect.animate.to_edge(UL),
            circ.animate.scale(2)
        )


class demo6(Scene):
    def construct(self):
        num1 = MathTex('-1')
        box = always_redraw(
            lambda: SurroundingRectangle(
            num1, fill_opacity = 0.8, fill_color = RED, buff = 0.5
        ))
        name = always_redraw(lambda:Tex('Area').next_to(num1, DOWN, buff = 0.85))
        self.play(Write(VGroup(num1, box, name)), run_time = 2)
        self.play(num1.animate.shift(UR), run_time = 2)
        self.wait()


class demo7(Scene):
    def construct(self):
        k = ValueTracker(5)
        
        num1 = always_redraw(
            lambda:DecimalNumber().set_value(k.get_value())
        )
    
        self.play(FadeIn(num1))
        self.wait()
        self.play(k.animate.set_value(0), run_time = 5, rate_func = linear)


class demo8(Scene):
    def construct(self):
        plane = (
            NumberPlane(x_range=[-4, 4, 2], x_length=7, y_range=[0, 16, 4], y_length=5)
            .to_edge(DOWN)
            .add_coordinates()
        )

        lables = plane.get_axis_labels(x_label='x', y_label='f(x)')
        parab = plane.get_graph(lambda x : x**2 , x_range=[-4, 4], color = RED)
        func_label = (
            MathTex('f(x)=x^2').scale(0.85)
            .next_to(parab, UR, buff=0.2)
            .set_color(RED)
        )
        area_under_curve = plane.get_riemann_rectangles(
            graph=parab,
            x_range=[0,3], dx = 0.1, stroke_width=0.1, stroke_color=GREEN
            )

        self.play(DrawBorderThenFill(plane))
        self.play(Write(VGroup(parab, lables, func_label)), run_time = 3)
        self.wait()
        self.play(Write(area_under_curve), run_time = 2)
        self.wait()


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
            dx = 0.01,
            secant_line_color = BLUE,
            secant_line_length = 3
            )
        )

        self.add(ax, func, pt, slope)
        self.play(k.animate.set_value(3), run_time = 3, rate_func = smooth)
        self.wait()



svg_dir = "C:\VScode\Python\Manim\practice_demos\svg_images"
img_dir = "C:\VScode\Python\Manim\practice_demos\images"

class demo10(Scene):
    def construct(self):
        yt_icon = SVGMobject(f"{svg_dir}\\icons8-youtube.svg")
        _3b1b_icon = SVGMobject(f"{svg_dir}\\3B1B_Logo.svg")
        yt_img = ImageMobject(f"{img_dir}\\icons8-youtube-144.png")

        self.play(DrawBorderThenFill(yt_icon))
        self.play(yt_icon.animate.scale(0.4).to_edge(UL), run_time = 2)
        self.play(DrawBorderThenFill(_3b1b_icon))
        self.play(_3b1b_icon.animate.scale(0.4).to_edge(UP), run_time = 2)
        self.play(FadeIn(yt_img))
        self.wait()

class graph(Scene):
    def construct(self):
        ax = (
            Axes(x_range=[-4, 4, 1], x_length=10, y_range=[-8, 8, ], y_length=6)
        .add_coordinates()
        )
        ax_lables = ax.get_axis_labels(x_label='x', y_label='f(x)')
        
        func = ax.plot(
            lambda x : np.sin(x)*np.sin(x) ,
             x_range=[-4, 4], 
             color = RED
             )
        # lable_func = MathTex(r"\frac{\sin{3\pi x}}{\pi x}").next_to(func, RIGHT).set_color(RED)

        self.play(DrawBorderThenFill(VGroup(ax, func,ax_lables)), run_time = 2)
        self.wait()