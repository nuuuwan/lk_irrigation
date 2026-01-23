# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--23_14:15:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **53,520 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 14:15:33 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:10:40 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:10:00 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:07:40 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-01-23 14:07:34 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:07:24 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.139 |  |
| 2026-01-23 14:07:02 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 14:06:44 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-23 14:06:02 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:05:50 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:05:20 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:05:04 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-01-23 14:04:32 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-23 14:04:27 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 14:04:26 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.055 |  |
| 2026-01-23 14:04:10 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:04:03 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-23 14:03:36 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:03:27 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:03:23 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:03:07 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:02:51 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-23 14:02:35 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-23 14:02:30 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:02:29 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 14:02:22 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:02:13 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-01-23 14:02:04 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:02:00 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-23 14:01:52 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:01:33 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:01:33 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:01:02 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:01:00 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:00:34 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.028 |  |
| 2026-01-23 14:00:12 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.141 |  |
| 2026-01-23 13:39:09 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 14:05:04 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-01-23 14:02:00 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-23 14:04:32 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-23 14:06:44 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-01-23 14:02:35 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-23 14:02:51 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-23 14:04:03 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-23 14:02:29 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 14:04:27 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 14:07:02 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-23 14:02:22 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:01:33 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:03:27 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:15:33 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:01:52 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:05:50 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:03:07 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:05:20 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:01:00 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:10:40 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:07:34 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:10:00 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:04:10 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-23 12:08:52 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:01:33 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:02:04 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 14:07:40 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-01-23 14:03:23 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:06:02 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:03:36 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:02:30 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:01:02 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:02:13 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-23 14:00:34 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | -0.028 |  |
| 2026-01-23 14:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-01-23 14:04:26 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.055 |  |
| 2026-01-23 14:07:24 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.139 |  |
| 2026-01-23 14:00:12 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)