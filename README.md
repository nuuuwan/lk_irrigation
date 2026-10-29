# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_08:05:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,987 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Ellagawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 08:05:45 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-10-29 08:05:27 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-10-29 08:05:18 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:05:11 | Panadugama (Nilwala Ganga) | 5.88 | 🟡 Alert | -0.044 |  |
| 2026-10-29 08:05:10 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-10-29 08:04:50 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | -0.076 |  |
| 2026-10-29 08:04:12 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:03:56 | Hanwella (Kelani Ganga) | 3.89 | 🟢 Normal | -0.051 |  |
| 2026-10-29 08:03:42 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.019 |  |
| 2026-10-29 08:03:20 | Putupaula (Kalu Ganga) | 3.74 | 🟡 Alert | 0.000 |  |
| 2026-10-29 08:02:49 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:02:46 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:02:30 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 08:02:28 | Ellagawa (Kalu Ganga) | 10.10 | 🟡 Alert | -0.020 |  |
| 2026-10-29 08:02:25 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-29 08:02:20 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-29 08:02:08 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:01:43 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:01:30 | Magura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.088 |  |
| 2026-10-29 08:01:29 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.092 |  |
| 2026-10-29 08:01:15 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-29 08:01:09 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-10-29 08:00:43 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-29 07:38:23 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.015 |  |
| 2026-10-29 07:29:28 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.014 |  |
| 2026-10-29 07:24:41 | Panadugama (Nilwala Ganga) | 5.91 | 🟡 Alert | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 06:02:20 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 07:09:17 | Baddegama (Gin Ganga) | 4.15 | 🟠 Minor Flood | -0.018 |  |
| 2026-10-29 07:21:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.44 | 🟠 Minor Flood | -0.061 |  |
| 2026-10-29 08:03:20 | Putupaula (Kalu Ganga) | 3.74 | 🟡 Alert | 0.000 |  |
| 2026-10-29 08:02:28 | Ellagawa (Kalu Ganga) | 10.10 | 🟡 Alert | -0.020 |  |
| 2026-10-29 08:05:11 | Panadugama (Nilwala Ganga) | 5.88 | 🟡 Alert | -0.044 |  |
| 2026-10-29 07:08:14 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-29 08:02:25 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-29 08:01:15 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-29 08:02:30 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 07:00:09 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:01:43 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:02:46 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:04:12 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:03:38 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:05:18 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:05:24 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:02:49 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:02:08 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-29 07:03:31 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.009 |  |
| 2026-10-29 08:00:43 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-29 07:05:21 | Badalgama (Maha Oya) | 3.19 | 🟢 Normal | -0.010 |  |
| 2026-10-29 08:02:20 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-29 08:01:09 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-10-29 08:05:45 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-10-29 08:05:10 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-10-29 07:29:28 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.014 |  |
| 2026-10-29 07:38:23 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.015 |  |
| 2026-10-29 08:03:42 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.019 |  |
| 2026-10-29 08:05:27 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-10-29 07:02:12 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-10-29 08:03:56 | Hanwella (Kelani Ganga) | 3.89 | 🟢 Normal | -0.051 |  |
| 2026-10-29 07:03:19 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.060 |  |
| 2026-10-29 07:00:14 | Pitabeddara (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.061 |  |
| 2026-10-29 08:04:50 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | -0.076 |  |
| 2026-10-29 08:01:30 | Magura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.088 |  |
| 2026-10-29 08:01:29 | Moragaswewa (Deduru Oya) | 1.40 | 🟢 Normal | -0.092 |  |
| 2026-10-29 07:05:55 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)