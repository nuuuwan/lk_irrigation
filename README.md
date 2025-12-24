# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_12:11:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,582 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 12:11:53 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:11:10 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:08:42 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:08:36 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:07:18 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.088 |  |
| 2025-12-24 12:07:05 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:06:34 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:06:23 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:06:05 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:05:04 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-24 12:04:59 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:04:57 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:04:44 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:04:42 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 12:04:37 | Weraganthota (Mahaweli Ganga) | -1.34 | 🟢 Normal | -0.156 |  |
| 2025-12-24 12:04:33 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:04:22 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.010 |  |
| 2025-12-24 12:04:20 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:03:57 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:03:52 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:03:47 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:03:43 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:03:31 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-24 12:03:16 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2025-12-24 12:03:13 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-24 12:03:00 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:02:36 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.099 |  |
| 2025-12-24 12:02:22 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.041 |  |
| 2025-12-24 12:01:56 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 12:01:54 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:01:52 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.143 |  |
| 2025-12-24 12:01:49 | Thanthirimale (Malwathu Oya) | 2.35 | 🟢 Normal | -0.040 |  |
| 2025-12-24 12:01:24 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-24 12:01:12 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-24 12:01:07 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:01:03 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-24 12:01:02 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:00:21 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-24 12:00:05 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:15:26 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 12:01:03 | Yaka Wewa (Ma Oya) | 0.96 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-24 12:01:24 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-24 12:00:21 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-24 12:01:56 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 12:04:42 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 12:07:05 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:01:54 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:01:07 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-24 11:09:36 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:03:57 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:04:20 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:04:44 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:08:42 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:03:00 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:11:53 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:01:02 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:11:10 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:03:47 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:00:05 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:03:52 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:04:33 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:03:43 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:06:05 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:06:23 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:08:36 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:02:22 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:04:57 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-24 12:03:31 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2025-12-24 12:03:13 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-24 12:04:22 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.010 |  |
| 2025-12-24 12:05:04 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-24 12:01:12 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-24 12:03:16 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2025-12-24 12:01:49 | Thanthirimale (Malwathu Oya) | 2.35 | 🟢 Normal | -0.040 |  |
| 2025-12-24 12:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.041 |  |
| 2025-12-24 12:07:18 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.088 |  |
| 2025-12-24 12:02:36 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.099 |  |
| 2025-12-24 12:01:52 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.143 |  |
| 2025-12-24 12:04:37 | Weraganthota (Mahaweli Ganga) | -1.34 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)