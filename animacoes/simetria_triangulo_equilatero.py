from manim import *

def finishScene(self):
    self.play(*[FadeOut(mob) for mob in self.mobjects])

class Start(Scene):
    def construct(self):
        f = Matrix(
            [("1", "2", "3"), ("3", "1", "2")], left_bracket="(",
            right_bracket=")")

        f_flat = VGroup(*VGroup(*f)[0])
        texto = Tex(r"f\ =\ ")

        f.to_corner(corner=UP + LEFT*3, buff=0.5)

        texto.next_to(f, LEFT)
        self.play(Write(texto))
        for i in VGroup(*f)[1:]:
            self.play(Write(i))

        for i in range(0,6):
            self.play(Write(f_flat[i]), **{"run_time": 0.75})
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
        Triangulo_rotacao.add(triangulo.copy(), labels_rotacionados.copy())

        self.play(Write(labels_originais))
        self.play(FadeIn(Triangulo_rotacao[0]))

        # ... some move or rotate mobjects around...
        self.play(Rotate(Triangulo_rotacao, 2*PI/3, about_point = baricentro, rate_func = linear, run_time = 3))

        self.play(Rotate(Triangulo_rotacao[1][0], -2*PI/3), Rotate(Triangulo_rotacao[1][1], -2*PI/3), Rotate(Triangulo_rotacao[1][2], -2*PI/3))

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        g = Matrix(
            [("1", "2", "3"), ("1", "3", "2")], left_bracket="(",
            right_bracket=")")

        g_flat = VGroup(*VGroup(*g)[0])

        texto_g = Tex(r"g\ =\ ")

        g.to_corner(corner=UP + LEFT*3, buff=0.5)

        texto_g.next_to(g, LEFT)
        self.play(Write(texto_g))
        for i in VGroup(*g)[1:]:
            self.play(Write(i))

        for i in range(0,6):
            self.play(Write(g_flat[i]), **{"run_time": 0.75})

        self.play(Write(labels_originais))

        self.play(FadeIn(triangulo))

        Triangulo_reflexao = VGroup()

        Triangulo_reflexao.add(triangulo, labels_rotacionados)
        matrix = [[-1, 0], [0, 1]]

        self.play(Triangulo_reflexao.animate.apply_matrix(matrix), run_time=1)

        self.add(Triangulo_reflexao[1][0].apply_matrix(matrix), Triangulo_reflexao[1][0].move_to(vertices_rotacionados[0]), Triangulo_reflexao[1][1].apply_matrix(matrix), Triangulo_reflexao[1][1].move_to(vertices_rotacionados[2]), Triangulo_reflexao[1][2].apply_matrix(matrix), Triangulo_reflexao[1][2].move_to(vertices_rotacionados[1]))

        self.wait(4)

        finishScene(self)
