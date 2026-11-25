# Fuzz Testing Analysis Report: Hypothesis Automated Bug Discovery

**Lab:** Lab 7: Fuzzing for Input Validation Bugs  
**Course:** Software Engineering (UE24CS341A)  
**Student:** Amith Prasad | **Roll No:** 33 (`PES1UG24AM033`)  

---

## 1. Executive Summary
Fuzz testing of the `spam_scoring` module revealed three critical unhandled exception pathways in the baseline implementation. Utilizing the **Hypothesis** property-based fuzz testing library, we subjected the functions to broad input strategies spanning null values, arbitrary unicode sequences, control characters, and varying lengths.

All three root causes were diagnosed, hardened with defensive guard clauses, and verified through a complete fuzzing test suite consisting of hundreds of generated examples with zero failures.

---

## 2. Fuzzing Counterexamples & Failure Trace Analysis

### Defect 1: `IndexError` in `sender_domain`
- **Minimal Counterexample Found by Hypothesis:** `email = ""`
- **Stack Trace:**
  ```text
  email.split('@')[1].lower()
  IndexError: list index out of range
  ```
- **Remediation:** Verify string type, check length of split list $\ge 2$, and strip/lowercase safely.

### Defect 2: `ValueError` in `first_link`
- **Minimal Counterexample Found by Hypothesis:** `text = ""` or `text = "no link here"`
- **Stack Trace:**
  ```text
  start = text.index('http')
  ValueError: substring not found
  ```
- **Remediation:** Replace non-defensive `str.index()` with `str.find()`, which returns `-1` on absence, returning `None`.

### Defect 3: `ZeroDivisionError` in `shout_ratio`
- **Minimal Counterexample Found by Hypothesis:** `text = ""` or `text = "12345!@#"`
- **Stack Trace:**
  ```text
  return len(upper) / len(letters)
  ZeroDivisionError: division by zero
  ```
- **Remediation:** Guard check `if not letters: return 0.0`.

---

## 3. Test Verification
Executing `pytest test_spam_scoring_hypothesis.py`:
```text
============================= test session starts =============================
collected 5 items

test_spam_scoring_hypothesis.py::test_sender_domain_never_crashes PASSED [ 20%]
test_spam_scoring_hypothesis.py::test_first_link_never_crashes PASSED    [ 40%]
test_spam_scoring_hypothesis.py::test_shout_ratio_never_crashes PASSED   [ 60%]
test_spam_scoring_hypothesis.py::test_all_uppercase_is_one PASSED        [ 80%]
test_spam_scoring_hypothesis.py::test_all_lowercase_is_zero PASSED       [100%]

============================== 5 passed in 0.42s ==============================
```
