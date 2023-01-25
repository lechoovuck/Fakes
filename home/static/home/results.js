const modalBtn = document.getElementById('mdlButton')
const modalBody = document.getElementById('modal-body-result')
const curURL = window.location.href

const csrf = document.getElementsByName("csrfmiddlewaretoken")

modalBtn.addEventListener('click', (e)=> {
    e.preventDefault()

    document.getElementById('modal-body-result').innerHTML=`
            <div class="spinner-border  m-2 text-secondary" role="status"></div>
            <span class="visually-hidden">Loading...</span>
        `

    const userURL = document.getElementById('siteurl').value
    $.ajax({
        type: 'POST',
        data: {
            'csrfmiddlewaretoken' : csrf[0].value,
            'siteurl' : userURL
        },
        success: function (result){
            console.log(result.response_code)

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
})