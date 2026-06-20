# Rendering

```bash
manim [flags] file.py SceneName
```

Renders the named scene class. Output: `media/videos/<file>/<resolution>/SceneName.mp4`.

## Quality flags

| Flag | Resolution / fps | Use |
|------|------------------|-----|
| `-ql` | 480p15 | fast iteration while building |
| `-qm` | 720p30 | review |
| `-qh` | 1080p60 | final |
| `-qk` | 4K60 | export |

## Common flags

- `-p` — preview: open the output when done
- `-s` — render only the **last frame** to PNG (fast layout/color check, skips the timeline)
- `--format gif` — output GIF instead of mp4 (`--format webm`, `mov` also valid; `mov` + transparency below)
- `-a` — render every scene in the file
- `-o NAME` — set output filename
- `-n K` — start from animation index K (skip ahead while iterating)
- `-r W,H` — custom resolution, e.g. `-r 1080,1920` for vertical/portrait
- `--fps 30` — override fps
- `--disable_caching` — force re-render (Manim caches partial movies; usually leave on)

## Iteration loop (no live studio)

Manim has no preview studio. Fastest loops:
1. `manim -s file.py SceneName` → inspect the last-frame PNG for layout/colors.
2. `manim -ql file.py SceneName` → watch motion at low res.
3. Bump to `-qh` only for the final render.

If you only changed the end, `-s` checks it instantly. Use `-n <index>` to jump to a later animation without replaying earlier ones.

## Transparency

```bash
manim -qh --format mov --transparent file.py SceneName   # alpha channel (ProRes 4444)
manim -qh --format webm --transparent file.py SceneName  # alpha (smaller)
```

Use a transparent render to overlay the animation on other footage.

## Portrait / social

```bash
manim -qh -r 1080,1920 file.py SceneName   # 9:16 vertical
```

Set `config.frame_width`/`frame_height` in-scene if you need the coordinate frame to match the aspect.

## Running via devbox

If the project is set up with devbox (recommended — see SKILL.md), prefix render commands with `devbox run --`, e.g. `devbox run -- manim -ql scene.py SceneName`, or enter `devbox shell` once and run `manim ...` directly. Avoid `bash -lc` wrappers — a login shell can change the working directory and manim won't find the scene file.

## ffmpeg

Manim shells out to the `ffmpeg` binary on PATH to encode. With devbox, ffmpeg comes from the Nix env automatically. With the uv + `imageio-ffmpeg` route, make sure the `.venv/bin/ffmpeg` symlink exists and the venv is on PATH. Error `FileNotFoundError: ffmpeg` means it isn't found.
