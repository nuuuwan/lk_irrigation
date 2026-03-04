# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--04_16:12:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,086 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 16:12:17 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:11:15 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:09:20 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-04 16:07:34 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.085 |  |
| 2026-03-04 16:07:31 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-03-04 16:07:31 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:07:25 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:07:07 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:06:51 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:06:36 | Panadugama (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:06:19 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:06:07 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:06:00 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-04 16:05:31 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-03-04 16:05:26 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:05:05 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:04:41 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:04:01 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:03:32 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-04 16:03:27 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:03:27 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-03-04 16:03:26 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-04 16:03:19 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:47 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:21 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:21 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:19 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 16:02:18 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-04 16:02:16 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:13 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:12 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:01:48 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:01:44 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-04 16:01:29 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | -0.110 |  |
| 2026-03-04 16:01:28 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:01:20 | Pitabeddara (Nilwala Ganga) | 9.18 | 🔴 Major Flood | 9.129 | 🔺 Rising |
| 2026-03-04 16:01:06 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-04 16:01:04 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-04 16:01:20 | Pitabeddara (Nilwala Ganga) | 9.18 | 🔴 Major Flood | 9.129 | 🔺 Rising |
| 2026-03-04 16:02:18 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-04 16:03:32 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-04 16:03:26 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-04 16:01:06 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-04 16:09:20 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-04 16:02:47 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 16:01:04 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 16:02:19 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 16:02:21 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:01:48 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:05:26 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:16 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:04:01 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:07:31 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:03:19 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:21 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:06:36 | Panadugama (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-04 15:05:09 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:04:41 | Glencourse (Kelani Ganga) | 8.15 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:01:28 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:06:07 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:07:25 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:03:27 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:12 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:11:15 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:06:51 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:07:07 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:12:17 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:13 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-04 16:07:31 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-03-04 16:06:00 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-04 16:01:44 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-04 16:05:31 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-03-04 16:03:27 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-03-04 16:07:34 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.085 |  |
| 2026-03-04 16:01:29 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)