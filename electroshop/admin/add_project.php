<?php
$name = $_POST['name'];
$price = $_POST['price'];
$desc = $_POST['description'];

$db = new SQLite3('../backend/database/shop.db');
$stmt = $db->prepare('INSERT INTO products (name, price, description) VALUES (:name, :price, :description)');
$stmt->bindValue(':name', $name, SQLITE3_TEXT);
$stmt->bindValue(':price', $price, SQLITE3_FLOAT);
$stmt->bindValue(':description', $desc, SQLITE3_TEXT);
$stmt->execute();

echo "Товар '$name' добавлен! <a href='index.php'>Назад</a>";
?>
