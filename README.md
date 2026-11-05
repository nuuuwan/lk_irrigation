# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_15:19:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,612 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 15:19:27 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:18:58 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:15:31 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:12:36 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-05 15:11:39 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2026-11-05 15:08:53 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.018 |  |
| 2026-11-05 15:07:02 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.164 |  |
| 2026-11-05 15:06:54 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-11-05 15:05:30 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.020 |  |
| 2026-11-05 15:05:29 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:05:22 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:05:14 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:05:05 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 15:04:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.078 |  |
| 2026-11-05 15:04:43 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.080 |  |
| 2026-11-05 15:04:42 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -36.000 |  |
| 2026-11-05 15:04:40 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -36.000 |  |
| 2026-11-05 15:04:20 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-05 15:04:15 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.049 |  |
| 2026-11-05 15:04:13 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-05 15:03:33 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:03:20 | Kuda Oya (Kirindi Oya) | 2.25 | 🟢 Normal | -0.019 |  |
| 2026-11-05 15:03:20 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-05 15:03:03 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-11-05 15:03:02 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.031 |  |
| 2026-11-05 15:02:57 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.077 |  |
| 2026-11-05 15:02:54 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.09 | 🟡 Alert | -0.030 |  |
| 2026-11-05 15:02:44 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-05 15:02:44 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-05 15:02:25 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 15:02:15 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:02:14 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-11-05 15:02:07 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-11-05 15:02:06 | Moragaswewa (Deduru Oya) | 3.41 | 🟢 Normal | -0.040 |  |
| 2026-11-05 15:02:03 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 15:02:00 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:01:53 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-05 15:01:30 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:01:23 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-05 15:01:21 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 15:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.09 | 🟡 Alert | -0.030 |  |
| 2026-11-05 15:02:44 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-05 15:01:23 | Ellagawa (Kalu Ganga) | 6.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-05 15:04:13 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-05 15:02:03 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 15:03:20 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-05 15:02:25 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 15:12:36 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-05 15:05:05 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 15:02:54 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:02:00 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:01:30 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:19:27 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:03:33 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:02:15 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:05:29 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:05:22 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 15:03:03 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-11-05 15:02:44 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-05 15:04:20 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-05 15:01:53 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-05 15:08:53 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.018 |  |
| 2026-11-05 15:03:20 | Kuda Oya (Kirindi Oya) | 2.25 | 🟢 Normal | -0.019 |  |
| 2026-11-05 15:11:39 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2026-11-05 15:02:07 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-11-05 15:05:30 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.020 |  |
| 2026-11-05 15:01:21 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-11-05 15:06:54 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.028 |  |
| 2026-11-05 15:02:14 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-11-05 15:03:02 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.031 |  |
| 2026-11-05 15:02:06 | Moragaswewa (Deduru Oya) | 3.41 | 🟢 Normal | -0.040 |  |
| 2026-11-05 15:04:15 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.049 |  |
| 2026-11-05 15:02:57 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.077 |  |
| 2026-11-05 15:04:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.078 |  |
| 2026-11-05 15:04:43 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.080 |  |
| 2026-11-05 14:05:10 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.155 |  |
| 2026-11-05 15:07:02 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.164 |  |
| 2026-11-05 15:04:42 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)