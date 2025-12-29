# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_11:17:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,998 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 11:17:27 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.008 |  |
| 2025-12-29 11:16:41 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:16:26 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:14:45 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-29 11:13:25 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:09:06 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:08:44 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-29 11:07:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2025-12-29 11:06:21 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-29 11:05:57 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-29 11:05:20 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-29 11:05:15 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-29 11:05:10 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:04:14 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.048 |  |
| 2025-12-29 11:03:57 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:03:51 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:03:36 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 11:03:28 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:03:10 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:03:00 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-29 11:02:59 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 11:02:54 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:02:46 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:02:24 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 11:02:15 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:02:14 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 11:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:01:59 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-29 11:01:47 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:01:23 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-29 11:01:23 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:01:19 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:01:10 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.021 |  |
| 2025-12-29 11:01:08 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:00:39 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:00:35 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.010 |  |
| 2025-12-29 11:00:31 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:00:14 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 11:06:21 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-29 11:05:15 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-29 11:03:00 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-29 11:02:24 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 11:05:57 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-29 11:02:14 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 11:03:36 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 11:02:59 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 10:09:27 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 11:00:31 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:02:54 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:01:47 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:16:26 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:03:57 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:16:41 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:01:08 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:03:28 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:05:10 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 10:09:33 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:00:14 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:01:23 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:02:46 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:03:10 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:02:15 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:09:06 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:01:19 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:13:25 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:03:51 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 11:17:27 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.008 |  |
| 2025-12-29 11:14:45 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-29 11:05:20 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-29 11:08:44 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-29 11:01:59 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-29 11:01:23 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-29 11:00:35 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.010 |  |
| 2025-12-29 11:01:10 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | -0.021 |  |
| 2025-12-29 11:04:14 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.048 |  |
| 2025-12-29 11:07:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.057 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)