#!/bin/bash
# ====== PASTE ANYTHING BELOW THIS LINE ======
: <<'CONTENT'
1. Add name
2. Delete name
3. Display names
4. Exit
Enter the Choice: 1
Enter a name: Prajwal
1. Add name
2. Delete name
3. Display names
4. Exit
Enter the Choice: 1
Enter a name: Amrita
1. Add name
2. Delete name
3. Display names
4. Exit
Enter the Choice: 1
Enter a name: Kavya
1. Add name
2. Delete name
3. Display names
4. Exit
Enter the Choice: 1
Enter a name: Drishti
1. Add name
2. Delete name
3. Display names
4. Exit
Enter the Choice: 3
['Prajwal', 'Amrita', 'Kavya', 'Drishti']
1. Add name
2. Delete name
3. Display names
4. Exit
Enter the Choice: 2
Deleted name is: Drishti
1. Add name
2. Delete name
3. Display names
4. Exit
Enter the Choice: 3
['Prajwal', 'Amrita', 'Kavya']
1. Add name
2. Delete name
3. Display names
4. Exit
Enter the Choice: 4
Exiting program.
CONTENT
# ====== END PASTE ======

# Print everything inside the CONTENT block
sed -n "/^: <<'CONTENT'$/,/^CONTENT$/p" "$0" | sed '1d;$d'
