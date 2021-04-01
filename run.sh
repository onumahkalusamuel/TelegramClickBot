phone='phone.txt'
#Visit Action
for i in 0
do
   while read p
     do
       python __v.py $p $i
     done < $phone
done
echo "Sleeping for 10 seconds"
sleep 10

#Join Action
for i in 0
do
   while read p
     do
       python __j.py $p $i
     done < $phone
done
echo "Sleeping for 10 seconds"
sleep 10

bash run.sh
