# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_20:14:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,216 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 20:14:22 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:14:21 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-28 20:12:25 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-05-28 20:11:00 | Urawa (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.082 |  |
| 2026-05-28 20:10:47 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-28 20:10:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.32 | 🟡 Alert | 0.000 |  |
| 2026-05-28 20:07:57 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-28 20:07:05 | Magura (Kalu Ganga) | 4.99 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-05-28 20:05:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:05:29 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-28 20:05:27 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:05:16 | Hanwella (Kelani Ganga) | 3.73 | 🟢 Normal | -0.031 |  |
| 2026-05-28 20:05:03 | Thawalama (Gin Ganga) | 3.38 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-05-28 20:04:51 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-28 20:04:13 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-05-28 20:04:12 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 20:04:03 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:03:45 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:03:30 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-28 20:03:22 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:03:07 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:03:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.059 |  |
| 2026-05-28 20:02:59 | Deraniyagala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-28 20:02:53 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-05-28 20:02:35 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:02:31 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.060 |  |
| 2026-05-28 20:02:22 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-28 20:02:17 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:01:59 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:01:22 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:01:22 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:01:04 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:00:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:00:47 | Pitabeddara (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-28 20:00:19 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:59:26 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 20:07:05 | Magura (Kalu Ganga) | 4.99 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-05-28 20:10:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.32 | 🟡 Alert | 0.000 |  |
| 2026-05-28 20:12:25 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-05-28 20:05:03 | Thawalama (Gin Ganga) | 3.38 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-05-28 20:02:53 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-05-28 20:02:59 | Deraniyagala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-28 20:05:29 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-28 20:03:30 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-05-28 20:00:47 | Pitabeddara (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-28 20:14:21 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-28 20:10:47 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-28 20:07:57 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-28 20:02:22 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-28 20:04:51 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-28 20:04:12 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 20:00:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:05:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:03:07 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:01:22 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:03:10 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:02:35 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:01:22 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:59:26 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:00:19 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:03:22 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:14:22 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:04:03 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:02:17 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:05:27 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:01:04 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:02:12 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:03:45 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:01:59 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-28 20:04:13 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-05-28 18:32:56 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.013 |  |
| 2026-05-28 20:05:16 | Hanwella (Kelani Ganga) | 3.73 | 🟢 Normal | -0.031 |  |
| 2026-05-28 20:03:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.059 |  |
| 2026-05-28 20:02:31 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.060 |  |
| 2026-05-28 20:11:00 | Urawa (Nilwala Ganga) | 2.15 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)