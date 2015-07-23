# CodeWork





### nfsv4 ACLs
=begin
r : READ_DATA			or LIST_DIRECTORY
w : WRITE_DATA      or ADD_FILE
p : APPEND_DATA     or ADD_SUBDIRECTORY
R : READ_NAMED_ATTRS
W : WRITE_NAMED_ATTRS
x : EXECUTE         or SEARCH_DIRECTORY
D : DELETE_CHILD
a : READ_ATTRIBUTES
A : WRITE_ATTRIBUTES
d : DELETE
c : READ_ACL
C : WRITE_ACL
o : WRITE_OWNER
s : SYNCHRONIZE
=cut
my %acls = ('r' => 'READ_DATA', 'w' => 'WRITE_DATA', 'p' => 'APPEND_DATA', 'R' => 'READ_NAMED_ATTRS', 
'c' => 'READ_ACL','C' => 'WRITE_ACL', 'x' => 'EXECUTE');

my @unknowns = ('a' => 'READ_ATTRIBUTES',
                'A' => 'WRITE_ATTRIBUTES',
				'D'  => 'DELETE_CHILD',
				'd'  => 'DELETE',
				's'  => 'SYNCHRONIZE',
				'o'  => 'WRITE_OWNER',
				'W'  => 'WRITE_NAMED_ATTRS');

### deleting the files or subdirectories created under /home				
				
my $sharedDrive = '/home/';

my @AclKeys = keys %acls;

foreach (@ACLs){

      #### read the directory files
      if($_ eq 'r'){
	       print "Acl is $_: %acls{$_}\n";
		   ## open directory
          # opendir my $dir, $sharedDrive or die "Cannot open directory: $!";
		  print "Can read\n" if -r "$sharedDrive";
	  }
	  
	  #### write files in the directory
	   if($_ eq 'w'){
	       print "Acl is $_: %acls{$_}\n";
		   ## open directory
		   print "Can read\n" if -w "$sharedDrive";


	  }
	  
	  
	  ####  ADD_SUBDIRECTORY in the directory
	   if($_ eq 'p'){
	       print "Acl is $_: %acls{$_}\n";
		   ## open directory
		   my $fh = opendir($_);
		   ### read directory
		   readdir($fh);

	  }	  
	  
	  ### search file in the directory
	  if($_ eq 'x'){
	       print "Acl is $_: %acls{$_}\n";
		   ## open directory
		   print "Can read\n" if -x "$sharedDrive";


	  }
	  
	  
	  ### READ_ACL of the directory
	  if($_ eq 'c'){
	       print "Acl is $_: %acls{$_}\n";
		   ## open directory
		   my $fh = opendir($_);
		   ### read directory
		   readdir($fh);

	  }	  
	  
	  ### WRITE_ACL of the directory
	  if($_ eq 'C'){
	       print "Acl is $_: %acls{$_}\n";
		   ## open directory
		   my $fh = opendir($_);
		   ### read directory
		   readdir($fh);

	  }		  
	  


}
