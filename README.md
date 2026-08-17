# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_15:11:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **236,020 measurements** from **39** stations.
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
| 2026-08-17 15:11:05 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:10:28 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:07:12 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 15:06:50 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:06:15 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:05:27 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-17 15:05:13 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-08-17 15:04:51 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-17 15:04:28 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-08-17 15:04:11 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-08-17 15:03:56 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:03:51 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:03:23 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:03:18 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:03:08 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:02:58 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 15:02:57 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:02:51 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 15:02:44 | Thanamalwila (Kirindi Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-08-17 15:02:35 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 15:02:31 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:02:29 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:02:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-17 15:02:19 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 15:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:02:07 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-08-17 15:01:55 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:01:49 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 15:01:36 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.020 |  |
| 2026-08-17 15:01:34 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.011 |  |
| 2026-08-17 15:01:31 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:01:23 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-08-17 15:01:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:01:13 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 15:01:04 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:00:50 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:00:45 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:00:31 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 15:04:11 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-08-17 15:02:27 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-17 15:05:27 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-17 15:02:19 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 15:01:49 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 15:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 15:02:58 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 15:02:35 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 15:02:51 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 15:07:12 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 15:00:50 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:03:23 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:01:55 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:01:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:00:31 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:02:31 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:03:56 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:10:28 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-08-17 14:24:25 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:11:05 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:01:13 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:03:18 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:03:08 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:02:29 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:02:57 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:03:51 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:00:45 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:06:50 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:01:04 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:01:31 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-17 15:05:13 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-08-17 15:02:44 | Thanamalwila (Kirindi Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-08-17 15:04:51 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-17 15:01:34 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.011 |  |
| 2026-08-17 15:04:28 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-08-17 15:01:36 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.020 |  |
| 2026-08-17 15:01:23 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-08-17 15:02:07 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.021 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)