#!/usr/bin/bash
 
#$http://blog.mclaughlinsoftware.com/2015/05/17/bash-arrays-mysql/
# Assign user and password
username="${1}"
database="${2}"
directory="${3}"
 
# List the parameter values passed.
echo "Username:  " ${username}
echo "Database:  " ${database}
echo "Directory: " ${directory}
echo ""
 
# Define an array.
declare -a cmd
 
# Assign elements to an array.
cmd[0]="actor.sql"
cmd[1]="film.sql"
cmd[2]="movie.sql"
 
# Call the array elements.
for i in ${cmd[*]}; do
  mysql -s -u${username} -p -D${database} < ${directory}/${i} > /dev/null 2>/dev/null
done
 
# Connect and pipe the query result minus errors and warnings to the while loop.
mysql -u${username} -p -D${database} <<<'show tables' 2>/dev/null |
 
# Read through the piped result until it's empty.
while IFS='\n' read list; do
  if [[ ${list} = "Tables_in_sampledb" ]]; then
    echo $list
    echo "----------------------------------------"
  else
    echo $list
  fi
done
echo ""
 
# Connect and pipe the query result minus errors and warnings to the while loop.
mysql -u${username} -p -D${database} <<<'SELECT CONCAT(a.actor_name," in ",f.film_name) AS "Actors in Films" FROM actor a INNER JOIN movie m ON a.actor_id = m.actor_id INNER JOIN film f ON m.film_id = f.film_id' 2>/dev/null |
 
# Read through the piped result until it's empty.
while IFS='\n' read actor_name; do
  if [[ ${actor_name} = "Actors in Films" ]]; then
    echo $actor_name
    echo "----------------------------------------"
  else
    echo $actor_name
  fi
done