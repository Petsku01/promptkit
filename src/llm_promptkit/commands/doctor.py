"""Doctor command for promptkit."""

from pathlib import Path

from rich.table import Table

from ..config import get_config
from ..console import console
from ..services import analyze_prompt


def doctor_command(args):
    """Analyze a prompt for common issues."""
    config = get_config()
    
    if getattr(args, 'file', None):
        path = Path(args.file)
        if not path.exists():
            console.print(f"[red]Error: File not found: {args.file}[/red]")
            return
        text = path.read_text()
        display_text = args.file
    else:
        text = args.target if args.target else ""
        display_text = "text prompt"
    
    # ML-based analysis (use config default if not overridden)
    ml_enabled = getattr(args, 'ml', config.doctor_ml_enabled)
    ml_model = getattr(args, 'model', config.doctor_ml_model)
    
    if ml_enabled:
        try:
            from ..ml_doctor import MLDoctor
            from ..doctor.models import DoctorIssue, IssueSeverity
            
            console.print(f"[bold]Analyzing {display_text} with ML...[/bold]")
            console.print(f"[dim]Model: {ml_model}[/dim]\n")
            
            ml_doctor = MLDoctor(model=ml_model)
            
            if not ml_doctor.is_available():
                console.print("[yellow]Warning: Ollama not available. Falling back to rule-based analysis.[/yellow]")
                console.print("[dim]To use ML mode, start Ollama: ollama serve[/dim]\n")
                issues = analyze_prompt(text.lower())
                _print_issues(issues)
                return
            
            ml_issues, metadata = ml_doctor.analyze(text)
            
            # Convert MLDoctorIssue to DoctorIssue for printing
            issues = []
            for ml_issue in ml_issues:
                severity = IssueSeverity(ml_issue.severity.upper())
                issues.append(DoctorIssue(
                    severity=severity,
                    category=ml_issue.category,
                    issue=ml_issue.issue,
                    suggestion=ml_issue.suggestion,
                    metadata={"confidence": ml_issue.confidence}
                ))
            
            _print_issues(issues)
            
            # Print metadata
            console.print(f"\n[dim]Overall Score: {metadata['overall_score']:.1%}[/dim]")
            if metadata.get('strengths'):
                console.print(f"[dim]Strengths: {', '.join(metadata['strengths'])}[/dim]")
            
        except ImportError as e:
            console.print(f"[red]Error: ML doctor module not available: {e}[/red]")
            console.print("[yellow]Falling back to rule-based analysis.[/yellow]\n")
            issues = analyze_prompt(text.lower())
            _print_issues(issues)
        except RuntimeError as e:
            console.print(f"[red]Error: {e}[/red]")
            console.print("[yellow]Falling back to rule-based analysis.[/yellow]\n")
            issues = analyze_prompt(text.lower())
            _print_issues(issues)
    else:
        # Rule-based analysis
        console.print(f"[bold]Analyzing {display_text}...[/bold]\n")
        issues = analyze_prompt(text.lower())
        _print_issues(issues)


def _print_issues(issues):
    """Print doctor issues in a table."""
    from ..doctor.models import DoctorIssue
    
    if not issues:
        console.print("[bold green]No issues found. Prompt looks solid.[/bold green]")
        return

    table = Table(title="Prompt Analysis", show_header=True, header_style="bold magenta")
    table.add_column("Severity", style="bold")
    table.add_column("Issue", style="cyan")
    table.add_column("Suggestion", style="green")

    for entry in issues:
        if isinstance(entry, DoctorIssue):
            table.add_row(entry.severity.value, entry.issue, entry.suggestion)
        else:
            # Legacy tuple support (severity, issue, suggestion)
            severity, issue, suggestion = entry
            table.add_row(severity.value if hasattr(severity, 'value') else str(severity), issue, suggestion)

    console.print(table)
