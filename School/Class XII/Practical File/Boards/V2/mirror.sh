#!/bin/bash
# ====== PASTE ANYTHING BELOW THIS LINE ======
: <<'CONTENT'
(4, 'ABHAY', 'FASHION STUDIES', 45000.0)
(1, 'RAJESH', 'IT', 60000.0)
(2, 'MANOJ KUMAR', 'HISTORY', 65000.0)
(3, 'ANUSHA', 'MARKETING', 70000.0)
CONTENT
# ====== END PASTE ======

# Print everything inside the CONTENT block
sed -n "/^: <<'CONTENT'$/,/^CONTENT$/p" "$0" | sed '1d;$d'
