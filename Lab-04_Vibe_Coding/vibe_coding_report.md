# Lab 4 Vibe Coding Report: Pair Programming with LLM

**Project:** Missile Command Repair Lab (`SETAPESU26/33_missileCommand`)  
**Student:** Amith Prasad | **Roll No:** 33 (`PES1UG24AM033`)  

---

## 1. LLM Pair Programming Interaction Log

### Prompt 1: Identifying the Gameplay Bug
> **Prompt:** "In this Pygame Missile Command code, players report that after firing several shots near the left battery, subsequent clicks near the left battery do nothing even though the center and right batteries still have 10 missiles each. What is the root cause?"
> **LLM Response:** The issue lies in `nearest_battery(target)`. It finds the minimum battery based solely on distance:
> ```python
> return min(self.batteries, key=lambda b: b.pos.distance_squared_to(target))
> ```
> In `launch()`, it checks `if battery.alive and battery.ammo > 0:`. If the geometrically closest battery is out of ammo, the condition fails and no missile is fired.  
> **Solution:** Filter available batteries first:
> ```python
> available = [b for b in self.batteries if b.alive and b.ammo > 0]
> if available:
>     return min(available, key=lambda b: b.pos.distance_squared_to(target))
> return min(self.batteries, key=lambda b: b.pos.distance_squared_to(target))
> ```

### Prompt 2: Thermal Explosion Color Gradient
> **Prompt:** "Write a Python implementation for `explosion_color(progress)` where progress goes from 0.0 to 1.0. I want it to simulate a realistic explosion: starting white-hot at the detonation point, transitioning through bright yellow into fireball orange, and finally fading to deep ember red."
> **LLM Response:** Provided 3-tier piecewise linear interpolation returning clamped RGB values.

### Prompt 3: City Rebuilding Scoring Policy
> **Prompt:** "How should `city_repair_threshold()` integrate with the game loop to rebuild cities without infinite loops?"
> **LLM Response:** Return a milestone constant such as `2000`. In `update()`, check `if self.score // threshold > self.repairs_awarded:` to safely award one rebuilt city per 2000 points.

---

## 2. Verification & Gameplay Validation
- Battery fallback tested: emptying Left Battery (10 shots) smoothly transfers subsequent left-side clicks to the Center Battery.
- Visual inspection confirms smooth color changes across explosions.
- City repair triggers successfully at 2,000 and 4,000 points.
