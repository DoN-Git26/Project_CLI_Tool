# Project Management CLI Tool

A small Python command-line application for organizing users, projects, and
tasks. It provides commands to add and list users, attach projects to users,
add tasks to projects, and mark tasks as complete. Records are stored locally
in a JSON file.

## Features

- Add and list users.
- Add projects to users and list a user's projects.
- Add tasks to projects, optionally noting who they are assigned to.
- List tasks and mark a task complete.
- Persist data between runs in `data/database.json`.
- Keep the CLI, model classes, and JSON storage helper in separate modules.

## Requirements

- Python 3.10 or later.
- `pip` to install the packages listed in `requirements.txt`.

The CLI itself uses Python's standard library. The requirements file also
lists `rich` and `python-dateutil`.

## Setup

Clone or download the project, then run the following commands from the project
root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Usage

Run commands from the project root with `python3 main.py`. Use
`python3 main.py --help` to see all commands, or add `--help` after a command
for its options.

### Users

```bash
python3 main.py add-user --name "Donex Oloo" --email "donex@example.com"
python3 main.py list-users
```

Names and email addresses must be unique when adding a user.

### Projects

```bash
python3 main.py add-project \
  --user "Donex Oloo" \
  --title "Website refresh" \
  --description "Update the company website" \
  --due_date "2026-12-01"

python3 main.py list-projects --user "Donex Oloo"
```

The user name must match an existing user. The due date is stored as text; the
CLI does not validate its format.

### Tasks

```bash
python3 main.py add-task \
  --project "Website refresh" \
  --title "Create the landing page" \
  --assigned_to "Donex Oloo"

python3 main.py list-tasks --project "Website refresh"
python3 main.py complete-task \
  --project "Website refresh" \
  --title "Create the landing page"
```

`--assigned_to` is optional. New tasks start with the status `Pending`;
`complete-task` changes the status to `Complete`.

## Data storage

The application reads and writes `data/database.json`. The file is created
when data is saved if it does not already exist. Its structure nests projects
under users and tasks under projects. Back up this file before manually
changing or removing stored data.

## Running tests

Run the test suite from the project root:

```bash
pytest -q
python3 -m unittest discover -s tests -v
```

## Project layout

```text
.
├── main.py                 # CLI commands and argument parsing
├── models/
│   ├── project.py          # Project model
│   ├── task.py             # Task model
│   └── user.py             # User model
├── utils/
│   └── storage.py          # JSON load/save helpers
├── data/
│   └── database.json       # Local application data
├── tests/
│   └── test_models.py      # Model unit test
└── requirements.txt        # Python package requirements
```

## Current limitations

- Projects and tasks are found by title, so titles are not guaranteed to be
  unique. If titles repeat, commands operate on the first matching project or
  task.
- The optional task assignee is stored as text and is not checked against the
  list of users.
- Project due dates are stored as text and are not parsed or enforced.
- The CLI currently supports adding and listing records, and completing tasks;
  it does not provide commands to edit or delete records.
