# AWS re:Invent 2025 Transcripts

This directory contains transcripts from AWS re:Invent 2025 sessions and conversations.

## Available Transcripts

- [AI Security Strategies with Okta's Auth0](./AI%20Security%20Strategies%20with%20Okta's%20Auth0/ai-security-strategies-with-okta's-auth0.md) - Securing AI agents with fine-grained access and Cross-App Access protocol
- [AWS CEO talks about AI Strategy](./AWS%20CEO%20talks%20about%20AI%20Strategy/aws-ceo-talks-about-ai-strategy.md) - Matt Garner on AI evolution and enterprise applications
- [AWS Cloud Formation Solutions Overview](./AWS%20Cloud%20Formation%20Solutions%20Overview/aws-cloud-formation-solutions-overview.md) - CloudFormation, AWS CDK, and infrastructure management
- [AWS Infrastructure Innovations](./AWS%20Infrastructure%20Innovations/aws-infrastructure-innovations.md) - Custom silicon, Graviton 5, Lambda Managed Instances, and Trainium 3
- [Generative AI multi agent fine tuning Overview](./Generative%20AI%20multi%20agent%20fine%20tuning%20Overview/generative-ai-multi-agent-fine-tuning-overview.md) - Multi-agent system for automated model fine-tuning
- [JPM and Netflix talks about Innovation in Payments and Streaming](./JPM%20and%20Netflix%20talks%20about%20Innovation%20in%20Payments%20and%20Streaming/jpm-and-netflix-talks-about-innovation-in-payments-and-streaming.md) - Blockchain, JPM Coin, and AI in streaming
- [Perplexity CEO talks about AI Search Innovations](./Perplexity%20CEO%20talks%20about%20AI%20Search%20Innovations/perplexity-ceo-talks-about-ai-search-innovations.md) - AI-powered search innovations

See [INDEX.md](./INDEX.md) for detailed summaries.

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
