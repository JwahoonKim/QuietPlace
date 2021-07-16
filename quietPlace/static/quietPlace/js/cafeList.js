let filterCondition = [];

const handleCafe = () => {
    const selectedTag = [];
    const getCafe = () => {
        return [... document.querySelectorAll('.cafe-box')];
    }

    // console.log(getCafe()[0].getElementsByTagName('li'));
    const filtering = () => {
        filterCondition.forEach((tag_positive) => {
            HideNotPositiveCafe(tag_positive);
        })
    }

    const getTagList = (cafe) => {
        return Array.from(cafe.getElementsByTagName('li'));   
    }

    const isTagPositive = (cafe, tag_positive) => {
        cafeTagList = getTagList(cafe);
        for(i = 0; i < cafeTagList.length; i++){
            if (cafeTagList[i].classList.contains(tag_positive)) {
                return true;
            }
            // 끝까지 다 봤는데 그 태그 positive가 아닌 경우
            if (i === cafeTagList.length - 1){
                return false;
            }
        }
    }

    const HideNotPositiveCafe = (tag_positive) => {
        cafes = getCafe();
        cafes.forEach( cafe => {
            if (isTagPositive(cafe, tag_positive) === false){
                cafe.classList.add('hide');
            }
        })
    }

    filtering();
}

const handleTag = () => {
    const getTags = () => {
        return [ ... document.querySelectorAll(".filter-tag-button")];
    }
    console.log(getTags())
    
    const handleOnClick = (tagDom) => {
        tagDom.onclick = () => {
            if (tagDom.classList.contains('selected')) {
                tagDom.classList.remove('selected');
                filterCondition = filterCondition.filter(tag => tag !== `${tagDom.id}_positive`)
            }
            else {
                tagDom.classList.add('selected');
                filterCondition.push(`${tagDom.id}_positive`);
                handleCafe();
                console.log(filterCondition)
            }
        }
    }

    // 모든 태그들에 onclick 함수를 걸어주기
    getTags().forEach(tagDom => {
        handleOnClick(tagDom);
    })
}

handleTag();


