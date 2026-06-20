# manim-best-practices

A [Claude Code](https://claude.com/claude-code) **agent skill** that teaches Claude to write and render [Manim](https://www.manim.community/) animations: programmatic, 3Blue1Brown-style math and explainer videos in Python.

The skill gives Claude domain knowledge for ManimCommunity: scene anatomy, mobjects and layout, animations, easing and timing, rendering, LaTeX math, plots and axes, updaters, and camera/3D. It is install-agnostic. It assumes the `manim` CLI is on your `PATH` and never prescribes how you got it.

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

Clone into your skills directory so Claude picks it up. The folder name should match the skill's `name` (`manim-best-practices`):

```bash
# user-level (all projects)
git clone https://github.com/fbereilh/manim-skill ~/.claude/skills/manim-best-practices

# or project-level
git clone https://github.com/fbereilh/manim-skill .claude/skills/manim-best-practices
```

Claude reads `SKILL.md` and pulls in the relevant `rules/*.md` on demand. Ask Claude to "make a Manim video of …" and it applies the skill.

## Requirements

You need the `manim` CLI (ManimCommunity) on your `PATH`, plus `ffmpeg`. LaTeX is optional and only needed for typeset equations (`MathTex` / `Tex`). The skill works with any install method: conda/pixi, Nix/devbox, the `manimcommunity/manim` Docker image, or pip into a venv. See `SKILL.md` → *Requirements* for details.

## License

MIT, see [LICENSE](LICENSE).
