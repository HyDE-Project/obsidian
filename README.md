# obsidian

HyDE's wallbash template for Obsidian.

## Preview:

![Preview Image](assets/ss1.png)
![Preview Image](assets/ss2.png)
![Preview Image](assets/ss3.png)
![Preview Image](assets/ss4.png)
![Preview Image](assets/ss5.png)

## Automated Installation (Only for use if current theme does not provide an obsidian theme)

This repository now provides a Python install script that:
- Detects your current wallpaper (if using SWWW)
- Uses Wallbash to generate a color palette from your wallpaper
- Converts the palette to a dynamic Obsidian theme (`theme.css`)
- Ensures your Obsidian vault is valid before installing

### Requirements
- Python 3.7+
- [swww](https://github.com/LionyxML/swww) (for automatic wallpaper detection)
- [HyDE/Wallbash](https://github.com/HyDE-Project/hyde)
- `wallbash.sh` (should be installed at `~/.local/lib/hyde/wallbash.sh`)
- `git` (for theme updates)

### Usage

1. Clone this repo anywhere on your system:
   ```sh
   git clone https://github.com/HyDE-Project/obsidian
   cd obsidian
   ```
2. Run the install script:
   ```sh
   python install.py
   ```
   - You will be prompted for your Obsidian vault location. Leave blank to use the default (`~/Documents/Obsidian Vault`).
   - The script will auto-detect your current wallpaper if you use SWWW, or prompt for a wallpaper path.
   - The script will generate a dynamic `theme.css` and place it in your Obsidian theme folder.
3. In Obsidian:
   - Go to **Settings > Appearance**
   - Click **Manage**
   - Select **Wallbash** from the theme dropdown

### Troubleshooting
- The script will only accept a valid Obsidian vault (must contain a `.obsidian` folder).
- If you use a different wallpaper manager, you can provide the wallpaper path manually.
- If you encounter errors, ensure all requirements are installed and your wallpaper path is correct.

### Updating the Theme
- After changing your wallpaper, **re-run the install script** to update your Obsidian theme colors.

## Manual Installation (Recommended)

1. Clone this repo to your obsidian vault's `.obsidian/themes/` directory.

   - Take note that the initial obsidian vault is located at `~/Documents/Obsidian Vault/`, however this is not always the case. Therefore, you may need to set the `OBSIDIAN_VAULT` environment variable to the correct path. This can be done by adding the following:
     - setting it in `~/.config/hyde/hyde.conf` `OBSIDIAN_VAULT=/path/to/your/obsidian/vault` (Recommended)
     - or setting the env in `hyprland.conf` `env = OBSIDIAN_VAULT,/path/to/your/obsidian/vault`
     - or line to your `.bashrc` or `.bash_profile` file or similar rc files

   ```bash
   export OBSIDIAN_VAULT="${HOME}/Documents/Obsidian Vault/"
   git clone https://github.com/HyDE-Project/obsidian "${OBSIDIAN_VAULT}/.obsidian/themes/Wallbash/"
   cd "${OBSIDIAN_VAULT}/.obsidian/themes/Wallbash/"
   ```

2. Now we need to have a copy of the `obsidian.dcol` file in the `~/.config/hyde/wallbash/Wall-Ways` directory.

   ```bash
   cp ./obsidian.dcol ~/.config/hyde/wallbash/Wall-Ways/
   ```

3. Run `hydectl reload` to apply the changes.
   - This will generate the `theme.css` file.

4. Set the theme in Obsidian settings.
   - ⚙Setting > Appearance️ > 📁 Open themes folder️ > Select Wallbash

    ![Preview Image](assets/apply.png)

### Installation preview:

https://github.com/user-attachments/assets/43b47291-9469-40de-9cb7-8b8ed4eb781d

> [!Note]
> After cloning be sure to do step #2 
> `cp ./obsidian.dcol ~/.config/hyde/wallbash/Wall-Ways/`
>


## Updating:

1. Navigate to your obsidian vault
2. `cd ./.obsidian/themes/Wallbash/`
3. git pull
4. `cp ./obsidian.dcol ~/.config/hyde/wallbash/Wall-Ways/ `
5. `hydectl reload`

