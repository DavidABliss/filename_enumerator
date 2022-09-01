# filename_enumerator
A simple script to renumber the files in a directory using the existing filename template or a user-provided one

This script renames all files in a given directory to add a simple incrementing number to the end of each file. Use this script when you have a directory of files that are in alphabetical order but which use irregular numbering (e.g. <code>file_1a.jpg, file_1b.jpg, file_2a.jpg, file_2b.jpg</code>). The script will maintain the alphabetical order of the files, but the numbers will be simplified to 1, 2, 3, 4, etc. The script will also output a plaintext report of all changed filenames.

Usage:
<code>filename_enumerator.py <path_to_directory></code>

Currently, the script attempts to preserve the original filename by default, but drops whatever text comes after the final undersctore as an attempt to remove the original numbers. For example, by default the script will rename <code>original_file_name_1a.jpg, original_file_name_1b.jpg</code> to <code>original_file_name_1.jpg, original_file_name_2.jpg</code>, preserving every original filename element prior to the final underscore.

Use the <code>-t --template</code> option followed by a string to provide a new template for the renamed files, or if the original filename template doesn't have file numbers separated by an underscore. For example, <code>-t new_template_</code> will produce files named <code>new_template_01, new_template_02, new_template_03, new_template_04</code>, etc. Enclose the template in quotes if it contains a space.

Use the <code>-f --format</code> option followed by a file extension to specify a file format to be targeted for renaming. By default, all files in the target directory will be renamed, but you can use this option to rename only files of a certain type, such as JPEGs. Files that have a different extension will be skipped.

Use the <code>-d --digits</code> option followed by a number to specify the number of digits to be used for the resulting filenames. If this option is not used, the script will use the fewest digits needed to accommodate all files in the directory (i.e. if the directory contains between 10 and 99 files, the renamed files will have two digit numbers).

Use the <code>-i --index</code> option followed by a number to specify the first number in the sequence for the renamed files. By default, the first file in the directory will be given the number 1, but you can use this option if you would like the numbering to start at zero or any number greater than 1.

Use the <code>-v --reverse</code> option to reverse the order of the renamed images. Use this if the files in a directory are in reverse alphabetical order, and the script will sort them so that the file that originally came last alphabetically will now come first.

To do: Add the ability to specify a specific file format to be targeted for renaming, ignoring all other file formats.
