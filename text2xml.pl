use Data::Dumper;

my @data;
my $final = {};
while (<DATA>){
	last if /^__END__$/;         # stop when __END__ is encountered
	s/\n//gsi;
	s/=/./gsi;
	push (@data,$_);
}

foreach (@data){
	print "$_ \n";
	createHash($_);
}
print Dumper(\$final);

sub createHash{
	
	my $val = shift;
	my @x = split('\.',$val); 
	my $i = 0;
	my $f = {};
	while($i < scalar(@x)){
		
		$f->{$x[$i+1]} = '['.$x[$i+2].']';
		
		if(exists($final->{$x[$i]})){
			print "second\n";
			$final->{$x[$i]} = ($final->{$x[$i]}, $f);
		}
		else{
			print "first\n";
			$final->{$x[$i]} = ($final->{$x[$i]}, $f);	
		}
		

		$i = $i+3;
		#print Dumper(\$final);	
	}

}



__DATA__
a.c=xyz
a.b=abc

__END__

a.b='xyz'
a.c='abc'
d='def'
a.e='ghi'

## expected output
<a>
	<b>xyz</b>
	<c>abc</c>
	<e>ghi</e>
</a>	
<d>de</d>

%h->{a}->{b} = 'xyz'
%h->{a}->{c} = 'abc'
%h->{d}		 = 'def'
%h->{a}->{e} = 'ghi'
