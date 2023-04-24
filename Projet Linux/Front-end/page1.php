<!-- # j'ai essayé de faire qlq traitements avec PHP mais ça a pas marché -->
<?php
	if ($_SERVER['REQUEST_METHOD'] === 'POST') {
		// Récupère le nom d'utilisateur saisi dans le formulaire
		$username = $_POST['username'];

		// Récupère le répertoire personnel de l'utilisateur
		$home_dir = "/home/" . $username;

		// Vérifie si le répertoire existe
		if (file_exists($home_dir)) {
			// Récupère la liste des fichiers et des dossiers dans le répertoire
			$files = scandir($home_dir);
			echo "<ul>";
			foreach ($files as $file) {
			    if ($file != "." && $file != "..") {
			        echo "<li>$file</li>";
			    }
			}
			echo "</ul>";
		} else {
			echo "<p class='error'>Le nom d'utilisateur est invalide.</p>";
		}
	}
	?>