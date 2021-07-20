let filterCondition = [];

const handleCafe = (switching) => {
    const getCafe = () => {
        return [...document.querySelectorAll('.cafe-box')];
    }

    // 태그를 on 했을 경우 
    const onFiltering = () => {
        filterCondition.forEach((tag_positive) => {
            console.log(filterCondition)
            const cafes = getCafe();
            cafes.forEach(cafe => {
                cafe.classList.remove('hide');
            })
            HideNotPositiveCafe(tag_positive);
        })
    }

    const getTagList = (cafe) => {
        return Array.from(cafe.getElementsByTagName('li'));
    }

    const isTagPositive = (cafe, tag_positive) => {
        const cafeTagList = getTagList(cafe);
        for (let i = 0; i < cafeTagList.length; i++) {
            if (cafeTagList[i].classList.contains(tag_positive)) {
                return true;
            }
            // 끝까지 다 봤는데 그 태그 positive가 아닌 경우
            if (i === cafeTagList.length - 1) {
                return false;
            }
        }
    }

    const HideNotPositiveCafe = (tag_positive) => {
        const cafes = getCafe();
        cafes.forEach(cafe => {
            if (isTagPositive(cafe, tag_positive) === false) {
                cafe.classList.add('hide');
            }
        })
    }

    //     ----------------- 실행 ------------------- //  
    onFiltering();

}


const handleTag = () => {
    const getTags = () => {
        return [...document.querySelectorAll(".filter-tag-button")];
    }
    // console.log(getTags())

    const handleOnClick = (tagDom) => {
        tagDom.onclick = () => {
            if (tagDom.classList.contains('selected')) {
                tagDom.classList.remove('selected');
                filterCondition = filterCondition.filter(tag => tag !== `${tagDom.id}_positive`)
                handleCafe();
            }
            else {
                tagDom.classList.add('selected');
                if (tagDom.id === "서울대입구역") {
                    const nokduDom = document.getElementById("대학동");
                    nokduDom.classList.remove('selected');
                    const nokdu = "대학동_positive";
                    filterCondition = filterCondition.filter(tag => tag !== nokdu);
                }
                else if (tagDom.id === "대학동") {
                    const seoulDom = document.getElementById("서울대입구역");
                    seoulDom.classList.remove('selected');
                    const seoul = "서울대입구역_positive";
                    filterCondition = filterCondition.filter(tag => tag !== seoul);
                }
                filterCondition.push(`${tagDom.id}_positive`);
                handleCafe();
            }
        }
    }

    // 모든 태그들에 onclick 함수를 걸어주기
    getTags().forEach(tagDom => {
        handleOnClick(tagDom);
    })
}


handleTag();


