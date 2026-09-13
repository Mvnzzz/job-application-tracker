#!/usr/bin/env python3
"""
Job Application Tracker
A simple command-line tool to track graduate job applications.
Uses only the Python standard library (no extra installs).
"""

from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_FILE = DATA_DIR / "applications.json"
EXPORT_FILE = DATA_DIR / "applications_export.csv"

STATUSES = ("wishlist", "applied", "interview", "offer", "rejected")
CSV_FIELDS = ("id", "company", "role", "status", "date_added", "link", "notes")


def load_apps() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def save_apps(apps: list[dict]) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(apps, f, indent=2)


def next_id(apps: list[dict]) -> int:
    if not apps:
        return 1
    return max(app["id"] for app in apps) + 1


def add_application(apps: list[dict]) -> None:
    print("\n--- Add application ---")
    company = input("Company: ").strip()
    role = input("Role / job title: ").strip()
    link = input("Job link (optional): ").strip()
    notes = input("Notes (optional): ").strip()

    print("Status options:", ", ".join(STATUSES))
    status = input("Status [applied]: ").strip().lower() or "applied"
    if status not in STATUSES:
        print(f"Unknown status '{status}', using 'applied'.")
        status = "applied"

    app = {
        "id": next_id(apps),
        "company": company,
        "role": role,
        "status": status,
        "date_added": date.today().isoformat(),
        "link": link,
        "notes": notes,
    }
    apps.append(app)
    save_apps(apps)
    print(f"Saved #{app['id']}: {company} — {role} ({status})")


def list_applications(apps: list[dict], status_filter: str | None = None) -> None:
    print("\n--- Applications ---")
    rows = apps
    if status_filter:
        rows = [a for a in apps if a["status"] == status_filter]

    if not rows:
        print("No applications found.")
        return

    for app in rows:
        link_bit = f" | {app['link']}" if app.get("link") else ""
        notes_bit = f"\n    notes: {app['notes']}" if app.get("notes") else ""
        print(
            f"#{app['id']}  {app['company']} — {app['role']}\n"
            f"    status: {app['status']}  |  added: {app['date_added']}{link_bit}{notes_bit}"
        )


def update_status(apps: list[dict]) -> None:
    if not apps:
        print("Nothing to update yet.")
        return

    list_applications(apps)
    try:
        app_id = int(input("\nID to update: ").strip())
    except ValueError:
        print("Please enter a number.")
        return

    app = next((a for a in apps if a["id"] == app_id), None)
    if not app:
        print(f"No application with id {app_id}.")
        return

    print("Status options:", ", ".join(STATUSES))
    status = input(f"New status [{app['status']}]: ").strip().lower()
    if not status:
        print("No change.")
        return
    if status not in STATUSES:
        print(f"Unknown status '{status}'.")
        return

    app["status"] = status
    save_apps(apps)
    print(f"Updated #{app_id} → {status}")


def delete_application(apps: list[dict]) -> None:
    if not apps:
        print("Nothing to delete yet.")
        return

    list_applications(apps)
    try:
        app_id = int(input("\nID to delete: ").strip())
    except ValueError:
        print("Please enter a number.")
        return

    app = next((a for a in apps if a["id"] == app_id), None)
    if not app:
        print(f"No application with id {app_id}.")
        return

    confirm = input(f"Delete #{app_id} {app['company']} — {app['role']}? [y/N]: ").strip().lower()
    if confirm != "y":
        print("Cancelled.")
        return

    apps[:] = [a for a in apps if a["id"] != app_id]
    save_apps(apps)
    print(f"Deleted #{app_id}.")


def status_summary(apps: list[dict]) -> None:
    print("\n--- Status summary ---")
    if not apps:
        print("No applications yet.")
        return

    counts = {status: 0 for status in STATUSES}
    for app in apps:
        status = app.get("status")
        if status in counts:
            counts[status] += 1
        else:
            counts.setdefault(status, 0)
            counts[status] += 1

    total = len(apps)
    for status in STATUSES:
        print(f"  {status}: {counts[status]}")
    extra = {k: v for k, v in counts.items() if k not in STATUSES}
    for status, n in sorted(extra.items()):
        print(f"  {status}: {n}")
    print(f"  total: {total}")


def export_csv(apps: list[dict]) -> None:
    print("\n--- Export to CSV ---")
    DATA_DIR.mkdir(exist_ok=True)
    with EXPORT_FILE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for app in apps:
            writer.writerow({field: app.get(field, "") for field in CSV_FIELDS})
    print(f"Exported {len(apps)} application(s) to {EXPORT_FILE}")


def show_menu() -> None:
    print(
        """
==============================
  Job Application Tracker
==============================
1) Add application
2) List all
3) List by status
4) Update status
5) Delete application
6) Status summary
7) Export to CSV
8) Quit
"""
    )


def main() -> None:
    apps = load_apps()
    while True:
        show_menu()
        choice = input("Choose (1-8): ").strip()
        if choice == "1":
            add_application(apps)
            apps = load_apps()
        elif choice == "2":
            list_applications(apps)
        elif choice == "3":
            print("Status options:", ", ".join(STATUSES))
            status = input("Filter status: ").strip().lower()
            if status not in STATUSES:
                print("Unknown status.")
            else:
                list_applications(apps, status)
        elif choice == "4":
            update_status(apps)
            apps = load_apps()
        elif choice == "5":
            delete_application(apps)
            apps = load_apps()
        elif choice == "6":
            status_summary(apps)
        elif choice == "7":
            export_csv(apps)
        elif choice == "8":
            print("Bye - keep applying.")
            break
        else:
            print("Pick a number from 1 to 8.")


if __name__ == "__main__":
    main()
