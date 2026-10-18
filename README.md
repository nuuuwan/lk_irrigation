# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_16:04:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,398 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 16:04:13 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.098 |  |
| 2026-10-18 16:04:08 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.029 |  |
| 2026-10-18 16:03:48 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | -0.083 |  |
| 2026-10-18 16:03:42 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.047 |  |
| 2026-10-18 16:03:39 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.019 |  |
| 2026-10-18 16:03:31 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-18 16:03:29 | Ellagawa (Kalu Ganga) | 7.66 | 🟢 Normal | -0.051 |  |
| 2026-10-18 16:03:26 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-18 16:03:01 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | -0.012 |  |
| 2026-10-18 16:02:57 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-18 16:02:45 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-18 16:02:28 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-10-18 16:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.83 | 🟢 Normal | -0.067 |  |
| 2026-10-18 16:02:21 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-18 16:02:08 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 16:01:57 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 16:01:42 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 16:01:30 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-18 16:01:26 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 16:01:14 | Weraganthota (Mahaweli Ganga) | -2.59 | 🟢 Normal | -0.177 |  |
| 2026-10-18 16:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-18 16:00:55 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.032 |  |
| 2026-10-18 16:00:48 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-18 16:00:34 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-18 16:00:30 | Moragaswewa (Deduru Oya) | 2.38 | 🟢 Normal | 0.296 | 🔺 Rising |
| 2026-10-18 16:00:15 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.064 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 15:05:00 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 15:07:54 | Panadugama (Nilwala Ganga) | 5.79 | 🟡 Alert | -0.061 |  |
| 2026-10-18 16:00:30 | Moragaswewa (Deduru Oya) | 2.38 | 🟢 Normal | 0.296 | 🔺 Rising |
| 2026-10-18 16:03:26 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-18 16:03:31 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-18 15:08:13 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-10-18 16:00:48 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-18 16:00:15 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-18 16:00:34 | Pitabeddara (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-18 16:01:42 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 16:02:08 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 16:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-18 16:01:30 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-18 16:01:26 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:03:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 14:14:05 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-18 16:01:57 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 15:08:05 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-18 16:02:57 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-18 16:02:45 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:05:12 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:01:29 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.010 |  |
| 2026-10-18 15:00:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-10-18 16:03:01 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | -0.012 |  |
| 2026-10-18 16:03:39 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.019 |  |
| 2026-10-18 16:02:21 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-18 16:04:08 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.029 |  |
| 2026-10-18 16:02:28 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-10-18 16:00:55 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.032 |  |
| 2026-10-18 15:07:11 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.046 |  |
| 2026-10-18 16:03:42 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.047 |  |
| 2026-10-18 16:03:29 | Ellagawa (Kalu Ganga) | 7.66 | 🟢 Normal | -0.051 |  |
| 2026-10-18 15:03:38 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.053 |  |
| 2026-10-18 16:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.83 | 🟢 Normal | -0.067 |  |
| 2026-10-18 16:03:48 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | -0.083 |  |
| 2026-10-18 15:05:46 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.086 |  |
| 2026-10-18 16:04:13 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.098 |  |
| 2026-10-18 16:01:14 | Weraganthota (Mahaweli Ganga) | -2.59 | 🟢 Normal | -0.177 |  |
| 2026-10-18 15:02:07 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -1.488 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)