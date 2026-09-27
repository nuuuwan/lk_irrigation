# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_23:23:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,766 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 23:23:44 | Panadugama (Nilwala Ganga) | 4.95 | 🟢 Normal | -0.031 |  |
| 2026-09-27 23:22:41 | Baddegama (Gin Ganga) | 4.42 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-27 23:11:00 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-09-27 23:10:17 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.011 |  |
| 2026-09-27 23:08:41 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-09-27 23:08:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-09-27 23:07:38 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-09-27 23:06:47 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:05:51 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.066 |  |
| 2026-09-27 23:05:00 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:04:42 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.000 |  |
| 2026-09-27 23:04:26 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-09-27 23:04:01 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:03:53 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-27 23:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | -0.011 |  |
| 2026-09-27 23:03:12 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:03:05 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:02:23 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | -0.051 |  |
| 2026-09-27 23:02:16 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-27 23:02:14 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-09-27 23:02:10 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:02:04 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-27 23:01:49 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | -0.013 |  |
| 2026-09-27 23:01:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:01:32 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | -0.090 |  |
| 2026-09-27 23:01:31 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-27 23:01:22 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:01:12 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:01:08 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:00:56 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-09-27 23:00:20 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 23:01:49 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | -0.013 |  |
| 2026-09-27 23:22:41 | Baddegama (Gin Ganga) | 4.42 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-27 23:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.95 | 🟡 Alert | -0.011 |  |
| 2026-09-27 23:08:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-09-27 23:02:16 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-27 23:01:31 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-09-27 23:03:53 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-27 23:02:04 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-27 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:00:20 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:01:12 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-27 21:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:01:22 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:03:05 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:01:47 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:01:08 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-27 22:02:07 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:00:56 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:04:01 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:03:12 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:02:06 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:05:00 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:06:47 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:02:10 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 23:04:42 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.000 |  |
| 2026-09-27 23:11:00 | Pitabeddara (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-09-27 23:07:38 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-09-27 22:06:48 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-09-27 23:08:41 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-09-27 23:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-09-27 23:02:14 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-09-27 23:10:17 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.011 |  |
| 2026-09-27 22:38:40 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.013 |  |
| 2026-09-27 23:04:26 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-09-27 23:23:44 | Panadugama (Nilwala Ganga) | 4.95 | 🟢 Normal | -0.031 |  |
| 2026-09-27 23:02:23 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | -0.051 |  |
| 2026-09-27 23:05:51 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.066 |  |
| 2026-09-27 23:01:32 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | -0.090 |  |
| 2026-09-27 18:01:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)