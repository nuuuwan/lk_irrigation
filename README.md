# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_11:15:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,542 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 11:15:26 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2025-12-24 11:12:50 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:11:13 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:09:36 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:08:57 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 11:08:31 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.009 |  |
| 2025-12-24 11:08:03 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 11:07:48 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:06:08 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2025-12-24 11:05:57 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:05:55 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-24 11:05:37 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.019 |  |
| 2025-12-24 11:05:23 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:04:53 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.010 |  |
| 2025-12-24 11:04:44 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:04:21 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:03:49 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:03:35 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 11:03:33 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-24 11:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.043 |  |
| 2025-12-24 11:03:14 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:03:13 | Weraganthota (Mahaweli Ganga) | -1.18 | 🟢 Normal | -0.175 |  |
| 2025-12-24 11:03:12 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.136 |  |
| 2025-12-24 11:03:01 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:02:56 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-24 11:02:48 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.071 |  |
| 2025-12-24 11:02:47 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-24 11:02:25 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.074 |  |
| 2025-12-24 11:02:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-24 11:02:13 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2025-12-24 11:02:09 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:01:55 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 11:01:54 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:01:54 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-24 11:01:44 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.137 |  |
| 2025-12-24 11:01:36 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:01:29 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:01:09 | Thanthirimale (Malwathu Oya) | 2.39 | 🟢 Normal | -0.050 |  |
| 2025-12-24 11:00:38 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 10:38:20 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2025-12-24 10:34:35 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 11:06:08 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2025-12-24 11:01:54 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-24 11:03:35 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 11:01:55 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 11:08:03 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 11:02:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-24 11:08:57 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 11:01:29 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:03:49 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:01:36 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:09:36 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:11:13 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:01:54 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:03:01 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:05:23 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:03:14 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:04:21 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:00:38 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:04:44 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:05:57 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:12:50 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:02:09 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:15:26 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2025-12-24 11:08:31 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.009 |  |
| 2025-12-24 11:05:55 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-24 11:04:53 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.010 |  |
| 2025-12-24 11:02:56 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-24 11:03:33 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-24 11:02:47 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-24 11:05:37 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.019 |  |
| 2025-12-24 11:02:13 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2025-12-24 10:14:00 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2025-12-24 11:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.043 |  |
| 2025-12-24 11:01:09 | Thanthirimale (Malwathu Oya) | 2.39 | 🟢 Normal | -0.050 |  |
| 2025-12-24 11:02:48 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.071 |  |
| 2025-12-24 11:02:25 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.074 |  |
| 2025-12-24 11:03:12 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | -0.136 |  |
| 2025-12-24 11:01:44 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.137 |  |
| 2025-12-24 11:03:13 | Weraganthota (Mahaweli Ganga) | -1.18 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)