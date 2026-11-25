"""
Unit Test Suite for Hardened Spam Scoring Filter (Lab 7)
Tests adversarial inputs, counterexamples found by fuzzing, and edge cases.
"""

import pytest
from spam_scoring import sender_domain, first_link, shout_ratio


class TestSenderDomainDefects:
    def test_empty_string(self):
        assert sender_domain("") == ""

    def test_none_input(self):
        assert sender_domain(None) == ""

    def test_missing_at_symbol(self):
        assert sender_domain("noatsignexample.com") == ""

    def test_trailing_at(self):
        assert sender_domain("user@") == ""

    def test_multiple_at_symbols(self):
        assert sender_domain("user@sub@domain.com") == "domain.com"

    def test_valid_standard_email(self):
        assert sender_domain("Amith.Prasad@Pes.Edu") == "pes.edu"


class TestFirstLinkDefects:
    def test_empty_string(self):
        assert first_link("") is None

    def test_none_input(self):
        assert first_link(None) is None

    def test_no_http_in_text(self):
        assert first_link("Hello world, this is a plain message.") is None

    def test_link_at_end_of_text(self):
        assert first_link("Check this out: https://pes.edu") == "https://pes.edu"

    def test_link_surrounded_by_text(self):
        assert first_link("Visit http://pes.edu for details.") == "http://pes.edu"


class TestShoutRatioDefects:
    def test_empty_string(self):
        assert shout_ratio("") == 0.0

    def test_none_input(self):
        assert shout_ratio(None) == 0.0

    def test_numbers_and_symbols_only(self):
        assert shout_ratio("1234567890 !@#$%^&*()") == 0.0

    def test_all_uppercase(self):
        assert shout_ratio("URGENT OFFER EXCLUSIVE") == 1.0

    def test_all_lowercase(self):
        assert shout_ratio("all lowercase test string") == 0.0

    def test_half_uppercase(self):
        assert shout_ratio("HeLlO!") == 0.6  # 3 uppercase out of 5 letters (H, L, O)
