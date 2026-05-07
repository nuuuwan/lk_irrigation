# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_03:15:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,819 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 03:15:59 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.111 |  |
| 2026-05-08 03:15:51 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.081 |  |
| 2026-05-08 03:15:48 | Panadugama (Nilwala Ganga) | 5.04 | 🟡 Alert | 0.068 | 🔺 Rising |
| 2026-05-08 03:15:40 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-08 03:14:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-08 03:13:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-08 03:09:44 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-08 03:08:04 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.072 |  |
| 2026-05-08 03:07:50 | Pitabeddara (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.018 |  |
| 2026-05-08 03:06:42 | Thanamalwila (Kirindi Oya) | 3.31 | 🟢 Normal | -0.098 |  |
| 2026-05-08 03:06:40 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.005 |  |
| 2026-05-08 03:05:42 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.389 | 🔺 Rising |
| 2026-05-08 03:04:00 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-08 03:03:56 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.031 |  |
| 2026-05-08 03:03:53 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 03:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.090 |  |
| 2026-05-08 03:03:34 | Giriulla (Maha Oya) | 2.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 03:03:11 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-05-08 03:03:07 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-08 03:02:32 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.042 |  |
| 2026-05-08 03:02:29 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.096 |  |
| 2026-05-08 03:01:45 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-08 03:01:42 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | -0.012 |  |
| 2026-05-08 03:01:41 | Kuda Oya (Kirindi Oya) | 3.10 | 🟢 Normal | -0.209 |  |
| 2026-05-08 03:01:18 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-05-08 03:01:08 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.061 |  |
| 2026-05-08 03:01:05 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-05-08 03:01:02 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.049 |  |
| 2026-05-08 03:00:44 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -4.053 |  |
| 2026-05-08 03:00:43 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-05-08 02:28:01 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | -4.053 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 03:15:48 | Panadugama (Nilwala Ganga) | 5.04 | 🟡 Alert | 0.068 | 🔺 Rising |
| 2026-05-07 23:00:34 | Weraganthota (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.746 | 🔺 Rising |
| 2026-05-08 03:05:42 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.389 | 🔺 Rising |
| 2026-05-08 03:01:05 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-05-08 03:09:44 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-08 03:14:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-08 02:04:38 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-08 03:04:00 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-08 03:03:34 | Giriulla (Maha Oya) | 2.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 02:03:44 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 03:15:40 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-08 03:03:53 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 03:13:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-08 03:01:45 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-08 03:06:40 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.005 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-08 03:03:07 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-08 03:00:43 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-05-08 03:03:11 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-05-08 03:01:42 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | -0.012 |  |
| 2026-05-08 03:07:50 | Pitabeddara (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.018 |  |
| 2026-05-08 03:01:18 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-05-08 03:03:56 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.031 |  |
| 2026-05-08 03:02:32 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.042 |  |
| 2026-05-08 03:01:02 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.049 |  |
| 2026-05-08 02:06:47 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.060 |  |
| 2026-05-08 02:06:43 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.061 |  |
| 2026-05-08 03:01:08 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.061 |  |
| 2026-05-07 18:00:09 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.063 |  |
| 2026-05-08 03:08:04 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.072 |  |
| 2026-05-08 03:15:51 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.081 |  |
| 2026-05-08 03:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.090 |  |
| 2026-05-08 03:02:29 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.096 |  |
| 2026-05-08 03:06:42 | Thanamalwila (Kirindi Oya) | 3.31 | 🟢 Normal | -0.098 |  |
| 2026-05-08 03:15:59 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.111 |  |
| 2026-05-08 02:05:05 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.131 |  |
| 2026-05-08 03:01:41 | Kuda Oya (Kirindi Oya) | 3.10 | 🟢 Normal | -0.209 |  |
| 2026-05-08 02:08:45 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.223 |  |
| 2026-05-08 03:00:44 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -4.053 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)