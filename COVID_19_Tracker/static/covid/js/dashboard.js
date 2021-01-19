$(document).ready( function () {
    let data = $('#table_id').DataTable();
} );
function myfunc(){
    let pathElement = document.getElementsByTagName("path");
    let thElement = document.getElementsByTagName("td");
    console.log(pathElement);
   for(var i=0;i<pathElement.length;i++)
   {
    pathElement[i].classList.add("map-color");
   }
   console.log(thElement);
   for(var i=0;i<thElement.length;i++)
   {
       thElement[i].classList.add('table-row');
   }
    
}
myfunc();