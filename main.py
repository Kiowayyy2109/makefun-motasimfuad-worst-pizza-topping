import os

LINE = "Pineapple on pizza is fine. The real crime is the person who orders it and then eats the crust first."

LIMIT = 200
if len(LINE) != 101 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 101 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# Defend the pineapple, then indict the crust-eater instead.
