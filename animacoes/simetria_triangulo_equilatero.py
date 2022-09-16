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

        self.wait(2)

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

        self.play(FadeIn(Triangulo_rotacao[0]))

        self.wait(3)

        self.play(Write(labels_originais))

        self.wait(2)

        self.play(Rotate(Triangulo_rotacao, 2*PI/3, about_point = baricentro, rate_func = linear, run_time = 3))

        self.play(Rotate(Triangulo_rotacao[1][0], -2*PI/3), Rotate(Triangulo_rotacao[1][1], -2*PI/3), Rotate(Triangulo_rotacao[1][2], -2*PI/3))

        self.wait(3)

        self.play(FadeOut(Triangulo_rotacao[1]), FadeOut(labels_originais))

        self.wait(2)

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

        Triangulo_reflexao = VGroup()

        Triangulo_reflexao.add(triangulo.copy(), labels_rotacionados.copy())

        self.play(FadeIn(Triangulo_reflexao[0]))

        self.wait(2)

        self.play(Write(labels_originais))

        self.wait(2)

        matrix = [[-1, 0], [0, 1]]

        self.play(Triangulo_reflexao.animate.apply_matrix(matrix), run_time=1)

        self.add(Triangulo_reflexao[1][0].apply_matrix(matrix), Triangulo_reflexao[1][0].move_to(vertices_rotacionados[0]), Triangulo_reflexao[1][1].apply_matrix(matrix), Triangulo_reflexao[1][1].move_to(vertices_rotacionados[2]), Triangulo_reflexao[1][2].apply_matrix(matrix), Triangulo_reflexao[1][2].move_to(vertices_rotacionados[1]))

        self.wait(2)

        self.play(FadeOut(Triangulo_reflexao[1]), FadeOut(labels_originais))

        self.wait(2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        composicao = Tex(r"$g \circ f\ =\ $")

        g.to_corner(corner=UP + LEFT*5, buff=0.5)

        f.next_to(g, RIGHT)

        composicao.next_to(g, LEFT)

        self.play(Write(composicao))

        for i in VGroup(*g)[1:]:
            self.play(Write(i))

        for i in range(0,6):
            self.play(Write(g_flat[i]), **{"run_time": 0.75})

        for i in VGroup(*f)[1:]:
            self.play(Write(i))

        for i in range(0,6):
            self.play(Write(f_flat[i]), **{"run_time": 0.75})


        self.wait(2)

        Triangulo_composicao = VGroup()

        triangulo_composicao = triangulo.to_corner(DOWN*2 + RIGHT*11)

        vertices_composicao = triangulo_composicao.get_vertex_groups()[0]

        baricentro = [ (vertices_composicao[0][0] + vertices_composicao[1][0] + vertices_composicao[2][0])/3, (vertices_composicao[0][1] +
            vertices_composicao[1][1] + vertices_composicao[2][1])/3, 0]

        vertices_originais_composicao = vertices_composicao.copy()

        vertices_originais_composicao[0][1] = vertices_originais_composicao[0][1]+1
        vertices_originais_composicao[1][0] = vertices_originais_composicao[1][0]-0.8
        vertices_originais_composicao[2][0] = vertices_originais_composicao[2][0]+0.9

        vertices_rotacionados_composicao = vertices_composicao.copy()

        vertices_rotacionados_composicao[0][1] = vertices_rotacionados_composicao[0][1]+0.3
        vertices_rotacionados_composicao[1][0] = vertices_rotacionados_composicao[1][0]-0.1
        vertices_rotacionados_composicao[2][0] = vertices_rotacionados_composicao[2][0]+0.5

        labels_originais_composicao = VGroup(*[
            Text(label).move_to(point) for label,point in zip(["1","2","3"],vertices_originais_composicao)
            ])

        labels_rotacionados_composicao = VGroup(*[
            Text(label).move_to(point) for label,point in zip(["1","2","3"],vertices_rotacionados_composicao)
            ])

        labels_originais_composicao.set_color(RED)

        Triangulo_composicao.add(triangulo_composicao.copy(), labels_rotacionados_composicao.copy())

        self.play(FadeIn(Triangulo_composicao[0]))

        self.wait(2)

        self.play(Rotate(Triangulo_composicao, 2*PI/3, about_point = baricentro, rate_func = linear, run_time = 3))

        self.play(Rotate(Triangulo_composicao[1][0], -2*PI/3), Rotate(Triangulo_composicao[1][1], -2*PI/3), Rotate(Triangulo_composicao[1][2], -2*PI/3))

        self.wait(2)

        matrix = [[-1, 0], [0, 1]]

        self.play(Triangulo_composicao.animate.apply_matrix(matrix), run_time=1)

        self.add(Triangulo_composicao[1][0].apply_matrix(matrix), Triangulo_composicao[1][0].move_to(vertices_rotacionados_composicao[2]),Triangulo_composicao[1][1].apply_matrix(matrix), Triangulo_composicao[1][1].move_to(vertices_rotacionados_composicao[1]), Triangulo_composicao[1][2].apply_matrix(matrix), Triangulo_composicao[1][2].move_to(vertices_rotacionados_composicao[0]))

        self.wait(5)

        finishScene(self)
