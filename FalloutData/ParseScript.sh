#!/bin/bash

awk 'BEGIN {FS = "@@@"; printf "#!/bin/bash\n" > "fdata.sh"} {
printf "curl -X POST -H \"Content-Type:application/json\" -d \x27{ \"created_utc\":%-s, \"score\":%-s, \"domain\":\"%-s\", \"title\":\"%-s\", \"author\":\"%-s\", \"ups\":%-s, \"downs\":%-s, \"num_comments\":%-s, \"permalink\":\"%-s\", \"thumbnail\":\"%-s\", \"url\":\"%-s\" }\x27 http://localhost:5000/fallout/\n ", $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11 > "fdata.sh"
}' fallout.txt