# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_08:24:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,966 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 08:24:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:17:36 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:14:33 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:12:20 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.009 |  |
| 2026-09-19 08:09:23 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.033 |  |
| 2026-09-19 08:08:50 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | -0.018 |  |
| 2026-09-19 08:08:05 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 08:06:51 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.045 |  |
| 2026-09-19 08:06:18 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.215 |  |
| 2026-09-19 08:05:00 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.027 |  |
| 2026-09-19 08:04:47 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:04:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-09-19 08:04:45 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:04:09 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:03:55 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | -0.030 |  |
| 2026-09-19 08:03:36 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:03:36 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.050 |  |
| 2026-09-19 08:03:30 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-09-19 08:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:03:27 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:03:18 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.039 |  |
| 2026-09-19 08:03:15 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:03:14 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-09-19 08:03:13 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-09-19 08:03:00 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-09-19 08:02:59 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-09-19 08:02:54 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-09-19 08:02:33 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:02:33 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:02:32 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:02:27 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:01:57 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:01:53 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.062 |  |
| 2026-09-19 08:01:46 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:01:22 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-19 08:01:14 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:01:09 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:00:19 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:00:17 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 08:03:00 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-09-19 08:08:05 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 08:01:46 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:01:09 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:02:27 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:24:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:03:27 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:03:15 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:02:33 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:02:54 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:00:19 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:01:57 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:04:45 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:04:47 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:17:36 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:03:36 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:04:09 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:01:14 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:14:33 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:02:33 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:00:17 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 08:12:20 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.009 |  |
| 2026-09-19 08:01:22 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-19 08:08:50 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | -0.018 |  |
| 2026-09-19 08:03:14 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-09-19 08:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-09-19 08:03:30 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-09-19 08:05:00 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.027 |  |
| 2026-09-19 08:03:13 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-09-19 08:03:55 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | -0.030 |  |
| 2026-09-19 08:09:23 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.033 |  |
| 2026-09-19 08:03:18 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.039 |  |
| 2026-09-19 08:06:51 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.045 |  |
| 2026-09-19 08:03:36 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.050 |  |
| 2026-09-19 08:02:59 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-09-19 08:01:53 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.062 |  |
| 2026-09-19 08:04:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-09-19 08:06:18 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)