import customtkinter as ctk
from services.modrinth import search_mods, get_compatible_version, download_mod
from tkinter import filedialog
from PIL import Image
import requests
import io

def search_all_mods():
    global download_count
    mod_names = mod_textbox.get("1.0", "end").splitlines()
    mc_version = minecraft_version_entry.get()
    loader = loader_dropdown.get().lower()
    dest_folder = destination_entry.get()

    for mod_name in mod_names:
        if mod_name.strip():
            mod = search_mods(mod_name)

            if not mod:
                print(f"{mod_name}: Mod not found")
                continue

            project_id = mod["project_id"]

            compatible_version = get_compatible_version(project_id, mc_version, loader)
            if compatible_version:
                print(f"{mod_name}: "f"{compatible_version['name']}")
                file_path = download_mod(compatible_version, dest_folder)
                print(f"Downloaded to: "f"{file_path}")
                if file_path:
                    display_mod(mod, compatible_version)
                    download_count += 1
                    results_label.configure(text=f"Downloaded Mods: {download_count}")
            else:
                print(f"{mod_name}:""No compatible version found")

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        destination_entry.delete(0, "end")
        destination_entry.insert(0, folder)

def toggle_dark_mode():
    if dark_mode_checkbox.get():
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

# gui card display
def display_mod(mod, version):
    mod_frame = ctk.CTkFrame(
        downloaded_mods_frame
    )
    mod_frame.pack(
        fill="x",
        padx=10,
        pady=5
    )
    try:
        icon_response = requests.get(
            mod["icon_url"]
        )
        icon_response.raise_for_status()
        icon_image = Image.open(
            io.BytesIO(icon_response.content)
        )
        icon_image = icon_image.resize(
            (64, 64)
        )
        icon = ctk.CTkImage(
            light_image=icon_image,
            dark_image=icon_image,
            size=(64, 64)
        )
        icon_label = ctk.CTkLabel(
            mod_frame,
            image=icon,
            text=""
        )
        icon_label.pack(
            side="left",
            padx=15,
            pady=15
        )
    except requests.RequestException:
        print(
            f"Could not download icon for "
            f"{mod['title']}"
        )
    mod_name_label = ctk.CTkLabel(
        mod_frame,
        text=mod["title"],
        font=("Arial", 18, "bold")
    )
    mod_name_label.pack(
        anchor="w",
        padx=15,
        pady=(10, 2)
    )
    description_label = ctk.CTkLabel(
        mod_frame,
        text=mod["description"],
        wraplength=400,
        justify="left"
    )
    description_label.pack(
        anchor="w",
        padx=15,
        pady=(0, 5)
    )
    filename = version["selected_file"]["filename"]
    filename_label = ctk.CTkLabel(
        mod_frame,
        text=f"✓ Downloaded: {filename}"
    )
    filename_label.pack(
        anchor="w",
        padx=15,
        pady=(0, 10)
    )

# gui create
app = ctk.CTk()
app.title("Minecraft Mod Downloader")
app.geometry("900x600")
ctk.set_appearance_mode("dark")


# SETTINGS

settings_frame = ctk.CTkFrame(app)
settings_frame.pack(
    fill="x",
    padx=20,
    pady=20
)
settings_header = ctk.CTkFrame(
    settings_frame,
    fg_color="transparent"
)
settings_header.pack(
    fill="x",
    padx=20,
    pady=15
)
settings_label = ctk.CTkLabel(
    settings_header,
    text="Settings",
    font=("Arial", 24, "bold")
)
settings_label.pack(
    side="left"
)

dark_mode_checkbox = ctk.CTkCheckBox(
    settings_header,
    text="Dark Mode",
    command=toggle_dark_mode
)
dark_mode_checkbox.pack(
    side="right"
)
dark_mode_checkbox.select()

settings_controls = ctk.CTkFrame(
    settings_frame,
    fg_color="transparent"
)
settings_controls.pack(
    fill="x",
    padx=20,
    pady=(0, 20)
)

#version entry
version_frame = ctk.CTkFrame(
    settings_controls,
    fg_color="transparent"
)
version_frame.pack(
    side="left",
    padx=(0, 20)
)
minecraft_version_label = ctk.CTkLabel(
    version_frame,
    text="Minecraft Version"
)
minecraft_version_label.pack(
    anchor="w",
    pady=(0, 5)
)
minecraft_version_entry = ctk.CTkEntry(
    version_frame,
    width=150,
    placeholder_text="e.g. 1.21.1"
)
minecraft_version_entry.pack()

#loader dropdown
loader_frame = ctk.CTkFrame(
    settings_controls,
    fg_color="transparent"
)
loader_frame.pack(
    side="left",
    padx=(0, 20)
)
loader_label = ctk.CTkLabel(
    loader_frame,
    text="Mod Loader"
)
loader_label.pack(
    anchor="w",
    pady=(0, 5)
)
loader_dropdown = ctk.CTkComboBox(
    loader_frame,
    values=[
        "Fabric",
        "Forge",
        "NeoForge",
        "Quilt"
    ],
    width=150
)
loader_dropdown.set("Fabric")
loader_dropdown.pack()

#destination file select
destination_frame = ctk.CTkFrame(
    settings_controls,
    fg_color="transparent"
)
destination_frame.pack(
    side="left",
    fill="x",
    expand=True
)
destination_label = ctk.CTkLabel(
    destination_frame,
    text="Destination Folder"
)
destination_label.pack(
    anchor="w",
    pady=(0, 5)
)
destination_row = ctk.CTkFrame(
    destination_frame,
    fg_color="transparent"
)
destination_row.pack(
    fill="x"
)
destination_entry = ctk.CTkEntry(
    destination_row,
    placeholder_text="Select Minecraft mods folder"
)
destination_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 10)
)
browse_button = ctk.CTkButton(
    destination_row,
    text="Browse",
    width=90,
    command=browse_folder
)
browse_button.pack(
    side="right"
)

# BOTTOM SECTION

bottom_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
bottom_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 20)
)

# mod list
mod_list_frame = ctk.CTkFrame(
    bottom_frame
)
mod_list_frame.pack(
    side="left",
    fill="both",
    expand=False,
    padx=(0, 10)
)
mod_list_frame.configure(
    width=300
)
mod_list_label = ctk.CTkLabel(
    mod_list_frame,
    text="Mod List",
    font=("Arial", 20, "bold")
)
mod_list_label.pack(
    anchor="w",
    padx=20,
    pady=15
)

mod_textbox = ctk.CTkTextbox(
    mod_list_frame
)
mod_textbox.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 10)
)

search_button = ctk.CTkButton(
    mod_list_frame,
    text="Search Mods",
    command=search_all_mods
)
search_button.pack(
    fill="x",
    padx=20,
    pady=(0, 20)
)

# found mods
results_frame = ctk.CTkFrame(bottom_frame)
results_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(10, 0)
)
download_count = 0

results_label = ctk.CTkLabel(
    results_frame,
    text=f"Downloaded Mods: {download_count}",
    font=("Arial", 20, "bold")
)
results_label.pack(
    anchor="w",
    padx=20,
    pady=15
)

# downloaded mods
downloaded_mods_frame = ctk.CTkScrollableFrame(
    results_frame
)
downloaded_mods_frame.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=(0, 10)
)

app.mainloop()