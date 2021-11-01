$stmt = $conn -> prepare("SELECT id, name, eid, salary, birth, ssn, phoneNumber, address, email, nickname, Password FROM credential WHERE name = ? and Password = ? ");
$stmt -> bind_param("is", $input_uname, $hashed_pwd);
$stmt -> execute();
$stmt -> bind_result($bind_id, $bind_name, $bind_eid, $bind_salary, $bind_birth, $bind_ssn, $bind_phoneNumber, $bind_address, $bind_email, $bind_nickname)
$stmt -> fetch();
