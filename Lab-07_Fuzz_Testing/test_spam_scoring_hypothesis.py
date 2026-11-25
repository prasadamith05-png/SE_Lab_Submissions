"""
Hypothesis Property-Based Fuzz Testing Suite for Spam Scoring Filter
PES University - Software Engineering Lab 7
"""

from hypothesis import given, strategies as st
import pytest
from spam_scoring import sender_domain, first_link, shout_ratio


# -----------------------------------------------------------------
# 1. Fuzzing sender_domain
# -----------------------------------------------------------------
@given(st.text() | st.none() | st.binary())
def test_sender_domain_never_crashes(s):
    """Property: Function must never raise an unhandled exception for any text or None."""
    result = sender_domain(s)
    assert isinstance(result, str)
    if isinstance(s, str) and "@" in s:
        parts = s.split("@")
        if len(parts) >= 2 and parts[1]:
            assert result == parts[1].strip().lower()


# -----------------------------------------------------------------
# 2. Fuzzing first_link
# -----------------------------------------------------------------
@given(st.text() | st.none() | st.binary())
def test_first_link_never_crashes(s):
    """Property: Function must return string or None without throwing ValueError."""
    result = first_link(s)
    assert result is None or isinstance(result, str)
    if isinstance(result, str):
        assert result.startswith("http")


# -----------------------------------------------------------------
# 3. Fuzzing shout_ratio
# -----------------------------------------------------------------
@given(st.text() | st.none() | st.binary())
def test_shout_ratio_never_crashes(s):
    """Property: Function must return float in range [0.0, 1.0] without ZeroDivisionError."""
    ratio = shout_ratio(s)
    assert isinstance(ratio, float)
    assert 0.0 <= ratio <= 1.0


# -----------------------------------------------------------------
# 4. Property invariants
# -----------------------------------------------------------------
@given(st.text(alphabet=st.characters(whitelist_categories=('Lu',))))
def test_all_uppercase_is_one(s):
    """Property: Any non-empty purely uppercase alphabetic string must have shout_ratio 1.0."""
    if s:
        assert shout_ratio(s) == 1.0


@given(st.text(alphabet=st.characters(whitelist_categories=('Ll',))))
def test_all_lowercase_is_zero(s):
    """Property: Any non-empty purely lowercase alphabetic string must have shout_ratio 0.0."""
    if s:
        assert shout_ratio(s) == 0.0
