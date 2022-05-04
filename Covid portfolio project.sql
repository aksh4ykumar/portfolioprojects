-- Tables for visualization for project
-- Creating queries for visualization																																																															
Select SUM(new_cases) as total_cases, 
	SUM(cast(new_deaths as int)) as total_deaths, 
	SUM(cast(new_deaths as int))/SUM(New_Cases)*100 as DeathPercentage
From Portfolioproject..CD
--Where location like '%states%'
where continent is not null 
--Group By date
order by 1,2


-- Table 2
Select location, SUM(cast(new_deaths as int)) as TotalDeathCount
From Portfolioproject..CD
--Where location like '%states%'
Where continent is null 
and location not in ('World', 'European Union', 'International')
Group by location
order by TotalDeathCount desc


-- Table 3
Select Location, Population, MAX(total_cases) as HighestInfectionCount,  Max((total_cases/population))*100 as PercentPopulationInfected
From Portfolioproject..CD
--Where location like '%states%'
Group by Location, Population
order by PercentPopulationInfected desc

-- Table 4
Select Location, Population,date, MAX(total_cases) as HighestInfectionCount,  Max((total_cases/population))*100 as PercentPopulationInfected
From PortfolioProject..CD
--Where location like '%states%'
Group by Location, Population, date
order by PercentPopulationInfected desc



-- Total cases vs Total deaths
-- Shows the likelihood of you dying if you have Covid in India
SELECT location
	date,
	total_cases,
	total_deaths,
	(total_deaths/total_cases)*100 AS Deathpercentage
FROM Portfolioproject..CD
WHERE location LIKE '%India%'
	AND continent IS NOT NULL
ORDER BY 1,2	

-- Total cases vs Population
-- Shows what percentage of population got Covid
SELECT location
	date,
	population,
	total_cases,
	(total_cases/population)*100 AS Percentage_population_infected
FROM Portfolioproject..CD
WHERE location LIKE '%India%' 
	AND continent is NOT NULL
ORDER BY 1,2

-- Countries with Highest Infection Rate compared to Population
SELECT location
	location,
	population,
	MAX(total_cases) as Highest_infection_count,
	MAX((total_cases/population))*100 AS Percentage_population_infected
FROM Portfolioproject..CD
-- WHERE location LIKE '%India%' 
	-- AND continent is NOT NULL
GROUP BY location,population
ORDER BY Percentage_population_infected DESC

-- Countries with highest deaths per population
SELECT location,
	MAX(CAST(total_deaths AS INT)) as total_death_count
FROM Portfolioproject..CD
WHERE continent IS NOT NULL
GROUP BY location
ORDER BY total_death_count DESC

-- Breaking down by continent 
SELECT continent,
	MAX(CAST(total_deaths AS INT)) as total_death_count
FROM Portfolioproject..CD
WHERE continent IS NOT NULL
GROUP BY continent
ORDER BY total_death_count DESC

-- GLOBAL NUMBERS	
SELECT SUM(new_cases) AS total_cases,
	SUM(CAST(new_deaths AS INT)) AS total_deaths,
	SUM(CAST(new_deaths AS INT))/SUM(New_Cases)*100 as Deathpercentage
FROM Portfolioproject..CD
WHERE continent IS NOT NULL
ORDER BY 1,2

-- Total population vs Total Vaccination
-- Shows percentage of population that has recieved at least one Covid vaccination 
SELECT d.continent,
	d.location,
	d.date,
	d.population,
	v.new_vaccinations,
	SUM(CONVERT(BIGINT,v.new_vaccinations)) OVER (PARTITION BY d.location ORDER BY d.location, d.date) AS Rollingpeoplevaccinated
FROM Portfolioproject..CD d
JOIN Portfolioproject..CV v
	ON d.location = v.location
	AND d.date = v.date
WHERE d.continent IS NOT NULL
ORDER BY 2,3

