# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_07:04:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,935 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 07:04:05 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-11-18 07:03:35 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-18 07:03:33 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 07:03:20 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 07:02:56 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.051 |  |
| 2026-11-18 07:02:44 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.049 |  |
| 2026-11-18 07:02:43 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:02:27 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:02:19 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-11-18 07:02:11 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:02:07 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:51 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:49 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-11-18 07:01:42 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:00:51 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:00:29 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:36:36 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:19:02 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 06:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-11-18 06:01:31 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-18 06:03:22 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-18 06:02:21 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-18 07:03:35 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-18 06:01:25 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-18 06:17:29 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-18 06:01:53 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 07:03:20 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 07:03:33 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 07:00:51 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:00:29 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:02:27 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 05:03:35 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:02:10 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:07:53 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:44 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:09:07 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:18:00 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:02:43 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 06:04:22 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:42 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:02:07 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:51 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:49 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:02:11 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:01:51 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:12:21 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.010 |  |
| 2026-11-18 06:04:55 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-11-18 06:00:57 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.011 |  |
| 2026-11-18 06:00:17 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.011 |  |
| 2026-11-18 07:02:19 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-11-18 06:06:16 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.019 |  |
| 2026-11-18 07:04:05 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-11-18 07:01:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-11-18 07:02:44 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.049 |  |
| 2026-11-18 06:04:36 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.050 |  |
| 2026-11-18 07:02:56 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)