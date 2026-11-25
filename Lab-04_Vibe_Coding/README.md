# Lab 4: Vibe Coding — Missile Command Repair Lab

**Course:** Software Engineering (UE24CS341A)  
**Institution:** PES University, Bengaluru  
**Student:** Amith Prasad | **Roll No:** 33 (`PES1UG24AM033`)  
**Assigned Repository:** `SETAPESU26/33_missileCommand`  

---

## 1. Objective
- Practice modern **Vibe Coding** workflows using an AI coding partner (LLM) for debugging, pair programming, and feature development.
- Identify and rectify subtle architectural and logical bugs in an interactive Pygame simulation.
- Implement creative game enhancements with critical human review.

---

## 2. Tasks Completed

### Task 1: Fix Battery Selection Bug (Crucial Gameplay Bug)
- **Problem:** `nearest_battery(target)` always selected whichever battery was geometrically closest, completely ignoring whether the battery was alive or had ammunition remaining. Clicks near an empty battery failed silently while other batteries had full ammo.
- **Fix:** Filtered batteries to only those with `alive == True` and `ammo > 0`. If all batteries are depleted, falls back gracefully.

### Task 2: Smooth Explosion Heat Gradient (`explosion_color`)
- **Enhancement:** Implemented a three-phase dynamic thermal color transition based on explosion normalized age ($0.0 \le p \le 1.0$):
  - Phase 1 ($0.0 \le p < 0.3$): Intense white-hot core fading into vibrant yellow.
  - Phase 2 ($0.3 \le p < 0.7$): Warm yellow expanding into fiery orange.
  - Phase 3 ($0.7 \le p \le 1.0$): Deep ember red fading out smoothly.

### Task 3: Visual & Console City Destruction Alert (`on_city_destroyed`)
- **Enhancement:** Triggers audible logging, tracking remaining cities, and notifying danger level when cities fall below 3.

### Task 4: City Rebuilding Scoring Milestone (`city_repair_threshold`)
- **Enhancement:** Returns `2000` points threshold. Automatically resurrects a destroyed city whenever the player's score increases by another 2,000 points.

---

## 3. Running the Program
```bash
# Install Pygame dependency
pip install pygame

# Launch game
python game.py
```
**Controls:** Click to fire interceptor missiles toward incoming targets. Press `R` to restart.

---

## 4. Key Deliverables
- [`game.py`](game.py): Clean, fully functional, and enhanced Missile Command simulation.
- [`vibe_coding_report.md`](vibe_coding_report.md): Prompt transcript, before/after analysis, and reflection.
