const onClickLikeButton = async (cafeId) => {
    const cafeLikeButton = document.getElementById(`${cafeId}-like-button`);
    const cafeCount = document.getElementById('cafe-count');
    const heart = cafeLikeButton.getElementsByTagName('i')[0];
    const response = await axios.get(`/posts/${cafeId}/like/`);

    if (response.data.cafeLikeOfUser == 1) {
        heart.style.color = "#dc3545";
        cafeCount.innerHTML = response.data.cafeLikeCount;
    } else {
        heart.style.color = "#616161";
        cafeCount.innerHTML = response.data.cafeLikeCount;
    }

}