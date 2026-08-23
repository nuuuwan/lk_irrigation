# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_17:17:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **241,479 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 17:17:06 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:11:05 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-23 17:11:02 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:10:21 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-08-23 17:10:08 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-23 17:09:50 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:08:33 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:06:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.27 | 🟢 Normal | -0.012 |  |
| 2026-08-23 17:06:35 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:06:25 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:06:06 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.009 |  |
| 2026-08-23 17:05:23 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:04:58 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:04:50 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:04:42 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.032 |  |
| 2026-08-23 17:04:36 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.133 |  |
| 2026-08-23 17:04:33 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:04:28 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-23 17:03:43 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-08-23 17:03:29 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-08-23 17:03:12 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:03:08 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:03:08 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:03:07 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:03:06 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:03:05 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:03:04 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:03:03 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:02:50 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:02:48 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:01:43 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:01:35 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:01:27 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:01:11 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.369 | 🔺 Rising |
| 2026-08-23 17:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-08-23 17:01:00 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:00:54 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:00:50 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:00:41 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:00:24 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:00:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 17:01:11 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.369 | 🔺 Rising |
| 2026-08-23 17:10:21 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-08-23 17:10:08 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-23 16:00:45 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-23 17:11:05 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-23 17:04:28 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-23 17:00:54 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:01:43 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:00:50 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:06:35 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-23 16:04:04 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:02:50 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:01:00 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:00:41 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:04:50 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:03:12 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:03:08 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-23 16:03:52 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:00:24 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:11:02 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:00:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:09:50 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:01:27 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:02:48 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:06:25 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:04:58 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:03:08 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:17:06 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:05:23 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:08:33 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:01:35 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:06:06 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.009 |  |
| 2026-08-23 17:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-08-23 17:06:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.27 | 🟢 Normal | -0.012 |  |
| 2026-08-23 17:03:43 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-08-23 16:00:53 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.020 |  |
| 2026-08-23 17:03:29 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-08-23 17:04:42 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.032 |  |
| 2026-08-23 17:04:36 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)