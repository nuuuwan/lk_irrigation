# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_22:27:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,304 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 22:27:17 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.014 |  |
| 2026-11-20 22:22:19 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:15:30 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-20 22:14:39 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-20 22:11:41 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-11-20 22:11:08 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | 0.691 | 🔺 Rising |
| 2026-11-20 22:09:00 | Nawalapitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.786 | 🔺 Rising |
| 2026-11-20 22:08:21 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-20 22:07:03 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:06:34 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 22:06:32 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-20 22:06:24 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-11-20 22:05:56 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.046 |  |
| 2026-11-20 22:04:44 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 22:04:32 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-11-20 22:04:21 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-20 22:04:04 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:03:59 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-20 22:03:27 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-20 22:03:22 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:02:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-20 22:02:52 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-20 22:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-20 22:02:46 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-20 22:02:44 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:02:40 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.628 | 🔺 Rising |
| 2026-11-20 22:01:50 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:01:44 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-11-20 22:01:28 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-11-20 22:01:20 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:00:52 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:00:46 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:00:42 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:00:41 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:00:20 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 22:09:00 | Nawalapitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.786 | 🔺 Rising |
| 2026-11-20 22:11:08 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | 0.691 | 🔺 Rising |
| 2026-11-20 22:02:40 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.628 | 🔺 Rising |
| 2026-11-20 22:11:41 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-11-20 22:04:32 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.284 | 🔺 Rising |
| 2026-11-20 22:14:39 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-20 22:02:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-20 22:08:21 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-20 22:03:27 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-20 22:02:52 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-20 22:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-20 22:03:59 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-20 22:06:34 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 22:02:46 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-20 22:00:20 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 22:04:44 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 22:15:30 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-20 22:00:41 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:04:04 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:01:50 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:03:22 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:00:42 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-20 18:00:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:22:19 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:07:03 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:02:44 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:00:52 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:00:46 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:01:20 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-20 22:04:21 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-20 22:06:24 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-11-20 22:06:32 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-20 22:01:28 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-11-20 18:01:40 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-20 22:27:17 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.014 |  |
| 2026-11-20 18:00:21 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.020 |  |
| 2026-11-20 22:01:44 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-11-20 22:05:56 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | -0.046 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)