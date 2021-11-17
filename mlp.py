from manimlib import *
import os

from manimlib import window
class MLP(Scene):
    def construct(self):
        
        face_img = ImageMobject('img/face_mask.png').set_width(1.5).move_to(LEFT * 5)
        txt_face_img_size = Text(
            "100 x 100", 
            font="Consolas", 
            font_size=15,
            t2c={"100 x 100": BLUE}
        ).move_to(LEFT * 3.5)
        
        txt_channel_size = Text(
            " x 3", 
            font="Consolas", 
            font_size=15,
            t2c={" x 3": ORANGE}
        ).move_to(LEFT * 2.8)
        
        self.play(AnimationGroup(
            Write(txt_face_img_size),
            GrowFromCenter(face_img),
            FocusOn(face_img),
           ), run_time=1
        )

        
        
        self.play(Write(txt_channel_size))
        bounding_box = Rectangle(width=10, height=6).move_to(RIGHT * 3)
        bounding_box.set_color(BLACK)
        bounding_box.set_fill(BLUE_C, opacity=0.3)
        bounding_box.set_stroke(BLACK, width=2)
        self.play(ShowCreation(bounding_box))
        input_pose = UP
                
        pic_txt_group = VGroup(txt_face_img_size, txt_channel_size)
        input_size_pos = np.array((-4, 2.5, 0.))
        input_size = Text(
            "30000",
            font="Ubuntu", 
            font_size=30,
            t2c={"30000": ORANGE}
        ).move_to(input_size_pos)
        
        inputs_layer = VGroup()
        for i in range(10):
            shape = Circle(
                radius= 0.2,
                color=ORANGE,
                stroke_width=2
            )
            if i == 4 or i == 5:
                shape = Text(
                   ".",
                   font="Ubuntu", 
                   font_size=30,
                   t2c={".": ORANGE}
                )
            inputs_layer.add(shape)
        inputs_layer.arrange(DOWN, buff=0.2)
        inputs_layer.move_to(LEFT * 4 + np.array((0, -0.3, 0.)))
    
        self.play(AnimationGroup(*[
            face_img.animate.shift(LEFT),
            Transform(pic_txt_group, input_size),
            bounding_box.animate.shift(LEFT * 3),
        ]))
        self.play(ShowCreation(inputs_layer))

        ## Hidden Layer
        hidden_size_pos = np.array((-2, 2.5, 0.))
        hidden_size = Text(
            "10000",
            font="Ubuntu", 
            font_size=30,
            t2c={"10000": GREY}
        ).move_to(hidden_size_pos)
        
        hidden_layer1 = VGroup()
        for i in range(8):
            shape = Circle(
                radius= 0.2,
                color=BLACK,
                stroke_width=2
            )
            if i == 3 or i == 4 :
                shape = Text(
                   ".",
                   font="Ubuntu", 
                   font_size=30,
                   t2c={".": BLACK}
                )
            hidden_layer1.add(shape)
        hidden_layer1.arrange(DOWN, buff=0.2)
        hidden_layer1.move_to(LEFT * 2 + np.array((0, -0.3, 0.)))
        self.play(AnimationGroup(
            *[TransformFromCopy(inputs_layer, hidden_layer1),
              TransformFromCopy(input_size, hidden_size)]
        ))
        
        # Hidden Layer 2
        hidden2_size_pos = np.array((0, 2.5, 0.))
        hidden2_size = Text(
            "100",
            font="Ubuntu", 
            font_size=30,
            t2c={"100": GREY}
        ).move_to(hidden2_size_pos)
        
        hidden_layer2 = VGroup()
        for i in range(6):
            shape = Circle(
                radius= 0.2,
                color=BLACK,
                stroke_width=2
            )
            if i == 2 or i == 3 :
                shape = Text(
                   ".",
                   font="Ubuntu", 
                   font_size=30,
                   t2c={".": BLACK}
                )
            hidden_layer2.add(shape)
        hidden_layer2.arrange(DOWN, buff=0.2)
        hidden_layer2.move_to(ORIGIN  + np.array((0, -0.3, 0.)))
        self.play(AnimationGroup(
            *[TransformFromCopy(hidden_layer1, hidden_layer2),
              TransformFromCopy(hidden_size, hidden2_size)]
        ))
        
        # Hidden Layer 3
        hidden3_size_pos = np.array((2, 2.5, 0.))
        hidden3_size = Text(
            "3",
            font="Ubuntu", 
            font_size=30,
            t2c={"3": ORANGE}
        ).move_to(hidden3_size_pos)
        
        hidden_layer3 = VGroup()
        results = []
        for i in range(3):
            c = Circle(
                  radius= 0.2,
                  color=ORANGE,
                  stroke_width=2
                )
            results.append(c)
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
            hidden_layer3.add(txt_comb)
        hidden_layer3.arrange(DOWN, buff=0.2)
        hidden_layer3.move_to(RIGHT * 2  + np.array((0, -0.3, 0.)))
        self.play(AnimationGroup(
            *[TransformFromCopy(hidden_layer2, hidden_layer3),
              TransformFromCopy(hidden2_size, hidden3_size)]
        ))
        
        edges_one = VGroup()
        input_layer_dots = []
        for shape in inputs_layer:
            if type(shape) is Circle:
                input_layer_dots.append(shape.get_arc_center() + np.array([0.22, 0, 0]))
                
        hidden_layer1_left_dots = []
        hidden_layer1_right_dots = []
        for shape in hidden_layer1:
            if type(shape) is Circle:
                hidden_layer1_left_dots.append(shape.get_arc_center() + np.array([-0.22, 0, 0]))
                hidden_layer1_right_dots.append(shape.get_arc_center() + np.array([0.22, 0, 0]))
                
        for start in input_layer_dots:
            for end in hidden_layer1_left_dots:
                edges_one.add(
                    Line(start=start[0], end=end[0], stroke_width= 1.2, color=GREY_B)
                )
        self.play(ShowCreation(edges_one))
        
        edges_two = VGroup()
        
        hidden_layer2_left_dots = []
        hidden_layer2_right_dots = []
        
        for shape in hidden_layer2:
            if type(shape) is Circle:
                hidden_layer2_left_dots.append(shape.get_arc_center() + np.array([-0.22, 0, 0]))
                hidden_layer2_right_dots.append(shape.get_arc_center() + np.array([0.22, 0, 0]))
        
        hidden_layer3_left_dots = []
        hot_fix_left = None
        for shape in hidden_layer3:
            for circle in shape:
                if type(circle) is Circle:
                    if hot_fix_left is None:
                        hot_fix_left = circle.get_arc_center()
                    hot_fix_left[0][1] = circle.get_arc_center()[0][1]
                    hidden_layer3_left_dots.append(hot_fix_left + np.array([-0.22, 0, 0]))
        
        # hidden1-hidden2
        for start in hidden_layer1_right_dots:
            for end in hidden_layer2_left_dots:
                edges_two.add(
                    Line(start=start[0], end=end[0], stroke_width= 1.2,  color=GREY_B)
                )
        self.play(ShowCreation(edges_two))
        
        # hidden2-hidden3
        edges_three = VGroup()
        for start in hidden_layer2_right_dots:
            for end in hidden_layer3_left_dots:
                edges_three.add(
                    Line(start=start[0], end=end[0], stroke_width= 1.2, color=GREY_B)
                )
        self.play(ShowCreation(edges_three))
        

        self.forward_pass(inputs_layer,edges_one,"Do foward pass..",hidden_layer1,edges_two,hidden_layer2, edges_three, results[2], "Face-Mask")
        pure_face_img = ImageMobject('img/other_faces/045_face.png').set_width(1.5).move_to(LEFT * 6)
        self.play(
            AnimationGroup(*[FadeOut(face_img), FadeIn(pure_face_img)], run_time=1.5)
        )
        self.forward_pass(inputs_layer,edges_one,"Do it again..",hidden_layer1,edges_two,hidden_layer2, edges_three, results[1], "Human Face")
        non_face_img = ImageMobject('img/other_noise/761_nonface.png').set_width(1.5).move_to(LEFT * 6)
        self.play(
            AnimationGroup(*[FadeOut(pure_face_img), FadeIn(non_face_img)], run_time=1.5)
        )
        self.forward_pass(inputs_layer,edges_one,"Keep forward..",hidden_layer1,edges_two,hidden_layer2, edges_three, results[0], "Non-Face")
       
    
    def forward_pass(self,inputs_layer, 
                     edges_one, 
                     t,
                     hidden_layer1, 
                     edges_two, 
                     hidden_layer2 ,
                     edges_three,
                     last_element,
                     label_txt):
        ## Forward pass
        input_anim = []
        back_input_anim = []
        txt_forward = Text(
            t,
            font="Roman",
            font_size=30,
            gradient=(BLACK, BLUE),
        ).move_to(DOWN * 3.5)
        for i,shape in enumerate(inputs_layer):
            if type(shape) is Circle and i != 2 and i != 7 :
                input_anim.append(shape.animate.set_fill("#fa8e3c", opacity=0.8))
        for i, shape in enumerate(edges_one):
            if type(shape) is Line and i != 2 * 6 and i != 7 * 6:
                input_anim.append(shape.animate.set_stroke(width=3, color="#fa8e3c"))
        input_anim.append(ShowCreation(txt_forward))
        self.play(LaggedStart(*input_anim), run_time=1)
        
        for shape in inputs_layer:
            if type(shape) is Circle:
                back_input_anim.append(shape.animate.set_fill(None, opacity=0))
        for shape in edges_one:
            if type(shape) is Line:
                back_input_anim.append(shape.animate.set_stroke(width=1.2, color=GREY_B))
        
        for i, shape in enumerate(hidden_layer1):
            if type(shape) is Circle and i != 1 and i != 4:
                back_input_anim.append(shape.animate.set_fill(GREY_D, opacity=0.8))
        
        for i, shape in enumerate(edges_two):
            if type(shape) is Line and i != 1 * 4 and i != 4 * 4:
                back_input_anim.append(shape.animate.set_stroke(width=3, color="#fa8e3c"))
        
        self.play(LaggedStart(*back_input_anim), run_time=1.5)
        
        
        hidden_layer1_anim = []
        for shape in hidden_layer1:
            if type(shape) is Circle:
                hidden_layer1_anim.append(shape.animate.set_fill(None, opacity=0))
        for shape in edges_two:
            if type(shape) is Line:
                hidden_layer1_anim.append(shape.animate.set_stroke(width=1.2, color=GREY_B))
                
        for i, shape in enumerate(hidden_layer2):
            if type(shape) is Circle and i != 3:
                hidden_layer1_anim.append(shape.animate.set_fill(GREY_D, opacity=0.8))
        
        for i, shape in enumerate(edges_three):
            if type(shape) is Line and i >3:
                hidden_layer1_anim.append(shape.animate.set_stroke(width=3, color="#fa8e3c"))
        self.play(LaggedStart(*hidden_layer1_anim), run_time=1.5)
        
        hidden_layer2_anim = []
        
        for shape in hidden_layer2:
            if type(shape) is Circle:
                hidden_layer2_anim.append(shape.animate.set_fill(None, opacity=0))
        for shape in edges_three:
            if type(shape) is Line:
                hidden_layer2_anim.append(shape.animate.set_stroke(width=1.2, color=GREY_B))
        hidden_layer2_anim.append(last_element.animate.set_fill("#fa8e3c", opacity=0.8))
        
        self.play(LaggedStart(*hidden_layer2_anim), run_time=1.5)
        
        # Results.
        arrow = Arrow(RIGHT * 2.5  + np.array((0, -0.3, 0.)), 
                      RIGHT * 3.5  + np.array((0, -0.3, 0.)))
        arrow.set_fill(color=BLUE, opacity=1)
        txt_result = Text(
            label_txt,
            font_size=25,
            gradient=("#fa8e3c", ORANGE),
        ).move_to(RIGHT *4  + np.array((0, -0.3, 0.)))
        self.play(AnimationGroup(*[GrowArrow(arrow), Write(txt_result)]))
        self.wait(2)
        self.play(AnimationGroup(
            *[FadeOut(arrow), last_element.animate.set_fill(None, opacity=0), Uncreate(txt_result), Uncreate(txt_forward)]))
    