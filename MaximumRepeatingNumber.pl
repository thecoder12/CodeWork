### Maximum repeating number
## http://codingtonic.blogspot.in/2015/01/maximum-repeating-number.html
use Data::Dumper;

@array = qw(2 1 3 3 4 3 4 1 3);
my %h = ();
foreach (@array){
	$h{$_}++;
}
# @val = sort values %h;
my @keys = sort { $h{$b} <=> $h{$a} } keys(%h);

print Dumper(\@keys[0]);