Select d.continent, d.location, d.date, d.population, v.new_vaccinations
, SUM(CONVERT(bigint,v.new_vaccinations)) OVER (Partition by d.Location Order by d.location, CONVERT(date, d.date)) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
From PortfolioProject..CD d
Join PortfolioProject..CV V
	On d.location = v.location
	and d.date = v.date
where d.continent is not null 
order by 2,3

-- Using Temp Table

DROP Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)

Insert into #PercentPopulationVaccinated
Select d.continent, d.location, d.date, d.population, v.new_vaccinations
, SUM(CONVERT(BIGINT,v.new_vaccinations)) OVER (Partition by d.Location Order by d.location, CONVERT(date, d.date)) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
From PortfolioProject..CD d
Join PortfolioProject..CV v
	On d.location = v.location
	and d.date = v.date
--where dea.continent is not null 
--order by 2,3

Select *, (RollingPeopleVaccinated/Population)*100
From #PercentPopulationVaccinated

-- Creating View

Create View PercentPopulationVaccinated as
Select d.continent, d.location, d.date, d.population, v.new_vaccinations
, SUM(CONVERT(bigint,v.new_vaccinations)) OVER (Partition by d.Location Order by d.location, CONVERT(date, d.date)) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
From PortfolioProject..CD d
Join PortfolioProject..CV v
	On d.location = v.location
	and d.date = v.date
where d.continent is not null 

SELECT *
FROM PercentPopulationVaccinated


-- FOCUSING ON INDIA
-- selecting india
SELECT *
FROM Portfolioproject..CD
WHERE location LIKE '%india%'
	AND continent IS NOT NULL

-- selecting date from 2022 and location india
SELECT *
FROM Portfolioproject..CD
WHERE date > '2022-01-01'
	AND location LIKE '%india%'

-- ordering by date
SELECT *
FROM Portfolioproject..CD
WHERE date > '2022-01-01'
	AND location LIKE '%india%'
	AND continent IS NOT NULL
ORDER BY date

-- total new cases in 2022 in india till march
SELECT location,
	(
	SELECT SUM(new_cases)
	FROM Portfolioproject..CD
	WHERE date BETWEEN '2021-12-31' AND '2022-03-01'
		AND location LIKE '%india%'
		AND continent IS NOT NULL

	)
FROM Portfolioproject..CD
WHERE date > '2022-01-01'
	AND location LIKE '%india%'
	AND continent IS NOT NULL
GROUP BY location

-- total new cases in india 
SELECT location,
	SUM(new_cases) AS total_new_cases
FROM Portfolioproject..CD
WHERE location LIKE '%india%'
	AND continent IS NOT NULL
GROUP BY location


-- rolling people vaccinated in india from the temp table above
Select *, (RollingPeopleVaccinated/Population)*100
From #PercentPopulationVaccinated
WHERE Location LIKE '%india%'
	AND continent IS NOT NULL

-- rolling people vaccinated in india from 2022
Select *
From #PercentPopulationVaccinated
WHERE Location LIKE '%india%'
	AND Date > '2021-12-31 00:00:00:000'
	AND continent IS NOT NULL


-- Shows what percentage of population got Covid in india
-- now putting it in view
SELECT location
	date,
	population,
	total_cases,
	(total_cases/population)*100 AS Percentage_population_infected
FROM Portfolioproject..CD
WHERE location LIKE '%India%' 
	AND continent is NOT NULL
ORDER BY 1,2

-- selecting the vaccination in india
SELECT *
FROM Portfolioproject..CV
WHERE location LIKE '%india%'
	AND continent IS NOT NULL

-- life expectancy in india
SELECT location,
	life_expectancy
FROM Portfolioproject..CV
WHERE location LIKE '%india%'
	AND continent IS NOT NULL

-- cardio vascular death rate 
SELECT location,
	cardiovasc_death_rate,
	population_density
FROM Portfolioproject..CV
WHERE location LIKE '%india%'
	AND continent IS NOT NULL

SELECT *,
	population_density
FROM Portfolioproject..CV
WHERE location LIKE '%india%'
	AND continent IS NOT NULL

