var cb = document.getElementById("id_is_for_everyone");
var slot = document.getElementById("addQuestForm").lastElementChild;
var slotField = document.getElementById("id_slots");

cb.addEventListener("change", function() {
    if(cb.checked == true) {
        slot.style.display = "none";
        slotField.value = 0;
    } else {
        slot.style.display = "block";
        slotField.value = "";
    }
})