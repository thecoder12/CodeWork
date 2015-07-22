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

use XML::Simple;
$path = 'text2xml.xml';
open my $fh, '>:encoding(iso-8859-1)', $path or die "open($path): $!";
XMLout($final, OutputFile => $fh);

sub createHash{
	
	my $val = shift;
	my @x = split('\.',$val); 
	my $i = 0;
	my $f = {};
	while($i < scalar(@x)){
		
		$f->{$x[$i+1]} = '['.$x[$i+2].']';
		
		if(exists($final->{$x[$i]})){
			print "second\n";
			#print Dumper(\$f);	
			#$final->{$x[$i]}->[1] = ($final, $f);
			$final->{$x[$i]}->{$x[$i+1]} = $f;
		}
		else{
			print "first\n";
			#$final->{$x[$i]}->[0] = ($final, $f);
			$final->{$x[$i]}->{$x[$i+1]} = $f;
		}
		
		$i = $i+3;
	}

}



__DATA__
a.c=xyz
a.b=abc
b.c=qqq
a.d=www
z=zzz
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