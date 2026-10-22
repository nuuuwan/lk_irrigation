# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_23:06:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,278 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 23:06:35 | Dunamale (Aththanagalu Oya) | 2.99 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 23:06:19 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | -0.020 |  |
| 2026-10-22 23:06:07 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 23:05:37 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 23:05:01 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.207 |  |
| 2026-10-22 23:04:47 | Rathnapura (Kalu Ganga) | 4.58 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 23:04:45 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | -0.020 |  |
| 2026-10-22 23:04:18 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-22 23:04:15 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-10-22 23:03:23 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.060 |  |
| 2026-10-22 23:03:22 | Hanwella (Kelani Ganga) | 4.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 23:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-22 23:02:36 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 23:02:33 | Holombuwa (Kelani Ganga) | 1.63 | 🟢 Normal | -0.062 |  |
| 2026-10-22 23:02:31 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-22 23:02:28 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-22 23:02:26 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 23:02:22 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 23:02:09 | Moragaswewa (Deduru Oya) | 5.18 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-10-22 23:02:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-22 23:01:52 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.051 |  |
| 2026-10-22 23:01:37 | Pitabeddara (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-22 23:01:29 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-10-22 23:01:27 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 23:01:24 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-22 23:01:22 | Giriulla (Maha Oya) | 2.67 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-22 23:01:16 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-22 23:01:09 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-22 23:01:09 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-22 23:00:33 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-10-22 22:27:24 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | 0.071 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 23:02:09 | Moragaswewa (Deduru Oya) | 5.18 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-10-22 23:02:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-22 23:01:22 | Giriulla (Maha Oya) | 2.67 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-22 23:02:31 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-22 23:06:35 | Dunamale (Aththanagalu Oya) | 2.99 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 23:05:37 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 23:04:47 | Rathnapura (Kalu Ganga) | 4.58 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 23:01:37 | Pitabeddara (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-22 23:04:18 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-22 23:01:27 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 23:02:26 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 18:02:35 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 23:06:07 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 22:11:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 23:02:22 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 21:06:10 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 23:03:22 | Hanwella (Kelani Ganga) | 4.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 23:01:09 | Wellawaya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-22 23:02:28 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-22 23:01:29 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:11:32 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:02:06 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:03:34 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 23:02:36 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-22 22:04:41 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-22 23:01:16 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-22 23:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-22 23:01:09 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-22 23:06:19 | Thawalama (Gin Ganga) | 2.74 | 🟢 Normal | -0.020 |  |
| 2026-10-22 23:00:33 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-10-22 23:04:45 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | -0.020 |  |
| 2026-10-22 23:04:15 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-10-22 22:09:52 | Urawa (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.027 |  |
| 2026-10-22 23:01:52 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.051 |  |
| 2026-10-22 23:03:23 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.060 |  |
| 2026-10-22 23:02:33 | Holombuwa (Kelani Ganga) | 1.63 | 🟢 Normal | -0.062 |  |
| 2026-10-22 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-10-22 23:05:01 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)