#!/usr/bin/env python3
"""
Convert Otter.ai transcript directory to formatted Markdown.
Usage: python convert-otter-to-md.py <transcript-directory>

Expected directory structure:
  transcript-directory/
    ├── transcript-name.txt
    ├── transcript-name.mp3
    └── ai-summary.txt (optional)

Output: transcript-name.md in parent directory (reinvent-transcripts/)
"""

import sys
import re
from pathlib import Path
from datetime import datetime


def parse_otter_transcript(txt_content):
    """Parse Otter.ai transcript format."""
    lines = txt_content.strip().split('\n')
    
    speakers = []
    current_speaker = None
    current_time = None
    current_text = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if line is a speaker header (e.g., "Speaker 1  00:00")
        speaker_match = re.match(r'^(.*?)\s{2,}(\d{2}:\d{2})$', line)
        
        if speaker_match:
            # Save previous speaker's text
            if current_speaker and current_text:
                speakers.append({
                    'speaker': current_speaker,
                    'time': current_time,
                    'text': ' '.join(current_text)
                })
                current_text = []
            
            current_speaker = speaker_match.group(1)
            current_time = speaker_match.group(2)
        else:
            # This is continuation of current speaker's text
            current_text.append(line)
    
    # Don't forget the last speaker
    if current_speaker and current_text:
        speakers.append({
            'speaker': current_speaker,
            'time': current_time,
            'text': ' '.join(current_text)
        })
    
    return speakers


def clean_ai_summary(summary_text):
    """Clean and format AI summary text for markdown."""
    lines = summary_text.strip().split('\n')
    cleaned_lines = []
    skip_patterns = [
        'Summary',
        'Transcript',
        'Template:',
        'General',
        'This list can be reordered',
        'Add action item',
        'To drag an action item',
        'Use the up and down arrow keys',
        'To drop the item',
        'To cancel drag and drop'
    ]
    
    in_outline = False
    pending_bullet = False
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and UI instructions
        if not line or any(pattern in line for pattern in skip_patterns):
            continue
        
        # Main sections
        if line == 'Overview':
            cleaned_lines.append('### Overview\n')
            continue
        elif line == 'Outline':
            cleaned_lines.append('### Outline\n')
            in_outline = True
            continue
        
        # Handle bullet points
        if line.startswith('•'):
            pending_bullet = True
            continue
        
        # If we have a pending bullet, this line is the bullet content
        if pending_bullet:
            cleaned_lines.append(f'- {line}')
            pending_bullet = False
            continue
        
        # Subsections in Outline (not starting with "Speaker", reasonable length, not a bullet continuation)
        if in_outline and not line.startswith('Speaker'):
            # Check if it's a subsection header (reasonably short and looks like a title)
            if len(line) < 80 and not line[0].islower():
                # This is a subsection header
                cleaned_lines.append(f'\n**{line}**\n')
                continue
        
        # Regular paragraph text (for Overview section)
        if not in_outline:
            cleaned_lines.append(f'{line}\n')
    
    return '\n'.join(cleaned_lines)


def generate_markdown(speakers, title, ai_summary=None, audio_filename=None):
    """Generate formatted markdown from parsed transcript."""
    md = f"# {title}\n\n"
    
    # Metadata
    md += f"**Date:** {datetime.now().strftime('%B %d, %Y')}\n"
    md += f"**Source:** otter.ai\n\n"
    
    # Audio link if provided
    if audio_filename:
        md += f"🎧 [Listen to recording](./{audio_filename})\n\n"
    
    # AI Summary if provided
    if ai_summary:
        md += "## AI Summary\n"
        cleaned_summary = clean_ai_summary(ai_summary)
        md += f"{cleaned_summary}\n\n"
    
    # Speakers list
    unique_speakers = sorted(set(s['speaker'] for s in speakers))
    md += "## Speakers\n\n"
    for speaker in unique_speakers:
        md += f"- {speaker}\n"
    md += "\n"
    
    # Transcript
    md += "## Transcript\n\n"
    for entry in speakers:
        md += f"**{entry['speaker']} ({entry['time']}):**  \n"
        md += f"{entry['text']}\n\n"
    
    return md


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert-otter-to-md.py <transcript-directory>")
        print("\nExpected directory structure:")
        print("  transcript-directory/")
        print("    ├── transcript-name.txt")
        print("    ├── transcript-name.mp3")
        print("    └── ai-summary.txt (optional)")
        sys.exit(1)
    
    input_dir = Path(sys.argv[1])
    
    if not input_dir.exists():
        print(f"Error: Directory '{input_dir}' not found")
        sys.exit(1)
    
    if not input_dir.is_dir():
        print(f"Error: '{input_dir}' is not a directory")
        sys.exit(1)
    
    # Find the transcript TXT file
    txt_files = list(input_dir.glob("*.txt"))
    txt_files = [f for f in txt_files if f.name != "ai-summary.txt"]
    
    if not txt_files:
        print(f"Error: No transcript .txt file found in '{input_dir}'")
        sys.exit(1)
    
    if len(txt_files) > 1:
        print(f"Warning: Multiple .txt files found, using '{txt_files[0].name}'")
    
    transcript_file = txt_files[0]
    
    # Check for AI summary
    ai_summary_file = input_dir / "ai-summary.txt"
    ai_summary = None
    if ai_summary_file.exists():
        ai_summary = ai_summary_file.read_text()
        print(f"✓ Found AI summary")
    
    # Check for audio file
    audio_extensions = ['.mp3', '.mp4', '.m4a', '.wav']
    audio_file = None
    for ext in audio_extensions:
        potential_audio = transcript_file.with_suffix(ext)
        if potential_audio.exists():
            audio_file = potential_audio
            print(f"✓ Found audio file: {audio_file.name}")
            break
    
    # Read and parse transcript
    txt_content = transcript_file.read_text()
    speakers = parse_otter_transcript(txt_content)
    
    # Generate title from directory name
    title = input_dir.name
    
    # Determine audio filename for markdown link
    audio_filename = None
    if audio_file:
        if audio_file.suffix == '.mp3':
            audio_filename = audio_file.name.replace('.mp3', '.mp4')
        else:
            audio_filename = audio_file.name
    
    # Generate markdown
    markdown = generate_markdown(speakers, title, ai_summary, audio_filename)
    
    # Output to same directory with sanitized filename
    output_filename = title.replace(" ", "-").lower() + ".md"
    output_file = input_dir / output_filename
    
    # Write output
    output_file.write_text(markdown)
    print(f"✓ Converted to '{output_file}'")
    
    # Rename audio file to .mp4 if it's .mp3 (in same directory)
    if audio_file and audio_file.suffix == '.mp3':
        dest_audio = input_dir / audio_file.name.replace('.mp3', '.mp4')
        import shutil
        shutil.copy2(audio_file, dest_audio)
        audio_file.unlink()  # Remove original .mp3
        print(f"✓ Renamed audio to '{dest_audio.name}' (.mp3 → .mp4 for GitHub)")


if __name__ == "__main__":
    main()
