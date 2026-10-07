"""Turn the ad scripts in scripts.json into voiceover MP3s with ElevenLabs."""

import json
import os
from pathlib import Path

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "JBFqnCBsd6RMkjVDRZzb")
MODEL_ID = os.getenv("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2")
OUTPUT_DIR = Path("output")


def main() -> None:
    if not API_KEY:
        raise SystemExit("Missing ELEVENLABS_API_KEY. Copy .env.example to .env and add your key.")

    client = ElevenLabs(api_key=API_KEY)
    scripts = json.loads(Path("scripts.json").read_text(encoding="utf-8"))
    OUTPUT_DIR.mkdir(exist_ok=True)

    for script in scripts:
        for lang, text in script["versions"].items():
            audio = client.text_to_speech.convert(
                voice_id=VOICE_ID,
                model_id=MODEL_ID,
                text=text,
                output_format="mp3_44100_128",
            )
            out_file = OUTPUT_DIR / f"{script['id']}_{lang}.mp3"
            with open(out_file, "wb") as f:
                for chunk in audio:
                    f.write(chunk)
            print(f"✓ {script['format']} [{lang}] → {out_file}")


if __name__ == "__main__":
    main()
