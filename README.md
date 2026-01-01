# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_15:15:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,808 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 15:15:12 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:13:37 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-01 15:11:41 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:09:19 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:07:42 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-01-01 15:07:36 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:06:52 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-01-01 15:06:02 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:05:35 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-01-01 15:05:30 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 15:05:17 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | -0.019 |  |
| 2026-01-01 15:05:09 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-01 15:04:45 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:04:28 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:04:13 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-01-01 15:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-01-01 15:03:50 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-01-01 15:03:49 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:03:47 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:03:10 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:02:57 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:02:51 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-01-01 15:02:49 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:02:47 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:02:38 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:02:36 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:02:31 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:02:24 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 15:02:23 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:02:18 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.060 |  |
| 2026-01-01 15:02:06 | Horowpothana (Yan Oya) | 3.36 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-01 15:01:59 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-01-01 15:01:57 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.054 |  |
| 2026-01-01 15:01:57 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.060 |  |
| 2026-01-01 15:01:23 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 15:01:13 | Weraganthota (Mahaweli Ganga) | -1.71 | 🟢 Normal | -0.060 |  |
| 2026-01-01 15:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:00:59 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-01-01 15:00:42 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | -0.060 |  |
| 2026-01-01 15:00:24 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 15:04:13 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.253 | 🔺 Rising |
| 2026-01-01 15:02:06 | Horowpothana (Yan Oya) | 3.36 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-01 15:13:37 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-01 15:05:09 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-01 15:01:23 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 15:02:24 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-01 15:05:30 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 14:12:27 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 15:04:28 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:04:45 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:02:38 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:02:31 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:02:36 | Baddegama (Gin Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:09:19 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:03:47 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:11:41 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:02:49 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:15:12 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-01 15:06:52 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-01-01 15:06:02 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:03:49 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:02:23 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:02:57 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:03:10 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-01-01 15:03:50 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-01-01 15:02:51 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-01-01 15:00:24 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | -0.013 |  |
| 2026-01-01 15:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-01-01 15:05:17 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | -0.019 |  |
| 2026-01-01 15:05:35 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-01-01 15:00:59 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-01-01 15:01:59 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-01-01 15:01:57 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.054 |  |
| 2026-01-01 15:01:13 | Weraganthota (Mahaweli Ganga) | -1.71 | 🟢 Normal | -0.060 |  |
| 2026-01-01 15:00:42 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | -0.060 |  |
| 2026-01-01 15:02:18 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.060 |  |
| 2026-01-01 15:01:57 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.060 |  |
| 2026-01-01 15:07:42 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)