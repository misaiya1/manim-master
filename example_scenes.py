#!/usr/bin/env python

from manimlib.imports import *
import numpy as np


# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flag -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)
#abcd

class Scene_(Scene):
    CONFIG = {"camera_config": {"background_color": "#ffffff"}}


class MySPWM(Scene):
    def construct(self):

        Vphase = 0.866
        # Vphase = 1

        '''line and word'''
        lineP = Line(np.array([-5, Vphase, 0]), np.array([5, Vphase, 0]), color=PINK)
        reference = DashedVMobject(Line(LEFT * 5, RIGHT * 5, color=GRAY))
        lineN = Line(np.array([-5, -Vphase, 0]), np.array([5, -Vphase, 0]), color=PINK)
        self.add(lineP)
        self.add(lineN)
        self.add(reference)
        ##########################################################################################
        #title = TextMobject("Vdc = %s* 相峰值" %(Vphase*2) )
        #title.to_corner(UP + LEFT)



        # basel = TexMobject(
        #     "\\sum_{n=1}^\\infty "
        #     "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        # )
        #VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            #FadeInFrom(basel, UP),
        )
        self.wait()

        # transform_title = TexMobject("That was a transform")
        # transform_title.to_corner(UP + LEFT)
        # self.play(
        #     Transform(title, transform_title),
        #     LaggedStart(*map(FadeOutAndShiftDown, basel)),
        # )
        # self.wait()

        '''arrow'''
        arrowU = Vector(UP, color=YELLOW)
        arrowV = Vector(UP, color=GREEN)
        arrowW = Vector(UP, color=RED)

        dot0 = Dot(color=PINK, fill_opacity=1.0)

        arrowU.move_to([0, 0.5, 0])
        arrowV.move_to([0, 0.5, 0])
        arrowW.move_to([0, 0.5, 0])

        arrowV.rotate(-TAU / 3, about_point=ORIGIN)
        arrowW.rotate(TAU / 3, about_point=ORIGIN)

        '''circle'''
        circle = Circle(radius=1, color=GRAY)
        circle.set_fill(BLUE, opacity=0)

        roo = VGroup(arrowU, arrowV, arrowW, circle, dot0)
        roo.move_to([-5, 0, 0])
        self.play(GrowFromCenter(arrowU))
        self.play(GrowFromCenter(arrowV))
        self.play(GrowFromCenter(arrowW))
        self.play(GrowFromCenter(dot0))
        self.play(GrowFromCenter(circle))
        self.wait(0)
        self.play(FadeOut(circle))

        dotU = Dot(point=[arrowU.get_start()[0], arrowU.get_end()[1], 0], color=YELLOW, fill_opacity=0.0)
        dotV = Dot(point=[arrowU.get_start()[0], arrowV.get_end()[1], 0], color=GREEN, fill_opacity=0.0)
        dotW = Dot(point=[arrowU.get_start()[0], arrowW.get_end()[1], 0], color=RED, fill_opacity=0.0)

        roo = VGroup(arrowU, arrowV, arrowW, dot0)
        roo.save_state()
        dotU.save_state()
        dotV.save_state()
        dotW.save_state()

        def update_rotate_move(mob, alpha):
            roo.restore()
            dotU.restore()
            dotV.restore()
            dotW.restore()
            roo.shift(RIGHT * 10 * alpha)
            # roo.move_to(np.array((1., 0., 0.)) * 5 * (alpha*2-1))
            roo.rotate(3 * PI * alpha, axis=OUT, about_point=arrowU.get_start())
            roo.shift(DOWN * (arrowU.get_start()[1]))
            # roo.next_to(reference, UP)

            minY = min(arrowU.get_end()[1], arrowV.get_end()[1], arrowW.get_end()[1])
            maxY = max(arrowU.get_end()[1], arrowV.get_end()[1], arrowW.get_end()[1])

            if minY < -Vphase:
                roo.shift(UP * (-Vphase - minY))
            elif maxY > Vphase:
                roo.shift(DOWN * (maxY - Vphase))

            dotU.move_to([arrowU.get_start()[0], arrowU.get_end()[1], 0])
            dotV.move_to([arrowV.get_start()[0], arrowV.get_end()[1], 0])
            dotW.move_to([arrowW.get_start()[0], arrowW.get_end()[1], 0])

        pathU = TracedPath(dotU.get_center, color=YELLOW)
        pathV = TracedPath(dotV.get_center, color=GREEN)
        pathW = TracedPath(dotW.get_center, color=RED)
        pathO = TracedPath(dot0.get_center, color=PINK)

        pathU.set_color(color=YELLOW)
        pathV.set_color(color=GREEN)
        pathW.set_color(color=RED)
        pathO.set_color(color=PINK)

        self.add(pathU)
        self.add(pathV)
        self.add(pathW)
        self.add(pathO)
        self.play(
            UpdateFromAlphaFunc(roo, update_rotate_move),
            run_time=4
        )
        self.wait(1)

        self.wait(3)


