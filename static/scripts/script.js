function ibg(){

    let ibg=document.querySelectorAll("._ibg");
    for (var i = 0; i < ibg.length; i++) {
    if(ibg[i].querySelector('img')){
    ibg[i].style.backgroundImage = 'url('+ibg[i].querySelector('img').getAttribute('src')+')';
    }
    }
}
ibg();

function selectDateTime(date, time) {
    document.getElementById('selected_date').value = date;
    document.getElementById('selected_time').value = time;
    document.getElementById('selectedDateTime').innerHTML = 'Выбранное время: ' + time + ', ' + date;
}
function formatPhoneNumber(input) {
    let phoneNumber = input.value.replace(/\D/g, '');
    if (phoneNumber.length > 0) {
        // Форматирование номера телефона
        phoneNumber = '+7 (' + phoneNumber.substring(1, 4) + ') ' + phoneNumber.substring(4, 7) + '-' + phoneNumber.substring(7, 9) + '-' + phoneNumber.substring(9, 11);
    }
    input.value = phoneNumber;
}

document.addEventListener("DOMContentLoaded", function() {
    var horsenameSelect = document.getElementById("namehorse");
    var selectedHorse = localStorage.getItem("selectedHorse");
    if (horsenameSelect) {
        if (selectedHorse) {
            horsenameSelect.value = selectedHorse;
        }
        horsenameSelect.addEventListener("change", function() {
            selectedHorse = this.value;
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/getname", true);
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    console.log("Данные переданы");
                    localStorage.setItem("selectedHorse", selectedHorse);
                    //Перезагрузка страницы
                    location.reload();
                }
            };
            xhr.send("horsename=" + selectedHorse);
        });
    }
});

const btnUp = {
    el: document.querySelector('.btn-up'),
    show() {
      // удалим у кнопки класс btn-up_hide
      this.el.classList.remove('btn-up_hide');
    },
    hide() {
      // добавим к кнопке класс btn-up_hide
      this.el.classList.add('btn-up_hide');
    },
    addEventListener() {
      // при прокрутке содержимого страницы
      window.addEventListener('scroll', () => {
        // определяем величину прокрутки
        const scrollY = window.scrollY || document.documentElement.scrollTop;
        // если страница прокручена больше чем на 400px, то делаем кнопку видимой, иначе скрываем
        scrollY > 400 ? this.show() : this.hide();
      });
      // при нажатии на кнопку .btn-up
      document.querySelector('.btn-up').onclick = () => {
        // переместим в начало страницы
        window.scrollTo({
          top: 0,
          left: 0,
          behavior: 'smooth'
        });
      }
    }
  };
btnUp.addEventListener();

let menu_tap = document.querySelector('.menu-link__tap');
let cross_anim = document.querySelector('.link-tap__cross'); 
open = false;
menu_tap.addEventListener("click", function(e){
    let tap_menu = document.querySelector('.menu-list__sub-menu');
    tap_menu.classList.toggle('_active');
    if(open==false){
        cross_anim.classList.remove("_close");
        cross_anim.classList.toggle('_open');
        open = true;
      }
      else{
        cross_anim.classList.remove("_open");
        cross_anim.classList.toggle('_close');
        open = false;
      }
    });
    
    let menu_span = document.querySelector('.icon-menu');
    let menu_burger  = document.querySelector('.menu__body');
    menu_span.addEventListener("click", function(e){
      menu_span.classList.toggle('_active');
      menu_burger.classList.toggle('_active');
      document.body.classList.toggle("_lock");
    });


for (let x = 0; x <= 10; x++) {
  let form__choose2 = document.querySelectorAll(`.chooseblock__${x}2`);
   form__choose2.forEach(function(element){
         element.style.backgroundColor = "#97292e";
         element.addEventListener("click", function(e){
           alert("Данное время уже занятно")
       });
   });
};
let choose__form = document.querySelector('.choose-form__container');

for (let x = 0; x <= 10; x++) {
  let form__choose1 = document.querySelectorAll(`.chooseblock__${x}1`);
  form__choose1.forEach(function(element){
    element.style.backgroundColor = "#0d6928";
    element.addEventListener("click", function(e){
      choose__form.classList.toggle("_active");
      document.body.classList.toggle("_lock");
    });
  });
  let form__close = document.querySelector('.form-choose__close');
  form__close.addEventListener("click", function(e){
  choose__form.classList.remove("_active");
  document.body.classList.remove("_lock");
});
};

/*let form__close = document.querySelector('.form-choose__close');
form__close.addEventListener("click", function(e){
  choose__form.classList.remove("_active");
  document.body.classList.remove("_lock");
});*/


    
    
    