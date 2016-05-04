/**
 * base.js
 * Application-specific business logic goes here.
 * Guy Whorley
 */

$(document).ready(function() {

    //logEnabled=false;
    log.debug("Start doc.ready().","text-transform: uppercase");
    log.warn("My warning message.", log.BOLD);
    log.error("My error message.");
    log.debug("User input validated okay... submitting form to myDb.org:7890",log.GREEN);
    log.always("My always message.");
    log.info("My info message with red",log.RED);
    log.debug("End doc.ready().","text-transform: uppercase;");
  }); //end document.ready()
