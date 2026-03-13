"""Extra edge case tests for HENNGE challenge main.py"""
import subprocess
import sys
import os

def run_test(name, input_str, expected):
    result = subprocess.run(
        [sys.executable, "main.py"],
        input=input_str,
        capture_output=True,
        text=True,
        cwd=os.path.dirname(os.path.abspath(__file__))
    )
    actual = result.stdout.strip()
    passed = actual == expected
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")
    if not passed:
        print(f"  Expected: {expected!r}")
        print(f"  Got:      {actual!r}")
        if result.stderr:
            print(f"  Stderr:   {result.stderr.strip()}")
    return passed

all_pass = True

# Test 1: N=1 minimum, X=1 minimum, Yn at boundary -100
# (-100)^4 = 100000000
all_pass &= run_test(
    "Boundary: Yn = -100",
    "1\n1\n-100\n",
    "100000000"
)

# Test 2: Yn at boundary 100 (positive, excluded)
all_pass &= run_test(
    "Boundary: Yn = 100 (positive, excluded)",
    "1\n1\n100\n",
    "0"
)

# Test 3: X=100 (max) with all negatives -1
# 100 * (-1)^4 = 100 * 1 = 100
nums = " ".join(["-1"] * 100)
all_pass &= run_test(
    "X=100 all -1s",
    f"1\n100\n{nums}\n",
    "100"
)

# Test 4: X=100 with all zeros
nums_z = " ".join(["0"] * 100)
all_pass &= run_test(
    "X=100 all zeros",
    f"1\n100\n{nums_z}\n",
    "0"
)

# Test 5: N=100 test cases, each with X=1 and Yn=-1
# Each case -> 1, total output: 100 lines of "1"
cases = ""
expected_lines = []
n = 100
cases_str = f"{n}\n"
idx = 0
while idx < n:
    cases_str += "1\n-1\n"
    expected_lines.append("1")
    idx += 1
all_pass &= run_test(
    "N=100, each X=1 Yn=-1",
    cases_str,
    "\n".join(expected_lines)
)

# Test 6: Mixed boundary values in one case
# Yn = [-100, -50, 0, 50, 100]
# Non-positive: -100, -50, 0
# (-100)^4 + (-50)^4 + 0^4 = 100000000 + 6250000 + 0 = 106250000
all_pass &= run_test(
    "Mixed boundary values",
    "1\n5\n-100 -50 0 50 100\n",
    "106250000"
)

# Test 7: X=0 should be invalid (0 < X <= 100 constraint, but let's see)
# X=0 means the next line should have 0 numbers.
# If next line is empty, split gives [], len([]) == 0 == X -> result 0
# But actually X=0 violates the constraint 0 < X. The problem states
# 0 < X <= 100, so X=0 shouldn't appear. Let's skip this.

# Test 8: Mismatch where X=5 but only 1 number given
all_pass &= run_test(
    "X mismatch: X=5, 1 number",
    "1\n5\n42\n",
    "-1"
)

# Test 9: All same negative number
# 5 copies of -3: 5 * 81 = 405
all_pass &= run_test(
    "All same negative -3",
    "1\n5\n-3 -3 -3 -3 -3\n",
    "405"
)

# Test 10: Multiple mismatch cases
# Case 1: X=2, 3 nums -> -1
# Case 2: X=3, 2 nums -> -1
# Case 3: valid -> 1
all_pass &= run_test(
    "Multiple mismatches then valid",
    "3\n2\n1 2 3\n3\n1 2\n1\n-1\n",
    "-1\n-1\n1"
)

# Test 11: Negative zero edge (just "0" and "-0" aren't different in Python, but test -0 input)
# int("-0") == 0 in Python, so 0^4 = 0
all_pass &= run_test(
    "Negative zero parsing",
    "1\n1\n-0\n",
    "0"
)

# Test 12: int32 range check - maximum possible sum
# Worst case: 100 values of -100. Each (-100)^4 = 10^8. 100 * 10^8 = 10^10.
# But problem says "final output is guaranteed to be within int32 range"
# so this case wouldn't appear. Let's test a sum near int32 max (2147483647)
# Actually, let's just make sure it handles large sums correctly
# 21 copies of -7: (-7)^4 = 2401, 21*2401 = 50421
all_pass &= run_test(
    "21 copies of -7",
    "1\n21\n" + " ".join(["-7"] * 21) + "\n",
    "50421"
)

print()
if all_pass:
    print("=" * 50)
    print("ALL EXTRA EDGE CASE TESTS PASSED!")
    print("=" * 50)
else:
    print("=" * 50)
    print("SOME TESTS FAILED! Review needed.")
    print("=" * 50)
