# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_23:03:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,625 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 23:03:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:02:57 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-09-18 23:02:50 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.100 |  |
| 2026-09-18 23:02:45 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-18 23:02:39 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.089 |  |
| 2026-09-18 23:02:13 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.010 |  |
| 2026-09-18 23:01:21 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-09-18 23:01:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:08 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:04 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:02 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:00 | Magura (Kalu Ganga) | 3.91 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-18 23:00:45 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:29:59 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 23:02:57 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-09-18 22:02:38 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-18 22:06:25 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-18 23:01:00 | Magura (Kalu Ganga) | 3.91 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-18 23:02:45 | Hanwella (Kelani Ganga) | 1.31 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-18 22:04:54 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-18 22:02:30 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-18 22:05:59 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-18 22:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 22:10:14 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-18 22:10:58 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-18 22:29:59 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:04 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:00:45 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:03:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:07:50 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:02:46 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:04:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:00:25 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:02 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:21 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-18 22:02:58 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 23:01:08 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:03:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:04:17 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-09-18 23:02:13 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:06:26 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-18 22:05:05 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-09-18 23:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-09-18 22:03:29 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-09-18 22:07:14 | Panadugama (Nilwala Ganga) | 3.37 | 🟢 Normal | -0.032 |  |
| 2026-09-18 22:03:15 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2026-09-18 22:07:17 | Baddegama (Gin Ganga) | 2.80 | 🟢 Normal | -0.047 |  |
| 2026-09-18 22:05:17 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.064 |  |
| 2026-09-18 23:02:39 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.089 |  |
| 2026-09-18 23:02:50 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)