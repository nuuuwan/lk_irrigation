# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_21:11:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,213 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 21:11:03 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | -0.302 |  |
| 2026-10-22 21:09:38 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:08:26 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-22 21:08:15 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:08:00 | Glencourse (Kelani Ganga) | 12.44 | 🟢 Normal | -0.009 |  |
| 2026-10-22 21:07:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 21:07:04 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:06:18 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-22 21:06:17 | Pitabeddara (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-22 21:06:11 | Rathnapura (Kalu Ganga) | 4.48 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-22 21:06:10 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 21:05:27 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 21:05:25 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-22 21:05:07 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-10-22 21:03:42 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:03:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:03:37 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-22 21:03:35 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 21:03:33 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-22 21:03:31 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:03:29 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.021 |  |
| 2026-10-22 21:03:12 | Giriulla (Maha Oya) | 2.53 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-22 21:03:12 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-22 21:02:29 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:02:27 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.037 |  |
| 2026-10-22 21:02:27 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-22 21:02:26 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-10-22 21:02:17 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:01:59 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-22 21:01:59 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.070 |  |
| 2026-10-22 21:01:53 | Moragaswewa (Deduru Oya) | 5.08 | 🟡 Alert | 0.112 | 🔺 Rising |
| 2026-10-22 21:01:50 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-22 21:01:32 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.052 |  |
| 2026-10-22 21:01:22 | Horowpothana (Yan Oya) | 3.03 | 🟢 Normal | 1.035 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 21:01:53 | Moragaswewa (Deduru Oya) | 5.08 | 🟡 Alert | 0.112 | 🔺 Rising |
| 2026-10-22 21:01:22 | Horowpothana (Yan Oya) | 3.03 | 🟢 Normal | 1.035 | 🔺 Rising |
| 2026-10-22 21:03:12 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-22 20:01:16 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-22 21:03:12 | Giriulla (Maha Oya) | 2.53 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-22 21:06:11 | Rathnapura (Kalu Ganga) | 4.48 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-22 21:06:17 | Pitabeddara (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-22 21:08:26 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-22 21:06:18 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-22 21:07:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 21:05:25 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-22 21:03:35 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 18:02:35 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 21:06:10 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 21:05:27 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 21:02:29 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:07:04 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:08:15 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:03:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-22 20:00:14 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:09:38 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:03:31 | Badalgama (Maha Oya) | 3.56 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:03:42 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:02:17 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-22 21:08:00 | Glencourse (Kelani Ganga) | 12.44 | 🟢 Normal | -0.009 |  |
| 2026-10-22 21:03:33 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-22 21:02:27 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-22 21:01:59 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-22 21:03:37 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-22 21:02:26 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-10-22 21:03:29 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | -0.021 |  |
| 2026-10-22 21:05:07 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-10-22 21:01:50 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-22 21:02:27 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.037 |  |
| 2026-10-22 21:01:32 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.052 |  |
| 2026-10-22 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-10-22 21:01:59 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.070 |  |
| 2026-10-22 21:11:03 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | -0.302 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)