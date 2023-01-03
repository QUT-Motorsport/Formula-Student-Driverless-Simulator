.PHONY: all help build run run_ue4

FSDS_IMAGE_NAME = fsds_image
UE4_IMAGE_NAME = fsds_ue4_image
export USERNAME=fsds
export HOST_UID=$(shell id -u)

all:
	@echo "usage: make [COMMAND]"
	@echo
	@echo "COMMAND options:"
	@echo "    build_fsds"
	@echo "        - builds the FSDS image"
	@echo "    run_fsds xauthority_path=<path/to/Xauthority>"
	@echo "        - runs the simulator (FSDS)"
	@echo "    build_ue4"
	@echo "        - builds the Unreal Engine 4.27 image"
	@echo "    run_ue4 xauthority_path=<path/to/Xauthority>"
	@echo "        - runs Unreal Engine 4.27"

help: all

build_fsds:
	docker build -f Dockerfile.fsds -t $(FSDS_IMAGE_NAME) \
    --network=host \
	--build-arg USERNAME=$(USERNAME) \
	--build-arg HOST_UID=$(HOST_UID) \
    .

run_fsds:
	docker run \
		-it \
		--rm \
		--privileged \
		--net=host \
		--gpus=all \
		--env=DISPLAY=$(DISPLAY) \
		--env=QT_X11_NO_MITSHM=1 \
		--env=SDL_HINT_CUDA_DEVICE='0' \
		--mount type=bind,source=$$(pwd)/../settings.json,destination=/home/$(USERNAME)/Formula-Student-Driverless-Simulator/settings.json \
		--mount type=bind,source=/tmp/.X11-unix,destination=/tmp/.X11-unix \
		--mount type=bind,source=$(xauthority_path),destination=/home/$(USERNAME)/.Xauthority \
		$(FSDS_IMAGE_NAME) \
		/bin/bash -c /home/$(USERNAME)/FSDS.sh -windowed -ResX=1080 -ResY=720


build_ue4:
	@echo "Before running, follow these instructions to step 5:"
	@echo "https://docs.unrealengine.com/4.27/en-US/SharingAndReleasing/Containers/ContainersQuickStart/"

	docker build -f Dockerfile.ue4 -t $(UE4_IMAGE_NAME) \
	.

run_ue4:
	@echo "Before running, follow these instructions to step 5:"
	@echo "https://docs.unrealengine.com/4.27/en-US/SharingAndReleasing/Containers/ContainersQuickStart/"

	docker run \
		-it \
		--rm \
		--privileged \
		--net=host \
		--gpus=all \
		--env=DISPLAY=$(DISPLAY) \
		--mount type=bind,source=$$(pwd)/..,destination=/home/ue4/Formula-Student-Driverless-Simulator/ \
		--mount type=bind,source=/tmp/.X11-unix,destination=/tmp/.X11-unix \
		--mount type=bind,source=/run/user/1000/gdm/Xauthority,destination=/home/ue4/.Xauthority \
		$(UE4_IMAGE_NAME) \
		/bin/bash

run_exported:
	@echo "Will only work if run_ue4 works and a project has been exported."
	@echo "See `Exporting from UE4` in docker/README.md"
	docker run \
		-it \
		--rm \
		--privileged \
		--net=host \
		--gpus=all \
		--env=DISPLAY=$(DISPLAY) \
		--mount type=bind,source=$$(pwd)/..,destination=/home/ue4/Formula-Student-Driverless-Simulator/ \
		--mount type=bind,source=/tmp/.X11-unix,destination=/tmp/.X11-unix \
		--mount type=bind,source=/run/user/1000/gdm/Xauthority,destination=/home/ue4/.Xauthority \
		$(UE4_IMAGE_NAME) \
		/bin/bash -c "~/Formula-Student-Driverless-Simulator/export/LinuxNoEditor/Blocks.sh -windowed -ResX=1080 -ResY=720"
