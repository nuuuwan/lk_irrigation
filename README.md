# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_06:30:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,344 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 06:30:36 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | -0.002 |  |
| 2025-12-24 06:14:25 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.005 |  |
| 2025-12-24 06:13:53 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2025-12-24 06:11:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.095 |  |
| 2025-12-24 06:11:28 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:11:03 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:10:16 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-24 06:06:17 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.083 |  |
| 2025-12-24 06:06:15 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:06:01 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2025-12-24 06:05:19 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | -0.023 |  |
| 2025-12-24 06:05:14 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 06:04:56 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.396 |  |
| 2025-12-24 06:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.059 |  |
| 2025-12-24 06:04:25 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-24 06:04:24 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.015 |  |
| 2025-12-24 06:04:12 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2025-12-24 06:04:11 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2025-12-24 06:04:10 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2025-12-24 06:03:49 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 06:03:47 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:03:46 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-24 06:03:36 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:03:13 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:03:11 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:03:07 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:03:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 06:02:54 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-24 06:02:18 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:02:12 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 06:01:44 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:01:34 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.055 |  |
| 2025-12-24 06:01:32 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 06:01:31 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:01:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 06:01:30 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 06:01:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:00:33 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 06:00:27 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:00:13 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.051 |  |
| 2025-12-24 05:41:41 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 06:04:12 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2025-12-24 06:13:53 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2025-12-24 06:04:25 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-24 06:02:12 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 06:03:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 06:01:30 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 06:05:14 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 06:01:32 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 06:01:30 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 06:00:33 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 06:03:49 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-24 06:01:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:03:11 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:00:27 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:01:44 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:03:47 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:03:13 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:06:15 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:03:36 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:11:03 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:11:28 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:02:18 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:03:07 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:01:31 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:30:36 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | -0.002 |  |
| 2025-12-24 06:14:25 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.005 |  |
| 2025-12-24 06:06:01 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2025-12-24 06:02:54 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-24 06:10:16 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-24 06:03:46 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-24 06:04:24 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.015 |  |
| 2025-12-24 06:05:19 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | -0.023 |  |
| 2025-12-24 06:00:13 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.051 |  |
| 2025-12-24 06:01:34 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.055 |  |
| 2025-12-24 06:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | -0.059 |  |
| 2025-12-24 06:06:17 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.083 |  |
| 2025-12-24 06:11:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.095 |  |
| 2025-12-24 06:04:56 | Urawa (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.396 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)