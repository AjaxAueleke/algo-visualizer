"""Headless correctness harness for the sorts in app.py.

Each visualizer sort is run against a freshly shuffled list using pygame's
dummy SDL drivers (so no window/audio device is required) and the result is
asserted to be fully sorted. This is the regression proof for the radix and
counting sort fixes in particular.

Run from anywhere:  python examples/verify_sorts.py
Exit code is non-zero if any sort fails.
"""
import os
import random
import sys

# Use pygame's headless drivers so this runs without a display or audio device.
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

# Make the repo root importable regardless of the current working directory.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import app  # noqa: E402  (import only after env + sys.path are set up)

PADDING = 1
SCREEN_WIDTH = 6
X = 1

SORTS = {
    "bubble_sort": app.bubble_sort,
    "insertion_sort": app.insertion_sort,
    "merge_sort": app.merge_sort,
    "heap_sort": app.heap_sort,
    "quick_sort": app.quick_sort,
    "counting_sort": app.counting_sort,
    "radix_sort": app.radix_sort,
}


def main():
    random.seed(1234)
    failures = []
    for name, fn in SORTS.items():
        data = random.sample(range(200), 30)  # distinct, 1-3 digit values
        expected = sorted(data)
        fn(data, app.screen, PADDING, SCREEN_WIDTH, X)
        ok = data == expected
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        if not ok:
            failures.append(name)
            print(f"    expected: {expected}")
            print(f"    got:      {data}")

    app.pygame.quit()
    if failures:
        print(f"\n{len(failures)} sort(s) FAILED: {', '.join(failures)}")
        sys.exit(1)
    print(f"\nAll {len(SORTS)} sorts produced correctly sorted output.")


if __name__ == "__main__":
    main()
