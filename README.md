# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_11:25:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,561 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 11:25:46 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.047 |  |
| 2026-11-04 11:12:34 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.052 |  |
| 2026-11-04 11:11:10 | Giriulla (Maha Oya) | 2.76 | 🟢 Normal | -0.108 |  |
| 2026-11-04 11:09:42 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-11-04 11:09:11 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -96.000 |  |
| 2026-11-04 11:09:08 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | -96.000 |  |
| 2026-11-04 11:08:19 | Galgamuwa (Mee Oya) | 1.01 | 🟢 Normal | -0.027 |  |
| 2026-11-04 11:08:17 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:08:02 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-11-04 11:07:06 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.047 |  |
| 2026-11-04 11:06:11 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | -0.229 |  |
| 2026-11-04 11:05:37 | Badalgama (Maha Oya) | 4.07 | 🟢 Normal | -0.079 |  |
| 2026-11-04 11:05:19 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.052 |  |
| 2026-11-04 11:04:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-04 11:04:46 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 11:04:14 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:04:13 | Putupaula (Kalu Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 11:04:09 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-11-04 11:03:48 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.061 |  |
| 2026-11-04 11:03:21 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:03:20 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-11-04 11:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:02:39 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-11-04 11:02:28 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 11:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-04 11:02:19 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:02:08 | Ellagawa (Kalu Ganga) | 6.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-04 11:02:06 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:45 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-11-04 11:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:30 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 11:01:22 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-11-04 11:01:20 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:01:16 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:12 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:00:51 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.090 |  |
| 2026-11-04 11:00:42 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-04 11:00:32 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-11-04 11:00:23 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:00:19 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 11:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-04 11:09:42 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.835 | 🔺 Rising |
| 2026-11-04 11:04:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-04 11:00:42 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-04 11:04:13 | Putupaula (Kalu Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 11:04:46 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 11:02:28 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 11:01:30 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 11:02:08 | Ellagawa (Kalu Ganga) | 6.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-04 11:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:16 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:00:23 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:04:14 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:12 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:02:06 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:08:17 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:20 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:03:21 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:02:19 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:01:45 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-11-04 11:08:02 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-11-04 11:03:20 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-11-04 11:04:09 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-11-04 11:08:19 | Galgamuwa (Mee Oya) | 1.01 | 🟢 Normal | -0.027 |  |
| 2026-11-04 11:02:39 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-11-04 11:01:22 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-11-04 11:00:19 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.032 |  |
| 2026-11-04 11:00:32 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-11-04 11:25:46 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.047 |  |
| 2026-11-04 11:07:06 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.047 |  |
| 2026-11-04 11:12:34 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.052 |  |
| 2026-11-04 11:05:19 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.052 |  |
| 2026-11-04 11:03:48 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.061 |  |
| 2026-11-04 11:05:37 | Badalgama (Maha Oya) | 4.07 | 🟢 Normal | -0.079 |  |
| 2026-11-04 11:00:51 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.090 |  |
| 2026-11-04 11:11:10 | Giriulla (Maha Oya) | 2.76 | 🟢 Normal | -0.108 |  |
| 2026-11-04 11:06:11 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | -0.229 |  |
| 2026-11-04 11:09:11 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -96.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)