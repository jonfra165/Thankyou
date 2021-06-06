function formatDate(date) {
    /*
      Funktion som tar ett datum (JS-objekt) och 
      returnar datum i formatet yyyy-mm-dd
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
  
  // Väntar tills sidan har laddats klart (tills hela DOM-trädet är konstruerat)
  $(document).ready(function () {
    $(".carousel-control-next, .carousel-control-prev").hide();

    // Skickar ett ajax-anrop till adressen "/calendar-events" (där alla poster för inloggad användare returneras i JSON)
    $.ajax({
      url: "/calendar-events"
    }).done(function (data) {
      // Allt fungerar bra, vi fick ett svar från URL som sparas i parametern "data"

      // Läser in listan med poster och gör om det till datastrukturer (lista med objekt)
      const posts = JSON.parse(data);

      // Bygger vår kalender (simple-calendar)
      $("#container").simpleCalendar({
        events: posts, // Alla poster som ska visas i kalendern (det blir en "prick" för varje datum en post finns)
        onDateSelect: function (date, events) {
          // När vi klickat på ett datum i kalendern, hämta alla inlägg det valda datumet
          $.ajax({
            url: "/calendar-events-by-date/"+formatDate(date)
          }).done(function(data) {
            const posts = JSON.parse(data);
            
            // Tar bort alla barn (tömmer div-elementet) på ev. poster
            $(".carousel-inner").empty();

            // forEach (alltså för varje objekt (post) i listan) skriv ut posten på sidan
            posts.forEach(function(post, index) {
              // post => Själva posten
              // index => platsen i listan som vi är på (i vår forEach-loop)
              console.log(post)
              // Letar upp elementet med id:t "posts" och lägger till en sträng med element
              
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