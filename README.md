# ElevenLabs for the Mexican Market 🇲🇽🎙️

A small demo by [Herbert Beltrán](https://www.linkedin.com/in/herbertbeltran/) showing how Mexican agencies and brands can use ElevenLabs to produce **multilingual voiceovers in minutes instead of days**.

It takes real-world ad formats common in Mexico (radio spots, social video ads, and phone menus) and generates voiceovers in Mexican Spanish, English, and Portuguese with the ElevenLabs API.

---

## 🎧 Listen to the samples

Generated with this project using the ElevenLabs API:

| Format | Mexican Spanish | English | Portuguese |
|---|---|---|---|
| Radio spot (20s) | [▶ es-MX](samples/radio-spot-taqueria_es-MX.mp3) | [▶ en](samples/radio-spot-taqueria_en.mp3) | [▶ pt](samples/radio-spot-taqueria_pt.mp3) |
| Social video ad (15s) | [▶ es-MX](samples/social-ad-inmobiliaria_es-MX.mp3) | [▶ en](samples/social-ad-inmobiliaria_en.mp3) | |
| Phone menu / IVR | [▶ es-MX](samples/ivr-clinica_es-MX.mp3) | | |

## Why this matters

Mexican clients want faster, higher-quality production on tighter budgets. Today a single radio spot often means booking voice talent, studio time, and revision rounds, which takes days and costs the same again for each extra language.

AI voice changes that:

| | Traditional voiceover | With ElevenLabs |
|---|---|---|
| Turnaround | Days | Minutes |
| Extra language | Re-book talent and studio | Same script, new version |
| Last-minute edits | New recording session | Edit text, regenerate |
| Scale | Limited by talent availability | Hundreds of versions per month |

## Business case

`business_case.py` compares monthly costs for an agency. With the sample assumptions below (edit them to match real quotes):

- 20 spots per month × 2 languages = 40 voiceovers
- Traditional: MXN $3,500 per voiceover (talent + studio)
- AI voice: MXN $2,000 monthly plan + MXN $150 review time per voiceover

```
Traditional cost:   $140,000 MXN  (~3 days each)
AI voice cost:        $8,000 MXN  (~1 hour each)
Monthly savings:    $132,000 MXN (94%)
Annual savings:   $1,584,000 MXN
```

> These figures are illustrative assumptions, not market data. The point is the structure of the savings: cost per extra version drops close to zero.

## Go-to-market opportunities in Mexico

1. **Advertising agencies**: radio, TV, and social spots, plus fast A/B variations
2. **Public sector**: accessible public-service announcements for education, health, and tourism campaigns
3. **Tourism**: multilingual audio guides and promotional content for international visitors
4. **Customer service**: IVR menus and voice agents for clinics, banks, and retail
5. **E-learning and corporate training**: narrated courses produced at scale

## How to run it

```bash
git clone https://github.com/herbertbeltran/elevenlabs-mx-demo.git
cd elevenlabs-mx-demo
pip install -r requirements.txt
cp .env.example .env        # then add your ElevenLabs API key
python generate.py          # creates MP3 files in /output
python business_case.py     # prints the cost comparison
```

## Project structure

```
├── samples/           # generated MP3 voiceovers
├── scripts.json       # ad scripts in es-MX, en, and pt
├── generate.py        # turns each script into an MP3 voiceover
├── business_case.py   # traditional vs. AI voice cost comparison
└── .env.example       # API key and voice settings
```

## About me

Marketing Director at [OCTO Marketing Digital](https://www.octomd.com), Zapopan, Jalisco. I've closed more than US$935,000 in business, and I work with brands, agencies, and the Jalisco state government.

📫 [LinkedIn](https://www.linkedin.com/in/herbertbeltran/) · [hbeltran@octomd.com](mailto:hbeltran@octomd.com)
