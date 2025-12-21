# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_15:16:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,031 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 15:16:26 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:13:42 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-21 15:07:59 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | -0.080 |  |
| 2025-12-21 15:07:53 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2025-12-21 15:07:39 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.047 |  |
| 2025-12-21 15:07:05 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:06:59 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.009 |  |
| 2025-12-21 15:06:53 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.041 |  |
| 2025-12-21 15:05:44 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2025-12-21 15:05:37 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:05:34 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 15:05:09 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:05:04 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:04:56 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:04:47 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:04:05 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:03:24 | Horowpothana (Yan Oya) | 4.83 | 🟢 Normal | -0.039 |  |
| 2025-12-21 15:02:54 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 15:02:54 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:02:44 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-21 15:02:41 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:02:41 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-21 15:02:37 | Weraganthota (Mahaweli Ganga) | -0.68 | 🟢 Normal | -0.597 |  |
| 2025-12-21 15:02:30 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:02:27 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-21 15:02:24 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2025-12-21 15:02:21 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:02:20 | Manampitiya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.029 |  |
| 2025-12-21 15:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | -0.100 |  |
| 2025-12-21 15:02:11 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-21 15:02:10 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.022 |  |
| 2025-12-21 15:01:49 | Thanthirimale (Malwathu Oya) | 5.05 | 🟡 Alert | -0.037 |  |
| 2025-12-21 15:01:39 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:01:32 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2025-12-21 15:01:23 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-21 15:01:08 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:01:05 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:00:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-21 14:22:58 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.041 |  |
| 2025-12-21 14:21:17 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 15:01:49 | Thanthirimale (Malwathu Oya) | 5.05 | 🟡 Alert | -0.037 |  |
| 2025-12-21 15:02:11 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-21 15:01:23 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-21 15:00:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-21 15:02:41 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-21 15:02:54 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 15:05:34 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 15:01:08 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:04:05 | Moragaswewa (Deduru Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:02:21 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:05:09 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:01:39 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:02:54 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:07:05 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:04:47 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:01:05 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:05:04 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:02:41 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:05:37 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:16:26 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:04:56 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:02:30 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 15:01:32 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2025-12-21 15:06:59 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.009 |  |
| 2025-12-21 15:02:27 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-21 15:13:42 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-21 15:05:44 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2025-12-21 15:07:53 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2025-12-21 15:02:24 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2025-12-21 15:02:44 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-21 15:02:10 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.022 |  |
| 2025-12-21 15:02:20 | Manampitiya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.029 |  |
| 2025-12-21 15:03:24 | Horowpothana (Yan Oya) | 4.83 | 🟢 Normal | -0.039 |  |
| 2025-12-21 15:06:53 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.041 |  |
| 2025-12-21 15:07:39 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.047 |  |
| 2025-12-21 15:07:59 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | -0.080 |  |
| 2025-12-21 15:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | -0.100 |  |
| 2025-12-21 15:02:37 | Weraganthota (Mahaweli Ganga) | -0.68 | 🟢 Normal | -0.597 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)