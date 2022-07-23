# Blender2Godot
A very basic plugin to automatically export several Blender meshes to Godot.

To access the GUI, you need to be in Object Mode.

![asd](https://github.com/Perococco/Blender2Godot/blob/develop/doc/eg.png?raw=true)

All meshes selected will be exported individually in their own folder named from the name of the mesh. 

For instance if the folder in the GUI is "Assets", then after exporting the meshes you will get the following files

```bash
Assets
  ├── Cube
  │   └── Cube.glb
  ├── Icosphere
  │   └── Icospher.glb
```

## Todo

- [ ] Persist the folder selection
- [ ] Add the possibility to change some option of the export
