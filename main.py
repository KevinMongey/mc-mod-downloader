import customtkinter as ctk
from services.modrinth import search_mods, get_compatible_version, download_mod
from tkinter import filedialog

def search_all_mods():
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
            else:
                print(f"{mod_name}:""No compatible version found")

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        destination_entry.delete(0, "end")
        destination_entry.insert(0, folder)

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

# -------------------
# SETTINGS
# -------------------
settings_frame = ctk.CTkFrame(app)
settings_frame.pack(
    fill="x",
    padx=20,
    pady=20
)
settings_label = ctk.CTkLabel(
    settings_frame,
    text="Settings",
    font=("Arial", 24, "bold")
)
settings_label.pack(
    anchor="w",
    padx=20,
    pady=15
)

#version entry
minecraft_version_label = ctk.CTkLabel(
    settings_frame,
    text="Minecraft Version"
)
minecraft_version_label.pack(
    anchor="w",
    padx=20,
    pady=(0, 5)
)
minecraft_version_entry = ctk.CTkEntry(
    settings_frame,
    placeholder_text="e.g. 1.21.1"
)
minecraft_version_entry.pack(
    anchor="w",
    padx=20,
    pady=(0, 15)
)

#loader dropdown
loader_label = ctk.CTkLabel(
    settings_frame,
    text="Mod Loader"
)
loader_label.pack(
    anchor="w",
    padx=20,
    pady=(0, 5)
)
loader_dropdown = ctk.CTkComboBox(
    settings_frame,
    values=[
        "Fabric",
        "Forge",
        "NeoForge",
        "Quilt"
    ]
)
loader_dropdown.set("Fabric")
loader_dropdown.pack(
    anchor="w",
    padx=20,
    pady=(0,15)
)

#destination file select
destination_label = ctk.CTkLabel(
    settings_frame,
    text="Destination Folder"
)
destination_label.pack(
    anchor="w",
    padx=20,
    pady=(0, 5)
)
destination_entry = ctk.CTkEntry(
    settings_frame,
    width=400
)
destination_entry.pack(
    anchor="w",
    padx=20,
    pady=(0, 10)
)
browse_button = ctk.CTkButton(
    settings_frame,
    text="Browse",
    command=browse_folder
)
browse_button.pack(
    anchor="w",
    padx=20,
    pady=(0, 20)
)

# -------------------
# BOTTOM SECTION
# -------------------

bottom_frame = ctk.CTkFrame(app)
bottom_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 20)
)

# mod list
mod_list_frame = ctk.CTkFrame(bottom_frame)
mod_list_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
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
results_label = ctk.CTkLabel(
    results_frame,
    text="Downloaded Mods",
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