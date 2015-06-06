## add two largest integers from array
my @input = (1,2,3,4,5,6,7,8,9,2);

@input = reverse sort{$a <=> $b}@input;

print "Sum -> ". ($input[0] + $input[1]);