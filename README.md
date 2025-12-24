# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_03:03:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,108 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 03:03:42 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 03:03:20 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 1.091 | 🔺 Rising |
| 2025-12-25 03:02:58 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 1.091 | 🔺 Rising |
| 2025-12-25 03:02:44 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 03:02:43 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.079 |  |
| 2025-12-25 03:02:18 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-25 03:02:09 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:02:05 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-25 03:01:32 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 03:01:27 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-25 03:01:12 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-25 03:01:03 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:00:54 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-25 03:00:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2025-12-25 03:00:27 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.009 |  |
| 2025-12-25 02:55:37 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:53:53 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-25 02:46:44 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-25 02:45:12 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:42:18 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:40:59 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-25 02:35:59 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-25 02:33:47 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:13:32 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.028 |  |
| 2025-12-25 02:12:00 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:10:37 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-25 02:08:50 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 00:16:54 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 21.600 | 🔺 Rising |
| 2025-12-25 03:03:20 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 1.091 | 🔺 Rising |
| 2025-12-25 03:00:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2025-12-25 01:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-25 02:40:59 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-25 03:00:54 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-25 03:02:18 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-25 03:02:44 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 01:01:58 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-25 02:35:59 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-25 03:01:32 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 02:05:37 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 02:10:37 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-25 02:46:44 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-25 03:03:42 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 02:04:49 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:01:03 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:03:51 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:08:50 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:02:09 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:09:50 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:42:18 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 01:08:39 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:04:55 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:02:58 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:45:12 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:55:37 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-25 02:33:47 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 03:00:27 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.009 |  |
| 2025-12-25 03:02:05 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-25 03:01:27 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-25 03:01:12 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-25 02:13:32 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.028 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-25 03:02:43 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.079 |  |
| 2025-12-25 01:01:41 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.995 |  |
| 2025-12-25 01:02:33 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -8.000 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)