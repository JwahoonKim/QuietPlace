console.log('connect-complete')

const searchCafe = (inputValue) => {
    
};

// Cafe를 전부 가져오는 함수
const getAllCafe = () => {

};

// 메인 이미지 슬라이드쇼
var myImage=document.getElementById("mainImage");
var imageArray=["forHeader/images/woman.jpg", "forHeader/images/coffee.jpg", "forHeader/images/computer.jpg", "forHeader/images/main-ppl.jpg"]
var imageIndex=0;

function changeImage () {
    myImage.setAttribute("src", imageArray[imageIndex]);
    imageIndex++;
    if(imageIndex >= imageArray.length) {
        imageIndex = 0;
    }
}
setInterval(changeImage,3000);