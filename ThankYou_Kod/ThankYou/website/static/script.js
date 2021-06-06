function formatDate(date) {
    /*
      Function that takes a date (JS-objekt) and
      returns it in the format yyyy-mm-dd
    */
    var d = new Date(date),
      month = '' + (d.getMonth() + 1),
      day = '' + d.getDate(),
      year = d.getFullYear();

    if (month.length < 2)
      month = '0' + month;
    if (day.length < 2)
      day = '0' + day;

    return [year, month, day].join('-');
  }
  
  // Waiting for the page to load
  $(document).ready(function () {
    $(".carousel-control-next, .carousel-control-prev").hide();

    // Sends a ajax-call to the address "/calendar-events"
    $.ajax({
      url: "/calendar-events"
    }).done(function (data) {
      // The answe from the URL is saved in "data"

      // Reads the list of records and converts it into data structures
      const posts = JSON.parse(data);

      // Builds our calendar (simple-calendar)
      $("#container").simpleCalendar({
        events: posts, // All entries to be displayed in the calendar will be shown as a "dot" for each date an entry exists
        onDateSelect: function (date, events) {
          // Once we click on a date in the calendar, all posts will retrieve on the selected date
          $.ajax({
            url: "/calendar-events-by-date/"+formatDate(date)
          }).done(function(data) {
            const posts = JSON.parse(data);
            
            // Empties the div element on any poster
            $(".carousel-inner").empty();

            // For each object, post, in the list - print post 
            posts.forEach(function(post, index) {
              console.log(post)
              // Finds the element with id "posts" and adds a string with elements
              
              if (post.image || post.summary) {
                  $(".carousel-control-next, .carousel-control-prev").show();
              } else {
                  $(".carousel-control-next, .carousel-control-prev").hide();
              }
          
              if (post.image && post.summary) {
                $(".carousel-inner").append(`
                  <div class="carousel-item">
                    <img src="${post.image}" alt="Tillhörande bild till inlägget" width="600em" height="600em">
                    <div class="carousel-caption carousel-button">
                      <h5>${post.summary}</h5>
                      <!-- Button trigger modal -->
                      <button type="button" class="btn btn-warning calendar-button" data-bs-toggle="modal" data-bs-target="#exampleModal_${post.id}">
                        Delete
                      </button>

                      <!-- Modal -->
                      <div class="modal fade" id="exampleModal_${post.id}" tabindex="-1" aria-labelledby="exampleModalLabel_${post.id}" aria-hidden="true">
                        <div class="modal-dialog">
                          <div class="modal-content">
                            <div class="modal-header">
                              <h5 class="modal-titel text-dark display-6" id="exampleModalLabel_${post.id}">Delete Post!</h5>
                              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body text-dark text-start">
                              Are you sure you want delete this post?
                            </div>
                            <div class="modal-footer">
                              <button type="button" class="btn btn-secondary calendar-button" data-bs-dismiss="modal">Close</button>
                              <a class="btn btn-warning" href="/delete/${post.id}" role="button">Delete</a>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
              ` );
              } else if(post.image) {
                $(".carousel-inner").append(`
                  <div class="carousel-item">
                    <img src="${post.image}" alt="Tillhörande bild till inlägget" width="600em" height="600em">
                    <div class="carousel-caption carousel-button">
                      <!-- Button trigger modal -->
                      <button type="button" class="btn btn-warning calendar-button" data-bs-toggle="modal" data-bs-target="#exampleModal_${post.id}">
                        Delete
                      </button>

                      <!-- Modal -->
                      <div class="modal fade" id="exampleModal_${post.id}" tabindex="-1" aria-labelledby="exampleModalLabel_${post.id}" aria-hidden="true">
                        <div class="modal-dialog">
                          <div class="modal-content">
                            <div class="modal-header">
                              <h5 class="modal-titel text-dark display-6" id="exampleModalLabel_${post.id}">Delete Post!</h5>
                              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body text-dark text-start">
                              Are you sure you want delete this post?
                            </div>
                            <div class="modal-footer">
                              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                              <a class="btn btn-warning calendar-button" href="/delete/${post.id}" role="button">Delete</a>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
              ` );
              } else {
                $(".carousel-inner").append(`
                  <div class="carousel-item">
                    <img src="https://www.yogafordig.nu/wp-content/uploads/2019/10/Mindfulness-4-583x437.jpeg" alt="Tillhörande bild till inlägget" width="600em" height="600em">
                    <div class="carousel-caption carousel-button">
                      <h5>${post.summary}</h5>
                      <!-- Button trigger modal -->
                      <button type="button" class="btn btn-warning calendar-button" data-bs-toggle="modal" data-bs-target="#exampleModal_${post.id}">
                        Delete
                      </button>

                      <!-- Modal -->
                      <div class="modal fade" id="exampleModal_${post.id}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog">
                          <div class="modal-content">
                            <div class="modal-header">
                              <h5 class="modal-titel text-dark display-6" id="exampleModalLabel_${post.id}">Delete Post!</h5>
                              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body text-dark text-start">
                              Are you sure you want delete this post?
                            </div>
                            <div class="modal-footer">
                              <button type="button" class="btn btn-secondary calendar-button btn-sm" data-bs-dismiss="modal">Close</button>
                              <a class="btn btn-warning" href="/delete/${post.id}" role="button">Delete</a>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
              ` );
              }
              if (index === 0)
                  $(".carousel-item").addClass('active')
              });
            });

          }
        });

        setTimeout(function() {
          $(".today").click();
          $("#carouselExampleControls").fadeIn(1000);
        }, 500);

      }).fail(function(error) {
        console.log(error);
      });
    });

// Checks if password is valid 

    var myInput = document.getElementById("inputPassword");
    var letter = document.getElementById("letter");
    var capital = document.getElementById("capital");
    var number = document.getElementById("number");
    var length = document.getElementById("length");  
    
    // When the user clicks on the password field, show the message box
    myInput.onfocus = function() {
      document.getElementById("message").style.display = "block";
    }
    
    // When the user clicks outside of the password field, hide the message box
    myInput.onblur = function() {
      document.getElementById("message").style.display = "none";
    }
    
    // When the user starts to type something inside the password field
    myInput.onkeyup = function() {
      // Validate lowercase letters
      var lowerCaseLetters = /[a-z]/g;
      if(myInput.value.match(lowerCaseLetters)) {  
        letter.classList.remove("invalid");
        letter.classList.add("valid");
      } else {
        letter.classList.remove("valid");
        letter.classList.add("invalid");
      }
      
      // Validate capital letters
      var upperCaseLetters = /[A-Z]/g;
      if(myInput.value.match(upperCaseLetters)) {  
        capital.classList.remove("invalid");
        capital.classList.add("valid");
      } else {
        capital.classList.remove("valid");
        capital.classList.add("invalid");
      }
    
      // Validate numbers
      var numbers = /[0-9]/g;
      if(myInput.value.match(numbers)) {  
        number.classList.remove("invalid");
        number.classList.add("valid");
      } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
      }
  
      // Validate length
      if(myInput.value.length >= 8) {
        length.classList.remove("invalid");
        length.classList.add("valid");
      } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
      }
  
    }