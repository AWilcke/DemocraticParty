var express = require('express');
var router = express.Router();

const low = require('lowdb')
const storage = require('lowdb/file-async')

const db = low('db.json', { storage })

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'sfff' });
});

router.get('/test', function(req, res, next) {
	
});

router.get('/about', function (req, res) {

});
router.get('/fun', function(req, res){

})

function random (low, high) {
    return Math.floor(Math.random() * (high - low) + low)
}

module.exports = router;
