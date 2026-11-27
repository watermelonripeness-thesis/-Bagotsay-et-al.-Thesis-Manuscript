import sys
from pathlib import Path

src = Path(sys.argv[1])
text = src.read_text(encoding="utf-8")

FIXES = [
    ("\\setcounter{subsection}{8}\n", ""),
    ("since each contained a detectable thump response, as described in Section 3.6.3.",
     "since each contained a detectable thump response, as described in Section 3.6.2."),
    ("including the augmented copies described in Section 3.6.3, and applied to the test set",
     "including the augmented copies described in Section 3.6.4, and applied to the test set"),
    ("The classifiers were trained on the 31 acoustic features described in Section 3.6.1,",
     "The classifiers were trained on the 31 acoustic features described in Section 3.6.2,"),
    ("computed from the training set, including the augmented copies described in Section 3.6.2.",
     "computed from the training set, including the augmented copies described in Section 3.6.4."),
    ("drawn only from the test recordings (Section 3.6.2)",
     "drawn only from the test recordings (Section 3.6.4)"),
    ("given the difference in background noise identified in Section 3.6.2.",
     "given the difference in background noise identified in Section 3.6.4."),
    ("calculated before partitioning, as described in Section 3.6.2.",
     "calculated before partitioning, as described in Section 3.6.3."),
    ("The eight image architectures described in Section 3.7.2.1",
     "The eight image architectures described in Section 3.7.1.2"),
    ("as outlined in Table 20, including",
     "as outlined in Table~\\ref{tab:testing-metrics-for-system-integration-589}, including"),
]

for old, new in FIXES:
    if text.count(old) != 1:
        print("SKIP", old[:70])
        continue
    text = text.replace(old, new)
    print("OK  ", old[:70])

out = src.with_name(src.stem + "_fixed" + src.suffix)
out.write_text(text, encoding="utf-8")
print(out)
