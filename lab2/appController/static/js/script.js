$(document).ready(function() {
    // Обработчик изменения значения меню
    $('#menu').change(function() {
        // Определяем выбранный пункт меню
        var selectedOption = $(this).val();
        
        // Очищаем контейнер от предыдущих полей ввода
        $('#input-container').empty();
        
        // Добавляем поля ввода в контейнер в зависимости от выбранного пункта меню
        if (selectedOption === 'option2') {
            $('#input-container').append('<input type="password" name="password_input" id="password_input" placeholder="Enter password for root user">');
        }
    });
});
