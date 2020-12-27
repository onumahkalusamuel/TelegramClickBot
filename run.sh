phone='phone.txt'
#Message Action
for i in 0 1 2 3 4
do
   while read p
     do
       python __m.py $p $i
     done < $phone
done
echo "Sleeping for 20 seconds"
sleep 20

#Visit Action
for i in 0 1 2 3 4
do
   while read p
     do
       python __v.py $p $i
     done < $phone
done
echo "Sleeping for 20 seconds"
sleep 20

bash run.sh
