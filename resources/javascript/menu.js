$li = $('li');
$a = $('a');

$a.on('click', function(e){
  e.preventDefault();
  $li.removeClass('current');
  $(this).parent().addClass('current');
});