import os
import subprocess
from datetime import datetime

# === CONFIG ===
langs = ["D_W_15K_V2", "D_Y_15K_V2"]
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Working directories
basic_bert_dir = os.path.join(os.getcwd(), "basic_bert_unit")
interaction_dir = os.path.join(os.getcwd(), "interaction_model")

# === RUN PIPELINE ===
for lang in langs:
    print(f"\n==============================")
    print(f"   🌍 Running pipeline for: {lang}")
    print(f"==============================\n")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"{lang}_{timestamp}.log")

    # Prepare environment with correct LANG
    env = os.environ.copy()
    env["LANG"] = lang

    with open(log_file, "w") as f:
        # Step 1: Run Basic BERT Unit
        print(f"[INFO] Starting Basic BERT Unit for {lang} ...")
        f.write(f"===== Basic BERT Unit ({lang}) =====\n")
        subprocess.run(
            ["python3", "main.py"],
            cwd=basic_bert_dir,        # ✅ run inside its own directory
            env=env,
            stdout=f,
            stderr=subprocess.STDOUT,
            check=False
        )

        # Step 2: Run Interaction Model (run.sh)
        print(f"[INFO] Starting Interaction Model for {lang} ...")
        f.write(f"\n===== Interaction Model ({lang}) =====\n")
        subprocess.run(
            ["bash", "run.sh"],
            cwd=interaction_dir,       # ✅ run inside its own directory
            env=env,
            stdout=f,
            stderr=subprocess.STDOUT,
            check=False
        )

    print(f"[✔] Completed {lang}. Log saved to {log_file}")
