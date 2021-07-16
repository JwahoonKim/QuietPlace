const handleTag = () => {
    const getTags = () => {
        return document.querySelectorAll(".filter-tag")
    }

    const handleOnClick = (tagDom) => {
        tagDom.onclick = () => {
            if (tagDom.classList.contains('selected')) {
                tagDom.classList.remove('selected');
            }
            else {
                tagDom.classList.add('selected');
            }
        }
    }
    
    // 모든 태그들에 onclick 함수를 걸어주기
    getTags().forEach(tagDom => {
        handleOnClick(tagDom);
    })
    
}

handleTag()


