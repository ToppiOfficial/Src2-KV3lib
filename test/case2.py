import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from keyvalue import *

# Create root and scratch nodes
root = KVNode(_class="RootNode")
scratch = KVNode(_class="ScratchArea")

# Create a bone node
bone = KVNode(
    _class="DefineBone",
    name="test_bone",
    note="Hello this is a test note\nand for multiline as well",
    origin=KVVector3(15.0, 0.0, 0.0),
    angles=KVVector3(25.0, 90.0, 90.0),
    do_not_discard=KVBool(False),
    parent_bone="head_0"
)

scratch.add_child(bone)
root.add_child(scratch)

root.properties.update({
    "model_archetype": "",
    "primary_associated_entity": "",
    "anim_graph_name": "",
    "document_sub_type": "ModelDocSubType_None"
})

kv_doc = KVDocument()
kv_doc.add_root("rootNode", root)

kv_text = kv_doc.to_text()
print(kv_text)
