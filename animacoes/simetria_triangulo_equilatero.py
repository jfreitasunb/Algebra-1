from manim import *

def finishScene(self):
    self.play(*[FadeOut(mob) for mob in self.mobjects])

class Start(Scene):
    def construct(self):
        rref_matrix_p1 = Matrix(
            [("1", "2", "3"), ("3", "1", "2")], left_bracket="(",
            right_bracket=")")

        rref_matrix_p1_flat = VGroup(*VGroup(*rref_matrix_p1)[0])
        texto = Tex(r"f=")

        rref_matrix_p1.to_corner(corner=UP + LEFT*2, buff=0.5)

        texto.next_to(rref_matrix_p1, LEFT)
        self.play(Write(texto))
        for i in VGroup(*rref_matrix_p1)[1:]:
            self.play(Write(i))

        for i in range(0,6):
            self.play(Write(rref_matrix_p1_flat[i]), **{"run_time": 0.75})
        self.wait(4)
        triangulo = Triangle().scale(2)

        vertices = triangulo.get_vertex_groups()[0]

        baricentro = [ (vertices[0][0] + vertices[1][0] + vertices[2][0])/3, (vertices[0][1] + vertices[1][1] + vertices[2][1])/3, 0]

        vertices_originais = vertices.copy()
        vertices_originais[0][1] = vertices_originais[0][1]+1.3
        vertices_originais[1][0] = vertices_originais[1][0]-1.0
        vertices_originais[2][0] = vertices_originais[2][0]+1.0

        vertices_rotacionados = vertices.copy()
        vertices_rotacionados[0][1] = vertices_rotacionados[0][1]+0.3
        vertices_rotacionados[1][0] = vertices_rotacionados[1][0]-0.2
        vertices_rotacionados[2][0] = vertices_rotacionados[2][0]+0.3

        labels_originais = VGroup(*[
            Text(label).move_to(point) for label,point in zip(["1","2","3"],vertices_originais)
            ])

        labels_rotacionados = VGroup(*[
            Text(label).move_to(point) for label,point in zip(["1","2","3"],vertices_rotacionados)
            ])

        labels_originais.set_color(RED)

        Triangulo_rotacao = VGroup()
        Triangulo_rotacao.add(triangulo, labels_rotacionados)

        self.play(Write(labels_originais))
        self.play(FadeIn(triangulo))

        # ... some move or rotate mobjects around...
        self.play(Rotate(Triangulo_rotacao, 2*PI/3, about_point = baricentro, rate_func = linear, run_time = 3))

        self.play(Rotate(Triangulo_rotacao[1][0], -2*PI/3), Rotate(Triangulo_rotacao[1][1], -2*PI/3), Rotate(Triangulo_rotacao[1][2], -2*PI/3))

        Triangulo_reflexao = VGroup()
        Triangulo_reflexao.add(triangulo, labels_rotacionados)

        self.wait(4)
        matrix = [[-1, 0], [0, 1]]
        self.play(Triangulo_reflexao.animate.apply_matrix(matrix), run_time=1)
        #self.add(Triangulo_reflexao[1][0].apply_matrix(matrix), Triangulo_reflexao[1][0].move_to(vertices_rotacionados[2]), Triangulo_reflexao[1][1].apply_matrix(matrix), Triangulo_reflexao[1][1].move_to(vertices_rotacionados[1]), Triangulo_reflexao[1][2].apply_matrix(matrix), Triangulo_reflexao[1][2].move_to(vertices_rotacionados[0]))
        self.wait(4)

        finishScene(self)
