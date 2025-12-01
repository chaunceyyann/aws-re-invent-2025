# Project Structure

## Repository Organization

```
.
├── .github/              # GitHub configuration
│   ├── workflows/        # GitHub Actions CI/CD pipelines
│   ├── dependabot.yml    # Dependency update automation
│   └── pull_request_template.md
├── .kiro/                # Kiro AI assistant configuration
│   └── steering/         # AI guidance documents
├── .vscode/              # VSCode editor settings
├── docs/                 # Documentation and diagrams
│   └── architect.drawio.png
├── event-info/           # AWS re:Invent 2025 event details
│   ├── overview.md       # Conference information
│   ├── schedule.md       # Event schedule
│   └── topics.md         # Session topics and themes
├── .gitignore            # Git ignore patterns
├── .pre-commit-config.yaml  # Pre-commit hook configuration
├── CONTRIBUTING.md       # Contribution guidelines
├── LICENSE               # Project license
└── README.md             # Project overview
```

## Key Directories

### `/event-info`
Contains reference information about AWS re:Invent 2025:
- Conference details, dates, and location
- High-level schedule and session types
- Topics covering AI/ML, serverless, security, databases, etc.

### `/docs`
Documentation and architecture diagrams for demo projects.

### `/.github`
GitHub-specific configuration:
- Workflows for CI/CD automation
- PR templates for consistent contributions
- Dependabot for dependency management

### `/.kiro/steering`
AI assistant guidance documents for maintaining consistency.

## File Naming Conventions

- Use lowercase with hyphens for directories and files (kebab-case)
- Markdown files: `*.md`
- Configuration files: Use standard names (`.gitignore`, `.pre-commit-config.yaml`)

## Ignored Files

The `.gitignore` excludes:
- Python artifacts: `__pycache__/`, `*.pyc`, `venv/`, `*.egg-info/`
- Node.js: `node_modules/`, `npm-debug.log`
- Terraform: `.terraform/`, `*.tfstate`, `.terraform.lock.hcl`
- System files: `.DS_Store`, `Thumbs.db`
- Build outputs: `dist/`, `build/`

## Branch Structure

- `main`: Production-ready code (protected, requires PR + 1 approval)
- `dev`: Development branch (protected, requires PR + 1 approval)
- Feature branches: `type/jira-123` format (e.g., `feature/jira-123`, `bugfix/proj-456`)

## Commit Convention

All commits must follow: `jira-123: description` format
- Lowercase ticket ID
- Colon + space separator
- Descriptive message in lowercase
- Exception: `deps-auto:` for automated dependency updates
