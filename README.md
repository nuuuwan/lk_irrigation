# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_15:09:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,177 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 15:09:21 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-01-07 15:09:18 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-01-07 15:09:02 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-07 15:07:41 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:06:36 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 15:06:21 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-01-07 15:06:21 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-01-07 15:05:37 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:05:36 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 15:05:32 | Padiyathalawa (Maduru Oya) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-01-07 15:04:43 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-07 15:04:40 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-01-07 15:04:37 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:04:32 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:04:17 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-01-07 15:03:53 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:03:30 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:03:25 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-07 15:03:18 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-01-07 15:02:58 | Katharagama (Menik Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-07 15:02:55 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-07 15:02:50 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 15:02:06 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:01:58 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-01-07 15:01:57 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:01:36 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -4.696 |  |
| 2026-01-07 15:01:33 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-07 15:01:26 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:01:23 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.107 |  |
| 2026-01-07 15:01:18 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:01:16 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:01:13 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -4.696 |  |
| 2026-01-07 15:01:09 | Weraganthota (Mahaweli Ganga) | -1.13 | 🟢 Normal | -0.020 |  |
| 2026-01-07 15:00:47 | Horowpothana (Yan Oya) | 2.58 | 🟢 Normal | -0.031 |  |
| 2026-01-07 15:00:33 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:00:26 | Siyambalanduwa (Heda Oya) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-01-07 15:00:07 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-01-07 14:18:30 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-07 14:17:43 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 15:04:17 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-01-07 15:04:43 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-07 15:03:18 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-01-07 15:09:02 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-07 15:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 15:05:36 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 15:06:36 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 15:05:37 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:01:57 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:01:18 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:01:16 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:02:50 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:07:41 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:03:53 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:03:30 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:04:32 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:04:40 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:04:37 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:00:33 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 14:17:43 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:02:06 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-07 15:06:21 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-01-07 15:09:21 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-01-07 15:03:25 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-07 15:02:58 | Katharagama (Menik Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-07 15:01:33 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-07 15:02:55 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-07 15:04:40 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-01-07 15:05:32 | Padiyathalawa (Maduru Oya) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-01-07 15:01:09 | Weraganthota (Mahaweli Ganga) | -1.13 | 🟢 Normal | -0.020 |  |
| 2026-01-07 15:09:18 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-01-07 15:06:21 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.021 |  |
| 2026-01-07 15:00:07 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-01-07 15:01:58 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-01-07 15:00:26 | Siyambalanduwa (Heda Oya) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-01-07 15:00:47 | Horowpothana (Yan Oya) | 2.58 | 🟢 Normal | -0.031 |  |
| 2026-01-07 13:10:18 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.036 |  |
| 2026-01-07 15:01:23 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.107 |  |
| 2026-01-07 15:01:36 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -4.696 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)