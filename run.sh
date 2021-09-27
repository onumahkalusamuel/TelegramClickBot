phone='phone.txt'

#Join Action
for i in 0 1 2 3 4
do
   while read p
     do
       if command -v python3 &> /dev/null
       then python3 __j.py $p $i
       else python __j.py $p $i
       fi
     done < $phone
done
echo "Sleeping for 30 seconds"
sleep 30

#Message Action
for i in 0 1 2 3 4
do
   while read p
     do
       if command -v python3 &> /dev/null
       then python3 __m.py $p $i
       else python __m.py $p $i
       fi
     done < $phone
done
echo "Sleeping for 30 seconds"
sleep 30

#Visit Action
for i in 0 1 2 3 4
do
   while read p
     do
       if command -v python3 &> /dev/null
       then python3 __v.py $p $i
       else python __v.py $p $i
       fi
     done < $phone
done
echo "Sleeping for 30 seconds"
sleep 30

bash run.sh
