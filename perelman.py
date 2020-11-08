from manim import *

class Equation(Scene):
    def construct(self):
        ricci = MathTex(
            "\\frac{d}{dt}g_{ij}(t)", "=", "-2R_{ij}"      # Ricci Flow differential equation
        )
        self.play(Write(ricci))

class RicciSphere(ThreeDScene):
    def construct(self):
        # axes = ThreeDAxes()
        big = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[RED_D, RED_E], resolution=(30, 64)
        )
        small = ParametricSurface(
            lambda u, v: np.array([
                0.001 * np.cos(u) * np.cos(v),
                0.001 * np.cos(u) * np.sin(v),
                0.001 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[RED_D, RED_E], resolution=(30, 64)
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # self.add(axes)
        self.play(Write(big))
        self.wait(2)
        self.play(Transform(big, small), run_time = 3)
        # self.play(FadeOut(axes, big))

class Singularity(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)

        # axes = ThreeDAxes()
        cassini = ParametricSurface(       # cassini oval, connected
            lambda u, v: np.array([
                1.5 * np.cos(u) * (np.sin(v) * 1.98 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.99)**4 - (np.sin(2*v))**2))),
                1.5 * (np.cos(v) * 1.98 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.99)**4 - (np.sin(2*v))**2))),
                1.5 * np.sin(u) * (np.sin(v) * 1.98 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.99)**4 - (np.sin(2*v))**2)))
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[BLUE_D, BLUE_E], resolution=(45, 45)
        )
        lemniscate = ParametricSurface(    # cassini oval, (almost) singularity, lemniscate
            lambda u, v: np.array([
                1.5 * np.cos(u) * (np.sin(v) * 2*0.9999999999 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.9999999999)**4 - (np.sin(2*v))**2))),
                1.5 * (np.cos(v) * 2*0.9999999999 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.9999999999)**4 - (np.sin(2*v))**2))),
                1.5 * np.sin(u) * (np.sin(v) * 2*0.9999999999 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.9999999999)**4 - (np.sin(2*v))**2)))
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[RED_D, RED_E], resolution=(45, 45)
        )
        # eggs = ParametricSurface(          # cassini oval, split, two "eggs" lol
        #    lambda u, v: np.array([
        #        1.5 * np.cos(u) * (np.sin(v) * 2.02 * np.sqrt(np.cos(2*v) + np.sqrt((1/1.01)**4 - (np.sin(2*v))**2))),
        #        1.5 * (np.cos(v) * 2.02 * np.sqrt(np.cos(2*v) + np.sqrt((1/1.01)**4 - (np.sin(2*v))**2))),
        #        1.5 * np.sin(u) * (np.sin(v) * 2.02 * np.sqrt(np.cos(2*v) + np.sqrt((1/1.01)**4 - (np.sin(2*v))**2)))
        #    ]), v_min=-np.arcsin((1/1.01)**2)/2, v_max=np.arcsin((1/1.01)**2)/2, u_min=-PI / 2, u_max=PI / 2,
        #    checkerboard_colors=[RED_D, RED_E], resolution=(45, 45)
        # )

        self.add(cassini)

        self.begin_ambient_camera_rotation(rate=PI/4)
        self.wait(4)
        # self.stop_ambient_camera_rotation()
        # self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES)
        self.wait()

        self.play(Transform(cassini, lemniscate), run_time = 4)

        # self.begin_ambient_camera_rotation(rate=PI/2)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        # self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES)
        self.wait()

        # self.play(Transform(cassini, eggs), run_time = 2)

        # self.begin_ambient_camera_rotation(rate=PI/2)
        # self.wait(4)
        # self.stop_ambient_camera_rotation()
        # self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES)
        # self.wait()

