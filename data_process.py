from manimlib import *
import os

TOP_LEFT = np.array((-5, 3.5, 0.))
class DataProcessing(Scene):
    def construct(self):
        title = Text("Team 23 Data Processing", 
                    font="Consolas", 
                    font_size=90,
                    t2c={"Team 23 Data Processing": BLUE})
        self.play(FadeIn(title, UP))
        self.wait(1)
        self.play(FadeOut(title, UP))
        
        head = Text("Data collection",
                    font="Arial", 
                    font_size=30,
                    t2c={"Data collection": ORANGE},
                    )
        self.play(head.animate.shift(TOP_LEFT), run_time=0)
        self.play(Write(head), run_time=0.5)
        self.wait(0.1)
        self.scen_one()
        self.wait(1)
        
    def scen_one(self):
        ## Create
        original_image = ImageMobject('img/origin_mask_face_img.png').set_shadow(1)
        txt_size = Text(
                    "size: M x N",
                    font="Sans", 
                    font_size=40,
                    t2c={"size: M x N": BLUE},
        ).move_to(DOWN * 2.5)
        square_size = Text(
                    "size: 100 x 100",
                    font="Sans", 
                    font_size=20,
                    t2c={"size: 100 x 100": ORANGE},
        ).move_to(DOWN * 2.5).shift(RIGHT * 1).shift(UP * 2.5)
        
        self.play(AnimationGroup(
            *[FadeIn(original_image, scale=-10),ShowCreation(txt_size)],run_time=0.5
        )
            
        )
        self.wait(0.5)
        self.play(AnimationGroup(
            *[txt_size.animate.shift(LEFT * 4),original_image.animate.shift(LEFT * 4)]
        ))
        self.wait(0.5)
        
        ## Face crop 
        square = Square(side_length=1.5)
        square.set_color(RED)
        square_pose = LEFT * 4
        square_pose[1] = 1
        square.move_to(square_pose)
        self.play(ShowCreation(square), run_time=0.5)
        self.wait(0.5)
        
        # Move face
        face_img = ImageMobject('img/face_mask.png').set_width(1.5).move_to(square_pose)
        
        square_pose = RIGHT * 5
        self.play(AnimationGroup(
            *[square.animate.shift(square_pose),
              face_img.animate.shift(square_pose), 
              TransformFromCopy(txt_size, square_size)]), run_time=0.8
        )
        self.play(FocusOn(square, color=BLUE))
        self.wait(1)
        
        self.remove(original_image)
        self.remove(square)
        self.remove(txt_size)
        
        # Fade out older one
        square_pose[1] += 1
        square_pose[0] = LEFT[0] * 6.5
        self.play(AnimationGroup(
            *[square.animate.shift(square_pose),
              face_img.animate.shift(square_pose), 
              square_size.animate.shift(square_pose)]), run_time=1
        )
        square_pose[0] += 1
        txt_label = Text(
                    "Label:Face with mask",
                    font="Sans", 
                    font_size=20,
                    t2c={"Label:Face with mask": ORANGE},
        ).move_to(square_pose)
        self.play(Transform(square_size, txt_label))
        # Load other images
        self.load_group_images(np.array((0.5, 2., 0.)), './img/other_masks/', '... 359',"", square_pose)
        square_pose[1] -=2
        
        self.load_group_images(np.array((-1.5, 0., 0.)), './img/other_faces/', '... 331',"Label:Face", square_pose)
        square_pose[1] -=2
        self.load_group_images(np.array((-1.5, -2., 0.)), './img/other_noise/', '... 369',"Label:Non-Face", square_pose)
        
        
        self.wait(2)
    def load_group_images(self, base_pose, folder_path, num, label, label_pse):
        other_images = []
        anim_images = []
        files = os.listdir(folder_path)
        tmp_square_pose = base_pose
        i = -4
        for file in files:
            tmp_img = ImageMobject(folder_path + file).set_width(1.5).move_to(tmp_square_pose + RIGHT * i)
            other_images.append(tmp_img)
            anim_images.append(FadeIn(tmp_img))
            i += 2
        
        txt_num = Text(
                num,
                font="Sans", 
                font_size=20,
                t2c={num: BLACK},
            ).move_to(tmp_square_pose + RIGHT * i)
        anim_images.append(Write(txt_num))
        
        if len(label) > 0:
            txt_label = Text(
                    label,
                    font="Sans", 
                    font_size=20,
                    t2c={label: ORANGE},
            ).move_to(label_pse)
            anim_images.append(Write(txt_label))
        self.play(*anim_images)