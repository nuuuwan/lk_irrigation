# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_19:14:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,515 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 19:14:37 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.475 | 🔺 Rising |
| 2026-03-01 19:12:38 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.008 |  |
| 2026-03-01 19:11:11 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:10:10 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:08:43 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:08:24 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:08:18 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:07:51 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:07:00 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:06:36 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.009 |  |
| 2026-03-01 19:06:20 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 19:06:12 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:05:17 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:05:05 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:04:57 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.123 |  |
| 2026-03-01 19:04:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:04:27 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:03:41 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.022 |  |
| 2026-03-01 19:03:38 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-03-01 19:03:35 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:03:21 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:03:20 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:03:16 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 19:02:44 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-03-01 19:02:44 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:02:37 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:02:18 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:02:18 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.065 |  |
| 2026-03-01 19:02:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:01:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-03-01 19:01:39 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:01:14 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:01:06 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:01:03 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 19:14:37 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.475 | 🔺 Rising |
| 2026-03-01 18:01:36 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-03-01 18:01:43 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-01 19:03:16 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 19:06:20 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 19:01:03 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:02:09 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:08:24 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:02:18 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:03:35 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 18:01:07 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:08:18 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:02:44 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:07:51 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:07:00 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:01:14 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:04:27 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:02:37 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:03:21 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:10:10 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:04:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:05:05 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:06:12 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:05:17 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:08:43 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:11:11 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:01:39 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:01:06 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-01 19:12:38 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.008 |  |
| 2026-03-01 19:06:36 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | -0.009 |  |
| 2026-03-01 19:02:44 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-03-01 19:01:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-03-01 18:00:31 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-03-01 18:01:23 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.013 |  |
| 2026-03-01 19:03:38 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-03-01 19:03:41 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.022 |  |
| 2026-03-01 19:02:18 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.065 |  |
| 2026-03-01 19:04:57 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)