import os
import sys
import shutil
import configparser
import subprocess

# --- CONFIGURABLES ---
WALLBASH_REPO = "https://github.com/HyDE-Project/obsidian"
THEME_NAME = "Wallbash"
WALLBASH_SCRIPT = os.path.expanduser("~/.local/lib/hyde/wallbash.sh")
DCOL_TO_CSS = {
    "background": "--background-primary",
    "foreground": "--text-normal",
    "accent": "--interactive-accent",
    "muted": "--text-muted",
    "border": "--background-modifier-border",
    # Add more mappings as needed
}
# ---------------------

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

def ensure_theme_dir(vault):
    theme_dir = os.path.join(vault, ".obsidian", "themes", THEME_NAME)
    os.makedirs(theme_dir, exist_ok=True)
    return theme_dir

def clone_or_update_repo(theme_dir):
    if os.path.isdir(os.path.join(theme_dir, ".git")):
        subprocess.run(["git", "-C", theme_dir, "pull"], check=True)
    else:
        subprocess.run(["git", "clone", WALLBASH_REPO, theme_dir], check=True)

def get_swww_wallpaper():
    try:
        output = subprocess.check_output("swww query", shell=True, text=True)
        for line in output.splitlines():
            if "image:" in line:
                # Split on 'image:' and take the path, strip whitespace
                path = line.split("image:")[1].strip()
                if os.path.isfile(path):
                    return path
    except Exception as e:
        print(f"Could not detect wallpaper via swww: {e}")
    return None

def run_wallbash(wallpaper_path):
    if not os.path.isfile(WALLBASH_SCRIPT):
        print(f"wallbash.sh not found at {WALLBASH_SCRIPT}")
        sys.exit(1)
    if not os.path.isfile(wallpaper_path):
        print(f"Wallpaper not found: {wallpaper_path}")
        sys.exit(1)
    print(f"[*] Running wallbash on {wallpaper_path} ...")
    subprocess.run(["bash", WALLBASH_SCRIPT, wallpaper_path], check=True)
    dcol_path = wallpaper_path + ".dcol"
    if not os.path.isfile(dcol_path):
        print(f"Failed to generate .dcol file: {dcol_path}")
        sys.exit(1)
    return dcol_path

def dcol_to_css(dcol_path, css_path):
    # Map dcol keys to Obsidian CSS variables
    DCOL_TO_CSS = {
        # Primary backgrounds
        "dcol_pry1": "--background-primary",
        "dcol_pry2": "--background-secondary",
        "dcol_pry3": "--background-secondary-alt",
        "dcol_pry4": "--background-modifier-border",
        # Text
        "dcol_txt1": "--text-normal",
        "dcol_txt2": "--text-muted",
        "dcol_txt3": "--text-faint",
        "dcol_txt4": "--text-accent",
        # Accents and highlights
        "dcol_acc1": "--interactive-accent",
        "dcol_acc2": "--interactive-accent-hover",
        "dcol_acc3": "--highlight-matched",
        "dcol_acc4": "--highlight-active",
        # UI elements
        "dcol_ui1": "--divider-color",
        "dcol_ui2": "--scrollbar-thumb-bg",
        "dcol_ui3": "--scrollbar-thumb-hover-bg",
        # Code blocks
        "dcol_cod1": "--code-background",
        "dcol_cod2": "--code-normal",
        "dcol_cod3": "--code-comment",
        "dcol_cod4": "--code-keyword",
        "dcol_cod5": "--code-string",
        "dcol_cod6": "--code-function",
        # Borders and modifiers
        "dcol_brd1": "--background-modifier-border",
        "dcol_brd2": "--background-modifier-hover",
        # ToDo: Add more as needed, based on .dcol output
    }
    values = {}
    with open(dcol_path) as f:
        for line in f:
            if "=" in line:
                key, val = line.strip().split("=", 1)
                key = key.strip()
                val = val.strip().strip('"')
                values[key] = val
    with open(css_path, "w") as css:
        css.write(".theme-dark {\n")
        for dcol_key, css_var in DCOL_TO_CSS.items():
            if dcol_key in values:
                css.write(f"    {css_var}: #{values[dcol_key]};\n")
        css.write("}\n")

def ensure_manifest(theme_dir):
    manifest = os.path.join(theme_dir, "manifest.json")
    if not os.path.isfile(manifest):
        with open(manifest, "w") as f:
            f.write('{\n'
                    f'  "name": "{THEME_NAME}",\n'
                    '  "version": "1.0.0",\n'
                    '  "minAppVersion": "1.0.0",\n'
                    '  "author": "The HyDE Project",\n'
                    '  "authorUrl": "https://github.com/HyDE-Project"\n'
                    '}\n')

def main():
    print("[*] Detecting Obsidian vault...")
    vault = get_obsidian_vault()
    print(f"[*] Using vault: {vault}")

    print("[*] Ensuring theme directory exists...")
    theme_dir = ensure_theme_dir(vault)

    print("[*] Cloning or updating Wallbash theme repo...")
    clone_or_update_repo(theme_dir)

    # Try to auto-detect wallpaper with swww
    wallpaper_path = get_swww_wallpaper()
    if not wallpaper_path:
        if len(sys.argv) > 1:
            wallpaper_path = sys.argv[1]
        else:
            wallpaper_path = input("Enter the path to your current wallpaper: ").strip()
    print(f"[*] Using wallpaper: {wallpaper_path}")
    dcol_path = run_wallbash(wallpaper_path)

    print("[*] Generating theme.css from .dcol ...")
    css_path = os.path.join(theme_dir, "theme.css")
    dcol_to_css(dcol_path, css_path)

    print("[*] Ensuring manifest.json exists...")
    ensure_manifest(theme_dir)

    print("[*] Installation complete!")
    print("1. Open Obsidian")
    print("2. Go to Settings > Appearance")
    print("3. Click 'Manage' button")
    print(f"4. Select '{THEME_NAME}' from the theme dropdown")
    print("If you change your wallpaper/theme, re-run this script to update the colors.")

if __name__ == "__main__":
    main()