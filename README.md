# CAA2.0 (Community Authority Agent)

Read-only Reddit research and drafting assistant designed to improve the quality of participation in selected subreddits.

## What this tool does
- Reads public posts (and later, limited comment context) from a small set of subreddits
- Prioritizes high-signal threads
- Prepares a private queue (CSV for MVP) for human review

## What this tool does NOT do
- No automated posting
- No automated replying
- No voting, following, or DMs
- No engagement manipulation
- Human approval required for every post/comment

## User agent
Use a stable descriptive user agent:
`script:CAA2.0:v1 (by u/BenJoeM; read-only)`

## Setup
1. Copy `.env.example` to `.env` (do not commit `.env`)
2. Add your Reddit API credentials (read-only)
3. Install dependencies

```bash
pip install -r requirements.txt
