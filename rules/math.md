# Math & LaTeX

`MathTex` / `Tex` typeset with a real LaTeX installation. **Requires LaTeX** — if not installed, rendering throws (missing `latex`/`dvisvgm`). Plain `Text` needs no LaTeX; use it for non-math text.

## Install LaTeX (only if using MathTex/Tex)

- mac: `brew install --cask mactex-no-gui` (full, large) or `brew install --cask basictex` (small; may need `tlmgr install` for extra packages like `standalone`, `preview`, `dvisvgm`).
- Linux: a TeX dist plus `dvisvgm` (e.g. `apt install texlive texlive-latex-extra dvisvgm`).

Verify: `latex --version` and `dvisvgm --version` resolve.

## MathTex vs Tex

```python
MathTex(r"x^2 + y^2 = r^2")        # math mode (no $...$ needed)
Tex(r"The area is $\pi r^2$")      # text mode; wrap math in $...$
```

Always use **raw strings** (`r"..."`) so backslashes survive: `r"\frac{a}{b}"`, `r"\int_0^1 x\,dx"`, `r"\sqrt{2}"`.

## Substrings & coloring

`MathTex` splits on its arguments — pass multiple strings to address parts:

```python
eq = MathTex("a^2", "+", "b^2", "=", "c^2")
eq[0].set_color(BLUE)          # color a^2
self.play(Write(eq))
self.play(Indicate(eq[4]))     # emphasize c^2
```

`set_color_by_tex(eq, "b", RED)` colors any submobject whose tex contains `"b"`.

## Animating equations

```python
eq1 = MathTex("a + b")
eq2 = MathTex("b + a")
self.play(TransformMatchingTex(eq1, eq2))   # moves shared tokens, morphs the rest
```

Great for step-by-step derivations: render each line as `MathTex`, then `TransformMatchingTex` from one to the next so common terms glide into place.

## Tips

- LaTeX errors usually mean a missing package — read the `.log` path Manim prints; install via `tlmgr install <pkg>` (basictex) or use the full MacTeX.
- For a quick math label without LaTeX, Unicode in `Text` works for simple cases: `Text("x² + y²")`. Use `MathTex` when you need real fractions, integrals, matrices, alignment.
