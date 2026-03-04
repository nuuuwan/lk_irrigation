# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--05_05:11:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,551 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 05:11:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.055 |  |
| 2026-03-05 05:08:32 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-03-05 05:07:08 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:07:06 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:07:04 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:06:52 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-05 05:06:42 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:06:37 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 05:06:09 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-05 05:06:03 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:05:27 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:05:15 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:05:03 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:04:43 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:04:40 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:04:32 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.061 |  |
| 2026-03-05 05:04:21 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:04:02 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 05:04:01 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-05 05:03:35 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:03:05 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.050 |  |
| 2026-03-05 05:02:54 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:02:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:02:35 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-03-05 05:02:21 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-05 05:01:56 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:54 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:49 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.119 |  |
| 2026-03-05 05:01:30 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:21 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:18 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:11 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:00 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-05 05:00:46 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:00:29 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-05 05:00:27 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 05:08:32 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-03-05 05:01:00 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-04 18:01:40 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-05 03:14:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-05 05:02:21 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-05 05:06:09 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-05 05:06:52 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-05 05:00:29 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-05 05:04:01 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-05 05:04:02 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 18:01:42 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 05:06:37 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 05:00:46 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:02:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:18 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:02:54 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 02:21:13 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-04 18:02:59 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:07:08 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:06:03 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:03:35 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:54 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:04:21 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:04:40 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:11 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:00:27 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:56 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:05:15 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:04:43 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:21 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:01:30 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:06:42 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:05:03 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 05:02:35 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-03-05 05:03:05 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.050 |  |
| 2026-03-05 05:11:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.055 |  |
| 2026-03-05 05:04:32 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.061 |  |
| 2026-03-05 05:01:49 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)