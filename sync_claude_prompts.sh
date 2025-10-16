#!/usr/bin/env bash
set -euo pipefail

src_dir=".claude/commands"
dest_dir=".github/prompts"

mkdir -p "$dest_dir"

find "$src_dir" -type f -name "*.md" -print0 | while IFS= read -r -d '' file; do
  rel_path="${file#"$src_dir/"}"

  # Skip files that are not inside a subdirectory
  if [[ "$rel_path" == "$file" || "$rel_path" != */* ]]; then
    continue
  fi

  subdir="${rel_path%%/*}"
  base_name="${rel_path##*/}"

  # Strip the .md suffix before adding the .prompt.md suffix
  base_no_ext="${base_name%.md}"
  cp "$file" "$dest_dir/${subdir}-${base_no_ext}.prompt.md"
done
