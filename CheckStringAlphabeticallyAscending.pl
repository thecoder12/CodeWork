## check if the string is in progression of alphabets acsii-wise
$str = 'abca';

@ASCII = unpack("C*", $str);

print "==@ASCII=";

$i=0;

while ($i < $#ASCII){

if($ASCII[$i] > $ASCII[++$i]){
print "Not in sequence...$i";
last;
}

}