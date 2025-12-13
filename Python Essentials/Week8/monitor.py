import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

#to start the program, best to save it to the desktop under 'Monitor.py'. go to command prompt, type 'cd Desktop' then 'python Monitor.py'
# This program simulates a cybersecurity monitoring system that checks for suspicious events and sends email alerts when threats are detected.

# EMAIL ALERT FUNCTION

def send_email_alert(subject, message, to_email):
    #configure your credentials here, if using gmail, you'll need app password
    from_email = "your_email@example.com"
    password = "your_email_password"
    to_email = "receiver@example.com"

    #create the message here
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("[EMAIL] Alert email sent successfully.")
    except Exception as e:
        print("[ERROR] Could not send email:", e)

# EVENT CHECKING FUNCTION

def check_event(event):
    """
    Check the event string for suspicious keywords.
    Returns alert message or None.
    """
    threat_patterns = {
        "failed login": "Failed login attempt detected!",
        "unknown ip": "Connection from unknown IP detected!",
        "malware": "Malware activity identified!",
        "unauthorized access": "Unauthorized access attempt!"
    }

    event_lower = event.lower()

    for keyword, alert in threat_patterns.items():
        if keyword in event_lower:
            return alert

    return None

# LOGGING FUNCTION

def log_threat(event, alert_msg):
    """
    Logs threat details into local log file with timestamp.
    """
    try:
        with open("threat_log.txt", "a") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{timestamp}] EVENT: {event} | ALERT: {alert_msg}\n")
    except Exception as e:
        print("[ERROR] Unable to write to log file:", e)

# MAIN MONITORING LOOP

def main():
    receiver_email = "receiver@example.com"

    print("=== Cybersecurity Monitoring System ACTIVE ===")
    print("Press CTRL + C to stop.\n")

    # Example simulated incoming events (rotate through them)
    demo_events = [
        "User admin had a failed login",
        "Routine system check OK",
        "System connected to unknown IP 203.0.113.5",
        "Possible malware signature found",
        "Unauthorized access attempt to /secure/data",
        "User logged in successfully"
    ]

    index = 0

    while True:
        try:
            event = demo_events[index]
            print(f"[SCAN] Processing event: {event}")

            alert_msg = check_event(event)

            if alert_msg:
                print("[THREAT DETECTED]", alert_msg)

                # Log threat locally
                log_threat(event, alert_msg)

                # Email alert
                subject = "🚨 Cybersecurity Threat Detected"
                body = f"A security threat was detected:\n\nEvent: {event}\nAlert: {alert_msg}"

                send_email_alert(subject, body, receiver_email)

            else:
                print("[OK] No threat detected.")

            # Rotate through demo events (simulating live events)
            index = (index + 1) % len(demo_events)

            # Delay to avoid spamming
            time.sleep(5)

        except KeyboardInterrupt:
            print("\n=== Monitoring stopped by user. ===")
            break
        except Exception as e:
            print("[ERROR] Unexpected system issue:", e)
            time.sleep(2)  # Prevent crash loop


# Run the program
if __name__ == "__main__":
    main()
