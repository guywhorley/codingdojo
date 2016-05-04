// ToDO: add custom namespace
/*jshint esversion: 6 */

/**
 * @file <p>This file contains wrapper functions for console logging.</p>
 * <p>A date/time string is added to the log message. Also, optional CSS styles
 * can be applied.</p>
 * @author Guy Whorley
 * @version 1.0
 */

/**
 *  @summary Flag indicating whether or not to write log messages.
 *  <p>Set to true to enabled console log messages; false to disable.
 *  Note that <code>log.always()</code> disregards the logEnabled flag.</p>
 *  @type {boolean}
 */
var logEnabled = true; //true = log; false = no messages;

/**
 *  @summary the log object provides methods to Write to console log with
 *  date/time stamp and an optional css format string.
 *  @name log
 *  @type {Object}
 */
var log = {
    /**
     *  @constant
     *  @member {string} RED
     *  @desc Specifies bold white text with red background.
     */
    RED: "background-color: red; color:white; font-weight: 800;",

    /** @member {string} YELLOW
     *  @desc Specifies bold black text with yellow background.
     */
    YELLOW: "background-color: yellow; font-weight: 800; color: black;",

    /** @member {string} GREEN
     *  @desc Specifies white text with green background.
     */
    GREEN: "background-color: green; color: white;",

    /** @member {string} BOLD
     *  @desc Specifies bold underline text.
     */
    BOLD: "font-weight: 800; text-decoration: underline",

    /** @function info
     *  @desc Write an informational message to console log.
     *  @param {string} msg - 'info' message for console log
     *  @param {string} styStr - optional css-rule for message styling
        @example log.info("Hello World");
        @example log.info("Hello World", log.RED);
     */
    info: function(msg, styStr) {
      styStr = styStr || "";
      if (logEnabled) { console.info("  %c%s - [INFO ] - %s", styStr, ts(), msg); }
    },

    /** @function warn
     *  @desc write a warning message to console log.
     *  @param {string} msg - 'warn' message for console log
     *  @param {string} styStr - optional css-rule for message styling
     *  @example log.warn("Hello World");
     *  @example log.warn("Hello World", log.RED);
     */
    warn: function(msg, styStr) {
      styStr = styStr || "";
      if (logEnabled) { console.warn("  %c%s - [WARN ] - %s", styStr, ts(), msg); }
    },

    /** @function error
     *  @desc Write an error message to console log.
     *  @param {string} msg - 'error' message for console log. This message will
     * always print to console regardless of @link logEnabled
     *  @param {string} styStr - optional css-rule for message styling */
    error: function(msg, styStr) {
      styStr = styStr || "";
      console.error("%c%s - [ERROR] - %s", styStr, ts(), msg);
    },

    /** @function debug
     *  @desc Write a debug message to console log.
     *  @param {string} msg - 'debug' message for console log.
     *  @param {string} styStr - optional css-rule for message styling */
    debug: function(msg, styStr) {
      styStr = styStr || "";
      if (logEnabled) { console.debug("  %c%s - [DEBUG] - %s",styStr,ts(), msg); }
    },
    /** @function always
      * @desc Write an informational message to console log. This messages will
     *  print to console regardless of the logEnabled flag.
     *  @param {string} msg - 'error' message for console log. This message will
     * always print to console regardless of @link logEnabled
     *  @param {string} styStr - optional css-rule for message styling */
    always: function(msg, styStr) {
      styStr = styStr || "";
      console.warn("  %c%s - [INFO] - %s", styStr, ts(), msg);
    } //end log levels
}; //end log object

/**
 * @function ts
 * @desc Get a string representation of current timestamp in the following
 * format:
 * <p>yyyy-mm-dd || hh-mm-ss-ms</p>
 *
 * @return {string}  formated date/time stamp
 */
function ts() {
    var d = new Date();
    var day = d.getMonth() + 1;
    var sec = d.getSeconds();
    var hour = d.getHours();
    var min = d.getMinutes();

    if (hour < 10) { hour = "0" + hour; }
    if (sec  < 10) { sec = "0" + sec; }
    if (day  < 10) { day = "0" + day; }
    if (min  < 10) { min = "0" + min; }

    return d.getFullYear() + "-" + day + "-" + d.getDate() + " || " + hour +
        ":" + d.getMinutes() + ":" + sec + ":" + padMillis(d.getMilliseconds());
} //getLogTime

/**
 * @function padMillis
 * @desc If the millisecond value is less than three digits, add leading zeros
 * to bring the value to three digits. 
 * @param  {number} ms - milliseconds
 * @return {string} string representation of padded milliseconds
 */
function padMillis(ms) {
    if (ms < 10) { return "00" + ms; }
    else if (ms < 100) { return "0" + ms; }
    return ms.toString();
} //padmillis
