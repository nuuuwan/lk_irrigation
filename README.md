# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_10:28:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **252,429 measurements** from **39** stations.
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
| 2026-09-05 10:28:30 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:25:26 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-05 10:23:32 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:12:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:10:01 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-05 10:08:38 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-09-05 10:08:15 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:07:48 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-05 10:06:12 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:04:57 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:04:55 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.061 |  |
| 2026-09-05 10:04:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:04:17 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:04:14 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-09-05 10:04:02 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:03:54 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-09-05 10:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:03:39 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-09-05 10:03:19 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-05 10:03:17 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-09-05 10:03:11 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:02:59 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:02:59 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-09-05 10:02:54 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 10:02:46 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-05 10:02:45 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:02:44 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-09-05 10:02:27 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:02:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:01:34 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:01:33 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.078 |  |
| 2026-09-05 10:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:01:18 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:01:14 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.030 |  |
| 2026-09-05 10:01:10 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.163 |  |
| 2026-09-05 10:01:02 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:00:20 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:00:08 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 10:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-09-05 10:10:01 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-05 10:02:46 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-05 10:02:54 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 10:07:48 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-05 10:25:26 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-05 10:02:27 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:00:08 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:28:30 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:04:02 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:01:18 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:01:34 | Galgamuwa (Mee Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 09:11:14 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:02:45 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:04:17 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:23:32 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:04:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:04:57 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:02:00 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:06:12 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:02:59 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:08:15 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:00:20 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:03:11 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:12:28 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:03:54 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-05 10:08:38 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-09-05 10:04:14 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-09-05 10:03:17 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-09-05 10:03:39 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-09-05 10:03:19 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-09-05 10:02:59 | Hanwella (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-09-05 10:01:14 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.030 |  |
| 2026-09-05 10:02:44 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-09-05 10:04:55 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.061 |  |
| 2026-09-05 10:01:33 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.078 |  |
| 2026-09-05 10:01:10 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)