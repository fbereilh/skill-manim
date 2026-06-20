# manim-best-practices

A [Claude Code](https://claude.com/claude-code) **agent skill** for writing and rendering [Manim](https://www.manim.community/) animations: programmatic, 3Blue1Brown-style math and explainer videos in Python.

It hands Claude the ManimCommunity reference it needs: scene anatomy, mobjects and layout, animations, easing and timing, rendering, LaTeX math, plots and axes, updaters, and camera/3D. You bring your own `manim`. The skill assumes the CLI sits on your `PATH` and never tells you how to install it.

## What's inside

```
SKILL.md            # entry point: requirements, scene anatomy, render loop, links to rules
rules/              # focused, load-on-demand reference
  animations.md       play()/.animate, transforms, LaggedStart
  mobjects.md         shapes, styling, positioning, VGroup
  timing.md           run_time, rate_func easing, sequencing
  render.md           quality flags, stills, gif/transparent, environment wrappers
  text.md             Text vs MarkupText vs MathTex, fonts
  math.md             MathTex/Tex + LaTeX notes
  graphs.md           Axes, plot, NumberPlane (the 3b1b core)
  updaters.md         ValueTracker / always_redraw (per-frame logic)
  camera.md           MovingCamera, ThreeDScene
```

## Install

Clone it into your skills directory. Name the folder to match the skill's `name` (`manim-best-practices`):

```bash
# user-level (all projects)
git clone https://github.com/fbereilh/manim-skill ~/.claude/skills/manim-best-practices

# or project-level
git clone https://github.com/fbereilh/manim-skill .claude/skills/manim-best-practices
```

Claude reads `SKILL.md` and loads the matching `rules/*.md` when it needs them. Ask it to "make a Manim video of …" and it follows the skill.

## Requirements

Put the `manim` CLI (ManimCommunity) and `ffmpeg` on your `PATH`. Add LaTeX only if you render equations (`MathTex` / `Tex`). Any install method works: conda/pixi, Nix/devbox, the `manimcommunity/manim` Docker image, or pip in a venv. `SKILL.md` → *Requirements* has the specifics.

## License

MIT, see [LICENSE](LICENSE).
