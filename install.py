import os
import subprocess
import sys

WALLBASH_REPO = "https://github.com/HyDE-Project/obsidian"
THEME_NAME = "Wallbash"


def get_obsidian_vault():
    default = os.path.expanduser("~/Documents/Obsidian Vault")
    prompt = f"Enter the path to your Obsidian vault (leave blank for default: {default}): "
    vault = input(prompt).strip()
    if not vault:
        vault = default
    if os.path.isdir(vault) and os.path.isdir(os.path.join(vault, ".obsidian")):
        return vault
    print("Invalid vault path: must be a directory containing a .obsidian folder.")
    sys.exit(1)


def main():
    vault = get_obsidian_vault()
    theme_dir = os.path.join(vault, ".obsidian", "themes", THEME_NAME)

    # Clone the Wallbash repo
    if not os.path.isdir(theme_dir):
        subprocess.run(["git", "clone", WALLBASH_REPO, theme_dir], check=True)
    else:
        print(f"Theme directory already exists: {theme_dir}")

    # Copy obsidian.dcol to ~/.config/hyde/wallbash/always/
    dcol_src = os.path.join(theme_dir, "obsidian.dcol")
    dcol_dst_dir = os.path.expanduser("~/.config/hyde/wallbash/always/")
    os.makedirs(dcol_dst_dir, exist_ok=True)
    dcol_dst = os.path.join(dcol_dst_dir, "obsidian.dcol")
    if os.path.isfile(dcol_src):
        subprocess.run(["cp", dcol_src, dcol_dst], check=True)
    else:
        print(f"obsidian.dcol not found in {theme_dir}")
        sys.exit(1)

    # Run hydectl reload
    subprocess.run(["hydectl", "reload"], check=True)
    print("[+] Wallbash theme installed and hydectl reloaded.")


if __name__ == "__main__":
    main()
