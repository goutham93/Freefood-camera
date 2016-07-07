<?php include("./header.php"); ?> <!-- Main --> <?php $files = scandir("./pictures/"); $recent = "-1"; foreach ($files as $file) {
	if((substr($file, -4) == "jpeg") && ($file > $recent)) {
		$recent = $file;
	}
}?>
<script type="text/javascript">
	function incrementSeconds() {
		var seconds = document.getElementById("seconds");
		seconds.innerHTML++;
		if (seconds.innerHTML == "15") {
			location.reload();
		}
	}
	setInterval(incrementSeconds, 1000);
</script>
<div class='container well text-center' style='margin-top:130px'>
	<h1 class='text-center'>Free food in the DGP lounge!</br></h1>	
	<h2 class='text-center'>Here's what is left right now:</h2>
	<img class='center-block' src=./pictures/<?=$recent?> width="800" height="600"></img>
	<h3 class='text-center'>Image taken <span id="seconds">0</span> seconds ago.</br>To get notified of free food, sign up for the mailing list</br>
	<a href="http://www.dgp.toronto.edu/mailman/listinfo/freefood">http://www.dgp.toronto.edu/mailman/listinfo/freefood</a></h3>
	<a class='btn btn-info' href="./timelapse.php">Timelapse</a>
</div>
<?php include("./footer.php"); ?>
	
