# NOTE: These instructions are for linux with docker installed

# Running FSDS from official binary
```
make build_fsds
make run_fsds xauthority_path=<path/to/Xauthority>
```

# Running UE4 to edit the sim
Follow these instructions to step 5: https://docs.unrealengine.com/4.27/en-US/SharingAndReleasing/Containers/ContainersQuickStart/.

This will get you access to the image `ghcr.io/epicgames/unreal-engine:dev-4.27`.

```
make build_ue4
make run_ue4 xauthority_path=<path/to/Xauthority>
```
Then, inside the container:
```
cd ~/Formula-Student-Driverless-Simulator/AirSim
./setup.sh
```

Clean (optional - useful if builds are playing up)
```
rm -rf build_debug
```

Build
```
./build.sh
```

Run the unreal project
```
~/UnrealEngine/Engine/Binaries/Linux/UE4Editor ~/Formula-Student-Driverless-Simulator/UE4Project/FSOnline.uproject
```

When asked to rebuild the 'Blocks' and 'AirSim' modules, choose 'Yes'. This is the step where the plugin part of AirSim is compiled.

After it builds, it should give you a UE4 editor.

If you make changes to AirLib you have to run build.sh again.

If you make changes to the plugin code or AirLib, you only have to recompile the plugin. This can be done from within the Unreal Editor. go to to Window -> Developer tools -> Modules. Search for AirSim and click Recompile.

# Exporting from UE4
1. Open the UE4Project in the Unreal Editor
2. Ensure 'File' -> 'Package Project' -> 'Build configuration' is set to 'Development' ('Shipping' build does not work...something about version mis-matches: https://github.com/microsoft/AirSim/issues/2826),
3. Choose 'File' -> 'Package Project' -> 'Linux'
4. Select home/ue4/Formula-Student-Driverless-Simulator/export
5. Wait until it finishes (will probably take >15 minutes).


# Running Exported Project
```
make run_ue4 xauthority_path=<path/to/Xauthority>
```

Inside UE4 container:
```
~/Formula-Student-Driverless-Simulator/export/LinuxNoEditor/Blocks.sh -windowed -ResX=1080 -ResY=720
```