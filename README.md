# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_04:14:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,734 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 04:14:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-24 04:13:28 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-24 04:11:44 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | -0.028 |  |
| 2026-03-24 04:08:25 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-03-24 04:07:36 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.170 |  |
| 2026-03-24 04:06:22 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-03-24 04:06:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-24 04:05:42 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-03-24 04:05:04 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.031 |  |
| 2026-03-24 04:04:44 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:04:29 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:04:21 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-24 04:03:52 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:03:24 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-24 04:03:15 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:03:07 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-24 04:03:03 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:02:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:02:47 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:02:31 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:02:31 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.112 |  |
| 2026-03-24 04:02:20 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:02:11 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:01:55 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:01:50 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:01:31 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:01:25 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.040 |  |
| 2026-03-24 04:01:19 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-03-24 04:00:49 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-24 04:00:49 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:00:49 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:00:48 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.003 |  |
| 2026-03-24 03:46:40 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 03:19:52 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-24 04:03:07 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-24 04:14:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-24 04:06:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-24 03:04:21 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-24 03:04:59 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 04:00:49 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:02:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:00:49 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:03:52 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:02:11 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:01:55 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:00:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 02:01:38 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:03:15 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:04:44 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:01:31 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:01:50 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:02:31 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:02:47 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-24 03:28:00 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:03:03 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:02:20 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-24 04:00:48 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.003 |  |
| 2026-03-24 04:13:28 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-03-24 04:03:24 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:02:17 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-03-24 04:04:21 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-03-24 04:00:49 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-24 04:08:25 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2026-03-24 04:06:22 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-03-24 04:05:42 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-03-24 04:01:19 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-03-24 04:11:44 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | -0.028 |  |
| 2026-03-24 04:05:04 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.031 |  |
| 2026-03-24 04:01:25 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | -0.040 |  |
| 2026-03-23 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.101 |  |
| 2026-03-24 04:02:31 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.112 |  |
| 2026-03-24 04:07:36 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)