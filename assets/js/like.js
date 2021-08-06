var likes = document.querySelector('.card-deck-wrapper').querySelectorAll('a')
var flag = 0;
for (var i = 0; i < likes.length; i++) {
    likes[i].onclick = function () {
        console.log(flag)
        if (this.id == 'aa' || this.id == "bb" || this.id == "cc" || this.id == "dd" || this.id == "ee"||
            this.id == "ff" || this.id == "gg" || this.id == "hh" || this.id == "ii")
        {
            return
        }
        if (this.style.color == 'red') {
            this.setAttribute('style', 'color: white !important');
            setTimeout(function () {
                location.reload();
            }, 2000);
        } else {
            this.setAttribute('style', 'color: red !important');
            setTimeout(function () {
                location.reload();
            }, 2000);
        }
    }
}