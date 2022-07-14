$(document).ready(function () {
    checkCookie();
});

function checkCookie() {
    const test = document.cookie
        .split('; ')
        .find(x => x.startsWith('mytoken'))

    if (test) { // 로그인 상태 //
        console.log('main js logged in status')
        let loginBtn = document.querySelector(".w-btn w-btn-gray");
        loginBtn.innerHTML = "로그아웃";
        loginBtn.addEventListener("click", logOut);

        let signupBtn = document.querySelector(".btn-mypg");
        signupBtn.style.display = 'none';


    } else {

        console.log('main js logged out status')

    }

}



function logOut() {
    document.cookie = "mytoken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.cookie = "name=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    window.location.href = "/"
}





var alert = function (msg, type) {
    swal({
        title: '',
        text: msg,
        type: type,
        timer: 1500,
        customClass: 'sweet-size',
        showConfirmButton: false
    });
}

var confirm = function (msg, title, resvNum) {
    swal({
        title: title,
        text: msg,
        type: "warning",
        showCancelButton: true,
        confirmButtonClass: "btn-danger",
        confirmButtonText: "예",
        cancelButtonText: "아니오",
        closeOnConfirm: false,
        closeOnCancel: true
    }, function (isConfirm) {
        if (isConfirm) {
            swal('', '예약이 승인되었습니다.', "success");
        } else {
            swal('', '예약이 거부되었습니다.', "failed");
        }

    });
}

function Alert() {
    alert('gg', 'success');
}

function Confirm() {
    confirm('', '회원가입 및 로그인이 필요합니다');
}



