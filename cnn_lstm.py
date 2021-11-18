from re import S
from warnings import showwarning
from PIL.ImageFilter import Kernel
from manimlib import *

import os

from manimlib import window
from manimlib.utils import color
class CNN_LSTM(Scene):
    def construct(self):
        
        face_img = ImageMobject('img/face_mask.png').set_width(1.5).move_to(LEFT * 5)
        txt_cnn = Text(
            "[BS, 3, 100, 100]",
            font="Consolas", 
            font_size=20,
            t2c={"[BS, 3, 100, 100]": BLUE}
        ).move_to(LEFT * 5 + DOWN)

        self.play(AnimationGroup(
            FadeIn(face_img),
            Write(txt_cnn),
            FocusOn(face_img),
           ), run_time=1
        )
        face_img.fix_in_frame()
        txt_cnn.fix_in_frame()
        
        cnn_block1 = Square(
            color=BLACK,
            side_length=1,
            stroke_width=0.5
        ).get_grid(6, 6, 4).arrange_in_grid(buff=0.01)
        cnn_block1.set_fill(RED_A, opacity=1)
        
        self.play(AnimationGroup(*[ShowCreation(cnn_block1)]))
        self.play(AnimationGroup(*[
            FadeOut(face_img),
            cnn_block1.animate.shift(LEFT * 5),
            txt_cnn.animate.shift(DOWN * 1)
        ]))
        
        cnn_block1_channle_2 = Square(
            color=BLACK,
            side_length=1,
            stroke_width=0.5
        ).get_grid(6, 6, 4).arrange_in_grid(buff=0.01).move_to(LEFT * 5 + UP * 0.2 + RIGHT * 0.2)
        cnn_block1_channle_2.set_fill(GREEN_B, opacity=1)
        
        cnn_block1_channle_3 = Square(
            color=BLACK,
            side_length=1,
            stroke_width=0.5
        ).get_grid(6, 6, 4).arrange_in_grid(buff=0.01).move_to(LEFT * 5 + UP * 0.4 + RIGHT * 0.4)
        cnn_block1_channle_3.set_fill(BLUE_E, opacity=1)
        cnn_block1.add(txt_cnn)
        
        self.play(AnimationGroup(*[
            TransformFromCopy(cnn_block1, cnn_block1_channle_2),
            TransformFromCopy(cnn_block1_channle_2, cnn_block1_channle_3)
        ]))
        
        cnn_block1_group = VGroup(cnn_block1, cnn_block1_channle_2, cnn_block1_channle_3, txt_cnn)
        
        kernel_layer = Square(
            color=BLACK,
            side_length=1,
            stroke_width=0.5
        ).get_grid(3, 3, 1).arrange_in_grid(buff=0.05).set_fill(ORANGE, opacity=1).move_to(ORIGIN)
        txt_cnn_block2 = Text("Kernel: 3 x 3",
            font="Consolas", 
            font_size=20,
            t2c={"Kernel: 3 x 3": ORANGE}
        ).move_to(ORIGIN + DOWN)
        kernel_group = VGroup(kernel_layer,txt_cnn_block2)
        self.play(TransformFromCopy(cnn_block1_group, kernel_group))
        colors = [BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E]
        feature_map_group = VGroup()
        for i in range(5):
            feature_map_group.add(Square(
            color=BLACK,
            side_length=1,
            stroke_width=0.2
           ).get_grid(6, 6, 3).arrange_in_grid(buff=0.01).set_fill(colors[i], opacity=1))
        
        feature_map_group.arrange(RIGHT + UP, buff=-2)
        feature_map_group.move_to(RIGHT * 4.5)
        
        txt_cnn_block2 = Text("Feature maps",
            font="Consolas", 
            font_size=20,
            t2c={"Feature maps": BLUE}
        ).move_to(RIGHT * 4 + DOWN * 2)
        feature_map_group.add(txt_cnn_block2)
        
        self.play(TransformFromCopy(kernel_group, feature_map_group))
        
        sub_block = VGroup(kernel_group, feature_map_group)
        full_scene = VGroup(cnn_block1_group, sub_block)
        self.play(AnimationGroup(*[full_scene.animate.scale(0.5)]))
        self.play(AnimationGroup(*[full_scene.animate.shift(LEFT * 3 + UP * 2)]))
        
        sub_block2 = sub_block.copy().move_to(RIGHT * 3 + UP * 1.7)
        sub_block2.add(
            Text(
                "x 5",
                font="Consolas", 
                font_size=20,
                t2c={"x 5": BLACK}
            ).move_to(RIGHT * 5),
            Circle(
                radius=0.4
            ).move_to(RIGHT * 5)
        )
        self.play(ShowCreation(sub_block2))
        
        linear_layer = VGroup()
        linear_layer.add(Text(
                   "Linear output:",
                   font="Ubuntu", 
                   font_size=30,
                   t2c={"Linear output:": BLACK}
        ))
        for i in range(15):
            shape = Circle(
                radius= 0.15,
                color=BLACK,
                stroke_width=2
            ).set_fill(color=GREY_B, opacity=0.8)
            if i == 6 or i == 7 or i == 8:
                shape = Text(
                   ".",
                   font="Ubuntu", 
                   font_size=30,
                   t2c={".": BLACK}
                )
            linear_layer.add(shape)
        linear_layer.add(Text(
                   "= 2048",
                   font="Ubuntu", 
                   font_size=30,
                   t2c={"= 2048": BLACK}
        ))
        linear_layer.arrange(RIGHT, buff=0.2)
        linear_layer.move_to(DOWN * 0.3 + LEFT * 0.5)
        self.play(ShowCreation(linear_layer), run_time=1.5)
        lstm_square = Rectangle(
            width=5,
            height=3,
            color=BLACK,
            fill_color=BLUE_E
        ).move_to(DOWN * 2.2 + LEFT * 0.5)
        input_line  = Arrow(start=lstm_square.get_center() + 1.8 * RIGHT + UP, end=lstm_square.get_right() +0.5 * RIGHT + UP,stroke_color=BLACK)
        c_line = Arrow(start= lstm_square.get_left() + 0.5 * LEFT + DOWN, end=lstm_square.get_right() +0.5 * RIGHT + DOWN,stroke_color=BLACK)
        input_x = Circle(
            color=RED_C,
            radius=0.2,
            
        ).set_fill(color=RED_C, opacity=0.8).move_to(lstm_square.get_center() + 2 * LEFT + UP)
        
        input_connecton = Line(start=lstm_square.get_center() + 1.8 * LEFT + UP , end= lstm_square.get_center() + RIGHT + UP,stroke_color=BLACK)
        input_interface = Line(start=lstm_square.get_center() + 2 * LEFT + UP * 1.5, end=lstm_square.get_center() + 2 * LEFT + UP * 1.2, stroke_color=BLACK)
        
        gate_1 = Circle(
            color=BLUE_B,
            radius=0.2,
            
        ).set_fill(color=BLUE_B, opacity=0.8).move_to(lstm_square.get_center() + LEFT )
        
        gate_2 = Circle(
            color=BLUE_B,
            radius=0.2,
            
        ).set_fill(color=BLUE_B, opacity=0.8).move_to(lstm_square.get_center() )
        
        gate_3 = Circle(
            color=BLUE_B,
            radius=0.2,
            
        ).set_fill(color=BLUE_B, opacity=0.8).move_to(lstm_square.get_center() + RIGHT)
        
        gate_4 = Circle(
            color=BLUE_B,
            radius=0.2,
            
        ).set_fill(color=BLUE_B, opacity=0.8).move_to(lstm_square.get_center() + RIGHT * 2)

        
        line_a = Line(start=lstm_square.get_center() + RIGHT + UP, end=gate_3.get_top(), stroke_color=BLACK)
        line_b = Line(start=gate_3.get_bottom() + DOWN * 0.81 , end=gate_3.get_bottom(), stroke_color=BLACK)
        line_c = Line(start=gate_2.get_bottom() + DOWN * 0.5 , end=gate_2.get_bottom(), stroke_color=BLACK)
        line_d = Line(start=gate_4.get_bottom() + DOWN * 0.81 , end=gate_4.get_bottom(), stroke_color=BLACK)
        line_e = Line(start=gate_1.get_bottom() + DOWN * 0.81 , end=gate_1.get_bottom(), stroke_color=BLACK)
        line_f = Line(start=gate_2.get_top() + UP * 0.81 , end=gate_2.get_top(), stroke_color=BLACK)
        line_g = Line(start=gate_1.get_top(), end=gate_1.get_top() +  UP * 0.81, stroke_color=BLACK)
        line_h = Line(start=lstm_square.get_center() + 2 * RIGHT + UP, end=gate_4.get_top(), stroke_color=BLACK)
        line_j = Line(start=gate_2.get_bottom() + DOWN * 0.5, end=gate_2.get_bottom() + DOWN * 0.5 + RIGHT, stroke_color=BLACK)
        
        lstm = VGroup(
            gate_1,
            gate_2,
            gate_3,
            gate_4,
            line_a,
            line_b,
            line_c,
            line_d,
            line_e,
            line_f,
            line_h,
            line_g,
            line_j,
            lstm_square,
            c_line,
            input_line,
            input_connecton,
            input_interface,
            input_x
        )
        # Polygon
        self.play(AnimationGroup(*[
            ShowCreation(lstm),
        ]), run_time=2)
        
        lstm.add(linear_layer)
        self.wait(1)
        
        self.play(AnimationGroup(*[
            ShrinkToCenter(sub_block2),
            ShrinkToCenter(full_scene),
            lstm.animate.shift(UP * 2)]))
        results = VGroup()
        results.add(Text(
                   "Prediction Result:",
                   font="Ubuntu", 
                   font_size=20,
                   t2c={"Prediction Result:": BLACK}
        ))
        for i in range(3):
            c = Circle(
                  radius= 0.2,
                  color=ORANGE,
                  stroke_width=2
                ).set_fill(color =ORANGE, opacity=0.8)
            txt_comb = VGroup(
                c,
                Text(
                    str(i),
                    font="Roman", 
                    font_size=20,
                    t2c={str(i): ORANGE}
                    )
            )
            txt_comb.arrange(RIGHT, buff=0.2)
            results.add(txt_comb)

        results.arrange(RIGHT, buff= 1)
        results.move_to(DOWN * 2.5)
        self.play(FadeIn(results, shift=UP))
        