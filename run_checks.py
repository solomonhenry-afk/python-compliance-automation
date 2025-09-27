from checks import iam_check, s3_policy_check

if __name__ == "__main__":
    print("🔍 Running compliance checks...")
    iam_check.run()
    s3_policy_check.run()
    print("✅ Compliance scan finished")
