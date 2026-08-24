# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_22:34:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,550 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 22:34:41 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:32:45 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:19:14 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:12:37 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.048 |  |
| 2026-08-24 22:09:59 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:09:08 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 22:07:39 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-08-24 22:07:01 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:06:30 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-08-24 22:06:23 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:06:07 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 22:04:05 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-24 22:05:35 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-24 22:03:49 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 22:05:08 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 22:01:45 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-24 22:01:12 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 22:09:08 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 22:01:54 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 22:00:35 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 21:05:56 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 22:03:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:00:16 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:32:45 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:06:23 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:03:52 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:03:23 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:02:21 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:34:41 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:19:14 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:00:57 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:00:53 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:02:32 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:02:15 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:02:09 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:03:21 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:04:29 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:07:01 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:09:59 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:01:16 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:13:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-24 22:06:30 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-08-24 18:01:27 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-24 22:07:39 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-08-24 22:00:45 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.010 |  |
| 2026-08-24 22:02:57 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-08-24 22:02:07 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-08-24 22:06:07 | Ellagawa (Kalu Ganga) | 4.84 | 🟢 Normal | -0.032 |  |
| 2026-08-24 22:12:37 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.048 |  |
| 2026-08-24 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)