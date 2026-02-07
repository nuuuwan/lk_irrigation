# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--08_03:18:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,112 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 03:18:52 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.008 |  |
| 2026-02-08 03:16:12 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:14:55 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:14:41 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:12:41 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-02-08 03:11:57 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-02-08 03:11:38 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:11:18 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:11:10 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.227 |  |
| 2026-02-08 03:10:41 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:08:48 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-08 03:08:04 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.005 |  |
| 2026-02-08 03:07:44 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:07:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-02-08 03:06:40 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:06:09 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:06:01 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-02-08 03:05:59 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-08 03:05:08 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.040 |  |
| 2026-02-08 03:04:47 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:03:38 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-08 03:03:02 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:02:53 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:02:46 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:02:32 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:02:11 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:01:40 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-08 03:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-02-08 03:01:20 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-02-08 03:00:57 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:00:38 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-02-08 03:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:58:58 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:56:06 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:52:32 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.024 |  |
| 2026-02-08 02:46:26 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:38:21 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.092 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-08 03:07:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-02-08 03:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-02-08 03:08:48 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-08 02:38:21 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-08 03:00:38 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-02-08 03:01:40 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-08 03:05:59 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-08 03:10:41 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:04:47 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:00:57 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 00:01:38 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:02:46 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:16:12 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:07:44 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:06:09 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:14:41 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:03:02 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:58:58 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:02:23 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:02:53 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:11:38 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:02:32 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:06:40 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-08 02:02:00 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 03:08:04 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.005 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-08 03:18:52 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.008 |  |
| 2026-02-08 03:12:41 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-02-08 03:11:57 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-02-08 03:06:01 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-02-08 03:03:38 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-08 02:11:27 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.018 |  |
| 2026-02-08 03:01:20 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-02-07 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.020 |  |
| 2026-02-08 02:52:32 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.024 |  |
| 2026-02-08 03:05:08 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.040 |  |
| 2026-02-08 03:11:10 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.227 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)