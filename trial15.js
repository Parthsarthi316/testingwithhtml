var choices=document.querySelectorAll("td")

for(var i=0;i<choices.length;i++){
choices[i].addEventListener('click',changeMarker)
}



function changeMarker()
{
 if(this.textContent==="")
  this.textContent="X";
  else if(this.textContent==="X")
  this.textContent="0";
  else {
    this.textContent="";
  }
}
