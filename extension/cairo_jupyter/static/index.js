// cairo_jupyter doesn't have any JS code.
//
// This file is added to make Jupyter happy so it will load the extension.
define(function(){

    function load_ipython_extension(){
        console.info('loaded cairo_jupyter.');
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});
