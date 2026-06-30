# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_01:46:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,926 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 01:46:00 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.012 |  |
| 2026-07-01 01:21:35 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:11:35 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:09:27 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:09:06 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.038 |  |
| 2026-07-01 01:07:43 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.019 |  |
| 2026-07-01 01:07:18 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-07-01 01:06:57 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.059 |  |
| 2026-07-01 01:06:51 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:06:42 | Putupaula (Kalu Ganga) | 1.74 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-01 01:04:34 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:04:13 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-07-01 01:04:08 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 01:01:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-07-01 01:02:28 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-07-01 01:06:42 | Putupaula (Kalu Ganga) | 1.74 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-01 01:04:08 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-01 01:03:58 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 01:00:49 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 01:00:54 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:01:55 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 23:00:52 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:08:51 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-01 00:02:15 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:03:37 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:00:16 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:03:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:06:51 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:02:03 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:11:35 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:04:34 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-30 18:02:00 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:09:27 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-01 00:03:23 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-01 01:21:35 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-30 21:12:20 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.005 |  |
| 2026-07-01 01:04:13 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-07-01 01:03:47 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-30 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-01 01:02:45 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-07-01 01:46:00 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.012 |  |
| 2026-07-01 01:07:43 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | -0.019 |  |
| 2026-07-01 01:07:18 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-07-01 01:02:12 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.021 |  |
| 2026-07-01 01:04:03 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-07-01 01:09:06 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.038 |  |
| 2026-07-01 00:00:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.042 |  |
| 2026-07-01 00:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.045 |  |
| 2026-07-01 01:06:57 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.059 |  |
| 2026-07-01 00:03:18 | Ellagawa (Kalu Ganga) | 7.01 | 🟢 Normal | -0.096 |  |
| 2026-07-01 01:03:45 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)