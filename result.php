<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="style.css">
	<title>Recognized</title>
</head>
<body>
  <a class="logo" href="index.html">
    <img class="logo__img" src="assets/img/logo.png" alt="SeeText" width="25" height="25">
    <span class="logo__text">Text Recognition</span>
  </a>    

	<div class="result__wrapper">
		<h2>RESULT</h2>
		<textarea class="result_textarea" name="result" id="res" cols="30" rows="10">
			<?php $res = $_GET['text_values']; 
			$res_edited = trim($res);
			echo $res_edited ?>
		</textarea>

		<!--  popup -->
		<div class="popupBubble">
		<button class="copy__btn trigger" id="copy_btn">Copy</button>
		<div class="popup">
			<p><strong>Текст скопирован</strong></p>
		</div>
		</div>
		<!--  -->

		<a class="back__btn" id="back_btn" href="index.html">Back</a>

	</div>


	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
	<script src="save.js"></script>
</body>
</html>