/* jshint esversion: 11, jquery: true */

// newsletter form in footer
$("#newsletter-form").on("submit", function(event) {
    // empty the form errors
    $("#newsletter-errors").html("");
    event.preventDefault();

    // check for valid patterns
    let newsletterEmail = $("#newsletter_email").val();
    let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if (!emailPattern.test(newsletterEmail)) {
        // check for valid email pattern
        $("#newsletter-errors").html(
            `<div class="alert alert-danger alert-dismissible fade show" role="alert">
                Invalid email format.
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>`
        );
        return;
    }

    // async form submission to Django view
    $.ajax({
        url: $(this).attr("action"),
        type: "POST",
        data: $(this).serialize(),
        success: function(response) {
            let messageDiv = $("#newsletter-errors");
            if (response.success) {
                messageDiv.html(
                    `<div class="alert alert-success alert-dismissible fade show" role="alert">
                        ${response.message}
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>`
                );
                $("#newsletter-form")[0].reset();
            } else {
                messageDiv.html(
                    `<div class="alert alert-danger alert-dismissible fade show" role="alert">
                        ${response.message}
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>`
                );
            }
        },
        error: function() {
            $("#newsletter-errors").html(
                `<div class="alert alert-danger alert-dismissible fade show" role="alert">
                    Error: Please try again.
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>`
            );
        }
    });
});
