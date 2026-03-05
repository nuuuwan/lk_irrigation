# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--05_11:17:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **89,786 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 11:17:50 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:17:11 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-03-05 11:16:35 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.016 |  |
| 2026-03-05 11:12:04 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:10:49 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:07:37 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-03-05 11:07:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:07:24 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:05:52 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-05 11:05:42 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:05:19 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 11:05:12 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-03-05 11:04:43 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:04:38 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-03-05 11:04:37 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:04:08 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:03:58 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.098 |  |
| 2026-03-05 11:03:49 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | -0.010 |  |
| 2026-03-05 11:03:48 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:03:36 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:03:24 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-03-05 11:03:24 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-05 11:03:04 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-05 11:02:59 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-05 11:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-03-05 11:02:36 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-05 11:01:55 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:01:44 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.080 |  |
| 2026-03-05 11:01:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-05 11:01:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:01:19 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-03-05 11:01:19 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:01:17 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:00:49 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:00:49 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:00:35 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-05 11:01:19 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-03-05 11:02:59 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-05 11:03:24 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-05 11:02:36 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-05 11:05:52 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-05 11:05:19 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-05 11:00:49 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:01:55 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:01:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:01:17 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:01:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:17:50 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-05 10:00:25 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:04:08 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:05:42 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:03:36 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:10:49 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:12:04 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:04:37 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:00:35 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:07:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:04:43 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:03:48 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:01:19 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:07:24 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:00:49 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-05 10:04:56 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-05 11:17:11 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-03-05 11:05:12 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-03-05 11:03:04 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-05 11:03:24 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-03-05 11:03:49 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | -0.010 |  |
| 2026-03-05 11:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-05 11:16:35 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.016 |  |
| 2026-03-05 11:07:37 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-03-05 11:04:38 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-03-05 11:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-03-05 11:01:44 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.080 |  |
| 2026-03-05 11:03:58 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)