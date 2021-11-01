if($bind_id != ""){

	drawLayout($bind_id, $bind_name, $bind_eid, $bind_salary, $bind_birth, $bind_ssn,$bind_phoneNumber, $bind_address, $bind_email, $bind_nickname)
}

else{

	echo "</div>";
	echo "</nav>";
	echo "<div class = 'container text-center'>";
	echo "<div class = 'alert alert-danger'>";
	echo "The account information your provide does not exist.";
	echo "<br>";
	echo "</div>";
	echo "<a href = 'index.html'>Go back</a>";
	echo "</div>";
	
	return;
}
