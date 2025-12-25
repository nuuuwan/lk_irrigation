# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_14:09:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,555 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 14:09:55 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.030 |  |
| 2025-12-25 14:08:43 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.043 |  |
| 2025-12-25 14:08:29 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.034 |  |
| 2025-12-25 14:06:01 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-25 14:05:49 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 14:05:40 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:05:26 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-25 14:04:58 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-25 14:04:03 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:03:24 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-25 14:03:23 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:03:18 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2025-12-25 14:03:16 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:03:12 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.040 |  |
| 2025-12-25 14:03:09 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:03:08 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.094 |  |
| 2025-12-25 14:03:00 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:02:53 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:02:50 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:02:50 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 14:02:37 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:02:15 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2025-12-25 14:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:59 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:30 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 14:01:29 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:16 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:14 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-25 14:01:01 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:00:49 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-12-25 14:00:37 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:58:32 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.021 |  |
| 2025-12-25 13:22:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-25 13:19:59 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2025-12-25 13:19:24 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:17:04 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:16:29 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:14:46 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.034 |  |
| 2025-12-25 13:13:27 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.043 |  |
| 2025-12-25 13:12:27 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 14:04:58 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-25 13:22:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-25 14:06:01 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-25 14:02:50 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 14:05:49 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 14:01:30 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 14:02:50 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:01 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:16 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:48 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:12:27 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:02:37 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:03:09 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:05:40 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:02:53 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:59 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:03:23 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:00:37 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:03:16 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:29 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:03:00 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:04:03 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:01:14 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2025-12-25 13:10:20 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.010 |  |
| 2025-12-25 14:03:24 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-25 14:05:26 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-25 14:00:49 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-12-25 14:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-25 13:19:59 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2025-12-25 13:58:32 | Manampitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.021 |  |
| 2025-12-25 14:09:55 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.030 |  |
| 2025-12-25 14:02:15 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2025-12-25 14:08:29 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.034 |  |
| 2025-12-25 14:03:18 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2025-12-25 14:03:12 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.040 |  |
| 2025-12-25 14:08:43 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.043 |  |
| 2025-12-25 14:03:08 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)