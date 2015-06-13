
## Q1. Write a program to recursively remove adjacent duplicates in a string
## http://codingtonic.blogspot.in/p/druva.html

@input = qw( 1 2 3 4 4 5 6 7 8 8);
# @input = grep { $_ = $a } @input;
our @final = ();
RemoveAdjDup(\@input);

sub RemoveAdjDup{

	my $ip = shift @_;
	#print "=@$ip=\n";
	
	$first = shift(@$ip);
	$second = shift(@$ip);	
	
	if(!$second)
	{
		unshift(@final,$first);
		return;
	}
	

	if($first == $second){
		unshift(@final,$first);
	}
	else{
		unshift(@final,$first);
		unshift(@$ip,$second);
	}
	print "=@final=\n";
	RemoveAdjDup(\@$ip);

}
print "\n FINAL --> ".reverse(@final)." \n";
