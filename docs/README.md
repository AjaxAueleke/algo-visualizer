# docs

This folder holds documentation assets for Algo-Visualizer.

## Adding the demo GIF

The main `README.md` references an animated demo at `docs/demo.gif`:

```markdown
![demo](docs/demo.gif)
```

To record one:

1. Run the visualizer: `python app.py`
2. Press a number key (e.g. `5` for Quick Sort) to start an animation.
3. Capture the window with any screen recorder and export it as a GIF
   (e.g. [Peek](https://github.com/phw/peek) on Linux, or
   [ScreenToGif](https://www.screentogif.com/) on Windows).
4. Save the file here as `demo.gif`.

Once `docs/demo.gif` exists, it will render automatically in the README.
