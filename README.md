# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_13:26:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,264 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 13:26:35 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.023 |  |
| 2026-09-18 13:13:47 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.018 |  |
| 2026-09-18 13:11:51 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.170 |  |
| 2026-09-18 13:11:20 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-18 13:10:57 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:10:46 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-18 13:10:39 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.102 |  |
| 2026-09-18 13:09:14 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:06:53 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:06:28 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:05:12 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:05:02 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 13:04:31 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:04:28 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.010 |  |
| 2026-09-18 13:03:58 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:03:58 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-09-18 13:03:38 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | -0.011 |  |
| 2026-09-18 13:03:20 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-18 13:02:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:02:49 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:02:45 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | -0.020 |  |
| 2026-09-18 13:02:36 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.145 |  |
| 2026-09-18 13:02:35 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.041 |  |
| 2026-09-18 13:02:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:02:31 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 13:02:30 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-18 13:02:22 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:02:20 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:02:19 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-09-18 13:01:15 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-09-18 13:01:14 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:01:11 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 13:01:03 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:01:02 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:00:53 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-18 13:00:42 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 13:00:53 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-18 13:10:46 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-18 13:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 13:02:31 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 13:01:11 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 13:05:02 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 13:11:20 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-18 13:02:49 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:00:42 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:04:31 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:10:57 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:02:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:05:12 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-18 12:01:30 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:02:45 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:01:02 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:06:28 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:02:22 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:02:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:03:58 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:01:14 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:01:03 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:09:14 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:02:20 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-18 13:04:28 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.010 |  |
| 2026-09-18 13:03:20 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-18 13:02:30 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-18 13:01:15 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | -0.011 |  |
| 2026-09-18 13:03:58 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-09-18 13:03:38 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | -0.011 |  |
| 2026-09-18 13:13:47 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.018 |  |
| 2026-09-18 13:02:19 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-09-18 13:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | -0.020 |  |
| 2026-09-18 13:26:35 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.023 |  |
| 2026-09-18 11:28:09 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | -0.029 |  |
| 2026-09-18 13:02:35 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.041 |  |
| 2026-09-18 13:10:39 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.102 |  |
| 2026-09-18 13:02:36 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.145 |  |
| 2026-09-18 13:11:51 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)