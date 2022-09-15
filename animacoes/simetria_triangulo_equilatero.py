from manim import *

def finishScene(self):
    self.play(*[FadeOut(mob) for mob in self.mobjects])

class Start(Scene):
    def construct(self):

        triangulo = Triangle().scale(2)

        vertices = triangulo.get_vertex_groups()[0]

        baricentro = [ (vertices[0][0] + vertices[1][0] + vertices[2][0])/3, (vertices[0][1] + vertices[1][1] + vertices[2][1])/3, 0]

        vertices[0][1] = vertices[0][1]+0.3
        vertices[1][0] = vertices[1][0]-0.2
        vertices[2][0] = vertices[2][0]+0.3

        labels = VGroup(*[
            Text(label).move_to(point) for label,point in zip(["1","2","3"],vertices)
            ])
        Tri = VGroup()
        Tri.add(triangulo, labels)

        #self.play(FadeIn(triangulo))

        # ... some move or rotate mobjects around...
        self.play(Rotate(Tri, 2*PI/3, about_point = baricentro, rate_func = linear, run_time = 3))

        self.play(Rotate(Tri[1][0], -2*PI/3), Rotate(Tri[1][1], -2*PI/3), Rotate(Tri[1][2], -2*PI/3))

        # some animations remove mobjects from the screen
        #self.play(FadeOut(triangulo))

        self.wait(4)
        matrix = [[-1, 0], [0, 1]]
        matrix2 = [[0, -1]]
        self.play(Tri.animate.apply_matrix(matrix), run_time=1)
        self.add(Tri[1][0].apply_matrix(matrix), Tri[1][0].move_to(vertices[2]), Tri[1][1].apply_matrix(matrix), Tri[1][1].move_to(vertices[1]))
        self.wait(4)

        finishScene(self)
