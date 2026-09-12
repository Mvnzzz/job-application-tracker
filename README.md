# Job Application Tracker

A simple command-line tool to track graduate job applications. Built with **Python 3** and the standard library only (no pip packages).

## Why this project

I built this while applying for computer science graduate / IT roles in the UK. It stores applications in a local JSON file and lets you add, list, filter, and update statuses from the terminal.

## Features

- Add a company, role, status, link, and notes
- List all applications
- Filter by status (`wishlist`, `applied`, `interview`, `offer`, `rejected`)
- Update an application's status
- Data saved in `data/applications.json`

## Requirements

- Python 3.10+ (uses type hints like `list[dict]`; older Python may need small edits)

## How to run

```bash
python3 main.py
```

On Windows you can also try:

```bash
python main.py
```

## Example

```
Choose (1-5): 1
Company: Softwire
Role / job title: Graduate Software Developer
Job link (optional): https://online.softwire.com/apply
Notes (optional): Training-focused, London
Status [applied]: applied
```

## Project structure

```
job-application-tracker/
├── main.py              # CLI app
├── data/
│   └── applications.json
├── .gitignore
└── README.md
```

## What I practised

- Python fundamentals (functions, files, JSON, menus)
- Git commits and pushing a project to GitHub
- Writing a clear README for employers

## Licence

Personal learning project — use freely.