class MySPWM_two(Scene):
    def construct(self):

        Vphase = 0.866

        '''line and word'''
        lineP = Line(np.array([-5, Vphase, 0]), np.array([5, Vphase, 0]), color=PINK)
        reference = DashedVMobject(Line(LEFT * 5, RIGHT * 5, color=GRAY))
        lineN = Line(np.array([-5, -Vphase, 0]), np.array([5, -Vphase, 0]), color=PINK)
        self.add(lineP)
        self.add(lineN)
        self.add(reference)
        ##########################################################################################
        title1 = TextMobject("网侧变流器与机侧变流器处于同一直流系统")
        title1.to_corner(UP)
        title2 = TextMobject("交流中性点存在电势差")
        title2.next_to(title1, DOWN)

        self.play(
            Write(title1),
            Write(title2),
        )

        # basel = TexMobject(
        #     "\\sum_{n=1}^\\infty "
        #     "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        # )
        # VGroup(title, basel).arrange(DOWN)
        # self.play(
        #     Write(title),
        #     FadeInFrom(basel, UP),
        # )
        # self.wait()
        #
        # transform_title = TexMobject("That was a transform")
        # transform_title.to_corner(UP + LEFT)
        # self.play(
        #     Transform(title, transform_title),
        #     LaggedStart(*map(FadeOutAndShiftDown, basel)),
        # )
        # self.wait()

        '''arrow'''
        arrowU = Vector(UP, color=YELLOW)
        arrowV = Vector(UP, color=GREEN)
        arrowW = Vector(UP, color=RED)

        dot0 = Dot(color=PINK, fill_opacity=1.0)

        arrowU.move_to([0, 0.5, 0])
        arrowV.move_to([0, 0.5, 0])
        arrowW.move_to([0, 0.5, 0])

        arrowV.rotate(-TAU / 3, about_point=ORIGIN)
        arrowW.rotate(TAU / 3, about_point=ORIGIN)

        '''circle'''


        roo = VGroup(arrowU, arrowV, arrowW, dot0)
        roo.move_to([-3, 0, 0])
        #self.play(GrowFromCenter(roo))
        #########################################################
        arrowU2 = Vector(UP, color=YELLOW)
        arrowV2 = Vector(UP, color=GREEN)
        arrowW2 = Vector(UP, color=RED)

        dot02 = Dot(color=PINK, fill_opacity=1.0)

        arrowU2.move_to([0, 0.5, 0])
        arrowV2.move_to([0, 0.5, 0])
        arrowW2.move_to([0, 0.5, 0])

        arrowV2.rotate(-TAU / 3, about_point=ORIGIN)
        arrowW2.rotate(TAU / 3, about_point=ORIGIN)

        '''circle'''


        roo2 = VGroup(arrowU, arrowV, arrowW, dot0)
        roo2.move_to([3, 0, 0])
        #self.play(GrowFromCenter(roo2))



        roo = VGroup(arrowU, arrowV, arrowW, dot0)
        roo.move_to([-3, 0, 0])
        roo2 = VGroup(arrowU2, arrowV2, arrowW2, dot02)
        roo2.move_to([3, 0, 0])

        roo.save_state()
        roo2.save_state()

        def update_rotate_move(roo, alpha):
            roo.restore()

            # roo.move_to(np.array((1., 0., 0.)) * 5 * (alpha*2-1))
            roo.rotate(3 * PI * alpha, axis=OUT, about_point=arrowU.get_start())

            roo.shift(DOWN * (arrowU.get_start()[1]))
            # roo.next_to(reference, UP)

            minY = min(arrowU.get_end()[1], arrowV.get_end()[1], arrowW.get_end()[1])
            maxY = max(arrowU.get_end()[1], arrowV.get_end()[1], arrowW.get_end()[1])

            if minY < -Vphase:
                roo.shift(UP * (-Vphase - minY))
            elif maxY > Vphase:
                roo.shift(DOWN * (maxY - Vphase))


        def update_rotate_move2(roo2, alpha):
            roo2.restore()

            # roo.move_to(np.array((1., 0., 0.)) * 5 * (alpha*2-1))
            roo2.rotate(10 * PI * alpha, axis=OUT, about_point=arrowU2.get_start())

            roo2.shift(DOWN * (arrowU2.get_start()[1]))
            # roo.next_to(reference, UP)

            minY2 = min(arrowU2.get_end()[1], arrowV2.get_end()[1], arrowW2.get_end()[1])
            maxY2 = max(arrowU2.get_end()[1], arrowV2.get_end()[1], arrowW2.get_end()[1])

            if minY2 < -Vphase:
                roo2.shift(UP * (-Vphase - minY2))
            elif maxY2 > Vphase:
                roo2.shift(DOWN * (maxY2 - Vphase))

        self.play(
            UpdateFromAlphaFunc(roo, update_rotate_move),
            UpdateFromAlphaFunc(roo2, update_rotate_move2),
            run_time=10,
            rate_func = linear
        )
        self.wait(1)


