# Lab 7: Fuzz Testing & Input Validation Bug Discovery

**Course:** Software Engineering (UE24CS341A)  
**Institution:** PES University, Bengaluru  
**Student:** Amith Prasad | **Roll No:** 33 (`PES1UG24AM033`)  
**Base Repository:** `SETAPESU26/L6_L7_33_spam_scoring/lab7`  

---

## 1. Objective
- Understand fuzz testing and property-based automated testing using **Hypothesis**.
- Generate millions of semi-random, malformed, and adversarial inputs to discover crashing bugs.
- Perform root cause analysis on counterexamples found during fuzzing.
- Implement robust defensive programming fixes (guard clauses, exception boundaries, type checks) and verify that all hypothesis fuzz tests pass.

---

## 2. Target Functions Under Test
Located in `spam_scoring.py`:
1. `sender_domain(email)`: Extracts domain part from an email string.
2. `first_link(text)`: Extracts the first HTTP/HTTPS URL from a text message.
3. `shout_ratio(text)`: Computes ratio of uppercase alphabetic letters to total alphabetic letters.

---

## 3. Bugs Discovered via Hypothesis Fuzzing

| Function | Counterexample | Bug Type | Root Cause |
|---|---|---|---|
| `sender_domain` | `""` or `"amith"` | `IndexError: list index out of range` | Assumed `'@'` always exists; `split('@')[1]` fails when no `@` is present. |
| `sender_domain` | `None` | `AttributeError: 'NoneType' object has no attribute 'split'` | No `None` check. |
| `first_link` | `"Hello world"` | `ValueError: substring not found` | `text.index('http')` raises `ValueError` if substring is absent. |
| `first_link` | `None` | `AttributeError: 'NoneType' object has no attribute 'index'` | No `None` check. |
| `shout_ratio` | `""` or `"1234!@#"` | `ZeroDivisionError: division by zero` | When `len(letters) == 0`, divides by zero. |
| `shout_ratio` | `None` | `TypeError: 'NoneType' object is not iterable` | No `None` check. |

---

## 4. Running Fuzz Tests
```bash
# Install Hypothesis and pytest
pip install hypothesis pytest

# Run hypothesis fuzz test suite
pytest test_spam_scoring_hypothesis.py -v
```

---

## 5. Key Deliverables
- [`spam_scoring.py`](spam_scoring.py): Original code and refactored robust implementation.
- [`test_spam_scoring_hypothesis.py`](test_spam_scoring_hypothesis.py): Comprehensive property-based fuzz tests with Hypothesis.
- [`fuzzing_analysis_report.md`](fuzzing_analysis_report.md): Formal vulnerability report and remediation verification.
