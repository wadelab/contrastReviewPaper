#!/bin/bash

# Set the desired DPI and width in pixels
DPI=300
WIDTH_CM=14

# Convert width from cm to pixels (since 1 inch = 2.54 cm)
WIDTH_PIXELS=$(echo "$WIDTH_CM * $DPI / 2.54" | bc)

# Loop through all PDF files in the directory
for file in *.pdf; do
  # Extract the base name of the file (without extension)
  base_name="${file%.pdf}"

  # Convert PDF to TIFF
  convert -density $DPI "$file" -resize ${WIDTH_PIXELS}x -units PixelsPerInch "${base_name}.tiff"
done

