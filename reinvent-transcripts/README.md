# AWS re:Invent 2025 Transcripts

This directory contains transcripts from AWS re:Invent 2025 sessions and conversations.

## Source

Transcripts are sourced from otter.ai recordings taken during the conference (November 30 - December 4, 2025).

## Format

Each transcript is stored as a markdown file with:
- Session/conversation title
- Date and AI-generated summary
- Speakers list
- Full transcript with timestamps
- Audio files excluded from git (see .gitignore)

## Directory Structure

```
reinvent-transcripts/
├── README.md
├── INDEX.md                        # Index of all transcripts
├── convert-otter-to-md.py          # Conversion script
└── Transcript Name/                # Each transcript in its own directory
    ├── Transcript Name.txt         # Otter.ai export
    ├── Transcript Name.mp4         # Audio (gitignored, renamed from .mp3)
    ├── ai-summary.txt              # AI-generated summary
    └── transcript-name.md          # Generated markdown
```

## Converting Transcripts

1. Download transcript from otter.ai (export as TXT with audio)
2. Manually add `ai-summary.txt` to the directory
3. Run the conversion script:

```bash
python reinvent-transcripts/convert-otter-to-md.py "reinvent-transcripts/Transcript Name"
```

The script will:
- Parse the transcript TXT file
- Include AI summary if present
- Generate formatted markdown in the same directory
- Rename audio file (.mp3 → .mp4 for GitHub compatibility)

## Available Transcripts

See [INDEX.md](./INDEX.md) for a complete list of all transcripts.
