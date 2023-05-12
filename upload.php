<?php
if (($_FILES['my_file']['name']!="")){
// Where the file is going to be stored
	$target_dir = "upload/";
	$file = $_FILES['my_file']['name'];
	$path = pathinfo($file);
	$filename = $path['filename'];
	$ext = $path['extension'];
	$temp_name = $_FILES['my_file']['tmp_name'];
	$path_filename_ext = $target_dir.$filename.".".$ext;
 
// Check if file already exists
if (file_exists($path_filename_ext)) {
 // echo "Sorry, file already exists.";
 }else{
 move_uploaded_file($temp_name,$path_filename_ext);
 // echo "Congratulations! File Uploaded Successfully.";
 }

}



// -------------
$python = '<your-path-to-python-intrerp>';

$file_path = $target_dir . '' . $filename . '.' . $ext;

$recognizeText = exec($python . " text_detection_origin.py  --image-path=$file_path");



$filteredText = exec($python . " run.py");
echo $filteredText;


include 'extracted_text_values.php';
// Установка кодировки UTF-8
header('Content-Type: text/html; charset=utf-8');
// Вывод значений на экран
echo implode(' ', $text_values);


// возврат обратно на главную стр
// header('Location: '.'/'); 
?>