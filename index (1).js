const blog_card = document.querySelector('.blog-cards');

console.log(blog_card);

blog_card.addEventListener('click', ()=>{
    //window.location.href ="http://127.0.0.1:5500/blogContent.html";
    window.location.href ="http://127.0.0.1:5000/blogcontent";
})

function ellipsify(str){
    if(str.length>10){
        return(str.substring(0,80)+"----");
    }
    else{
        return str;
    }
}
let cardText=document.querySelector('.card-text');
cardText.innerHTML=ellipsify(cardText.textContent);
console.log(cardText.textContent)

// git clone https://github.com/Surajsinhar77/blog_post.git