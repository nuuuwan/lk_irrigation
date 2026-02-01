# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_13:41:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,574 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 13:41:22 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-01 13:22:16 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.034 |  |
| 2026-02-01 13:15:28 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 13:12:31 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 13:11:45 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:10:30 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 13:09:27 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:08:41 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-02-01 13:08:11 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:06:20 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 13:06:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-01 13:05:45 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.145 |  |
| 2026-02-01 13:05:39 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 13:05:34 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-02-01 13:04:22 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-02-01 13:03:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:03:19 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:03:03 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-02-01 13:03:01 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-02-01 13:03:00 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:02:51 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:02:51 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.010 |  |
| 2026-02-01 13:02:49 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-01 13:02:48 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-02-01 13:02:43 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:02:42 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:02:01 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.108 |  |
| 2026-02-01 13:01:54 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:01:48 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-02-01 13:01:43 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:01:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:01:36 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:01:31 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.150 |  |
| 2026-02-01 13:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.024 |  |
| 2026-02-01 13:01:13 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:00:55 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 13:00:44 | Thanthirimale (Malwathu Oya) | 2.07 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-02-01 13:00:39 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 13:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-01 12:59:05 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 13:02:49 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-01 13:06:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-01 13:15:28 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 13:00:44 | Thanthirimale (Malwathu Oya) | 2.07 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-02-01 13:41:22 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-01 13:00:55 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 13:00:39 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 13:06:20 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 13:05:39 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 13:12:31 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 13:10:30 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 13:01:42 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:01:36 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:02:43 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:01:43 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:09:27 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:02:42 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:03:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:01:54 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:11:45 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:03:00 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:03:19 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:08:11 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:01:13 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:02:51 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 13:08:41 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-02-01 13:02:51 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.010 |  |
| 2026-02-01 13:01:48 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-02-01 13:05:34 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-02-01 13:03:01 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-02-01 13:04:22 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-02-01 13:02:48 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-02-01 13:03:03 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-02-01 13:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.024 |  |
| 2026-02-01 13:22:16 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.034 |  |
| 2026-02-01 13:02:01 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.108 |  |
| 2026-02-01 13:05:45 | Thawalama (Gin Ganga) | 0.92 | 🟢 Normal | -0.145 |  |
| 2026-02-01 13:01:31 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)