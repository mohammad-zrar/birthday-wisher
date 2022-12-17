while true;
do
echo "Do you want to add another one ? [Y/N]"
read ans
case $ans in [Yy] )
echo "Enter name: "
read name
echo "Enter email address : "
read email
echo "Enter year of birth : "
read year
echo "Enter month of birth : "
read month
echo "Enter day of birth : "
read day
echo "This information added to birthdays.csv"
echo $name","$email","$year","$month","$day >> birthdays.csv
cat information.csv

continue;;
[Nn] ) 
echo "Exiting.."
exit;;
* ) 
echo "Invalid response";;
esac
done
