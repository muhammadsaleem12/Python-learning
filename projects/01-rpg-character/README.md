# ⚔️ RPG Character Creator

A lightweight Python script that validates input parameters and generates formatted ASCII stat bars for RPG characters using custom symbols.

---

## 📌 Features

* **Name Validation:** Checks for valid string type, non-empty input, max length (10 chars), and no spaces.
* **Stat Validation:** Ensures Strength (`STR`), Intelligence (`INT`), and Charisma (`CHA`) are integers between `1` and `4`.
* **Point Balance Check:** Requires the sum of all stats to equal exactly `7` points.
* **ASCII Stat Bars:** Displays stat levels using filled (`●`) and empty (`○`) indicator dots out of 10.

---

## 🚀 How It Works

### Example Output

```python
s = create_character("Zuko", 4, 2, 1)
print(s)