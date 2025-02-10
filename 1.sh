#!/bin/bash
PATH=/opt/someApp/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
get_size() {
	local path="$1"
        local size=$(du -sh "$path" | awk '{print $1}')
        echo "$size"
}

process_directory() {
        local dir="$1"
	local output_file='/home/student_bpk1/'
        echo "Directory: $dir ($(get_size "$dir"))"
        for item in "$dir"/*; do
                if [ -f "$item" ]; then
                        echo "File: $item ($(get_size "$item"))"
                elif [ -d "$item" ]; then
                process_directory "$item"
                fi
        done
}
process_directory '.' >> 'output_file'

