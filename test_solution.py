"""Test script for HENNGE challenge main.py - runs using subprocess to properly test stdin/stdout"""
import subprocess
import sys
import os

def run_test(name, input_str, expected):
    """Run main.py with given input and check output."""
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

# Test 1: Sample input from challenge
# Case 1: X=4, Yn=[3,-1,1,10] -> non-positive: -1 -> (-1)^4 = 1
# Case 2: X=5, Yn=[9,-5,-5,-10,10] -> non-positive: -5,-5,-10 -> 625+625+10000 = 11250
all_pass &= run_test(
    "Sample input from challenge",
    "2\n4\n3 -1 1 10\n5\n9 -5 -5 -10 10\n",
    "1\n11250"
)

# Test 2: All positive (sum should be 0)
all_pass &= run_test(
    "All positive numbers",
    "1\n3\n1 2 3\n",
    "0"
)

# Test 3: All negative
# -2, -3 -> 16 + 81 = 97
all_pass &= run_test(
    "All negative numbers",
    "1\n2\n-2 -3\n",
    "97"
)

# Test 4: Zero included (zero is non-positive, so included; 0^4 = 0)
# 0, -1 -> 0 + 1 = 1
all_pass &= run_test(
    "Zero included",
    "1\n2\n0 -1\n",
    "1"
)

# Test 5: X mismatch (X=3, only 2 numbers) -> -1
all_pass &= run_test(
    "X mismatch - fewer numbers",
    "1\n3\n1 2\n",
    "-1"
)

# Test 6: X mismatch (X=2, but 3 numbers) -> -1
all_pass &= run_test(
    "X mismatch - more numbers",
    "1\n2\n1 2 3\n",
    "-1"
)

# Test 7: Single large negative
# -100 -> 100^4 = 100000000
all_pass &= run_test(
    "Single large negative",
    "1\n1\n-100\n",
    "100000000"
)

# Test 8: Single positive
all_pass &= run_test(
    "Single positive",
    "1\n1\n5\n",
    "0"
)

# Test 9: Single zero
all_pass &= run_test(
    "Single zero",
    "1\n1\n0\n",
    "0"
)

# Test 10: Multiple test cases
# Case 1: -1, -2 -> 1+16 = 17
# Case 2: 1, 2, 3 -> 0
# Case 3: -3 -> 81
all_pass &= run_test(
    "Multiple mixed test cases",
    "3\n2\n-1 -2\n3\n1 2 3\n1\n-3\n",
    "17\n0\n81"
)

# Test 11: All zeros
# 0, 0, 0 -> 0+0+0 = 0
all_pass &= run_test(
    "All zeros",
    "1\n3\n0 0 0\n",
    "0"
)

# Test 12: Mix of zero and negatives
# 0, -1, 0, -2 -> 0+1+0+16 = 17
all_pass &= run_test(
    "Mix of zeros and negatives",
    "1\n4\n0 -1 0 -2\n",
    "17"
)

# Test 13: N=1, X=1, with single negative
all_pass &= run_test(
    "Single case single number",
    "1\n1\n-1\n",
    "1"
)

# Test 14: Testing with X mismatch in one of multiple cases
# Case 1: valid -> 1
# Case 2: X=3 but 2 numbers -> -1
all_pass &= run_test(
    "Mismatch in middle of multiple cases",
    "2\n1\n-1\n3\n1 2\n",
    "1\n-1"
)

print()
if all_pass:
    print("=" * 40)
    print("ALL TESTS PASSED! Solution is correct.")
    print("=" * 40)
else:
    print("=" * 40)
    print("SOME TESTS FAILED! Review needed.")
    print("=" * 40)
