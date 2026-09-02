import os
import requests

playlists = {
    "ulusalkanal.m3u8": "https://yt.tecostream.xyz/live/ulusalkanal",
    "beinsportshaber.m3u8": "https://yt.tecostream.xyz/live/beinsportshaber",
    "cnnturk.m3u8": "https://yt.tecostream.xyz/live/cnnturk",
    "ekoturk.m3u8": "https://yt.tecostream.xyz/live/ekoturk",
    "krttv.m3u8": "https://yt.tecostream.xyz/live/krttv",
    "ahaber.m3u8": "https://yt.tecostream.xyz/live/ahaber",
    "sozcutelevizyonu.m3u8": "https://yt.tecostream.xyz/live/sozcutelevizyonu",
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

output_dir = os.path.dirname(os.path.abspath(__file__))

for filename, url in playlists.items():

    print(f"Processing {filename}...")

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=True,
            timeout=20
        )

        response.raise_for_status()

        lines = [
            "#EXTM3U",
            "#EXT-X-VERSION:3",
            "#EXT-X-STREAM-INF:BANDWIDTH=7680000",
            response.url
        ]

        output_path = os.path.join(output_dir, filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

        print(f"Created {output_path}")

    except requests.HTTPError as e:
        print(f"ERROR {filename}: HTTP {response.status_code} - {response.url}")
        print("Skipping this playlist and continuing...")

    except requests.RequestException as e:
        print(f"ERROR {filename}: {e}")
        print("Skipping this playlist and continuing...")

    except Exception as e:
        print(f"ERROR {filename}: Unexpected error: {e}")
        print("Skipping this playlist and continuing...")

print("All playlists processed.")
