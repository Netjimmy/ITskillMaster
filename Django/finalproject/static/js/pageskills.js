/* function doFirst(){
	document.getElementsById('link').onclick=addList;	
}
var links=[]; */

/* function addList(){
	var link = document.getElementById("link");
							var output='';
							link.onclick = function() {
								
								output+=link.name;
								selectedSkills.innerHTML=output;
								
							};
} */
/* function addList(){
	var link = document.getElementsByClassName('link');
	var selected = document.getElementById('selectedSkills');
	var output = '';
	if(link.name){
		links.push(link.value)
		for(var i = 0; i<links.length; i++){
			output += links[i];
		}		
		selected.innerHTML = output;
	}
} */

/* var link = document.getElementsByClassName("link");
							link.onclick = function() {
								var output='';
								output+=link.name;
								selected.innerHTML=output;
							}; */
							
	/* var link = document.getElementById("link");
	var output='';
	link.onclick = function() {
		output+=link.name;
		selectedSkills.innerHTML=output;							
	}; */
	
	/* var output='';
	document.getElementById("link").onclick = function() {
		output+=document.getElementById("link").name+'<br>';
		selectedTable.innerHTML=output;							
	}; */
	
	var output='';
	document.getElementById("net").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='.net' checked='checked'>.Net</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("ajax").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='ajax' checked='checked'>AJAX</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("android").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='android' checked='checked'>Android</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("app").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='app' checked='checked'>App</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("asp").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='asp.net' checked='checked'>ASP.NET</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("c").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='c' checked='checked'>C</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("c#").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='c#' checked='checked'>C#</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("cnet").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='c.net' checked='checked'>C.NET</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("c++").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='c++' checked='checked'>C++</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("css").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='css' checked='checked'>CSS</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("html").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='html' checked='checked'>HTML</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("iOS").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='ios' checked='checked'>iOS</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("Java").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='java' checked='checked'>Java</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("JavaScript").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='javascript' checked='checked'>JavaScript</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("jQuery").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='jquery' checked='checked'>jQuery</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("JSP").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='jsp' checked='checked'>JSP</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("Linux").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='linux' checked='checked'>Linux</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("MySQL").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='mysql' checked='checked'>MySQL</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("Objective").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='objective-c' checked='checked'>Objective-C</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("PHP").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='php' checked='checked'>PHP</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("Python").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='python' checked='checked'>Python</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("Sql").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='sql' checked='checked'>Sql</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("Unix").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='unix' checked='checked'>Unix</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("Visual").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='visualbasic' checked='checked'>Visual Basic</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	var output='';
	document.getElementById("XML").onclick = function() {
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='xml' checked='checked'>XML</li>"+'<br>';
		sortable.innerHTML=output;							
	};
	
	
	
	
	
	/* var output='';
	document.getElementById("net").onclick = function() {
		output+=document.getElementById("net").value+'<br>';
		sortable.innerHTML=output;							
	}; */
	
	/* document.getElementById("sub").onclick = function() {
		output+=document.getElementById("sub").name+'<br>';
		selectedTable.innerHTML=output; */

	/* 	var sortable = document.getElementById('sortable');
		output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='"+d.value+"' checked='checked'>"+d.text+"<span class='buttons' type='button'>x</span></li>"
		sortable.innerHTML=output;
	}; */
	
	/* .on('click', function(d) {
				  var sortable = document.getElementById('sortable');
					output += "<li class='ui-state-default'><span class='ui-icon ui-icon-arrowthick-2-n-s'></span><input type='checkbox' name='id' value='"+d.tag+"' checked='checked'>"+d.text+"<span class='buttons' type='button'>x</span></li>"
					sortable.innerHTML=output;
	}); */
	
	/* document.write('這是第一行<br>'); */
	
	/* var link2 = document.getElementById("net");
	var output='';
	link2.onclick = function() {
		output+=link2.name;
		selectedSkills.innerHTML=output;							
	};
	
	var link3 = document.getElementById("ajax");
	var output='';
	link3.onclick = function() {
		output+=link3.name;
		selectedSkills.innerHTML=output;							
	}; */
	
	
	
	