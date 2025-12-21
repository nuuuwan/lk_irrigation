# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_13:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,928 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 13:03:20 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:03:16 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-21 13:02:59 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:02:45 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:02:34 | Thanthirimale (Malwathu Oya) | 5.10 | 🟡 Alert | -0.020 |  |
| 2025-12-21 13:02:04 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:37 | Horowpothana (Yan Oya) | 4.92 | 🟢 Normal | -0.059 |  |
| 2025-12-21 13:01:36 | Manampitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:34 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2025-12-21 13:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:23 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:19 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:00:56 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.032 |  |
| 2025-12-21 13:00:54 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-21 12:40:18 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:12:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:11:29 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:11:16 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.054 |  |
| 2025-12-21 12:08:53 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:06:51 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:06:51 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:06:39 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 12:06:22 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:06:15 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:06:13 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:05:33 | Weraganthota (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2025-12-21 12:05:22 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-21 12:05:20 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:05:18 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2025-12-21 12:04:59 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 13:02:34 | Thanthirimale (Malwathu Oya) | 5.10 | 🟡 Alert | -0.020 |  |
| 2025-12-21 12:05:33 | Weraganthota (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2025-12-21 13:03:16 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-21 13:00:54 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-21 12:03:11 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-21 12:06:39 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 13:03:20 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:23 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:01:47 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:02:59 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:01:43 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:06:13 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:06:22 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:19 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:02:13 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:01:30 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:12:26 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:00:10 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:08:53 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:02:45 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:36 | Manampitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:11:29 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:02:04 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:03:40 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2025-12-21 12:03:03 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-21 12:05:18 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2025-12-21 12:03:34 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.011 |  |
| 2025-12-21 12:05:22 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-21 13:01:34 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2025-12-21 13:00:56 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.032 |  |
| 2025-12-21 12:01:39 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | -0.040 |  |
| 2025-12-21 12:01:21 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.053 |  |
| 2025-12-21 12:11:16 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.054 |  |
| 2025-12-21 12:02:22 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.056 |  |
| 2025-12-21 12:02:19 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.057 |  |
| 2025-12-21 13:01:37 | Horowpothana (Yan Oya) | 4.92 | 🟢 Normal | -0.059 |  |
| 2025-12-21 12:04:06 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.083 |  |
| 2025-12-21 12:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)