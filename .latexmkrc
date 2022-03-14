add_cus_dep( 'acn', 'acr', 0, 'makeglossaries' );
add_cus_dep( 'glo', 'gls', 0, 'makeglossaries' );
add_cus_dep( 'tdn', 'tld', 0, 'makeglossaries' );
add_cus_dep( 'syg', 'syi', 0, 'makeglossaries' );
$clean_ext .= " acr acn alg glo gls glg ddn dld dlg slg syg syi tdn tld tlg ";
sub makeglossaries {
  my ($base_name, $path) = fileparse( $_[0] );
  pushd $path;
  my $return = system "makeglossaries", $base_name;
  popd;
  return $return;
} 
