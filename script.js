function fps()
{
    var new_image = document.createElement("img");
    new_image.className = "image";
    new_image.src = "../camera.jpg?time=" + Math.random();
    new_image.onload = function(){ setTimeout(fps, 1) }
    new_image.onerror = function(){ setTimeout(fps, 1) }
    document.body.appendChild(new_image);

    var images = document.getElementsByClassName("image");
    if (images.length > 10)
    {
        images[0].remove();
    }
}
fps();