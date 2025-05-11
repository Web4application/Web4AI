const express = require("express");
const router = express.Router();
const analyticsController = require("../controllers/analyticsController");

router.get("/task-insights", analyticsController.getTaskInsights);

module.exports = router;
