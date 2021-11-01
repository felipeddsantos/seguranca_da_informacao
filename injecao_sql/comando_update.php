$hashed_pwd = sha1($input_pwd);
$sql = "UPDATE credential SET nickname = ’$input_nickname’, salary = 50000;#’,
email = ’$input_email’, address = ’$input_address’, Password = ’$hashed_pwd’,
PhoneNumber = ’$input_phonenumber’ WHERE ID = $id;";
$conn -> query($sql);
