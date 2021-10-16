phone='phone.txt'

#Join Action
while read p
  do
    if command -v python3 &> /dev/null
    then python3 __j.py $p 1
    else python __j.py $p 1
    fi
  done < $phone

echo "Sleeping for 30 seconds"
sleep 30

#Message Action
while read p
  do
    if command -v python3 &> /dev/null
    then python3 __m.py $p 1
    else python __m.py $p 1
    fi
  done < $phone

echo "Sleeping for 30 seconds"
sleep 30

#Visit Action
while read p
  do
    if command -v python3 &> /dev/null
    then python3 __v.py $p 1
    else python __v.py $p 1
    fi
  done < $phone

echo "Sleeping for 30 seconds"
sleep 30

bash run.sh
