def create_log(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Success: {filename} has been created!")
    except Exception as e:
        print(f"Error: Could not create file. Reason: {e}")

message = "Security Log Entry: Unauthorized access detected at 14:00"
create_log('security_report.txt', message)
