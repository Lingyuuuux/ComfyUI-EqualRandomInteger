# ComfyUI Equal Random Integer

This custom node returns one uniformly selected integer from an inclusive range.

For example, if `minimum` is `0` and `maximum` is `4`, the possible outputs are
`0`, `1`, `2`, `3`, and `4`. Each value is selected with the same probability.

## Install

Copy the `ComfyUI-EqualRandomInteger` folder into:

```text
ComfyUI/custom_nodes/
```

Then restart ComfyUI.

## Use

In ComfyUI, add:

```text
jieidan/random/Equal Random Integer
```

Inputs:

- `minimum`: inclusive lower bound.
- `maximum`: inclusive upper bound.

Output:

- `value`: one integer selected from `[minimum, maximum]`.

The node uses Python's `secrets.randbelow()` to avoid modulo bias, and it is
marked as changed on every queue run so ComfyUI does not reuse a cached random
value.
