#!/bin/bash

# Ellenőrizze, hogy a megfelelő számú argumentum meg van-e adva
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <value_to_add> <output_file>"
    exit 1
fi

# Az argumentumok változókhoz rendelése
value_to_add="$1*60"
output_file="$2"

# Olvassa be a rendszer uptime-ját másodpercben
uptime_seconds=$(awk '{print $1}' /proc/uptime)

# Ellenőrizze, hogy az uptime érvényes lebegőpontos szám-e
if ! [[ "$uptime_seconds" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; then
    echo "Failed to read valid uptime!"
    exit 1
fi

# Adja össze az értékeket az awk segítségével
new_value=$(awk "BEGIN {print $uptime_seconds + $value_to_add}")

# Írja az új értéket a fájlba
echo "$new_value" > "$output_file"

echo "Updated value written to $output_file"