class AntiClockCircleRun(Scene):
    def construct(self):
        R2 = Circle(radius=2, color=GREEN)
        self.add(R2)
        R1 = RegularPolygon(n=3)  # Dot(color=RED,fill_opacity=1.0)
        self.add(R1)

        def rr(x, y, z, t):
            x = x + 2 * math.cos(2 * math.pi * t)
            y = y + 2 * math.sin(2 * math.pi * t)
            z = 0
            return [x, y, z]

        self.play(Homotopy(rr, R1), run_time=10, rate_func=linear)
        self.wait()


class DotUpDown(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject('this is some text').next_to(dot, RIGHT)
        self.add(dot, text)
        # group01 = VGroup(text,dot)
        text.add_updater(lambda a: a.next_to(dot, RIGHT))
        self.play(dot.shift, UP * 3)
        self.play(dot.shift, DOWN * 3)
        # 移除原先的绑定,下面这句无效，remove_updater不适合匿名函数，因此只能使用clear_updater
        text.remove_updater(lambda a: a.next_to(dot, RIGHT))

        # 清空绑定的所有关系
        text.clear_updaters()

        # 来来去去
        self.play(dot.shift, UP * 4, rate_func=there_and_back, run_time=2)


class Xarrange01(Scene):
    def construct(self):
        square1, square2 = VGroup(
            Square(color=RED),
            Square(color=BLUE)
        ).scale(0.5).set_x(-5)

        reference = DashedVMobject(Line(LEFT * 5, RIGHT * 5, color=GRAY))
        self.add(square1, square2, reference)

        square2.save_state()

        def update_rotate_move(mob, alpha):
            square2.restore()
            square2.shift(RIGHT * 10 * alpha)
            square2.rotate(3 * PI * alpha)

        self.play(
            square1.rotate, 3 * PI,
            square1.move_to, [5, 0, 0],
            UpdateFromAlphaFunc(square2, update_rotate_move),
            run_time=4
        )

        self.wait()


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()


class Bezier1(Scene_):

    def construct(self):
        hL = Line(color=BLUE).scale(7).shift(UP * 3)
        dot0 = Dot(color=ORANGE).shift(UP * 2)
        self.add(hL, dot0)
        vg = VGroup()
        doti = Dot(color=ORANGE).move_to(hL.get_start())
        l_1 = Line(color=BLACK, stroke_width=1.5).put_start_and_end_on(dot0.get_center(), doti.get_center())
        l_2 = l_1.copy().rotate(PI / 2).scale(10).set_color(PURPLE).set_stroke(width=6)
        doti.save_state()
        self.add(doti, l_1, l_2, vg)

        def anim(obj, alpha):
            doti.restore()
            doti.shift(RIGHT * hL.get_length() * alpha)
            l_1.put_start_and_end_on(dot0.get_center(), doti.get_center())
            l_2.become(l_1.copy().rotate(PI / 2).scale(100).set_color(PURPLE).set_stroke(width=6))
            vg.add(l_2.copy().set_stroke(width=2, color=PURPLE_E))

        self.play(UpdateFromAlphaFunc(doti, anim), run_time=8, rate_func=linear)
        self.wait()


class Bezier2(Scene_):

    def construct(self):
        dot_a = Dot(np.array([-3, -3, 0]), color=PURPLE_A)
        dot_b = Dot(np.array([0, 3, 0]), color=PURPLE_A)
        dot_c = Dot(np.array([3, -3, 0]), color=PURPLE_A)
        l_1 = Line(color=BLUE).put_start_and_end_on(dot_a.get_center(), dot_b.get_center())
        l_2 = Line(color=BLUE).put_start_and_end_on(dot_b.get_center(), dot_c.get_center())
        l_3 = l_1.copy()
        lineG = VGroup()
        self.add(dot_a, dot_b, dot_c, l_1, l_2, l_3, lineG)

        def anim(obj, alpha):
            dot_a.move_to(l_1.point_from_proportion(alpha))
            dot_b.move_to(l_2.point_from_proportion(alpha))
            l_3.put_start_and_end_on(dot_a.get_center(), dot_b.get_center())
            # if int(alpha*100) % 5 == 0:  #加if之后会间歇的加入中间的包络线
            #     lineG.add(l_3.copy().set_stroke(width=2, color=BLUE_A))
            lineG.add(l_3.copy().set_stroke(width=2, color=BLUE_A))  # 这行的话最后是用线填充这个区域

        self.play(UpdateFromAlphaFunc(l_3, anim), run_time=8, rate_func=linear)
        self.wait()

# See old_projects folder for many, many more


