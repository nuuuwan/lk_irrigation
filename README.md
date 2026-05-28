# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_23:09:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,318 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 23:09:51 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-05-28 23:09:42 | Panadugama (Nilwala Ganga) | 4.97 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-28 23:09:32 | Rathnapura (Kalu Ganga) | 5.38 | 🟡 Alert | 0.148 | 🔺 Rising |
| 2026-05-28 23:09:16 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-28 23:08:13 | Thawalama (Gin Ganga) | 3.43 | 🟢 Normal | -0.049 |  |
| 2026-05-28 23:06:27 | Hanwella (Kelani Ganga) | 3.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 23:06:21 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:05:50 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.019 |  |
| 2026-05-28 23:05:42 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 23:05:36 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-28 23:05:30 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:05:06 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:04:05 | Nawalapitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-28 23:04:03 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-28 23:03:59 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:03:54 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.192 |  |
| 2026-05-28 23:03:22 | Deraniyagala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-05-28 23:03:15 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.078 |  |
| 2026-05-28 23:03:10 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:03:04 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-05-28 23:02:30 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-28 23:02:14 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:02:14 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-28 23:02:08 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-28 23:02:04 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:01:48 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-28 23:01:46 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-05-28 23:01:41 | Glencourse (Kelani Ganga) | 11.74 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-28 23:01:35 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:01:03 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:00:13 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-28 22:19:24 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.048 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 23:09:32 | Rathnapura (Kalu Ganga) | 5.38 | 🟡 Alert | 0.148 | 🔺 Rising |
| 2026-05-28 21:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | 0.065 | 🔺 Rising |
| 2026-05-28 23:05:50 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.019 |  |
| 2026-05-28 23:03:22 | Deraniyagala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-05-28 23:09:51 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-05-28 23:01:46 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-05-28 23:09:42 | Panadugama (Nilwala Ganga) | 4.97 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-28 23:04:05 | Nawalapitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-28 23:01:41 | Glencourse (Kelani Ganga) | 11.74 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-28 23:09:16 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-28 21:04:57 | Pitabeddara (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-28 23:01:48 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-28 23:00:13 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-28 23:02:08 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-28 23:02:14 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-28 23:05:36 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-28 23:05:42 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 23:06:27 | Hanwella (Kelani Ganga) | 3.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 23:06:21 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-28 22:01:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:01:03 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:03:10 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 22:01:40 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:02:04 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.000 |  |
| 2026-05-28 22:09:33 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:01:35 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:05:06 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:03:10 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:05:30 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:02:12 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:02:14 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:03:59 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-28 23:02:30 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-28 23:04:03 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-28 18:32:56 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.013 |  |
| 2026-05-28 23:03:04 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-05-28 23:08:13 | Thawalama (Gin Ganga) | 3.43 | 🟢 Normal | -0.049 |  |
| 2026-05-28 23:03:15 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.078 |  |
| 2026-05-28 23:03:54 | Urawa (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.192 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)