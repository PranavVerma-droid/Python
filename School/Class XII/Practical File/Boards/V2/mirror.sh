#!/bin/bash
# ====== PASTE ANYTHING BELOW THIS LINE ======
: <<'CONTENT'
Hello World!
This will appear *exactly* as written.
Even special chars like $USER or `pwd` won't expand.
CONTENT
# ====== END PASTE ======

# Print everything inside the CONTENT block
sed -n "/^: <<'CONTENT'$/,/^CONTENT$/p" "$0" | sed '1d;$d'
