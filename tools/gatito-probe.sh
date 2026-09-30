#!/bin/sh
# Gatito Probe v0.1 — read-only Linux handheld inventory.
# Prints a report to stdout. It does not select a driver, change settings, or upload data.

set -u

section() {
    printf '\n===== %s =====\n' "$1"
}

show_file() {
    path=$1
    if [ -r "$path" ]; then
        printf '\n--- %s ---\n' "$path"
        case "$path" in
            */device-tree/compatible|*/device-tree/model)
                if command -v tr >/dev/null 2>&1; then
                    tr '\000' '\n' < "$path" 2>/dev/null
                else
                    printf 'present (use a null-aware reader to inspect)\n'
                fi
                ;;
            *)
                sed -n '1,60p' "$path" 2>/dev/null
                ;;
        esac
    else
        printf '\n--- %s: unavailable ---\n' "$path"
    fi
}

section 'Gatito Probe'
printf 'Version: 0.1\n'
printf 'Mode: read-only; output is not uploaded automatically.\n'

section 'System'
if command -v uname >/dev/null 2>&1; then
    uname -a
else
    printf 'uname: unavailable\n'
fi
show_file /etc/os-release
show_file /etc/issue
show_file /proc/version
show_file /proc/device-tree/model
show_file /proc/device-tree/compatible

section 'Video device nodes'
found_video_node=0
for node in /dev/dri /dev/fb*; do
    if [ -e "$node" ]; then
        found_video_node=1
        ls -ld "$node" 2>/dev/null
    fi
done
if [ "$found_video_node" -eq 0 ]; then
    printf 'No /dev/dri or /dev/fb* nodes found.\n'
fi

section 'Selected display/runtime environment'
if command -v printenv >/dev/null 2>&1; then
    for name in SDL_VIDEODRIVER SDL_RENDER_DRIVER SDL_AUDIODRIVER DISPLAY WAYLAND_DISPLAY LD_LIBRARY_PATH; do
        value=$(printenv "$name" 2>/dev/null || true)
        if [ -n "$value" ]; then
            printf '%s=%s\n' "$name" "$value"
        else
            printf '%s=<unset>\n' "$name"
        fi
    done
else
    printf 'printenv unavailable; selected environment values not collected.\n'
fi

section 'Candidate graphics libraries'
found_library=0
for root in /usr/lib /usr/lib32 /usr/lib/aarch64-linux-gnu /usr/lib/arm-linux-gnueabihf /lib /lib32 /opt/muos/frontend/lib; do
    [ -d "$root" ] || continue
    for candidate in \
        "$root"/libEGL.so* \
        "$root"/libGLES*.so* \
        "$root"/libMali*.so* \
        "$root"/libmali*.so* \
        "$root"/libSDL2*.so* \
        "$root"/libSDL3*.so* \
        "$root"/libgbm.so*; do
        if [ -e "$candidate" ] || [ -L "$candidate" ]; then
            found_library=1
            ls -ld "$candidate" 2>/dev/null
        fi
    done
done
if [ "$found_library" -eq 0 ]; then
    printf 'No matching libraries found in the standard search paths.\n'
fi

section 'PortMaster helpers'
for name in pm_platform_helper get_controls gptokeyb; do
    if command -v "$name" >/dev/null 2>&1; then
        printf '%s: %s\n' "$name" "$(command -v "$name" 2>/dev/null)"
    else
        printf '%s: unavailable in PATH\n' "$name"
    fi
done

section 'Interpretation'
printf '%s\n' 'This report lists candidates, not proof of the active graphics driver.'
printf '%s\n' 'To prove libraries used by a running game, collect its SDL/EGL log or inspect /proc/<pid>/maps while it is running.'
printf '%s\n' 'Review paths and environment values before sharing the report.'
printf '%s\n' 'No driver was selected or changed.'
