# Src2-KV3Lib

**Src2-KV3Lib** is a Python library for creating, manipulating, and serializing Source 2 KeyValues3 (KV3), such as those used in ModelDoc.

## Requirements

**Python 3.6+**

# Example
```py
root = KVNode("RootNode")
scratch = KVNode("ScratchArea")

bone = KVNode(
    "DefineBone",
    name="test_bone",
    note="Hello this is a test note\nand for multiline as well",
    origin=KVVector3(15.0, 0.0, 0.0),
    angles=KVArray(25.0, 90.0, 90.0),
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

header = KVHeader()
kv_text = root.to_kv(header, key="rootNode")

print(kv_text)
```

**Output**
```
<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:modeldoc28:version{fb63b6ca-f435-4aa0-a2c7-c66ddc651dca} -->
{
    rootNode =     {
        _class = "RootNode"
        model_archetype = ""
        primary_associated_entity = ""
        anim_graph_name = ""
        document_sub_type = "ModelDocSubType_None"
        children = [
            {
                _class = "ScratchArea"
                children = [
                    {
                        _class = "DefineBone"
                        name = "test_bone"
                        note = "Hello this is a test note\nand for multiline as well"
                        origin = [ 15.0, 0.0, 0.0 ]
                        angles = [ 25.0, 90.0, 90.0 ]
                        do_not_discard = false
                        parent_bone = "head_0"
                    },
                ]
            },
        ]
    }
}
```
