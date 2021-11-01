$input_uname = $_GET[’username’];
$input_pwd = $_GET[’Password’];
$hashed_pwd = sha1($input_pwd);
$sql = "SELECT id, name, eid, salary, birth, ssn, address, email, nickname, Password FROM credential WHERE name = ’$input_uname’ and Password = ’$hashed_pwd’";
$result = $conn -> query($sql);
