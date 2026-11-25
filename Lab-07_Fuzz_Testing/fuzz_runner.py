"""
Pure Python Fuzz Testing Runner for Spam Scoring Filter (Lab 7)
Generates randomized adversarial payloads, Unicode mutations, nulls, and malformed strings.
Executes 10,000 randomized test vectors to prove fault tolerance.
"""

import random
import string
from spam_scoring import sender_domain, first_link, shout_ratio

def generate_fuzz_payload():
    choice = random.randint(0, 7)
    if choice == 0:
        return None
    elif choice == 1:
        return ""
    elif choice == 2:
        # random ascii
        length = random.randint(1, 100)
        return "".join(random.choices(string.printable, k=length))
    elif choice == 3:
        # random unicode characters
        length = random.randint(1, 50)
        return "".join(chr(random.randint(0x00A0, 0x0500)) for _ in range(length))
    elif choice == 4:
        # email-like with missing parts or weird @
        ats = "@" * random.randint(0, 5)
        text = "".join(random.choices(string.ascii_letters, k=random.randint(0, 15)))
        return text + ats + text
    elif choice == 5:
        # url-like mutations
        prefix = random.choice(["http", "https", "http://", "htt", "HTTP", "hTtP", ""])
        body = "".join(random.choices(string.ascii_letters + "/.:", k=random.randint(0, 30)))
        return f"message {prefix}{body} end"
    elif choice == 6:
        # numbers and symbols only (testing ZeroDivision in shout_ratio)
        return "".join(random.choices(string.digits + string.punctuation + " \t\n", k=random.randint(1, 50)))
    else:
        # massive string
        return "A" * random.randint(1000, 5000)

def run_fuzz_campaign(iterations=10000):
    print(f"=== Starting Fuzzing Campaign ({iterations} iterations) ===")
    crashes = {"sender_domain": 0, "first_link": 0, "shout_ratio": 0}

    for i in range(iterations):
        payload = generate_fuzz_payload()

        # 1. Test sender_domain
        try:
            res = sender_domain(payload)
            assert isinstance(res, str)
        except Exception as e:
            crashes["sender_domain"] += 1
            print(f"[CRASH] sender_domain crashed on payload {repr(payload)}: {e}")

        # 2. Test first_link
        try:
            res = first_link(payload)
            assert res is None or isinstance(res, str)
        except Exception as e:
            crashes["first_link"] += 1
            print(f"[CRASH] first_link crashed on payload {repr(payload)}: {e}")

        # 3. Test shout_ratio
        try:
            res = shout_ratio(payload)
            assert isinstance(res, float)
            assert 0.0 <= res <= 1.0
        except Exception as e:
            crashes["shout_ratio"] += 1
            print(f"[CRASH] shout_ratio crashed on payload {repr(payload)}: {e}")

    total_crashes = sum(crashes.values())
    print("\n=== Fuzzing Campaign Results ===")
    print(f"Total Iterations: {iterations}")
    print(f"Sender Domain Crashes: {crashes['sender_domain']}")
    print(f"First Link Crashes:    {crashes['first_link']}")
    print(f"Shout Ratio Crashes:   {crashes['shout_ratio']}")
    print(f"Total Defects Found:   {total_crashes}")
    if total_crashes == 0:
        print("[SUCCESS] All functions proved robust against 10,000 randomized adversarial inputs!")
    return total_crashes == 0

if __name__ == "__main__":
    success = run_fuzz_campaign(10000)
    exit(0 if success else 1)
