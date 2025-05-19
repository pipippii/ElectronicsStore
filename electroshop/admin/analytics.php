<?php
$data = json_decode(file_get_contents('http://localhost:5000/api/analytics'), true);
echo "<h2>Аналитика</h2>";
echo "<p>Всего заказов: {$data['total_orders']}</p>";
echo "<p>Всего пользователей: {$data['total_users']}</p>";
?>