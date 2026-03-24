# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_10:14:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,969 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 10:14:47 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:14:14 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.046 |  |
| 2026-03-24 10:09:30 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:09:16 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:07:17 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:06:19 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:05:51 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:05:24 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-24 10:05:11 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:05:06 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:05:05 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-03-24 10:04:57 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:04:29 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.011 |  |
| 2026-03-24 10:04:11 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:04:02 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.119 |  |
| 2026-03-24 10:03:48 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-03-24 10:03:37 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:03:26 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-24 10:03:22 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:58 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:52 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-03-24 10:02:40 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:36 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:32 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:29 | Kithulgala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.350 |  |
| 2026-03-24 10:02:24 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.054 |  |
| 2026-03-24 10:02:19 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:18 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:12 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-03-24 10:02:10 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.060 |  |
| 2026-03-24 10:01:41 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:01:37 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:01:24 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-24 10:01:23 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:01:11 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:01:02 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:00:56 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 10:02:12 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-03-24 10:05:24 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-24 10:01:24 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-24 10:03:26 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-24 10:02:10 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:32 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:01:11 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:01:23 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:05:11 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:03:37 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:09:30 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:05:51 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:58 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:36 | Baddegama (Gin Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:14:47 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:01:41 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:40 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:03:22 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:04:57 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:06:19 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:05:06 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:04:11 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:07:17 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:19 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:02:18 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:09:16 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:01:37 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:01:02 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 10:00:56 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-24 10:03:48 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-03-24 10:04:29 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.011 |  |
| 2026-03-24 10:05:05 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-03-24 10:02:52 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-03-24 10:14:14 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.046 |  |
| 2026-03-24 10:02:24 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.054 |  |
| 2026-03-24 10:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.060 |  |
| 2026-03-24 10:04:02 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.119 |  |
| 2026-03-24 10:02:29 | Kithulgala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.350 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)