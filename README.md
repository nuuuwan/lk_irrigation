# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_13:14:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,475 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 13:14:22 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:12:50 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.018 |  |
| 2026-09-16 13:11:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | -0.070 |  |
| 2026-09-16 13:11:08 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.141 |  |
| 2026-09-16 13:09:35 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:09:10 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.159 |  |
| 2026-09-16 13:07:11 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-16 13:05:45 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:05:45 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:05:39 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:05:38 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:05:21 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:05:17 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.051 |  |
| 2026-09-16 13:04:49 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.019 |  |
| 2026-09-16 13:03:07 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.059 |  |
| 2026-09-16 13:02:57 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-16 13:02:54 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:02:50 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:02:48 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:02:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:02:37 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:02:36 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.081 |  |
| 2026-09-16 13:02:25 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 13:02:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:02:21 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:02:19 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.150 |  |
| 2026-09-16 13:02:08 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:02:00 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:01:51 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | -0.027 |  |
| 2026-09-16 13:01:45 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:01:43 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.079 |  |
| 2026-09-16 13:01:42 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:01:27 | Magura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-09-16 13:01:15 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:00:48 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:00:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-16 13:00:39 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:00:26 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 13:00:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-16 13:02:57 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-16 13:07:11 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-16 13:02:25 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 13:09:35 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:02:00 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:02:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:01:45 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:01:42 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:05:45 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:05:21 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:00:48 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:02:37 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:02:08 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:05:45 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:01:15 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:14:22 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:02:21 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-16 13:05:38 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:05:39 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:02:48 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:02:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:00:39 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:02:54 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:00:26 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:02:50 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-09-16 13:12:50 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.018 |  |
| 2026-09-16 13:04:49 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.019 |  |
| 2026-09-16 13:01:27 | Magura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-09-16 13:01:51 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | -0.027 |  |
| 2026-09-16 13:05:17 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.051 |  |
| 2026-09-16 13:03:07 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | -0.059 |  |
| 2026-09-16 13:11:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | -0.070 |  |
| 2026-09-16 13:01:43 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.079 |  |
| 2026-09-16 13:02:36 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.081 |  |
| 2026-09-16 13:11:08 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.141 |  |
| 2026-09-16 13:02:19 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.150 |  |
| 2026-09-16 13:09:10 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)