<?php


namespace App\Http\Controllers;


use Illuminate\Http\Request;



class EstadoController extends Controller

{
    
	public function show($lat, $long)
	{
                               
		$data = array($lat, $long);
               
		$result = shell_exec('python /var/www/html/Urban/app/Http/Controllers/Scripts/Estado.py ' . escapeshellarg(json_encode($data)));

     		$resultData = json_decode($result, true);
    
           	return($resultData);
        
	}
}
