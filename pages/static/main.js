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
                    console.log(title)
                    swal('', '로그인 화면으로 이동합니다', 'success');
                    login();
                } else {

                }

            });
        }


        function Confirm() {
            confirm('', '로그인하시겠어요?');
        }
