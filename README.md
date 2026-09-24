# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_22:07:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,026 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 22:07:04 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.097 |  |
| 2026-09-24 22:06:39 | Norwood (Kelani Ganga) | 1.53 | 🟡 Alert | -0.020 |  |
| 2026-09-24 22:06:10 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 22:06:02 | Ellagawa (Kalu Ganga) | 8.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 22:05:47 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-24 22:05:28 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:05:25 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:04:59 | Rathnapura (Kalu Ganga) | 6.31 | 🟡 Alert | 0.138 | 🔺 Rising |
| 2026-09-24 22:03:57 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-24 22:03:51 | Deraniyagala (Kelani Ganga) | 3.56 | 🟢 Normal | -0.169 |  |
| 2026-09-24 22:03:50 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-24 22:03:29 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:03:18 | Glencourse (Kelani Ganga) | 14.39 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-09-24 22:02:50 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-24 22:02:44 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 22:02:41 | Thawalama (Gin Ganga) | 5.09 | 🟡 Alert | -0.030 |  |
| 2026-09-24 22:02:36 | Hanwella (Kelani Ganga) | 5.76 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-24 22:02:23 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-24 22:02:11 | Nawalapitiya (Mahaweli Ganga) | 3.34 | 🟢 Normal | -0.060 |  |
| 2026-09-24 22:02:09 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-09-24 22:02:09 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:01:26 | Holombuwa (Kelani Ganga) | 2.10 | 🟢 Normal | -0.320 |  |
| 2026-09-24 22:01:25 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:01:09 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:00:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 22:00:14 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 21:08:55 | Baddegama (Gin Ganga) | 4.52 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-09-24 22:06:10 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 22:00:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 21:14:13 | Panadugama (Nilwala Ganga) | 6.74 | 🟠 Minor Flood | -0.009 |  |
| 2026-09-24 22:04:59 | Rathnapura (Kalu Ganga) | 6.31 | 🟡 Alert | 0.138 | 🔺 Rising |
| 2026-09-24 22:03:57 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-24 22:06:39 | Norwood (Kelani Ganga) | 1.53 | 🟡 Alert | -0.020 |  |
| 2026-09-24 22:02:41 | Thawalama (Gin Ganga) | 5.09 | 🟡 Alert | -0.030 |  |
| 2026-09-24 21:08:16 | Kithulgala (Kelani Ganga) | 3.30 | 🟡 Alert | -0.239 |  |
| 2026-09-24 22:03:18 | Glencourse (Kelani Ganga) | 14.39 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-09-24 22:02:36 | Hanwella (Kelani Ganga) | 5.76 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-24 22:03:50 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-24 22:02:23 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-24 22:05:47 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-24 22:06:02 | Ellagawa (Kalu Ganga) | 8.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 22:02:44 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 22:00:14 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-24 21:07:06 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 21:03:04 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 21:07:03 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:05:28 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:02:09 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:05:25 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:03:29 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 22:01:09 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 21:04:03 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 21:04:50 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-09-24 21:02:06 | Peradeniya (Mahaweli Ganga) | 4.47 | 🟢 Normal | -0.010 |  |
| 2026-09-24 22:02:09 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-09-24 22:02:50 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-24 21:08:40 | Urawa (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.058 |  |
| 2026-09-24 22:02:11 | Nawalapitiya (Mahaweli Ganga) | 3.34 | 🟢 Normal | -0.060 |  |
| 2026-09-24 22:07:04 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.097 |  |
| 2026-09-24 22:03:51 | Deraniyagala (Kelani Ganga) | 3.56 | 🟢 Normal | -0.169 |  |
| 2026-09-24 22:01:26 | Holombuwa (Kelani Ganga) | 2.10 | 🟢 Normal | -0.320 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)