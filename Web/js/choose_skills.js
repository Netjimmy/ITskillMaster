function doFirst(){
	document.getElementById('theForm').onsubmit=addList;	
}
var tasks=[];
function addList(){
	var task = document.getElementById('task');
	var message = document.getElementById('message');
	var output='';
	
	if(task.value){
		tasks.push(task.value)
		
		for(var i = 0;i<tasks.length;i++){
			output+='<li>'+tasks[i]+'</li>'
		}		
		message.innerHTML=output;
	}
	 return false;		
}
window.addEventListener('load',doFirst,false);

.on('click', function(d){
	var output='';
	var message = document.getElementById('');
	output += output+='<li>'+tasks[i]+'</li>';
	message.innerHTML=output;	
});