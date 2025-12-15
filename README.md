# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_15:14:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,687 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 15:14:18 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.008 |  |
| 2025-12-15 15:10:04 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-15 15:09:30 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:08:41 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.011 |  |
| 2025-12-15 15:08:13 | Horowpothana (Yan Oya) | 3.90 | 🟢 Normal | -0.027 |  |
| 2025-12-15 15:07:59 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-15 15:07:39 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:06:55 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 15:05:16 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.042 |  |
| 2025-12-15 15:05:03 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:04:21 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:04:16 | Weraganthota (Mahaweli Ganga) | -1.39 | 🟢 Normal | -0.068 |  |
| 2025-12-15 15:04:12 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:03:56 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.75 | 🟢 Normal | -0.062 |  |
| 2025-12-15 15:03:54 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:03:50 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:03:45 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:03:37 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | -0.143 |  |
| 2025-12-15 15:03:31 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:03:13 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:03:06 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.027 |  |
| 2025-12-15 15:03:05 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:03:03 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2025-12-15 15:02:45 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:02:28 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.050 |  |
| 2025-12-15 15:02:27 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:02:25 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:02:17 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:02:12 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-15 15:02:11 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:01:51 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:01:51 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:01:20 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:01:01 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:00:38 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:00:12 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:00:07 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-15 14:27:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 15:02:12 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-15 15:07:59 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-15 15:06:55 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 15:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:01:20 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:03:05 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:09:30 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:03:50 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:01:51 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:03:56 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:00:12 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:04:12 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:02:11 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:03:54 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:05:03 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:01:01 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:02:27 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:01:51 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 15:14:18 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.008 |  |
| 2025-12-15 15:10:04 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-15 15:03:31 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:04:21 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:02:17 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:02:25 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:00:07 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:07:39 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:03:45 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:00:38 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:03:13 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:02:45 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-15 15:08:41 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.011 |  |
| 2025-12-15 15:03:03 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2025-12-15 15:03:06 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.027 |  |
| 2025-12-15 15:08:13 | Horowpothana (Yan Oya) | 3.90 | 🟢 Normal | -0.027 |  |
| 2025-12-15 15:05:16 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.042 |  |
| 2025-12-15 15:02:28 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.050 |  |
| 2025-12-15 15:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.75 | 🟢 Normal | -0.062 |  |
| 2025-12-15 15:04:16 | Weraganthota (Mahaweli Ganga) | -1.39 | 🟢 Normal | -0.068 |  |
| 2025-12-15 15:03:37 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | -0.143 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)