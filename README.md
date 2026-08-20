# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_17:21:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,779 measurements** from **39** stations.
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
| 2026-08-20 17:21:02 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:13:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:12:30 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.177 |  |
| 2026-08-20 17:12:19 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:12:18 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-20 17:11:02 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.046 |  |
| 2026-08-20 17:09:11 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:09:11 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.047 |  |
| 2026-08-20 17:08:47 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-08-20 17:08:24 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:07:53 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-20 17:07:35 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:07:34 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-08-20 17:07:25 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:06:31 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.009 |  |
| 2026-08-20 17:06:01 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-20 17:05:58 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:05:43 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:05:13 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:04:45 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:04:27 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 17:04:13 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-08-20 17:03:33 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:03:27 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:02:50 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.523 | 🔺 Rising |
| 2026-08-20 17:02:48 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:02:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-20 17:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-20 17:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-08-20 17:02:03 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:01:58 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:01:54 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:01:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-20 17:01:17 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:01:11 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:00:52 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:00:42 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:00:41 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:00:35 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 17:02:50 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.523 | 🔺 Rising |
| 2026-08-20 17:07:53 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-20 17:02:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-20 17:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-20 17:01:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-20 17:12:18 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-20 17:04:27 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 17:00:52 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:02:48 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:03:27 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:01:58 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:01:17 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:07:25 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:08:24 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:09:11 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:00:41 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:02:03 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:03:33 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:21:02 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:05:58 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:05:43 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:05:13 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:04:45 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:07:35 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:13:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:01:54 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:12:19 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:01:11 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:00:42 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-20 17:06:31 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.009 |  |
| 2026-08-20 17:06:01 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-20 17:07:34 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-08-20 17:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-08-20 17:08:47 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-08-20 17:04:13 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-08-20 17:00:35 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-08-20 17:11:02 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.046 |  |
| 2026-08-20 17:09:11 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.047 |  |
| 2026-08-20 17:12:30 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)