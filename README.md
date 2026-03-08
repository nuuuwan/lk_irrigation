# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_00:15:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 00:15:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:14:40 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:13:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:12:18 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.009 |  |
| 2026-03-09 00:12:14 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:10:17 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:08:15 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:07:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:06:52 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:06:41 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 00:06:09 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.038 |  |
| 2026-03-09 00:05:39 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 00:05:20 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:05:17 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:05:17 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:04:12 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-03-09 00:03:56 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:03:40 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:03:38 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.051 |  |
| 2026-03-09 00:03:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:03:17 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:03:08 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.038 |  |
| 2026-03-09 00:02:46 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 00:02:44 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:02:39 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.010 |  |
| 2026-03-09 00:02:25 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:02:18 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:55 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:48 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-09 00:01:38 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:19 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:13 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:05 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:02 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:00:36 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:00:13 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 23:39:28 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:38:53 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 00:04:12 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-03-09 00:05:39 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 00:06:41 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 18:00:14 | Weraganthota (Mahaweli Ganga) | -1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 00:00:13 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 00:02:46 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 00:02:25 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:12:14 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:02:18 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:02 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:03:56 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:19 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:55 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:31:40 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:06:42 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:39:28 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:05:17 | Norwood (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:05:17 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:14:40 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:03:17 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:10:17 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:05 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:03:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:38 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:06:52 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:01:13 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:03:18 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:08:15 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-08 23:20:43 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:05:20 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:03:40 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:15:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-09 00:12:18 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.009 |  |
| 2026-03-09 00:02:39 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.010 |  |
| 2026-03-09 00:01:48 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-09 00:06:09 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.038 |  |
| 2026-03-09 00:03:08 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.038 |  |
| 2026-03-09 00:03:38 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)