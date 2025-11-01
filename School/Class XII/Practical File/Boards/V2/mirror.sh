#!/bin/bash
# ====== PASTE ANYTHING BELOW THIS LINE ======
: <<'CONTENT'
CONTENT
# ====== END PASTE ======

# Print everything inside the CONTENT block
sed -n "/^: <<'CONTENT'$/,/^CONTENT$/p" "$0" | sed '1d;$d'
