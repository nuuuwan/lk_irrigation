# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_09:08:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,104 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 09:08:24 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:07:07 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.026 |  |
| 2026-09-18 09:06:46 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | -0.029 |  |
| 2026-09-18 09:05:57 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.019 |  |
| 2026-09-18 09:05:56 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:05:20 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-09-18 09:05:09 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.080 |  |
| 2026-09-18 09:04:58 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:03:58 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-18 09:03:53 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.015 |  |
| 2026-09-18 09:03:41 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-09-18 09:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:03:34 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.049 |  |
| 2026-09-18 09:03:27 | Magura (Kalu Ganga) | 4.26 | 🟡 Alert | -0.078 |  |
| 2026-09-18 09:03:24 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | -0.011 |  |
| 2026-09-18 09:03:22 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-18 09:03:13 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:03:12 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-09-18 09:03:10 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-18 09:02:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 09:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:02:38 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.015 |  |
| 2026-09-18 09:02:30 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-09-18 09:02:29 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:02:17 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-18 09:02:13 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-18 09:01:49 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-09-18 09:01:33 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:01:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.076 |  |
| 2026-09-18 09:01:13 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.020 |  |
| 2026-09-18 09:01:08 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.051 |  |
| 2026-09-18 09:00:53 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:00:52 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:00:50 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:00:11 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 09:03:27 | Magura (Kalu Ganga) | 4.26 | 🟡 Alert | -0.078 |  |
| 2026-09-18 09:01:49 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-09-18 09:02:17 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-18 09:03:58 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-18 09:03:10 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-18 09:02:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 09:03:22 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-18 09:00:52 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:01:33 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 08:02:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:05:56 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:00:53 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:04:58 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:03:13 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:08:24 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:00:50 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:02:29 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 09:02:13 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-18 08:04:27 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-09-18 09:03:24 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | -0.011 |  |
| 2026-09-18 09:03:12 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | -0.011 |  |
| 2026-09-18 09:03:53 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.015 |  |
| 2026-09-18 09:00:11 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | -0.015 |  |
| 2026-09-18 09:02:38 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.015 |  |
| 2026-09-18 09:05:57 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.019 |  |
| 2026-09-18 09:03:41 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-09-18 09:02:30 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-09-18 09:01:13 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.020 |  |
| 2026-09-18 09:07:07 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.026 |  |
| 2026-09-18 09:06:46 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | -0.029 |  |
| 2026-09-18 09:05:20 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-09-18 08:08:37 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.037 |  |
| 2026-09-18 09:03:34 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.049 |  |
| 2026-09-18 09:01:08 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.051 |  |
| 2026-09-18 09:01:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.076 |  |
| 2026-09-18 09:05:09 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.080 |  |
| 2026-09-18 08:08:51 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)