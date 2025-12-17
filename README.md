# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_02:12:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,867 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 02:12:56 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:11:57 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.107 |  |
| 2025-12-18 02:09:53 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-18 02:09:52 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-18 02:09:52 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:09:51 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-18 02:09:49 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-18 02:08:52 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-18 02:08:14 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:08:13 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:08:11 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:08:10 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:04:53 | Yaka Wewa (Ma Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2025-12-18 02:04:07 | Thaldena (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2025-12-18 02:04:00 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:03:43 | Nakkala (Kumbukkan Oya) | 1.84 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2025-12-18 02:03:39 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.059 |  |
| 2025-12-18 02:03:38 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:03:34 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-18 02:03:24 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-18 02:02:42 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:02:35 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-18 02:02:20 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.061 |  |
| 2025-12-18 02:02:13 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.005 |  |
| 2025-12-18 02:02:07 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-18 02:02:07 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 02:01:41 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:01:33 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:01:10 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-18 02:01:06 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.013 |  |
| 2025-12-18 01:33:07 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:22:27 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 02:09:53 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-18 02:03:43 | Nakkala (Kumbukkan Oya) | 1.84 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2025-12-18 00:04:20 | Padiyathalawa (Maduru Oya) | 3.85 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2025-12-18 01:02:14 | Manampitiya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-18 02:01:10 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-18 02:03:24 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-18 02:08:52 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-18 02:02:07 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-18 02:02:07 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 01:03:36 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 01:33:07 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:01:33 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:08:14 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:03:38 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:06:14 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:09:52 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:01:57 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:02:42 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:01:20 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:12:56 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:04:00 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:02:52 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:01:41 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:02:13 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.005 |  |
| 2025-12-18 02:03:34 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-18 02:02:35 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2025-12-18 00:05:24 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-18 01:01:18 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-18 02:01:06 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.013 |  |
| 2025-12-18 01:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2025-12-18 02:04:53 | Yaka Wewa (Ma Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2025-12-18 01:02:34 | Horowpothana (Yan Oya) | 5.66 | 🟢 Normal | -0.020 |  |
| 2025-12-18 02:04:07 | Thaldena (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2025-12-18 02:03:39 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.059 |  |
| 2025-12-18 02:02:20 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.061 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-18 02:11:57 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)