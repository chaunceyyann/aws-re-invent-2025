# Technology Stack

## Languages & Frameworks

This is a polyglot repository supporting multiple technology stacks:

- **Python**: Primary language for demos and automation
- **JavaScript/Node.js**: For serverless and web applications
- **Terraform**: Infrastructure as Code for AWS resources

## Build Tools & Package Managers

- **Python**: pip, venv for virtual environments
- **Node.js**: npm/yarn for package management
- **Terraform**: For infrastructure provisioning

## Code Quality Tools

### Pre-commit Hooks

The project uses pre-commit hooks for automated validation:

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install
pre-commit install --hook-type commit-msg
```

### Formatters & Linters

- **Python**: Black (formatter), isort (import sorting)
- **YAML/JSON**: Prettier
- **Terraform**: terraform fmt, tflint, terraform-docs

### Validation Checks

- Trailing whitespace removal
- End-of-file fixer
- YAML/JSON syntax validation
- Large file prevention
- Merge conflict detection
- Case conflict detection

## Common Commands

### Git Workflow

```bash
# Start new feature
git checkout dev && git pull
git checkout -b feature/jira-123

# Commit with proper format
git commit -m "jira-123: implement feature"

# Push and create PR
git push origin feature/jira-123
```

### Pre-commit

```bash
# Run all hooks manually
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files
```

### Terraform

```bash
# Format code
terraform fmt -recursive

# Validate configuration
terraform validate

# Plan changes
terraform plan

# Apply changes
terraform apply
```

## CI/CD

- GitHub Actions for automated checks
- Required status check: `pr-checks`
- Automated branch deletion after merge
