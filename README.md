# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_14:22:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,875 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 14:22:19 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:18:30 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:18:09 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2025-12-22 14:11:04 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:10:36 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:09:24 | Galgamuwa (Mee Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:08:58 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-22 14:06:09 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:05:56 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:05:34 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:04:59 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:04:54 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.114 |  |
| 2025-12-22 14:04:01 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:04:01 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2025-12-22 14:03:49 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-22 14:03:47 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:03:37 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:03:26 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:03:24 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:03:23 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:03:22 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:03:18 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:02:38 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:02:33 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:02:32 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:02:28 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:02:20 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:02:13 | Weraganthota (Mahaweli Ganga) | -1.24 | 🟢 Normal | -0.142 |  |
| 2025-12-22 14:02:07 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:01:53 | Thanthirimale (Malwathu Oya) | 4.52 | 🟢 Normal | -0.079 |  |
| 2025-12-22 14:01:51 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 14:01:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:01:20 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:01:13 | Manampitiya (Mahaweli Ganga) | 2.44 | 🟢 Normal | -0.060 |  |
| 2025-12-22 14:01:02 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:01:01 | Horowpothana (Yan Oya) | 3.44 | 🟢 Normal | -0.044 |  |
| 2025-12-22 14:00:55 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:00:40 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 14:03:49 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-22 14:08:58 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-22 14:01:51 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 14:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 14:02:33 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:01:20 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:05:56 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:02:38 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:09:24 | Galgamuwa (Mee Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:02:28 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:03:47 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:02:07 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:03:24 | Glencourse (Kelani Ganga) | 8.88 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:01:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:01:02 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:04:59 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:00:40 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:03:37 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:11:04 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:04:01 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:18:30 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:22:19 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:02:20 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:05:34 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-22 14:03:26 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:10:36 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:03:23 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:00:55 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:02:32 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:06:09 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:03:18 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2025-12-22 14:18:09 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2025-12-22 14:04:01 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2025-12-22 14:01:01 | Horowpothana (Yan Oya) | 3.44 | 🟢 Normal | -0.044 |  |
| 2025-12-22 14:01:13 | Manampitiya (Mahaweli Ganga) | 2.44 | 🟢 Normal | -0.060 |  |
| 2025-12-22 14:01:53 | Thanthirimale (Malwathu Oya) | 4.52 | 🟢 Normal | -0.079 |  |
| 2025-12-22 14:04:54 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.114 |  |
| 2025-12-22 14:02:13 | Weraganthota (Mahaweli Ganga) | -1.24 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)