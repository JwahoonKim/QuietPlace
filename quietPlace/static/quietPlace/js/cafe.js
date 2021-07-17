const onCreateReview = async (cafeId) => {
  const reviewInputElement = document.getElementById("review-input");
  if (reviewInputElement.value) {
    let data = new FormData();
    data.append("content", reviewInputElement.value);
    const response = await axios.post(`cafe_review/`, data);
    const { reviewId, reviewCount, author_nickname } =
      response.data;
    const reviewElement = getReviewElement(
      author_nickname,
      reviewInputElement.value,
      cafeId,
      reviewId
    );
    console.log(reviewElement);
    document
      .getElementById(`${cafeId}-review-list`)
      .appendChild(reviewElement);
    onSetReviewCount(reviewCount);
    reviewInputElement.value = "";
  }
};

const onSetReviewCount = (reviewCount) => {
  const reviewCountElement = document.getElementById("review-count");
  reviewCountElement.innerHTML = `<strong>리뷰가 ${reviewCount}개 있습니다</strong>`;
};

const getReviewElement = (
  author_nickname,
  review,
  cafeId,
  reviewId
) => {
  let newReviewElement = document.createElement("div");
  newReviewElement.setAttribute("id", `${reviewId}-review`);
  newReviewElement.innerHTML = `<header class="comment__header">
                                  <img src={% static "forCafe/images/co1.jpg" %} class="comment__avatar" />
                                  <div class="comment__author">
                                    <strong class="review-nickname">${author_nickname}</strong>
                                  </div>
                                 </header>
                                 <div class="comment__text"> ${review} </div>
                                 <a onclick="onReviewDelete(${reviewId})">리뷰 삭제</a>`;
  return newReviewElement;
};


const onReviewDelete = async (cafeId, reviewId) => {
  if (confirm("정말 삭제하시겠습니까?") === true) {
    const review = document.getElementById(`${reviewId}-review`);
    await axios.delete(`/posts/cafe/${cafeId}/cafe_review/${reviewId}/`);
    review.remove();
  }
};

console.log()
