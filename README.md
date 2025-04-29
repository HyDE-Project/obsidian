# obsidian

HyDE's wallbash template for Obsidian.

## Preview:

![Preview Image](assets/ss1.png)
![Preview Image](assets/ss2.png)
![Preview Image](assets/ss3.png)
![Preview Image](assets/ss4.png)
![Preview Image](assets/ss5.png)

## Installation:

1. clone this repo to your obsidian vault's `.obsidian/themes/` directory.

- Take note that the initial obsidian vault is located at `~/Documents/Obsidian Vault/`,
  however this is not always the case.
  Therefore, you may need to set the `OBSIDIAN_VAULT` environment variable to the correct path.
  This can be done by adding the following:
  - setting it in ` ~/.config/hyde/hyde.conf` ` OBSIDIAN_VAULT=/path/to/your/obsidian/vault` (Recommended)
  - or setting the env in ` hyprland.conf` ` env = OBSIDIAN_VAULT,/path/to/your/obsidian/vault`
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

3. Run ` hydectl reload` to apply the changes.

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

## TODO

- [ ] Add a script to automate the installation process
