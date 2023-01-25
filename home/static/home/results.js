const modalBtn = document.getElementById('mdlButton')
const modalBody = document.getElementById('modal-body-result')
const curURL = window.location.href

console.log(modalBtn)
const csrf = document.getElementsByName("csrfmiddlewaretoken")

modalBtn.addEventListener('click', (e)=> {
    e.preventDefault()

    document.getElementById('modal-body-result').innerHTML=`
            <div class="spinner-border  m-2 text-secondary" role="status"></div>
            <span class="visually-hidden">Loading...</span>
        `

    const userURL = document.getElementById('siteurl').value

    console.log(userURL)
    $.ajax({
        type: 'POST',
        data: {
            'csrfmiddlewaretoken' : csrf[0].value,
            'siteurl' : userURL
        },
        success: function (result){
            if (result.level == 0){
                document.getElementById('modal-body-result').innerHTML=`
                <h5 style="color: #031633;"><b>${result.msg}</b></h5>
            `
            } else if (result.level == 1){
                document.getElementById('modal-body-result').innerHTML=`
                <h5 style="color: #664d03;"><b>${result.msg}</b></h5>
            `
            } else if (result.level == 2){
                document.getElementById('modal-body-result').innerHTML=`
                <h5 style="color: #842029;"><b>${result.msg}</b></h5>
            `
            } else if (result.level == 3){
                document.getElementById('modal-body-result').innerHTML=`
                <h5 style="color: #0d503c;"><b>${result.msg}</b></h5>
            `
            }
        }
    })
    /*modalBody.innerHTML=`
        <h5>Начать <b>${name}?</b></h5>
        <div class="text-muted">
            <ul>
                <li>Количество вопросов: <i>${questions_amount}</i></li>
                <li>Отведенное время: <i>${time} мин</i></li>
                <li>Порог прохождения: <i>${score_to_pass}%</i></li>
            </ul>
        </div>
    `
    */

})