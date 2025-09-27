def run():
    print("[S3 POLICY CHECK] Ensuring buckets are private and encrypted...")
    # mock check
    findings = ["bucket 'test-bucket' allows public read access"]
    for f in findings:
        print("⚠️", f)
