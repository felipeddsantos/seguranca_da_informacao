$sql = "SELECT id, name, eid, salary, birth, ssn, phoneNumber, address, email, nickname, Password FROM credential WHERE name = '$input_uname' and Password = '$hashed_pwd'";

if(!$result = $conn -> query($sql)){

	echo "</div>";
	echo "</nav>";
	echo "<div class = 'container text-center'>";
	die('There was an error running the query [' . $conn->error . ']\n');
	echo "</div>";
}
