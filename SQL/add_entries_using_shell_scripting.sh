#!/bin/bash

db='example_db_name.sqlite'
table='table1'

echo -n "===Welcome=="
echo -n "Please Enter the User Details:"

while [ 1 ]
do
    echo -n "First Name : "
    read fname
    if  [ '$fname' -eq '' ]; then echo "Value Needed"; exit 1;fi 

    echo -n "Last Name : "
    read lname
    if  [ '$lname' -eq '' ]; then echo "Value Needed"; exit 1;fi

    echo -n "Phone Number : "
    read phone_number
    if  [ '$phone_number' -eq '' ]; then echo "Value Needed"; exit 1;fi

    sqlite3 "$db" "INSERT INTO $table VALUES('$fname', '$lname', '$phone_number')" && echo -n "$fname Entered" || echo "ERROR"

    echo -n "Would You Like To continue ? (Y/N) : "
    read ans

    if [ '$ans' -eq 'n']
    then 
        echo -n "Good Bye....."
        exit 0
    else
        clear
    fi
done