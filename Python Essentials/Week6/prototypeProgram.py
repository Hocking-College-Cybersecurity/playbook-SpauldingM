# cybersecurity_prototype.py
# Functional prototype using tuples, dictionaries, and exception handling

def check_event(event):
    """
    Checks an event against known threat patterns stored in a dictionary.
    Returns an alert message or None.
    """

    # Dictionary of keywords -> alert message
    threat_patterns = {
        "failed login": "Failed login attempt detected!",
        "unknown ip": "Connection from unknown IP detected!",
        "malware": "Malware-related activity detected!"
    }

    # Normalize event text
    event_lower = event.lower()

    # Loop through threat patterns
    for keyword, alert in threat_patterns.items():
        if keyword in event_lower:
            return alert

    return None


def process_events(events):
    """
    Takes a list of tuples (event_id, event_message) and processes each.
    Uses exception handling to avoid crashes.
    """

    for event_tuple in events:
        try:
            # Expecting a tuple like: (id, message)
            event_id, message = event_tuple  

            print(f"\nProcessing Event ID: {event_id}")
            print(f"Message: {message}")

            alert = check_event(message)

            if alert:
                print("ALERT:", alert)
            else:
                print("No threat detected.")

        except ValueError:
            print("ERROR: Event data is not a valid (id, message) tuple.")
        except Exception as e:
            print("Unexpected error occurred:", e)


def main():
    """
    Main function that runs the prototype.
    """

    # Example structured event data (list of tuples)
    events = [
        (101, "User admin had a failed login"),
        (102, "Routine system check OK"),
        (103, "System connected to unknown IP 10.0.5.55"),
        (104, "Possible malware signature found"),
        (105, "User login successful"),
        ("BAD_DATA", "This will cause an exception")  # Intentional error
    ]

    print("=== Cybersecurity Prototype Started ===")

    # Use try/except so the program NEVER crashes
    try:
        process_events(events)
    except Exception as e:
        print("Critical system error:", e)

    print("\n=== Prototype Completed Successfully ===")


# Run the program
if __name__ == "__main__":
    main()
