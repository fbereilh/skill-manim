# Text & fonts

Three text mobjects — pick by need:

| Class | Engine | LaTeX? | Use for |
|-------|--------|--------|---------|
| `Text` | Pango | no | UI text, labels, titles — system fonts, emoji, CJK |
| `MarkupText` | Pango + markup | no | inline styling via PangoMarkup spans |
| `Tex` / `MathTex` | LaTeX | **yes** | typeset math & equations (see math.md) |

Prefer `Text` unless you need typeset math — it has no LaTeX dependency.

## Text

```python
Text("Hello", font_size=48, color=WHITE, weight=BOLD, font="Helvetica")
```

- `font_size` in points (default 48). `weight`: `NORMAL`, `BOLD`, etc.
- `font=` any installed system font name. `slant=ITALIC` for italics.
- Color parts with `t2c` (text-to-color), bold parts with `t2w`, slant with `t2s`:

```python
Text("speed = distance / time", t2c={"speed": YELLOW, "distance": BLUE, "time": GREEN})
```

- `line_spacing=`, and pass a string with `\n` for multiple lines.
- Animate with `Write(t)` (handwriting) or `FadeIn(t)`. `AddTextLetterByLetter(t)` types it out.

## MarkupText

```python
MarkupText('normal <span foreground="yellow">highlighted</span> <b>bold</b>')
```

PangoMarkup: `<b>`, `<i>`, `<u>`, `<span foreground="...">`, `<s>` strikethrough. Good for mixed inline styling without splitting into multiple mobjects.

## Fonts & emoji

`Text` uses Pango, so any installed system font works via `font=`. Color emoji rendering depends on an installed color-emoji font and is unreliable across platforms — prefer building icons from shapes (`VGroup` of primitives) when you need guaranteed output. For monochrome symbol glyphs (`♥`, `★`, arrows) `Text("♥")` is reliable.

## Positioning text

Same as any mobject: `.to_edge(UP)`, `.next_to(obj, DOWN)`, `.move_to(...)`. To label another mobject use `Text(...).next_to(obj, UP, buff=0.2)`, or for graphs use `Axes.get_graph_label` (see graphs.md).
