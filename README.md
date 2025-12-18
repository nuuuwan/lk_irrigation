# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_07:14:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,066 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 07:14:44 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-18 07:13:18 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:12:36 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:11:47 | Manampitiya (Mahaweli Ganga) | 3.33 | 🟡 Alert | 0.136 | 🔺 Rising |
| 2025-12-18 07:11:20 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 07:10:32 | Padiyathalawa (Maduru Oya) | 3.45 | 🟢 Normal | 0.487 | 🔺 Rising |
| 2025-12-18 07:09:35 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:09:30 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:07:18 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:06:41 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.031 |  |
| 2025-12-18 07:06:11 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2025-12-18 07:06:07 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:05:59 | Yaka Wewa (Ma Oya) | 1.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 07:05:50 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 07:05:31 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:04:53 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:04:02 | Thaldena (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-18 07:04:01 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:03:55 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 07:03:50 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2025-12-18 07:03:45 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2025-12-18 07:03:34 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2025-12-18 07:02:48 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:02:42 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.128 |  |
| 2025-12-18 07:02:26 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-18 07:02:17 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 07:02:08 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:02:01 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 07:01:48 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2025-12-18 07:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:01:15 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | -0.011 |  |
| 2025-12-18 07:00:42 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.040 |  |
| 2025-12-18 07:00:17 | Nakkala (Kumbukkan Oya) | 2.74 | 🟢 Normal | 0.579 | 🔺 Rising |
| 2025-12-18 07:00:10 | Horowpothana (Yan Oya) | 5.59 | 🟢 Normal | -0.031 |  |
| 2025-12-18 07:00:08 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:34:07 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 07:11:47 | Manampitiya (Mahaweli Ganga) | 3.33 | 🟡 Alert | 0.136 | 🔺 Rising |
| 2025-12-18 07:00:17 | Nakkala (Kumbukkan Oya) | 2.74 | 🟢 Normal | 0.579 | 🔺 Rising |
| 2025-12-18 07:10:32 | Padiyathalawa (Maduru Oya) | 3.45 | 🟢 Normal | 0.487 | 🔺 Rising |
| 2025-12-18 07:03:50 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2025-12-18 07:04:02 | Thaldena (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-18 07:05:59 | Yaka Wewa (Ma Oya) | 1.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 07:02:26 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-18 07:02:01 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 07:03:55 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 07:02:17 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 07:05:50 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 07:11:20 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 07:14:44 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-18 07:09:30 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:06:07 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:13:18 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:12:36 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:05:31 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:09:43 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:18:13 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:02:48 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:04:53 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:02:08 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:04:01 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:07:18 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:04:05 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:00:08 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-18 07:01:48 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2025-12-18 07:01:15 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | -0.011 |  |
| 2025-12-18 07:06:11 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2025-12-18 07:03:45 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2025-12-18 07:06:41 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.031 |  |
| 2025-12-18 07:00:10 | Horowpothana (Yan Oya) | 5.59 | 🟢 Normal | -0.031 |  |
| 2025-12-18 07:00:42 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.040 |  |
| 2025-12-18 07:03:34 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-18 07:02:42 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)