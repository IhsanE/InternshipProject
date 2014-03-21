<?php
$username = $_POST['searchField'];
$fp = fopen('~urlData.txt', 'w');
fwrite($fp, $username);
fclose($fp);
?>
