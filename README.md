# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_04:29:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,542 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 04:29:01 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.145 |  |
| 2026-06-26 04:18:16 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.016 |  |
| 2026-06-26 04:17:30 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:11:03 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:08:35 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-06-26 04:06:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-06-26 04:05:39 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-26 04:05:27 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:04:24 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.032 |  |
| 2026-06-26 04:04:18 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-26 04:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:03:31 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 72.727 | 🔺 Rising |
| 2026-06-26 04:03:15 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-26 04:03:01 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-06-26 04:02:54 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:02:37 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-26 04:02:31 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-06-26 04:02:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:02:23 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:02:19 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:02:17 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:01:52 | Ellagawa (Kalu Ganga) | 3.20 | 🟢 Normal | 72.727 | 🔺 Rising |
| 2026-06-26 04:01:49 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 04:01:27 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:01:12 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-26 04:00:40 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-26 04:00:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:00:15 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.082 |  |
| 2026-06-26 03:45:58 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.004 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 04:03:31 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 72.727 | 🔺 Rising |
| 2026-06-26 03:05:04 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-26 04:00:40 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-26 04:05:39 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-26 04:01:49 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 04:02:23 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:01:27 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:02:26 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:02:17 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:14:51 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:05:27 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:02:19 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:18:16 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:00:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:02:54 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:11:03 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:17:30 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:02:01 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:21 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:45:58 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.004 |  |
| 2026-06-26 04:04:18 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-26 04:03:15 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-26 04:02:37 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:02:25 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-26 04:01:12 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-26 02:05:47 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-06-26 04:03:01 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-06-26 04:18:16 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.016 |  |
| 2026-06-26 04:08:35 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-06-26 03:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.026 |  |
| 2026-06-26 04:02:31 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-06-26 04:06:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-06-26 04:04:24 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.032 |  |
| 2026-06-26 03:02:50 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.040 |  |
| 2026-06-26 04:00:15 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.082 |  |
| 2026-06-26 04:29:01 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.145 |  |
| 2026-06-26 03:06:27 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.563 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)