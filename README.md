# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_13:05:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,873 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 13:05:45 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-12 13:05:43 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:05:42 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2025-12-12 13:05:36 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | -0.399 |  |
| 2025-12-12 13:05:27 | Manampitiya (Mahaweli Ganga) | 3.31 | 🟡 Alert | -0.039 |  |
| 2025-12-12 13:05:17 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.019 |  |
| 2025-12-12 13:05:09 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:05:07 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:04:28 | Horowpothana (Yan Oya) | 6.18 | 🟡 Alert | 0.147 | 🔺 Rising |
| 2025-12-12 13:04:28 | Thanthirimale (Malwathu Oya) | 4.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 13:04:09 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.038 |  |
| 2025-12-12 13:04:04 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2025-12-12 13:03:53 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.129 |  |
| 2025-12-12 13:03:48 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:03:32 | Galgamuwa (Mee Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 13:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.33 | 🟢 Normal | -0.020 |  |
| 2025-12-12 13:03:27 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:03:23 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:03:01 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:02:35 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.040 |  |
| 2025-12-12 13:02:26 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:02:24 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:02:15 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:02:15 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-12 13:02:10 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.019 |  |
| 2025-12-12 13:02:06 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:02:03 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:01:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:00:43 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-12 12:13:49 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:10:08 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.046 |  |
| 2025-12-12 12:07:58 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:07:20 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 13:04:28 | Horowpothana (Yan Oya) | 6.18 | 🟡 Alert | 0.147 | 🔺 Rising |
| 2025-12-12 13:05:27 | Manampitiya (Mahaweli Ganga) | 3.31 | 🟡 Alert | -0.039 |  |
| 2025-12-12 13:00:43 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-12 13:05:45 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-12 12:06:46 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-12 13:03:32 | Galgamuwa (Mee Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 13:04:28 | Thanthirimale (Malwathu Oya) | 4.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 13:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:01:15 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:05:09 | Ellagawa (Kalu Ganga) | 6.44 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:01:38 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-12 12:04:32 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:02:15 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:05:07 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-12 13:05:43 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:02:06 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:02:26 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:03:01 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:02:07 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:03:27 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:02:03 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:02:24 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:03:48 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-12 13:03:23 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-12 12:03:55 | Padiyathalawa (Maduru Oya) | 1.46 | 🟢 Normal | -0.012 |  |
| 2025-12-12 13:05:17 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.019 |  |
| 2025-12-12 13:02:10 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.019 |  |
| 2025-12-12 13:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.33 | 🟢 Normal | -0.020 |  |
| 2025-12-12 13:02:15 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-12 13:04:04 | Nakkala (Kumbukkan Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2025-12-12 13:05:42 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2025-12-12 13:04:09 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | -0.038 |  |
| 2025-12-12 13:02:35 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.040 |  |
| 2025-12-12 11:11:32 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.043 |  |
| 2025-12-12 12:10:08 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.046 |  |
| 2025-12-12 12:04:14 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.050 |  |
| 2025-12-12 12:02:36 | Moragaswewa (Deduru Oya) | 1.69 | 🟢 Normal | -0.053 |  |
| 2025-12-12 13:03:53 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.129 |  |
| 2025-12-12 13:05:36 | Weraganthota (Mahaweli Ganga) | -1.02 | 🟢 Normal | -0.399 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)