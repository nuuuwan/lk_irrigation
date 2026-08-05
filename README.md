# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_19:21:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,837 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 19:21:37 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:18:51 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-08-05 19:17:34 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:16:56 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.024 |  |
| 2026-08-05 19:16:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.073 |  |
| 2026-08-05 19:11:33 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.109 |  |
| 2026-08-05 19:08:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:07:13 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:05:43 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.019 |  |
| 2026-08-05 19:05:29 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.048 |  |
| 2026-08-05 19:05:18 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | -0.125 |  |
| 2026-08-05 19:05:11 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:05:00 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:04:55 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-08-05 19:04:43 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.049 |  |
| 2026-08-05 19:04:00 | Peradeniya (Mahaweli Ganga) | 6.45 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-08-05 19:03:51 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.021 |  |
| 2026-08-05 19:03:40 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | -0.041 |  |
| 2026-08-05 19:03:35 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.060 |  |
| 2026-08-05 19:03:27 | Putupaula (Kalu Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:03:19 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.050 |  |
| 2026-08-05 19:03:15 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-05 19:02:59 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:02:58 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:02:56 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:02:30 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | -0.228 |  |
| 2026-08-05 19:02:23 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-08-05 19:02:15 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-08-05 19:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:01:52 | Nawalapitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.020 |  |
| 2026-08-05 19:01:35 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:01:08 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.021 |  |
| 2026-08-05 19:01:07 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | -0.052 |  |
| 2026-08-05 19:01:04 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-08-05 19:00:38 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-05 19:00:31 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:00:13 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 19:04:00 | Peradeniya (Mahaweli Ganga) | 6.45 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-08-05 19:18:51 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-08-05 19:00:38 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-05 19:03:15 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-05 19:02:58 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:00:13 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:01:35 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:07:13 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:08:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:00:31 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:02:56 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:05:11 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:03:27 | Putupaula (Kalu Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:17:34 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:21:37 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:02:59 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:05:00 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 19:04:55 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-05 19:05:43 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.019 |  |
| 2026-08-05 19:01:52 | Nawalapitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.020 |  |
| 2026-08-05 19:02:15 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-08-05 19:03:51 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.021 |  |
| 2026-08-05 19:01:08 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.021 |  |
| 2026-08-05 19:16:56 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.024 |  |
| 2026-08-05 19:02:23 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-08-05 19:03:40 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | -0.041 |  |
| 2026-08-05 19:05:29 | Deraniyagala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.048 |  |
| 2026-08-05 19:04:43 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.049 |  |
| 2026-08-05 19:03:19 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.050 |  |
| 2026-08-05 19:01:07 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | -0.052 |  |
| 2026-08-05 19:03:35 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.060 |  |
| 2026-08-05 19:16:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | -0.073 |  |
| 2026-08-05 19:11:33 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.109 |  |
| 2026-08-05 19:05:18 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | -0.125 |  |
| 2026-08-05 19:02:30 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | -0.228 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)