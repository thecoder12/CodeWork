@a = ('abcdefg','def','feg','gfedcba');

foreach(@a){


if(check_reverse_exists($_) == 1){last;}

}


sub check_reverse_exists{
my $b = shift @_;
$rev_str = reverse($b);

foreach (@a){
if($rev_str eq $_){
$len = length($rev_str);
$temp = substr($rev_str, $len/2,1);
print "$len $temp";
return 1;
last;
}

}
}