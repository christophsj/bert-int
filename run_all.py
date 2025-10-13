import os
import subprocess
from datetime import datetime

# === CONFIG ===
langs = ["zh", "ja", "fr"]
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Paths to scripts
basic_bert_script = os.path.join("basic_bert_unit", "main.py")
interaction_script = os.path.join("interaction_model", "run.sh")

# === RUN PIPELINE ===
for lang in langs:
    print(f"\n==============================")
    print(f"   🌍 Running pipeline for: {lang}")
    print(f"==============================\n")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"{lang}_{timestamp}.log")

    env = os.environ.copy()
    env["LANG"] = lang

    with open(log_file, "w") as f:
        # Step 1: Run Basic BERT Unit
        print(f"[INFO] Starting Basic BERT Unit for {lang} ...")
        f.write(f"===== Basic BERT Unit ({lang}) =====\n")
        subprocess.run(
            ["python", basic_bert_script],
            env=env,
            stdout=f,
            stderr=subprocess.STDOUT,
            check=False
        )

        # Step 2: Run Interaction Model (run.sh)
        print(f"[INFO] Starting Interaction Model for {lang} ...")
        f.write(f"\n===== Interaction Model ({lang}) =====\n")
        subprocess.run(
            ["bash", interaction_script],
            cwd="interaction_model",  # run from correct directory
            env=env,
            stdout=f,
            stderr=subprocess.STDOUT,
            check=False
        )

    print(f"[✔] Completed {lang}. Log saved to {log_file}")
