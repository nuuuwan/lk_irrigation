# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_10:17:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,207 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 10:17:14 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.042 |  |
| 2025-12-09 10:11:43 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-09 10:10:57 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:10:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.084 |  |
| 2025-12-09 10:08:40 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-09 10:08:15 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2025-12-09 10:07:33 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.024 |  |
| 2025-12-09 10:07:30 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:06:59 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-09 10:06:58 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-09 10:06:57 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-09 10:06:39 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.085 |  |
| 2025-12-09 10:06:28 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2025-12-09 10:06:24 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.030 |  |
| 2025-12-09 10:05:35 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.010 |  |
| 2025-12-09 10:05:11 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:05:02 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 10:04:55 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 10:04:38 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:04:19 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.010 |  |
| 2025-12-09 10:03:49 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:03:43 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:03:42 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.081 |  |
| 2025-12-09 10:03:40 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:03:30 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:03:15 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:03:13 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2025-12-09 10:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-09 10:02:48 | Yaka Wewa (Ma Oya) | 1.22 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2025-12-09 10:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.015 |  |
| 2025-12-09 10:02:29 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:02:23 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:02:21 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:02:19 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:01:38 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2025-12-09 10:01:14 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-09 10:01:02 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2025-12-09 10:00:54 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.142 |  |
| 2025-12-09 10:00:44 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 09:27:12 | Thanthirimale (Malwathu Oya) | 3.46 | 🟢 Normal | -0.142 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 10:06:59 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2025-12-09 09:05:53 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2025-12-09 10:02:48 | Yaka Wewa (Ma Oya) | 1.22 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2025-12-09 10:03:13 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2025-12-09 10:01:02 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2025-12-09 10:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-09 10:08:40 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-09 10:05:02 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 10:04:55 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 10:06:58 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-09 10:11:43 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-09 10:01:14 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-09 10:02:23 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:03:30 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:04:38 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:03:43 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:02:29 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:00:44 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:05:11 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:03:40 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:02:19 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:03:49 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:10:57 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:02:21 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:07:30 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 10:08:15 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2025-12-09 10:04:19 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.010 |  |
| 2025-12-09 10:05:35 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.010 |  |
| 2025-12-09 10:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.015 |  |
| 2025-12-09 10:06:28 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2025-12-09 10:01:38 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2025-12-09 10:07:33 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.024 |  |
| 2025-12-09 10:06:24 | Baddegama (Gin Ganga) | 2.02 | 🟢 Normal | -0.030 |  |
| 2025-12-09 10:17:14 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.042 |  |
| 2025-12-09 10:03:42 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.081 |  |
| 2025-12-09 10:10:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.084 |  |
| 2025-12-09 10:06:39 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.085 |  |
| 2025-12-09 10:00:54 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)