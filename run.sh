phone='phone.txt'
#Message Action
for i in 0 1 2 3 4
do
   while read p
     do
       python __m.py $p $i
     done < $phone
done
echo "Sleeping for 60 seconds"
sleep 60

#Visit Action
for i in 0 1 2 3 4
do
   while read p
     do
       python __v.py $p $i
     done < $phone
done
echo "Sleeping for 60 seconds"
sleep 60

bash run.sh
