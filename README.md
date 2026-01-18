# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--19_03:29:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **49,499 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 03:29:13 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:13:39 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:13:23 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:12:34 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:09:57 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-19 03:09:12 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:09:11 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:09:10 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:08:53 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-01-19 03:07:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-19 03:07:45 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-19 03:07:14 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:06:53 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:06:06 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-19 03:05:15 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:04:23 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-19 03:04:14 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:04:03 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 03:03:46 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-19 03:03:35 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:03:22 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:03:02 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.029 |  |
| 2026-01-19 03:02:59 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:02:46 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:02:18 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-19 03:02:17 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:02:11 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:02:10 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:02:05 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:02:02 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-19 03:01:51 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.010 |  |
| 2026-01-19 03:01:50 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:01:10 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.245 |  |
| 2026-01-19 03:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-19 02:38:08 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 03:04:23 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-19 03:07:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-01-19 02:04:13 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-19 03:07:45 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-19 03:02:18 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-19 03:09:57 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-19 03:03:46 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-19 03:04:03 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 03:06:06 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-19 03:02:17 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:02:59 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:02:10 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:02:11 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:29:13 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:05:15 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:03:22 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:05:15 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 02:03:10 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:13:23 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:09:12 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:13:39 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:01:50 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-19 01:16:36 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:02:05 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-19 02:32:29 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:07:14 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:06:53 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:03:35 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-18 18:01:56 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-19 02:17:04 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:04:14 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:02:46 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-19 03:08:53 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-01-19 03:01:51 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.010 |  |
| 2026-01-19 03:02:02 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-18 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.020 |  |
| 2026-01-19 03:03:02 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.029 |  |
| 2026-01-19 03:01:10 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.245 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)