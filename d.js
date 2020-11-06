db.people.aggregate([
        { $group: {
        	_id: null,
        	count:{$sum:1}

        }}
        ])
