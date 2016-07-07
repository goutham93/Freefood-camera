<?php include("assets/templates/header.php"); ?>
<!-- Main -->
<?php
$files = scandir("./pictures/");
sort($files);
?>
<script type="text/javascript">
        var i = 2; // first two will be parent and the pictures folder
        var files = <?php echo json_encode($files); ?>;
        console.log(files);
	function nextPicture() {
                var picture = document.getElementById("picture");
                console.log(files[i]);
		picture.src = "./pictures/" + files[i];
                i++;
        }
        setInterval(nextPicture, 1000);
</script>
<div class='container well text-center' style='margin-top:130px'>
        <h1>Free food in the DGP lounge!</br></h1>
        <h2>Here's the timelapse of what was left:</h2>
        <img id='picture' class='center-block' src=./pictures/ width="800" height="600"></img>
        <h3>To get notified of free food, sign up for the mailing list</br>
        <a href="http://www.dgp.toronto.edu/mailman/listinfo/freefood">http://www.dgp.toronto.edu/mailman/listinfo/freefood</a></h3>
</div>
<?php include("assets/templates/footer.php"); ?>


