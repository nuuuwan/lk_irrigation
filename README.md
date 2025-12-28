# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_14:08:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,218 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 14:08:14 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:08:08 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-28 14:07:46 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:07:07 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.009 |  |
| 2025-12-28 14:05:54 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.065 |  |
| 2025-12-28 14:05:32 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-28 14:05:32 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:05:29 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-28 14:05:26 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:05:14 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:04:57 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-28 14:04:51 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:04:27 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-28 14:03:50 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:03:21 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.019 |  |
| 2025-12-28 14:03:20 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2025-12-28 14:03:11 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-28 14:02:44 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:02:41 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:02:39 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:02:36 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:02:25 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.029 |  |
| 2025-12-28 14:02:20 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-28 14:02:13 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-28 14:02:03 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-28 14:01:57 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:01:53 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:01:32 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:01:17 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:01:02 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-28 14:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:00:50 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 14:00:16 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2025-12-28 13:20:04 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 14:02:03 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-28 14:02:20 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-28 14:05:32 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-28 14:08:08 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-28 14:04:27 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-28 14:05:29 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-28 14:00:50 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 13:10:03 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-28 14:04:51 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:02:41 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:01:57 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:03:50 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:05:26 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:05:59 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:05:14 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:02:44 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:10:43 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2025-12-28 13:04:36 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:01:53 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:01:32 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:05:32 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:02:39 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:08:14 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:01:17 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:07:46 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:02:36 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 14:07:07 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.009 |  |
| 2025-12-28 12:05:05 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2025-12-28 14:04:57 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-28 14:01:02 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-28 14:02:13 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-28 14:03:11 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-28 14:00:16 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2025-12-28 14:03:21 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.019 |  |
| 2025-12-28 14:03:20 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2025-12-28 14:02:25 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.029 |  |
| 2025-12-28 14:05:54 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)