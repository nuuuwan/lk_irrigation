# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_17:22:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,940 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 17:22:13 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.026 |  |
| 2025-12-13 17:12:36 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.017 |  |
| 2025-12-13 17:11:59 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:11:59 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.037 |  |
| 2025-12-13 17:11:55 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.009 |  |
| 2025-12-13 17:11:53 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:11:22 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-13 17:10:13 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-13 17:10:12 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:10:05 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-13 17:09:35 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:06:44 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2025-12-13 17:06:25 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.019 |  |
| 2025-12-13 17:05:59 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-13 17:05:50 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:05:45 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-13 17:05:43 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:05:43 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-13 17:05:27 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:05:18 | Manampitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.020 |  |
| 2025-12-13 17:04:30 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-13 17:04:01 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.061 |  |
| 2025-12-13 17:03:44 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2025-12-13 17:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:03:29 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:03:15 | Weraganthota (Mahaweli Ganga) | -1.31 | 🟢 Normal | -0.069 |  |
| 2025-12-13 17:02:51 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:02:49 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | -0.012 |  |
| 2025-12-13 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.100 |  |
| 2025-12-13 17:01:51 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 1.254 | 🔺 Rising |
| 2025-12-13 17:01:44 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:01:27 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.050 |  |
| 2025-12-13 17:01:18 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-13 17:01:16 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:00:57 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:00:54 | Horowpothana (Yan Oya) | 5.64 | 🟢 Normal | -0.030 |  |
| 2025-12-13 17:00:32 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:00:31 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:59:32 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.072 |  |
| 2025-12-13 16:35:16 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 17:01:51 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 1.254 | 🔺 Rising |
| 2025-12-13 17:05:43 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-13 17:11:22 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-13 17:01:18 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-13 17:04:30 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-13 17:10:13 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-13 17:05:45 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-13 17:05:59 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-13 17:10:05 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-13 17:00:31 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:00:32 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-13 16:02:54 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:09:35 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:10:12 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:05:50 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:11:59 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:05:27 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-13 17:11:55 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.009 |  |
| 2025-12-13 17:05:43 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:02:51 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:01:16 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:00:57 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:03:29 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:01:44 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-13 17:03:44 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2025-12-13 17:02:49 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | -0.012 |  |
| 2025-12-13 17:12:36 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.017 |  |
| 2025-12-13 17:06:25 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.019 |  |
| 2025-12-13 17:05:18 | Manampitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.020 |  |
| 2025-12-13 17:06:44 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2025-12-13 17:22:13 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.026 |  |
| 2025-12-13 17:00:54 | Horowpothana (Yan Oya) | 5.64 | 🟢 Normal | -0.030 |  |
| 2025-12-13 17:11:59 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.037 |  |
| 2025-12-13 17:01:27 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.050 |  |
| 2025-12-13 17:04:01 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.061 |  |
| 2025-12-13 17:03:15 | Weraganthota (Mahaweli Ganga) | -1.31 | 🟢 Normal | -0.069 |  |
| 2025-12-13 16:59:32 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.072 |  |
| 2025-12-13 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)