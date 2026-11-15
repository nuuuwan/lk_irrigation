# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_03:22:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,039 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 03:22:17 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | -0.016 |  |
| 2026-11-16 03:16:03 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.008 |  |
| 2026-11-16 03:14:58 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.017 |  |
| 2026-11-16 03:14:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.15 | 🟢 Normal | 1.047 | 🔺 Rising |
| 2026-11-16 03:10:10 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:09:15 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-16 03:06:54 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:06:49 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:06:14 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-16 03:05:52 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.005 |  |
| 2026-11-16 03:05:30 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -36.000 |  |
| 2026-11-16 03:05:29 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -36.000 |  |
| 2026-11-16 03:04:52 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-16 03:04:35 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-16 03:04:19 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:04:19 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-16 03:04:04 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:03:54 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-11-16 03:03:21 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:03:18 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-16 03:02:46 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-16 03:02:45 | Thalgahagoda (Nilwala Ganga) | 1.63 | 🟡 Alert | -0.012 |  |
| 2026-11-16 03:02:43 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-16 03:02:30 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | 3.347 | 🔺 Rising |
| 2026-11-16 03:02:24 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:02:23 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:02:19 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:01:56 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 03:01:50 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:01:38 | Peradeniya (Mahaweli Ganga) | 2.91 | 🟢 Normal | -0.038 |  |
| 2026-11-16 03:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:01:10 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:01:09 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.040 |  |
| 2026-11-16 03:00:33 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 02:44:59 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 03:02:45 | Thalgahagoda (Nilwala Ganga) | 1.63 | 🟡 Alert | -0.012 |  |
| 2026-11-16 03:02:30 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | 3.347 | 🔺 Rising |
| 2026-11-16 03:14:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.15 | 🟢 Normal | 1.047 | 🔺 Rising |
| 2026-11-16 02:28:48 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-11-16 03:02:46 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-16 03:09:15 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-16 03:02:43 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-16 03:04:52 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-16 03:01:56 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 03:01:10 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:06:54 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:04:19 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:01:50 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:02:24 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:06:49 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-16 02:02:20 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:00:33 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:02:19 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:02:23 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-16 02:03:02 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:04:04 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:10:10 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:03:21 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:37 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-16 03:05:52 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.005 |  |
| 2026-11-16 03:16:03 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.008 |  |
| 2026-11-16 03:06:14 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-16 03:04:19 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-16 03:03:18 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-11-16 03:03:54 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-11-16 03:04:35 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:01:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-16 03:22:17 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | -0.016 |  |
| 2026-11-16 03:14:58 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.017 |  |
| 2026-11-16 03:01:38 | Peradeniya (Mahaweli Ganga) | 2.91 | 🟢 Normal | -0.038 |  |
| 2026-11-16 03:01:09 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.040 |  |
| 2026-11-15 18:01:59 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.181 |  |
| 2026-11-16 03:05:30 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)