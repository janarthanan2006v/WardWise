# Dataset

**Product:** WardWise (E-ENT-07)

**Owner:** Janarthanan V (411723205021)

**Official publisher:** World Health Organization (WHO)

**Collection source:** WHO-hosted files from `cdn.who.int`, discovered through WHO publication and programme pages

**Licence / terms:** Both Week 1 sample publications state CC BY-NC-SA 3.0 IGO on their copyright pages. They may be copied and redistributed for non-commercial purposes with attribution. Checked on 23 October 2026.

**Privacy:** These are public clinical guidance documents and contain no patient records or private hospital data.

**How to rebuild:** `python tools/download.py urls.txt`

**How to recount:** `python tools/count_pages.py`

## Week 1 collection

| Files | Pages | Publication years | Downloaded on | Broken | Scanned |
|---:|---:|---|---|---:|---:|
| 2 PDFs | 216 | 2022-2025 | 23 Oct 2026 | 0 | 0 |

| File | Official source URL | Pages | SHA-256 |
|---|---|---:|---|
| `who_2025_kangaroo-mother-care-clinical-practice-guide.pdf` | https://cdn.who.int/media/docs/default-source/newborn-health/kangaroo_mother_care_a_clinical_practice_guide.pdf?download=true&sfvrsn=4211ba4c_4 | 140 | `7fc6d255f2eca96dc36eb22612f6105be9022f2370dfcac71d33e0098cfdc7b6` |
| `who_2022_implementing-end-tb-strategy-essentials.pdf` | https://cdn.who.int/media/docs/default-source/hq-tuberculosis/implementing-the-end-tb-strategy-the-essentials_-2022-update.pdf?download=true&sfvrsn=5f3c748b_3 | 76 | `d358d04ab3ba0f44317e257202fd6dfd06eb4951e7ce2d27f873a72449049bc5` |

The full local collection is stored in `data/raw/`, which is excluded from Git. The two Week 1 files are copied to `data/sample/` because their licence permits non-commercial redistribution with attribution. `data/manifest.csv` records the source URL, download date, byte size and full SHA-256 hash for each file.

## Collection notes

- The downloader identifies this repository in its User-Agent, waits two seconds between new downloads, skips existing files, checks `robots.txt`, validates the PDF signature and logs each successful file.
- On 23 October 2026, `https://cdn.who.int/robots.txt` returned HTTP 403 while the public documents themselves remained openly downloadable. The script treats an unavailable robots file as inconclusive and proceeds slowly. No blocked path, login, captcha or paywall was bypassed.
- This 216-page set is the Week 1 sample, not the project's final dataset. WardWise's tracker target remains 60+ WHO guideline documents and 6,000+ pages.
- Internal hospital SOPs are intentionally excluded until the hospital authorizes access and provides a secure tenant-specific storage process.
