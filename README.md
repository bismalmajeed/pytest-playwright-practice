# Pytest + Playwright Practice

Practice project for UI and API test automation with **pytest** and **Playwright (Python)**,
written against a public practice site (https://rahulshettyacademy.com).

[![Tests](https://github.com/bismalmajeed/pytest-playwright-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/bismalmajeed/pytest-playwright-practice/actions/workflows/ci.yml)

**Tech stack:** Python, pytest, Playwright, pytest-bdd, pytest-html, pytest-xdist, Page Object Model.

**Skills shown:** UI automation, API testing, network mocking, end-to-end API + UI flows,
data-driven tests, BDD (Gherkin), cross-browser runs, parallel execution, HTML reporting and CI.

## What's covered

| Area | Where | Topics |
|---|---|---|
| Pytest fundamentals | `pytestDir/` | fixtures (module / session / function scope), setup and teardown, `skip`, markers |
| Playwright basics | `playwright/test_playwrightBasics.py` | launching browsers, locators, `get_by_*` selectors |
| UI validations | `test_UIValidations_1.py`, `test_MoreValidations.py` | dynamic elements, child windows / popups, assertions with `expect` |
| Network mocking | `test_Network1.py`, `test_Network2.py` | `page.route` to fake API responses, rewrite requests, session storage login |
| API + UI end to end | `test_web_api.py`, `test_framework_web_api.py` | create an order through the API, verify it in the UI |
| Page Object Model | `playwright/pageObjects/` | `LoginPage`, `DashboardPage`, `OrdersHistoryPage`, `OrderDetailsPage` |
| Data-driven tests | `data/credentials.json` + `parametrize` | one test run per user |
| BDD | `test_pytest-bddTest.py`, `features/` | Gherkin scenario with `pytest-bdd` |
| CLI options | `playwright/conftest.py` | `--browser_name chrome / firefox / safari`, `--url_name` |

## Project structure

```
.
├── pytest.ini
├── requirements.txt
├── pytestDir/                 # pure pytest practice (fixtures, markers)
└── playwright/
    ├── conftest.py            # --browser_name option, browserInstance fixture
    ├── data/                  # credentials (git-ignored) + example file
    ├── features/              # Gherkin feature files
    ├── pageObjects/           # page object classes
    ├── utils/                 # API helpers and credentials loader
    └── test_*.py
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

Create your credentials file from the template. It is git-ignored, so your login never gets committed:

```bash
cp playwright/data/credentials.example.json playwright/data/credentials.json
```

Then edit `playwright/data/credentials.json`:

- `user_credentials`: an account you register at https://rahulshettyacademy.com/client/auth/register
- `practice_site`: the username and password shown on https://rahulshettyacademy.com/loginpagePractise/

## Running the tests

Each test file starts with its own run commands. Common ones, from the project root:

```bash
pytest                                                   # everything
pytest playwright/test_Network1.py -v -s                 # one file
pytest playwright/test_Network1.py::test_Network_1 -v -s # one test
pytest playwright -m smoke                               # only tests marked smoke
pytest playwright --headed                               # watch the browser
pytest playwright -n 3                                   # run in parallel (xdist)
```

Browser choice and reports:

```bash
pytest playwright --browser_name firefox
pytest playwright --browser_name safari      # runs Playwright WebKit
pytest playwright --tracing on --html=report.html
```

Tests that use the built-in `page` fixture pick the browser with Playwright's own
flag instead, e.g. `--browser firefox` or `--browser webkit`.

## Notes

- The practice site is shared and changes now and then, so a locator or a demo
  product can stop matching. Update the test when that happens.
- Every API order test creates a new order on the account you configure.
- Playwright's WebKit build can crash on some macOS versions. Update with
  `pip install -U playwright pytest-playwright && playwright install webkit`.

## Running in Jenkins

Set the job's custom workspace to the `playwright/` folder and use an Execute shell step:

```bash
pytest --browser_name chrome --tracing on --html=report.html
```
