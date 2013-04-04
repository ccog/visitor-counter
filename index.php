<?php
$current_count = system("python check_num.cgi");
echo " people found out about this cool website before you. Poser.\n"
system("python increment.cgi");
system("python time_check.cgi");
?>
