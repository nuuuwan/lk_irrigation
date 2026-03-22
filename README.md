# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_11:05:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,219 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 11:05:49 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:05:46 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.038 |  |
| 2026-03-22 11:05:07 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-22 11:04:58 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:03:54 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.070 |  |
| 2026-03-22 11:03:52 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:03:51 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | 21.969 | 🔺 Rising |
| 2026-03-22 11:03:29 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-22 11:03:22 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.040 |  |
| 2026-03-22 11:03:11 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:02:54 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:02:20 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-22 11:02:17 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-03-22 11:02:05 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-03-22 11:01:52 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.079 |  |
| 2026-03-22 11:01:52 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 11:01:29 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:25 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-22 11:01:23 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:21 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:17 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:15 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 11:00:36 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 21.969 | 🔺 Rising |
| 2026-03-22 11:00:34 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:00:09 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.090 |  |
| 2026-03-22 10:31:27 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-03-22 10:31:17 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 10:16:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.081 |  |
| 2026-03-22 10:13:09 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.069 |  |
| 2026-03-22 10:12:29 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.070 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 11:03:51 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | 21.969 | 🔺 Rising |
| 2026-03-22 11:02:05 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-03-22 11:05:07 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-22 11:02:20 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-22 10:02:30 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-22 11:03:29 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-22 10:03:47 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 11:01:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 11:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 11:02:54 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:52 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:29 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 10:01:35 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 10:05:29 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:21 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 10:08:24 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:03:11 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-22 10:31:17 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:00:34 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:04:58 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:23 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:15 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:05:49 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:03:52 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:17 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 10:05:19 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-22 10:01:48 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 11:01:25 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-22 09:06:08 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-22 11:02:17 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-03-22 10:31:27 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-03-22 11:05:46 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.038 |  |
| 2026-03-22 11:03:22 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.040 |  |
| 2026-03-22 10:13:09 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.069 |  |
| 2026-03-22 11:03:54 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.070 |  |
| 2026-03-22 11:01:52 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.079 |  |
| 2026-03-22 10:16:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.081 |  |
| 2026-03-22 10:08:08 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.090 |  |
| 2026-03-22 11:00:09 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)