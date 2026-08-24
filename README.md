# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_16:36:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,325 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 16:36:22 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-24 16:11:38 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-24 16:11:01 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:10:15 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:09:48 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:09:45 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-24 16:09:17 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 16:09:04 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:08:54 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:07:47 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.028 |  |
| 2026-08-24 16:07:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-08-24 16:07:09 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:06:40 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:06:32 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.028 |  |
| 2026-08-24 16:05:52 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:04:51 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:04:46 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:04:42 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:04:25 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:04:20 | Moragaswewa (Deduru Oya) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 16:04:15 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:03:43 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.073 |  |
| 2026-08-24 16:03:19 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:03:03 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-08-24 16:03:01 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:02:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:02:35 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:02:34 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-08-24 16:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 16:01:41 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:00:57 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-24 16:00:46 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:00:39 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:00:31 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:00:19 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.122 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 16:07:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-08-24 16:00:57 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-24 16:36:22 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-24 16:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 15:02:35 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 16:09:17 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 16:04:20 | Moragaswewa (Deduru Oya) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 16:09:45 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-24 16:11:38 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-24 16:04:42 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:00:31 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:01:41 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:09:48 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:11:01 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:08:54 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:09:04 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:05:52 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:06:40 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:00:46 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:02:34 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:02:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:10:15 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 15:03:25 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:04:46 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:07:09 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 16:04:25 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:03:01 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:04:51 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:03:19 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:02:35 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:00:39 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:04:15 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-08-24 15:02:49 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.020 |  |
| 2026-08-24 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-08-24 16:03:03 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-08-24 16:06:32 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.028 |  |
| 2026-08-24 16:07:47 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.028 |  |
| 2026-08-24 16:03:43 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.073 |  |
| 2026-08-24 16:00:19 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)