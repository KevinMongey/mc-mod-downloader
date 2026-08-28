import customtkinter as ctk
from services.modrinth import search_mods

def search_all_mods():
    mod_names = mod_textbox.get("1.0", "end")
    mod_names = mod_names.splitlines()

    for mod_name in mod_names:
        if mod_name.strip():
            results = search_mods(mod_name)

            for mod in results:
                print(mod["title"])


# gui
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

app.mainloop()