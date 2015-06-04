substrings('abc');
sub substrings {
  my $string = shift;

  my @result = ();

  foreach my $start (0..length($string)-1) {
    my $substr = substr($string, $start);
    while (length($substr)) {
        push @result, $substr;
        chop($substr);
    }
  }

  print @result;
}