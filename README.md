# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_02:26:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,953 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 02:26:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.015 |  |
| 2026-07-01 02:08:19 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.078 |  |
| 2026-07-01 02:08:16 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:06:28 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.005 |  |
| 2026-07-01 02:05:48 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:05:43 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.047 |  |
| 2026-07-01 02:05:20 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-01 02:04:41 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.019 |  |
| 2026-07-01 02:04:26 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | -90.000 |  |
| 2026-07-01 02:04:25 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-01 02:04:22 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | -90.000 |  |
| 2026-07-01 02:03:59 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 02:03:50 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-07-01 02:03:46 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:03:22 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:03:06 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-07-01 02:02:53 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-07-01 02:02:23 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-01 02:02:11 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.074 |  |
| 2026-07-01 02:02:11 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 02:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:01:39 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:01:26 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-01 02:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:01:21 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:00:26 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:46:00 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.074 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 02:03:06 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-07-01 01:06:42 | Putupaula (Kalu Ganga) | 1.74 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-01 02:02:23 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-01 02:05:20 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-01 02:04:25 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-01 02:03:59 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 02:02:11 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 02:03:22 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:05:48 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:00:26 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:00:52 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:08:51 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:03:46 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:00:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:03:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:01:39 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:11:35 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:04:34 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:02:00 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:08:16 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 02:01:21 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:21:35 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:12:20 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.005 |  |
| 2026-07-01 02:06:28 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.005 |  |
| 2026-07-01 01:04:13 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-07-01 02:03:50 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-07-01 02:02:53 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-06-30 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-01 02:01:26 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-01 02:26:13 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.015 |  |
| 2026-07-01 02:04:41 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.019 |  |
| 2026-07-01 01:09:06 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.038 |  |
| 2026-07-01 00:00:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.042 |  |
| 2026-07-01 02:05:43 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.047 |  |
| 2026-07-01 02:02:11 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.074 |  |
| 2026-07-01 02:08:19 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.078 |  |
| 2026-07-01 02:04:26 | Ellagawa (Kalu Ganga) | 6.80 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)