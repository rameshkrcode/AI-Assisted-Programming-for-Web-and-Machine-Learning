db.orders.aggregate([
  { $group: { _id: "$product_id", total_sold: { $sum: "$quantity" } } },
  { $sort: { total_sold: -1 } },
  { $limit: 5 }
]);