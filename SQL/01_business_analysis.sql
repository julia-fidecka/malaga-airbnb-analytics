SELECT 
    neighbourhood_cleansed,
    ROUND(AVG(price), 2) AS average_price,
    COUNT(id) AS number_of_oferts,
    ROUND(AVG(review_scores_rating), 2) AS average_score
FROM listings
WHERE price IS NOT NULL 
  AND price > 0
GROUP BY neighbourhood_cleansed
HAVING COUNT(id) >= 15
ORDER BY average_price DESC;

-- Bailen-Miraflores avg price (529.48) is way above city avg (213.35) - check for outliers in Python.

SELECT room_type, host_is_superhost, COUNT(id) as number_of_oferts, ROUND(AVG(price), 2) AS average_price, ROUND(AVG(review_scores_rating), 2) AS average_score FROM listings WHERE host_is_superhost IS NOT NULL AND price IS NOT NULL AND price > 0 GROUP BY room_type, host_is_superhost ORDER BY room_type, host_is_superhost DESC;

-- Superhosts have lower avg prices than regular hosts, likely due to outliers in the non-Superhost group.

SELECT STRFTIME('%Y-%m', c.date) AS month, ROUND((1 - AVG(c.available)) * 100, 2) AS occupancy_rate_pct FROM calendar as c INNER JOIN listings AS l ON c.listing_id = l.id WHERE l.price IS NOT NULL AND l.price > 0 GROUP BY monthORDER BY month ASC;
-- Calendar shows 365-day forward availability, peak occupancy in Sep/Oct, 2027-10 is incomplete.