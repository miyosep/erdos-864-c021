# Earlier material

Earlier drafts and full execution records remain in Git history. They are
not prerequisites for reading [the paper](paper/main.pdf) or running
[the public checks](REPRODUCING.md).

| Historical material | Immutable snapshot |
| --- | --- |
| Initial separated-reflection C021 note and equations | [Original note](https://github.com/miyosep/erdos-864-c021/blob/eca15a265f77e8fd875d4559bbbd0e21582c8405/archive/c021-original/C021_REVIEW_NOTE.md) |
| Original review ZIP | [C021 packet](https://github.com/miyosep/erdos-864-c021/blob/eca15a265f77e8fd875d4559bbbd0e21582c8405/archive/c021-original/C021_review_packet.zip) |
| Preliminary proofs, editorial notes and manifests | [Workspace archive](https://github.com/miyosep/erdos-864-c021/tree/eca15a265f77e8fd875d4559bbbd0e21582c8405/archive/workspace) |
| Old outputs, receipts and exact code/input snapshots | [Historical runs](https://github.com/miyosep/erdos-864-c021/tree/eca15a265f77e8fd875d4559bbbd0e21582c8405/evidence/runs) |
| Complete file relocation map | [Relocation record](https://github.com/miyosep/erdos-864-c021/blob/eca15a265f77e8fd875d4559bbbd0e21582c8405/evidence/RELOCATION.json) |

For a local copy of that historical layout:

```text
git clone https://github.com/miyosep/erdos-864-c021.git erdos-864-history
git -C erdos-864-history checkout eca15a265f77e8fd875d4559bbbd0e21582c8405
```

The initial C021 result has a narrower separated-reflection scope. Historical
status labels do not replace checking current theorem statements or provide
independent correctness certification. The [retention review](review/REPOSITORY_REVIEW.md)
explains why the current checkout keeps only reader and reproduction needs.
