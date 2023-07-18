
// Function to update the form's management form data
function updateManagementForm() {
    const totalFormsInput = document.getElementById("id_haushaltsposten_set-TOTAL_FORMS");
    const haushaltspostenForms = document.querySelectorAll(".haushaltsposten-form");

    totalFormsInput.value = haushaltspostenForms.length;
}

function addProjektForm(element) {
    let parentElement = element.parentElement;
    while (parentElement && !parentElement.classList.contains("haushaltsposten-form")) {
        parentElement = parentElement.parentElement;
    }

    if (!parentElement)
        return


    let total_count = parentElement.querySelector('[id*="TOTAL_FORMS"]');
    total_count.value = parseInt(total_count.value) + 1;

    let projekte = parentElement.querySelector(".projekt-container");
    let projekt = projekte.lastElementChild.cloneNode(true);

    projekt.innerHTML = projekt.innerHTML.replace(/-_set-(\d+)-/g, function (match, number) {
        let newNumber = parseInt(number) + 1;
        return "-_set-" + newNumber + "-";
    });

    projekt.innerHTML = projekt.innerHTML.replace(/projekt_set-(\d+)-/g, function (match, number) {
        let newNumber = parseInt(number) + 1;
        return "projekt_set-" + newNumber + "-";
    });

    projekte.appendChild(projekt);
}


function deleteProjektForm(element) {
    let parentElement = element.parentElement;
    while (parentElement && !parentElement.classList.contains("projekt-form")) {
        parentElement = parentElement.parentElement;
    }

    if (parentElement) {
        let total_count = parentElement.querySelector('[id*="TOTAL_FORMS"]');
        if (parseInt(total_count.value) > 1) {
            total_count.value = parseInt(total_count.value) - 1;
            parentElement.remove();
        }
        else
            alert("One Projekt need to exists!! >:(")
    }
}


function deletePostenForm(element) {
    let parentElement = element.parentElement;
    let grandparentElement = element.parentElement;
    while (parentElement && !parentElement.classList.contains("accordion")) {
        parentElement = parentElement.parentElement;
    }

    if (!parentElement)
        return

    while (grandparentElement && !grandparentElement.classList.contains("form-horizontal")) {
        grandparentElement = grandparentElement.parentElement;
    }

    if (!grandparentElement)
        return


    let total_count = grandparentElement.querySelector('[id*="TOTAL_FORMS"]');
    if (parseInt(total_count.value) > 1) {
        parentElement.remove()
        total_count.value = parseInt(total_count.value) - 1;
    }
    else
        alert("One Haushaltsposten need to exists!! >:(")
}

function add_total_forms_value() {
    // Increment the value of "id_haushaltsposten_set-TOTAL_FORMS"
    const totalFormsInput = document.querySelector('#id_haushaltsposten_set-TOTAL_FORMS');
    const totalFormsValue = parseInt(totalFormsInput.value);
    totalFormsInput.value = totalFormsValue + 1;
    return totalFormsValue;
}

function clone_last_form() {
    // Get the container element
    const container = document.getElementById('haushaltsposten-container');

    // Clone the last element
    const lastElement = container.lastElementChild.cloneNode(true);

    // Increment text occurrences of "_set-(number)-" by one
    const regex = /(?<!aufwand)_set-(\d+)-/g;

    const html = lastElement.innerHTML;
    lastElement.innerHTML = html.replace(regex, function (match, number) {
        const incrementedNumber = parseInt(number) + 1;
        return "_set-" + incrementedNumber + "-";
    });

    // Increment text occurrences of "_set-(number)-" by one
    const regex_bootstrap = /collapse(\d+)/g;

    lastElement.innerHTML = lastElement.innerHTML.replace(regex_bootstrap, function (match, number) {
        const incrementedNumber = parseInt(number) + 1;
        return "collapse" + incrementedNumber;
    });


    text_element = lastElement.querySelector(".accordion-header > button")
    text_element.textContent = "Empty Posten";

    // Remove all "projekt-form" from the "projekt-container" except one
    const projektContainer = lastElement.querySelector('.projekt-container');
    const projektForms = projektContainer.getElementsByClassName('projekt-form');
    while (projektForms.length > 1) {
        projektContainer.removeChild(projektContainer.lastElementChild);
    }

    // Replace the string "projekt_set-(number)-" with "projekt_set-0-"
    const text = projektContainer.innerHTML;
    const regex_inner = /projekt_set-(\d+)-/g;

    projektContainer.innerHTML = text.replace(regex_inner, () => "projekt_set-0-");

    // Append the cloned element to the container
    container.appendChild(lastElement);
}


function addHaushaltspostenForm() {
    add_total_forms_value();
    clone_last_form();
}

function update_title(event) {
    let parentElement = event.target.parentElement;
    while (parentElement && !parentElement.classList.contains("haushaltsposten-form")) {
        parentElement = parentElement.parentElement;
    }

    text_element = parentElement.querySelector(".accordion-header > button")
    text_element.textContent = event.target.value.toString();
}


// Add event listener for the "Add Projekt" button
document.addEventListener('click', function (event) {
    if (event.target.matches('.add-projekt-btn')) {
        addProjektForm(event.target);
    }
    if (event.target.matches('.delete-projekt-btn')) {
        deleteProjektForm(event.target);
    }
    if (event.target.matches('.delete-haushaltsposten-btn')) {
        deletePostenForm(event.target);
    }
});

// Add event listener for the "Add Haushaltsposten" button
document.getElementById('add-haushaltsposten-btn').addEventListener('click', function () {
    addHaushaltspostenForm();
});
