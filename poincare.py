from manim import *

class Manifold(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=10 * DEGREES)
        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u) - 0.75
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[MAROON_D, MAROON_E], resolution=(30, 30)
        )
        flat = ParametricSurface(
            lambda u, v: np.array([
                50 * np.cos(u) * np.cos(v),
                50 * np.cos(u) * np.sin(v),
                50 * np.sin(u) - 50
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[MAROON_D, MAROON_E], resolution=(30, 30)
        )

        self.add(sphere)
        self.wait()
        self.play(Transform(sphere, flat))
        self.wait()

class Closed(ThreeDScene):
    def construct(self):
        def param_plane(u, v):
            x = u
            y = v
            z = 0
            return np.array([x, y, z])

        square = ParametricSurface(
            param_plane,
            resolution=(22, 22),
            v_min=-2,
            v_max=+2,
            u_min=-2,
            u_max=+2,
            checkerboard_colors=[GREEN_C, GREEN_D]
        )

        plane = ParametricSurface(
            param_plane,
            resolution=(22, 22),
            v_min=-10,
            v_max=+12,
            u_min=-12,
            u_max=+10,
            checkerboard_colors=[GREEN_C, GREEN_D]
        )

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[GREEN_C, GREEN_D], resolution=(30, 30)
        )

        self.set_camera_orientation(phi=45 * DEGREES, theta=-30 * DEGREES)
        self.play(Write(square))
        self.wait(2)
        self.play(FadeOut(square))
        self.play(Write(plane))
        self.wait(2)
        self.play(FadeOut(plane))
        self.play(Write(sphere))
        self.wait(2)

# not part of render
class Circle(ThreeDScene):
    def construct(self):
        circle = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[MAROON_D, MAROON_E], resolution=(15, 15)
        )

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.play(FadeIn(circle))
        self.wait()

class Homeomorphic(ThreeDScene):
    def construct(self):
        # axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u),
                1.5 * np.sin(u),
                v
            ]), v_min=-1.5, v_max=1.5, u_min= 0, u_max= TAU,
            checkerboard_colors=[LIGHT_GREY, GREY], resolution=(15, 32)
        )
        circle = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                0.2
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[LIGHT_GREY, GREY], resolution=(15, 15)
        )
        disk = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u),
                1.5 * np.sin(u),
                v
            ]), v_min=-0.2, v_max=0.2, u_min= 0, u_max= TAU,
            checkerboard_colors=[LIGHT_GREY, GREY], resolution=(15, 32)
        )
        nothingness = ParametricSurface(
            lambda u, v: np.array([
                0.01 * np.cos(u) + 0.5,
                0.01 * np.sin(u),
                v
            ]), v_min=-0.001, v_max=0.001, u_min= 0, u_max= TAU,
            checkerboard_colors=[LIGHT_GREY, GREY], resolution=(15, 32)
        )
        handle = ParametricSurface(
            lambda u, v: np.array([
                (0.8 + 0.2 * np.cos(v)) * np.cos(u) + 1.5,
                0.2 * np.sin(v),
                (0.8 + 0.2 * np.cos(v)) * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=0, u_max=TAU,
            checkerboard_colors=[LIGHT_GREY, GREY], resolution=(30, 30)
        )
        torus = ParametricSurface(
            lambda u, v: np.array([
                (1 + 0.6 * np.cos(v)) * np.cos(u),
                0.6 * np.sin(v),
                (1 + 0.6 * np.cos(v)) * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=0, u_max=TAU,
            checkerboard_colors=[LIGHT_GREY, GREY], resolution=(30, 30)
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        # self.add(axes)
        self.add(cylinder, handle, circle)
        self.begin_ambient_camera_rotation(rate=PI/4)
        self.wait()
        self.play(Transform(cylinder, disk))
        self.play(Transform(cylinder, nothingness), Transform(circle, nothingness))
        self.play(FadeOut(cylinder), FadeOut(circle), Transform(handle, torus))
        self.wait()