from manim import *

# 3Blue1Brown-flavored palette
BG = "#0e1117"
P_COLOR = "#3aa9ff"   # true distribution P (blue)
Q_COLOR = "#ffc857"   # model distribution Q (yellow)
ACCENT = "#5eead4"    # teal accent
GOOD = "#7ee787"
BAD = "#ff6b6b"

P_VALS = [0.1, 0.5, 0.3, 0.1]
Q_VALS = [0.25, 0.25, 0.25, 0.25]
NAMES = ["A", "B", "C", "D"]


class KLDivergence(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.title_card()
        self.two_distributions()
        self.surprise()
        self.build_formula()
        self.cross_entropy()
        self.properties()
        self.asymmetry()
        self.outro()

    # --- helpers ---
    def clear_all(self, run_time=0.6):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=run_time)

    def chapter_tag(self, text):
        tag = Text(text, font_size=22, color=GREY_B).to_corner(UL).shift(DOWN * 0.1)
        return tag

    def bar_chart(self, values, color, label, label_color):
        chart = BarChart(
            values=values,
            bar_names=NAMES,
            y_range=[0, 0.6, 0.2],
            y_length=2.6,
            x_length=3.6,
            bar_colors=[color] * 4,
            bar_fill_opacity=0.9,
        )
        cap = Text(label, font_size=26, color=label_color).next_to(chart, UP, buff=0.25)
        return VGroup(chart, cap)

    # --- chapters ---
    def title_card(self):
        title = Text("Kullback–Leibler Divergence", font_size=52, color=WHITE)
        sub = Text("how far is your model Q from the truth P?",
                   font_size=30, color=ACCENT)
        sub.next_to(title, DOWN, buff=0.4)
        sym = MathTex(r"D_{\mathrm{KL}}(", "P", r"\,\|\,", "Q", ")",
                      font_size=64, color=WHITE)
        sym.next_to(sub, DOWN, buff=0.7)
        sym[1].set_color(P_COLOR)
        sym[3].set_color(Q_COLOR)

        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=1.0)
        self.play(Write(sym), run_time=1.2)
        self.wait(1.2)
        self.clear_all()

    def two_distributions(self):
        tag = self.chapter_tag("two distributions")
        self.add(tag)

        p_chart = self.bar_chart(P_VALS, P_COLOR, "true   P", P_COLOR).to_edge(LEFT, buff=1.0)
        q_chart = self.bar_chart(Q_VALS, Q_COLOR, "model   Q", Q_COLOR).to_edge(RIGHT, buff=1.0)

        self.play(FadeIn(p_chart, shift=UP * 0.3), run_time=1.0)
        self.play(FadeIn(q_chart, shift=UP * 0.3), run_time=1.0)
        self.wait(0.5)

        note = Text("Q tries to approximate P — but it's wrong.",
                    font_size=28, color=GREY_A).to_edge(DOWN, buff=0.6)
        self.play(Write(note), run_time=1.2)
        self.wait(1.3)
        self.clear_all()

    def surprise(self):
        tag = self.chapter_tag("information = surprise")
        self.add(tag)

        line = Text("An event of probability q carries", font_size=30, color=GREY_A)
        eq = MathTex(r"\text{surprise} = \log \frac{1}{q} = -\log q",
                     font_size=48, color=WHITE)
        eq.next_to(line, DOWN, buff=0.5)
        VGroup(line, eq).move_to(ORIGIN)

        self.play(Write(line), run_time=1.0)
        self.play(Write(eq), run_time=1.4)
        self.wait(0.6)

        idea = Text("Rare events surprise us more.", font_size=30, color=ACCENT)
        idea.next_to(eq, DOWN, buff=0.7)
        self.play(FadeIn(idea, shift=UP * 0.2), run_time=1.0)
        self.wait(1.4)
        self.clear_all()

    def build_formula(self):
        tag = self.chapter_tag("the definition")
        self.add(tag)

        intro = Text("Expected EXTRA surprise from using Q instead of P:",
                     font_size=28, color=GREY_A).to_edge(UP, buff=1.2)
        self.play(Write(intro), run_time=1.4)

        formula = MathTex(
            r"D_{\mathrm{KL}}(", "P", r"\,\|\,", "Q", ")", "=",
            r"\sum_{x}", "P(x)", r"\,\log", r"\frac{P(x)}{Q(x)}",
            font_size=48,
        )
        formula[1].set_color(P_COLOR)
        formula[3].set_color(Q_COLOR)
        formula[7].set_color(P_COLOR)   # P(x) weight
        formula.move_to(ORIGIN)

        self.play(Write(formula), run_time=2.0)
        self.wait(0.6)

        # reframe as an expectation
        expect = MathTex(
            r"=\; \mathbb{E}_{x \sim P}\!\left[\, \log \frac{P(x)}{Q(x)} \,\right]",
            font_size=52, color=WHITE,
        )
        expect.next_to(formula, DOWN, buff=0.7)
        self.play(FadeIn(expect, shift=UP * 0.2), run_time=1.4)
        self.wait(1.4)
        self.clear_all()

    def cross_entropy(self):
        tag = self.chapter_tag("a cleaner view")
        self.add(tag)

        cross = MathTex(r"H(P, Q) = -\sum_x P(x)\log Q(x)", font_size=44, color=WHITE)
        ent = MathTex(r"H(P) = -\sum_x P(x)\log P(x)", font_size=44, color=WHITE)
        rel = MathTex(r"D_{\mathrm{KL}}(", "P", r"\,\|\,", "Q",
                      r") = H(P, Q) - H(P)", font_size=50, color=WHITE)

        cross.to_edge(UP, buff=1.3)
        ent.next_to(cross, DOWN, buff=0.5)
        rel.next_to(ent, DOWN, buff=0.9)
        rel[1].set_color(P_COLOR)
        rel[3].set_color(Q_COLOR)

        caption = Text("extra bits to encode P using Q's code",
                       font_size=28, color=ACCENT).next_to(rel, DOWN, buff=0.6)

        self.play(Write(cross), run_time=1.3)
        self.play(Write(ent), run_time=1.3)
        self.play(Write(rel), run_time=1.4)
        self.play(FadeIn(caption, shift=UP * 0.2), run_time=1.0)
        self.wait(1.6)
        self.clear_all()

    def properties(self):
        tag = self.chapter_tag("properties")
        self.add(tag)

        p1 = MathTex(r"D_{\mathrm{KL}}(", "P", r"\,\|\,", "Q", r") \;\geq\; 0",
                     font_size=50, color=WHITE)
        p2 = MathTex(r"D_{\mathrm{KL}}(", "P", r"\,\|\,", "Q", r") = 0 \iff P = Q",
                     font_size=46, color=WHITE)
        for m in (p1, p2):
            m[1].set_color(P_COLOR)
            m[3].set_color(Q_COLOR)
        p1.to_edge(UP, buff=1.6)
        p2.next_to(p1, DOWN, buff=0.8)

        gibbs = Text("(Gibbs' inequality — never negative)",
                     font_size=26, color=GREY_B).next_to(p2, DOWN, buff=0.8)

        check = Text("✓", font_size=60, color=GOOD).next_to(p1, RIGHT, buff=0.6)

        self.play(Write(p1), run_time=1.2)
        self.play(FadeIn(check, scale=0.5), run_time=0.6)
        self.play(Write(p2), run_time=1.4)
        self.play(FadeIn(gibbs), run_time=0.9)
        self.wait(1.5)
        self.clear_all()

    def asymmetry(self):
        tag = self.chapter_tag("not a distance")
        self.add(tag)

        neq = MathTex(
            r"D_{\mathrm{KL}}(", "P", r"\,\|\,", "Q", ")",
            r"\;\neq\;",
            r"D_{\mathrm{KL}}(", "Q", r"\,\|\,", "P", ")",
            font_size=52,
        ).to_edge(UP, buff=1.4)
        neq[1].set_color(P_COLOR); neq[3].set_color(Q_COLOR)
        neq[5].set_color(BAD)
        neq[7].set_color(Q_COLOR); neq[9].set_color(P_COLOR)

        # concrete numbers for our P and uniform Q (in bits)
        v1 = MathTex(r"D_{\mathrm{KL}}(P \,\|\, Q) \approx 0.31 \text{ bits}",
                     font_size=40, color=P_COLOR)
        v2 = MathTex(r"D_{\mathrm{KL}}(Q \,\|\, P) \approx 0.35 \text{ bits}",
                     font_size=40, color=Q_COLOR)
        v1.next_to(neq, DOWN, buff=0.9)
        v2.next_to(v1, DOWN, buff=0.5)

        note = Text("order matters — it's a divergence, not a metric",
                    font_size=28, color=GREY_A).next_to(v2, DOWN, buff=0.8)

        self.play(Write(neq), run_time=1.6)
        self.play(FadeIn(v1, shift=RIGHT * 0.3), run_time=0.9)
        self.play(FadeIn(v2, shift=LEFT * 0.3), run_time=0.9)
        self.play(Write(note), run_time=1.2)
        self.wait(1.6)
        self.clear_all()

    def outro(self):
        line1 = Text("KL divergence =", font_size=40, color=WHITE)
        line2 = Text("the extra surprise of believing Q when the truth is P.",
                     font_size=34, color=ACCENT)
        line2.next_to(line1, DOWN, buff=0.4)
        grp = VGroup(line1, line2).move_to(ORIGIN)

        sym = MathTex(r"D_{\mathrm{KL}}(P \,\|\, Q) = \sum_x P(x)\log\frac{P(x)}{Q(x)}",
                      font_size=44, color=WHITE)
        sym.next_to(grp, DOWN, buff=0.9)

        self.play(Write(line1), run_time=1.0)
        self.play(FadeIn(line2, shift=UP * 0.2), run_time=1.0)
        self.play(Write(sym), run_time=1.6)
        self.wait(2.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.2)
