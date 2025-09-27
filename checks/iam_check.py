def run():
    print("[IAM CHECK] Ensuring no users have *:* admin policies...")
    # mock check
    findings = ["user_admin has overly broad privileges"]
    for f in findings:
        print("⚠️", f)
