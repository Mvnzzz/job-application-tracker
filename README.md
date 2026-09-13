# Job Application Tracker

A simple command-line tool to track graduate job applications. Built with **Python 3** and the standard library only (no pip packages).

## Why this project

I built this while applying for computer science graduate / IT roles in the UK. It stores applications in a local JSON file and lets you add, list, filter, update, and delete statuses from the terminal.

## Features

- Add a company, role, status, link, and notes
- List all applications
- Filter by status (`wishlist`, `applied`, `interview`, `offer`, `rejected`)
- Update an application's status
- Delete an application
- Status summary counts (wishlist / applied / interview / offer / rejected)
- Export all applications to CSV (`data/applications_export.csv`)
- Data saved in `data/applications.json`

## Requirements

- Python 3.10+ (uses type hints like `list[dict]`; older Python may need small edits)

## How to run

```bash
python main.py
```

On Mac/Linux you can also use:

```bash
python3 main.py
```

## Example

```
Choose (1-8): 1
Company: Softwire
Role / job title: Graduate Software Developer
Job link (optional): https://online.softwire.com/apply
Notes (optional): Training-focused, London
Status [applied]: applied
```

Export everything with menu option **7) Export to CSV** — writes `data/applications_export.csv` with columns: id, company, role, status, date_added, link, notes.

## Project structure

```
job-application-tracker/
├── main.py
├── data/
│   ├── applications.json         (created when you add your first application)
│   └── applications_export.csv   (created when you export)
├── .gitignore
└── README.md
```

## What I practised

- Python fundamentals (functions, files, JSON, CSV, menus)
- Git commits and pushing a project to GitHub
- Writing a clear README for employers

## Licence

Personal learning project — use freely.
