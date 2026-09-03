# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_17:03:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,882 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 17:03:23 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:03:06 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 17:02:57 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:02:53 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:02:50 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:02:48 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:02:43 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 17:02:42 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.041 |  |
| 2026-09-03 17:02:35 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.090 |  |
| 2026-09-03 17:02:35 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 17:02:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-03 17:01:54 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:01:32 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:01:17 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.011 |  |
| 2026-09-03 17:01:13 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:01:10 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:01:03 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:01:00 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:00:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:00:10 | Siyambalanduwa (Heda Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-09-03 16:35:33 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:29:47 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:21:11 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 16:05:22 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-03 17:02:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-03 16:13:08 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-03 16:07:54 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-03 17:03:06 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 16:08:54 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-03 16:07:10 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-03 17:02:35 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 17:02:43 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 16:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 17:02:53 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:02:48 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:12:11 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:02:50 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:01:13 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:03:28 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:01:32 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:02:57 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:01:54 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:03:01 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:06:50 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:03:23 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:01:00 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:05:28 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:05:51 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:01:03 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:29:47 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:01:10 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:03:29 | Thanamalwila (Kirindi Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 17:00:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 16:11:14 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-09-03 17:01:17 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.011 |  |
| 2026-09-03 17:00:10 | Siyambalanduwa (Heda Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-09-03 16:09:06 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-09-03 17:02:42 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.041 |  |
| 2026-09-03 16:01:28 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | -0.052 |  |
| 2026-09-03 16:02:50 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.062 |  |
| 2026-09-03 17:02:35 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.090 |  |
| 2026-09-03 16:05:24 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)