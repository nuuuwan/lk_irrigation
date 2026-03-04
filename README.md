# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--05_03:25:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,480 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 03:25:08 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-03-05 03:24:46 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-03-05 03:14:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-05 03:12:51 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -1.424 |  |
| 2026-03-05 03:09:46 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:07:49 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:05:58 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:05:48 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 03:05:40 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 03:05:36 | Glencourse (Kelani Ganga) | 8.18 | 🟢 Normal | -0.010 |  |
| 2026-03-05 03:05:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-05 03:04:53 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 03:04:14 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-05 03:04:05 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.167 |  |
| 2026-03-05 03:04:00 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -1.424 |  |
| 2026-03-05 03:03:55 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-05 03:03:47 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-03-05 03:03:45 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 03:02:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:02:11 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:02:09 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-05 03:02:01 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:54 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:51 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:50 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-05 03:01:47 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.006 |  |
| 2026-03-05 03:01:45 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:29 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-05 03:01:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:15 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:03 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:00:44 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 03:00:21 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-03-05 02:41:35 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 02:37:49 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 03:25:08 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-03-05 02:06:34 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-03-05 03:01:29 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-04 18:01:40 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-05 03:05:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-05 03:14:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-05 03:01:50 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-05 03:02:09 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-05 03:04:14 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-05 03:03:55 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-05 03:03:45 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 03:05:48 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 03:00:44 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 03:05:40 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-04 18:01:42 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 03:04:53 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 03:01:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:02:11 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 02:21:13 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-04 18:02:59 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-05 01:40:48 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:05:58 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:03 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:07:49 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:54 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:51 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:45 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:02:57 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:15 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:09:46 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 02:05:49 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:02:01 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-05 03:01:47 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.006 |  |
| 2026-03-05 03:03:47 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-03-05 01:02:16 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-05 03:05:36 | Glencourse (Kelani Ganga) | 8.18 | 🟢 Normal | -0.010 |  |
| 2026-03-05 03:00:21 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-03-05 03:04:05 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.167 |  |
| 2026-03-05 03:12:51 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -1.424 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)