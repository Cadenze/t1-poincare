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
        #    ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
        #    checkerboard_colors=[RED_D, RED_E], resolution=(45, 45)
        # )

        self.add(cassini)

        self.begin_ambient_camera_rotation(rate=PI/2)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        # self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES)
        self.wait()

        self.play(Transform(cassini, lemniscate), run_time = 2)

        self.begin_ambient_camera_rotation(rate=PI/2)
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
