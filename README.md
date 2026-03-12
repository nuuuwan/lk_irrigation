# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_00:11:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,770 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 00:11:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:10:47 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.026 |  |
| 2026-03-13 00:10:15 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 00:09:28 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:08:50 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 00:08:44 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-03-13 00:08:43 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-03-13 00:07:54 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-03-13 00:04:49 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:04:23 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-03-13 00:03:57 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:03:47 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-03-13 00:03:36 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:03:22 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:03:21 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:03:12 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:03:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:03:03 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 00:02:50 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 00:02:44 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:02:34 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.039 |  |
| 2026-03-13 00:02:30 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2026-03-13 00:02:29 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2026-03-13 00:02:19 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:01:47 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:01:45 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 00:01:23 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 00:00:55 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:00:40 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:00:18 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.047 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 00:02:30 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2026-03-13 00:08:44 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-03-13 00:03:47 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-03-12 22:16:26 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-13 00:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-13 00:01:45 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 22:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 00:02:50 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 00:10:15 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 00:01:23 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 00:03:03 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 00:08:50 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 00:00:18 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:01:47 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:00:55 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:01:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:03:57 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:01:36 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:04:07 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:03:22 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:02:44 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-12 22:12:15 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:03:12 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:11:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:00:40 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:03:36 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:03:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:02:19 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 23:10:31 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:09:28 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:04:49 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 00:07:54 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-03-13 00:10:47 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.026 |  |
| 2026-03-13 00:04:23 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-03-12 23:17:42 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-03-13 00:02:34 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.039 |  |
| 2026-03-12 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)