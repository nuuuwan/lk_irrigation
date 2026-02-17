# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_04:44:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,069 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 04:44:29 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.006 |  |
| 2026-02-18 04:40:40 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:36:02 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:28:15 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-18 04:27:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:26:49 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.007 |  |
| 2026-02-18 04:13:58 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:13:25 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:13:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-18 04:12:01 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.042 |  |
| 2026-02-18 04:10:34 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:09:28 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:08:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-18 04:06:50 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:06:46 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:06:05 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:05:31 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:04:01 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.003 |  |
| 2026-02-18 04:03:49 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:03:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:03:36 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-18 04:03:32 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:03:24 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:03:10 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:03:06 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 04:03:03 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-18 04:02:40 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-18 04:02:27 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-02-18 04:02:16 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-18 04:01:49 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:01:46 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.012 |  |
| 2026-02-18 04:01:45 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:01:44 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:01:43 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:01:28 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:01:09 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.032 |  |
| 2026-02-18 04:01:04 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-02-18 04:00:50 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:00:36 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-18 03:57:58 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 04:03:03 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-02-18 04:00:36 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-17 18:03:50 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-02-18 04:13:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-18 04:02:16 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-18 04:28:15 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-18 04:03:06 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 04:08:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-18 04:02:40 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-18 04:01:43 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:10:34 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:00:50 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:36:02 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:01:44 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:40:40 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:04:27 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:06:46 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:13:25 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:03:24 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:27:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:06:05 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:13:58 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:03:49 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:06:50 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:03:32 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-17 18:02:27 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:01:45 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:05:31 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:01:49 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:09:28 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-18 04:04:01 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.003 |  |
| 2026-02-18 04:44:29 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.006 |  |
| 2026-02-18 04:26:49 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.007 |  |
| 2026-02-18 04:03:36 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-18 04:01:04 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-02-18 04:02:27 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-02-18 04:01:46 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.012 |  |
| 2026-02-18 04:01:09 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.032 |  |
| 2026-02-18 04:12:01 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.042 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)