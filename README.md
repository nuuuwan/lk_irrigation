# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_17:19:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,246 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 17:19:11 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-24 17:18:25 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-24 17:12:58 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-24 17:11:14 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:10:47 | Baddegama (Gin Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:09:11 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:09:06 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:08:31 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:08:28 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-03-24 17:06:12 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:05:43 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:05:36 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:05:12 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-24 17:04:40 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-24 17:04:13 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.039 |  |
| 2026-03-24 17:04:07 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-03-24 17:03:50 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.012 |  |
| 2026-03-24 17:03:46 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-24 17:03:23 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 17:03:12 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:03:11 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-24 17:03:00 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:03:00 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:02:37 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-24 17:02:34 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:02:23 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-24 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-03-24 17:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:48 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:46 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:42 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:40 | Baddegama (Gin Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:23 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:21 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:08 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:07 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-24 17:00:36 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:00:34 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.105 |  |
| 2026-03-24 17:00:18 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 17:03:46 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-24 17:05:12 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-24 17:04:40 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-24 17:18:25 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-24 17:12:58 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-24 17:03:11 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-24 17:19:11 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-24 17:02:37 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-24 17:03:23 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 17:01:48 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:03:00 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:21 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:02:34 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:05:36 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:03:12 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:03:00 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:11:14 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:10:47 | Baddegama (Gin Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-24 16:03:32 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:42 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:08:31 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:06:12 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:05:43 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:00:36 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:09:11 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:46 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:09:06 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:08 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:01:23 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-24 17:08:28 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-03-24 17:02:23 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-24 17:01:07 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-24 17:04:07 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-03-24 17:00:18 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-03-24 17:03:50 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.012 |  |
| 2026-03-24 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-03-24 17:04:13 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.039 |  |
| 2026-03-24 17:00:34 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)