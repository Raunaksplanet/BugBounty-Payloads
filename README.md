# Custom Payloads & Wordlists

Curated payloads and wordlists for bug bounty fuzzing: XSS, SQLi, SSRF, LFI, open redirect, CRLF, WAF bypass, PDF exploits, plus recon wordlists (API, juicy files, ports, CMS) and regex patterns.

> Use only on targets you are authorized to test.

## Layout

| # | Folder | What is inside |
|---|--------|----------------|
| 01 | `01-recon-wordlists/` | 17 files: API endpoints, juicy files, resolvers, robots paths, sensitive extensions/keywords, cgi-bin, ports, wp-content, wordpress, phpmyadmin, kibana, sqldb, iis, jsp, zip, xml |
| 02 | `02-xss-payloads/` | Markdown XSS, open redirect, CRLF + `img-upload-payloads/` (file-upload XSS/SVG test files; filenames are the payloads, keep as-is) |
| 03 | `03-sqli-payloads/` | XOR-based SQLi list |
| 04 | `04-ssrf-lfi-traversal/` | Unix LFI traversal + SSRF file-upload list |
| 05 | `05-waf-bypass/` | Per-WAF XSS payloads: Akamai, Cloudflare, Cloudfront, Imperva, Incapsula, Wordfence |
| 06 | `06-pdf-exploits/` | 7 PoC PDFs (tracking, BXSS, calculator RCE, cookie prompt, domain) |
| 07 | `07-regex-patterns/` | 1592 common recon regexes |
| 08 | `08-misc-scripts/` | LFI test script + `sample.rar` (unverified sample, see note) |

## Usage

```bash
# fuzz with ffuf
ffuf -u https://target/FUZZ -w 01-recon-wordlists/01-api-endpoints.txt

# nuclei / dalfox examples
dalfox file 02-xss-payloads/01-markdown-xss-payloads.md
```

## Notes

- `02-xss-payloads/img-upload-payloads/`: filenames contain the actual XSS payloads for upload testing. Do not rename; some OSes struggle with special chars, copy single files as needed.
- `08-misc-scripts/sample.rar`: legacy unverified binary, kept for reference. Remove if unneeded.
- WAF payloads are endpoint-specific, not universal bypasses. Credit to original authors.
- See also: https://github.com/0xInfection/Awesome-WAF for WAF detection.

## Tags

`bug-bounty` `wordlist` `fuzzing` `xss` `sqli` `ssrf` `lfi` `waf-bypass` `recon` `payloads`
