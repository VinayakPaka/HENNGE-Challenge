"""
Comprehensive test suite for HENNGE Challenge main.py
Tests: sample input, edge cases, boundary values, mismatch handling
"""
import subprocess
import sys

def run_test(name, input_str, expected_output):
    """Run main.py with given input and compare output."""
    result = subprocess.run(
        [sys.executable, "main.py"],
        input=input_str,
        capture_output=True,
        text=True,
        cwd=r"c:\Users\Vinayak Paka\Documents\HENNGE challenge",
        timeout=10
    )
    actual = result.stdout.strip()
    expected = expected_output.strip()
    status = "PASS" if actual == expected else "FAIL"
    print(f"[{status}] {name}")
    if status == "FAIL":
        print(f"  Expected: {repr(expected)}")
        print(f"  Actual:   {repr(actual)}")
        if result.stderr:
            print(f"  Stderr:   {result.stderr.strip()}")
    return status == "PASS"

passed = 0
total = 0

# ==================== TEST CASES ====================

# 1. Sample input from the challenge
total += 1
if run_test("Sample Input", "2\n4\n3 -1 1 10\n5\n9 -5 -5 -10 10\n", "1\n11250"):
    passed += 1

# 2. All zeros
# 0^4 = 0, sum = 0
total += 1
if run_test("All Zeros", "1\n3\n0 0 0\n", "0"):
    passed += 1

# 3. All positive — all excluded, sum = 0
total += 1
if run_test("All Positive", "1\n4\n1 2 3 4\n", "0"):
    passed += 1

# 4. All negative
# (-1)^4 + (-2)^4 + (-3)^4 = 1 + 16 + 81 = 98
total += 1
if run_test("All Negative", "1\n3\n-1 -2 -3\n", "98"):
    passed += 1

# 5. Single element positive
total += 1
if run_test("Single Positive", "1\n1\n5\n", "0"):
    passed += 1

# 6. Single element negative
# (-5)^4 = 625
total += 1
if run_test("Single Negative", "1\n1\n-5\n", "625"):
    passed += 1

# 7. Single element zero
# 0^4 = 0
total += 1
if run_test("Single Zero", "1\n1\n0\n", "0"):
    passed += 1

# 8. Mix of positives, negatives, zeros
# negatives/zero: -3, 0 => (-3)^4 + 0^4 = 81 + 0 = 81
total += 1
if run_test("Mixed Values", "1\n5\n-3 2 0 7 -1\n", "82"):
    passed += 1

# 9. X mismatch — more numbers than X
total += 1
if run_test("Mismatch: More Numbers", "1\n2\n1 2 3\n", "-1"):
    passed += 1

# 10. X mismatch — fewer numbers than X
total += 1
if run_test("Mismatch: Fewer Numbers", "1\n5\n1 2 3\n", "-1"):
    passed += 1

# 11. Boundary: Yn = -100
# (-100)^4 = 100000000
total += 1
if run_test("Boundary Yn=-100", "1\n1\n-100\n", "100000000"):
    passed += 1

# 12. Boundary: Yn = 100 (positive, excluded)
total += 1
if run_test("Boundary Yn=100", "1\n1\n100\n", "0"):
    passed += 1

# 13. Multiple test cases
# Case 1: 1 number: -2 => 16
# Case 2: 2 numbers: 3 -4 => (-4)^4 = 256
# Case 3: 3 numbers: 0 0 0 => 0
total += 1
if run_test("Multiple Cases", "3\n1\n-2\n2\n3 -4\n3\n0 0 0\n", "16\n256\n0"):
    passed += 1

# 14. N=1 with X=1
total += 1
if run_test("N=1 X=1", "1\n1\n-1\n", "1"):
    passed += 1

# 15. Large boundary values
# 3 negatives at max: (-100)^4 * 3 = 300000000 (within int32)
total += 1
if run_test("Large Sum (3x -100)", "1\n3\n-100 -100 -100\n", "300000000"):
    passed += 1

# 16. X=0 mismatch with actual numbers
# X says 0 numbers but there's actually a line
# Actually with X=0, the line of numbers would be empty
# read_line would read the next valid line which would be the next test case
# Let's be careful: with X=0, nums_line split should give 0 elements
# But if X=0 and nums_line is empty, split gives [], len 0 == X -> sum = 0
# Actually with read_line skipping blank lines, this is complex
# Let me test X=0 scenario explicitly
# Wait - the constraint says 0 < X <= 100, so X >= 1. X=0 is not a valid input per spec.
# Skip this test.

# 17. Mismatch in one of multiple cases
# Case 1: valid, Case 2: mismatch
# (-1)^4 = 1, then X=3 with only 2 nums = -1
total += 1
if run_test("Mismatch in Multi-Case", "2\n1\n-1\n3\n1 2\n", "1\n-1"):
    passed += 1

# 18. All values are 1 (positive, all excluded)
total += 1
if run_test("All Ones", "1\n5\n1 1 1 1 1\n", "0"):
    passed += 1

# 19. All values are -1
# 5 * (-1)^4 = 5
total += 1
if run_test("All -1s", "1\n5\n-1 -1 -1 -1 -1\n", "5"):
    passed += 1

# 20. Large N with small cases
input_str = "5\n"
expected_lines = []
# Case 1: -1 => 1
input_str += "1\n-1\n"
expected_lines.append("1")
# Case 2: 2 => 2^4 + 3^4 = 16+81 (but both positive, excluded) = 0
input_str += "2\n2 3\n"
expected_lines.append("0")
# Case 3: -10 => 10000
input_str += "1\n-10\n"
expected_lines.append("10000")
# Case 4: 0 => 0
input_str += "1\n0\n"
expected_lines.append("0")
# Case 5: mismatch
input_str += "3\n1 2\n"
expected_lines.append("-1")

total += 1
if run_test("Five Cases Mixed", input_str, "\n".join(expected_lines)):
    passed += 1

# 21. Verify: the problem says "excluding when Yn is positive"
# So we include negative AND zero. Let's double-check zero handling.
# 0^4 = 0, so it doesn't change the sum but should be included.
# Test: -2 and 0 => (-2)^4 + 0^4 = 16 + 0 = 16
total += 1
if run_test("Zero Included in Calc", "1\n2\n-2 0\n", "16"):
    passed += 1

# ==================== SUMMARY ====================
print(f"\n{'='*40}")
print(f"Results: {passed}/{total} tests passed")
if passed == total:
    print("ALL TESTS PASSED!")
else:
    print(f"FAILED: {total - passed} test(s)")
