# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_06:29:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,553 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 06:29:01 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | -0.028 |  |
| 2025-12-22 06:20:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.092 |  |
| 2025-12-22 06:19:47 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:11:24 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.054 |  |
| 2025-12-22 06:10:45 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:07:19 | Horowpothana (Yan Oya) | 3.96 | 🟢 Normal | -0.066 |  |
| 2025-12-22 06:07:05 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-22 06:06:45 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:05:58 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:05:31 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | -0.029 |  |
| 2025-12-22 06:05:06 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:05:02 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-22 06:04:45 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-22 06:04:37 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-22 06:04:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.100 |  |
| 2025-12-22 06:04:10 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:03:56 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-22 06:03:47 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:03:45 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:03:31 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.051 |  |
| 2025-12-22 06:03:13 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-22 06:02:47 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.029 |  |
| 2025-12-22 06:02:46 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2025-12-22 06:02:39 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:02:33 | Weraganthota (Mahaweli Ganga) | -0.75 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-22 06:02:22 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:02:20 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.030 |  |
| 2025-12-22 06:02:11 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-22 06:01:59 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.015 |  |
| 2025-12-22 06:01:55 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:01:54 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2025-12-22 06:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:01:26 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.022 |  |
| 2025-12-22 06:01:21 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.021 |  |
| 2025-12-22 06:01:01 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.043 |  |
| 2025-12-22 06:00:59 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:00:26 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:00:22 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 06:03:13 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-22 06:05:02 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-22 06:02:33 | Weraganthota (Mahaweli Ganga) | -0.75 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-22 06:04:37 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-22 06:07:05 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-22 06:01:55 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:02:22 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:00:26 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:00:59 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:02:39 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:10:45 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:03:47 | Padiyathalawa (Maduru Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:05:06 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:06:45 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:05:58 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:04:10 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:19:47 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-22 06:03:56 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-22 06:02:11 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-22 06:04:45 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-22 06:00:22 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.013 |  |
| 2025-12-21 23:01:15 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.015 |  |
| 2025-12-22 06:01:59 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.015 |  |
| 2025-12-22 06:01:21 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.021 |  |
| 2025-12-22 06:01:26 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.022 |  |
| 2025-12-22 06:29:01 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | -0.028 |  |
| 2025-12-22 06:05:31 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | -0.029 |  |
| 2025-12-22 06:02:47 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.029 |  |
| 2025-12-22 06:02:20 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.030 |  |
| 2025-12-22 06:01:54 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2025-12-22 06:02:46 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2025-12-22 06:01:01 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.043 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-22 06:03:31 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.051 |  |
| 2025-12-22 06:11:24 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.054 |  |
| 2025-12-22 06:07:19 | Horowpothana (Yan Oya) | 3.96 | 🟢 Normal | -0.066 |  |
| 2025-12-22 06:20:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.092 |  |
| 2025-12-22 06:04:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)