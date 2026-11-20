document.addEventListener("DOMContentLoaded", function () {
    const productField = document.getElementById("id_product");
    const priceField = document.getElementById("id_selling_price");

    if (!productField || !priceField) return;

    function updateSellingPrice() {
        const selectedOption = productField.options[productField.selectedIndex];
        const price = selectedOption.dataset.price;

        if (price) {
            priceField.value = price;
        }
    }

    productField.addEventListener("change", updateSellingPrice);

    updateSellingPrice();
});
