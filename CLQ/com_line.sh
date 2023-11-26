#!/bin/bash
# Set the header
echo -e "Course Name\tUniversity Name\tModality\tDuration\tCity\tCountry" > merged_courses.tsv

# Copy the content of each other file (assuming all TSV files are in the current directory)
cat *.tsv | awk 'NR > 1' >> merged_courses.tsv

# Find the country with the most courses
mostCommonCountry=$(awk -F'\t' '{print $5}' merged_courses.tsv | sort | uniq -c | sort -nr | head -n 1)
numberOfCoursesInCountry=$(echo "$mostCommonCountry" | awk '{print $1}')
mostCommonCountryName=$(echo "$mostCommonCountry" | awk '{print $2}')
echo "Country with the most courses: $mostCommonCountryName"
echo "Number of courses: $numberOfCoursesInCountry"

# Find the city with the most courses
mostCommonCity=$(awk -F'\t' '{print $4}' merged_courses.tsv | sort | uniq -c | sort -nr | head -n 1)
numberOfCoursesInCity=$(echo "$mostCommonCity" | awk '{print $1}')
mostCommonCityName=$(echo "$mostCommonCity" | awk '{print $2}')
echo "City with the most courses: $mostCommonCityName"
echo "Number of courses: $numberOfCoursesInCity"

# Count courses with a part-time option
partTimeCoursesCount=$(awk -F'\t' '$3 ~ /Part-time/ {count++} END {print count}' merged_courses.tsv)
echo "Number of courses with a Part-time option: $partTimeCoursesCount"

# Count engineer courses
engineerCoursesCount=$(awk -F'\t' '$1 ~ /Engineer/ {count++} END {print count}' merged_courses.tsv)
percentageOfEngineerCourses=$(echo "scale=2; $engineerCoursesCount / $(wc -l < merged_courses.tsv) * 100" | bc)
echo "Number of courses with 'Engineer': $engineerCoursesCount"
echo "Percentage of courses with 'Engineer': $percentageOfEngineerCourses%"
