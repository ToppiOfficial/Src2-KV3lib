import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from keyvalue import *

kv_doc = KVDocument(format="generic", format_version="{7412167c-06e9-4698-aff2-e63eb59037e7}")

def create_weapon_sound(name: str, vsnd_file: str, volume=0.5, pitch=1.0):
    return KVNode(
        type="csgo_mega",
        preload_vsnds=KVBool(True),
        volume=volume,
        pitch=pitch,
        position_offset=KVArray(0.0, 0.0, 60.0),
        display_broadcast=KVBool(True),
        vsnd_files_track_01=vsnd_file,
        distance_volume_mapping_curve=KVArray(
            KVArray(50.28, 1.0, 0, -0.002969, 0, 0),
            KVArray(267.14, 0.356223, -0.002969, -0.000953, 0, 1),
            KVArray(1100.0, 0, -0.000428, 0, 0, 0)
        ),
        distance_unfiltered_stereo_mapping_curve=KVArray(
            KVArray(30.0, 1, 0, 0, 2, 3),
            KVArray(35.0, 0, 0, 0, 2, 3),
            KVArray(300.0, 0, 0, 0, 2, 3)
        ),
        vsnd_duration=0.301973
    )

# Add roots
kv_doc.add_root("Weapon_SMG_SILVERWOLF.Clipout",
                create_weapon_sound("Clipout", "weapons/models/toppi/smg_silverwolf/smg_silverwolf/sounds/smg_silverwolfclip_out.vsnd"))
kv_doc.add_root("Weapon_SMG_SILVERWOLF.Clipin",
                create_weapon_sound("Clipin", "weapons/models/toppi/smg_silverwolf/smg_silverwolf/sounds/smg_silverwolfclip_in.vsnd"))
kv_doc.add_root("Weapon_SMG_SILVERWOLF.Boltback",
                create_weapon_sound("Boltback", "weapons/models/toppi/smg_silverwolf/smg_silverwolf/sounds/smg_silverwolfslideback.vsnd"))
kv_doc.add_root("Weapon_SMG_SILVERWOLF.Boltforward",
                create_weapon_sound("Boltforward", "weapons/models/toppi/smg_silverwolf/smg_silverwolf/sounds/smg_silverwolfslideforward.vsnd"))
kv_doc.add_root("Weapon_SMG_SILVERWOLF.Charged",
                create_weapon_sound("Charged", "weapons/models/toppi/smg_silverwolf/smg_silverwolf/sounds/smg_silverwolfcharged.vsnd"))

# Remove first root
kv_doc.remove_root("Weapon_SMG_SILVERWOLF.Clipout")

# Serialize
kv_text = kv_doc.to_text()
print(kv_text)