class Surgery(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=30 * DEGREES)

    # mah gr8 cassini ovals rotated along the x-axis to create a pogchamp dumbbell
        cassini = ParametricSurface(       # cassini oval, connected
            lambda u, v: np.array([
                1.5 * np.cos(u) * (np.sin(v) * 1.98 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.99)**4 - (np.sin(2*v))**2))),
                1.5 * (np.cos(v) * 1.98 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.99)**4 - (np.sin(2*v))**2))),
                1.5 * np.sin(u) * (np.sin(v) * 1.98 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.99)**4 - (np.sin(2*v))**2)))
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[BLUE_D, BLUE_E], resolution=(45, 45)
        )

        lemniscate = ParametricSurface(    # cassini oval, (almost) singularity, lemniscate
            lambda u, v: np.array([
                1.5 * np.cos(u) * (np.sin(v) * 2*0.9999999999 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.9999999999)**4 - (np.sin(2*v))**2))),
                1.5 * (np.cos(v) * 2*0.9999999999 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.9999999999)**4 - (np.sin(2*v))**2))),
                1.5 * np.sin(u) * (np.sin(v) * 2*0.9999999999 * np.sqrt(np.cos(2*v) + np.sqrt((1/0.9999999999)**4 - (np.sin(2*v))**2)))
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[RED_D, RED_E], resolution=(45, 45)
        )

        egg1 = ParametricSurface(          # cassini oval, split, two "eggs" lol
            lambda u, v: np.array([
                1.5 * np.cos(u) * (np.sin(v) * 2.02 * np.sqrt(np.cos(2*v) + np.sqrt((1/1.01)**4 - (np.sin(2*v))**2))),
                1.5 * (np.cos(v) * 2.02 * np.sqrt(np.cos(2*v) + np.sqrt((1/1.01)**4 - (np.sin(2*v))**2))),
                1.5 * np.sin(u) * (np.sin(v) * 2.02 * np.sqrt(np.cos(2*v) + np.sqrt((1/1.01)**4 - (np.sin(2*v))**2)))
            ]), v_min=-np.arcsin((1/1.01)**2)/2 + 0.001, v_max=np.arcsin((1/1.01)**2)/2 - 0.001, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[TEAL_D, TEAL_E], resolution=(45, 45)
        )

        egg2 = ParametricSurface(          # cassini oval, split, two "eggs" lol
            lambda u, v: np.array([
                1.5 * np.cos(u) * (np.sin(v) * 2.02 * np.sqrt(np.cos(2*v) + np.sqrt((1/1.01)**4 - (np.sin(2*v))**2))),
                -1.5 * (np.cos(v) * 2.02 * np.sqrt(np.cos(2*v) + np.sqrt((1/1.01)**4 - (np.sin(2*v))**2))),
                1.5 * np.sin(u) * (np.sin(v) * 2.02 * np.sqrt(np.cos(2*v) + np.sqrt((1/1.01)**4 - (np.sin(2*v))**2)))
            ]), v_min=-np.arcsin((1/1.01)**2)/2 + 0.001, v_max=np.arcsin((1/1.01)**2)/2 - 0.001, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[TEAL_D, TEAL_E], resolution=(45, 45)
        )

        sphere1 = ParametricSurface(       # half sphere
                lambda u, v: np.array([
                1.15 * np.cos(u) * np.cos(v),
                1.15 * np.cos(u) * np.sin(v) -1.5,
                1.15 * np.sin(u)
            ]), v_min=0, v_max=PI, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[RED_D, RED_E], resolution=(45,45)
        )

        sphere2 = ParametricSurface(       # half sphere
                lambda u, v: np.array([
                1.15 * np.cos(u) * np.cos(v),
                1.15 * np.cos(u) * np.sin(v) +1.5,
                1.15 * np.sin(u)
            ]), v_min=-PI, v_max=0, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[RED_D, RED_E], resolution=(45,45)
        )

    # reversing the singularity  
        self.add(lemniscate)
        self.play(Transform(lemniscate, cassini))
    # cutting out problem, replace with caps
        self.play(FadeOut(lemniscate))
        self.play(FadeIn(egg1), FadeIn(egg2))
        self.wait(2)
        self.play(FadeIn(sphere1), FadeIn(sphere2))
    # (no) ricci flow again
        self.begin_ambient_camera_rotation(rate=PI/6)
        # self.play(Transform(egg1, sphere1), Transform(egg2, sphere2), run_time = 4)
        self.wait(6)

class TwoSpheres(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=30 * DEGREES)

        sphere1 = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v) - 2.5,
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[PURPLE_C, PURPLE_D], resolution=(15, 32)
        )

        sphere2 = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v) + 2.5,
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[PURPLE_C, PURPLE_D], resolution=(15, 32)
        )

        cylinder = ParametricSurface(
            lambda u, v: np.array([
                0.5 * np.cos(u),
                v,
                0.5 * np.sin(u)
            ]), v_min=-2.5, v_max=2.5, u_min= 0, u_max= TAU,
            checkerboard_colors=[PURPLE_C, PURPLE_D], resolution=(15, 32)
        )

        cylinder1 = ParametricSurface(
            lambda u, v: np.array([
                0.5 * np.cos(u),
                v,
                0.5 * np.sin(u)
            ]), v_min=-1, v_max=1, u_min= 0, u_max= TAU,
            checkerboard_colors=[PURPLE_C, PURPLE_D], resolution=(15, 32)
        )

        sphere0 = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[PURPLE_C, PURPLE_D], resolution=(15, 32)
        )

        sphere5 = ParametricSurface(
            lambda u, v: np.array([
                3 * np.cos(u) * np.cos(v),
                3 * np.cos(u) * np.sin(v),
                3 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[GOLD_D, GOLD_E], resolution=(15, 32)
        )

        self.play(FadeIn(sphere1), FadeIn(sphere2), FadeIn(cylinder))
        self.wait()
        self.play(Transform(sphere1, sphere0), Transform(sphere2, sphere0), Transform(cylinder, cylinder1))
        self.wait()
        self.play(Transform(sphere1, sphere5))

# not part of render
class SphereTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=30 * DEGREES)

        sphere1 = ParametricSurface(       # half sphere
                lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v) + 1,
                1.5 * np.sin(u)
            ]), v_min=0, v_max=PI, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[RED_D, RED_E], resolution=(45,45)
        )

        sphere2 = ParametricSurface(       # half sphere
                lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v) - 1,
                1.5 * np.sin(u)
            ]), v_min=-PI, v_max=0, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[RED_D, RED_E], resolution=(45,45)
        )

        self.play(FadeIn(sphere1), FadeIn(sphere2))
        self.wait()