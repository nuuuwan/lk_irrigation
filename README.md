# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_17:32:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,040 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 17:32:15 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.008 |  |
| 2025-12-12 17:16:46 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.024 |  |
| 2025-12-12 17:11:26 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | -0.041 |  |
| 2025-12-12 17:11:07 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:10:46 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.009 |  |
| 2025-12-12 17:10:18 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.058 |  |
| 2025-12-12 17:07:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | -0.028 |  |
| 2025-12-12 17:07:17 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-12 17:07:12 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.022 |  |
| 2025-12-12 17:06:08 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:05:57 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.042 |  |
| 2025-12-12 17:05:55 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:05:46 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.021 |  |
| 2025-12-12 17:05:41 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2025-12-12 17:05:33 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-12 17:05:23 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-12 17:05:18 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-12 17:05:18 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:05:17 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.029 |  |
| 2025-12-12 17:05:11 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | -0.180 |  |
| 2025-12-12 17:04:52 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 17:04:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-12 17:04:20 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:03:50 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.063 |  |
| 2025-12-12 17:03:22 | Manampitiya (Mahaweli Ganga) | 3.13 | 🟡 Alert | -0.063 |  |
| 2025-12-12 17:03:19 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:03:01 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-12 17:02:58 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-12 17:02:45 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-12 17:02:37 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2025-12-12 17:02:36 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:02:26 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.041 |  |
| 2025-12-12 17:02:12 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2025-12-12 17:01:40 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:01:37 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:01:16 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2025-12-12 17:01:09 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.040 |  |
| 2025-12-12 17:00:36 | Padiyathalawa (Maduru Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 17:02:37 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2025-12-12 17:03:22 | Manampitiya (Mahaweli Ganga) | 3.13 | 🟡 Alert | -0.063 |  |
| 2025-12-12 17:04:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-12 17:02:45 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-12 17:05:33 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-12 17:02:58 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-12 17:05:18 | Peradeniya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-12 17:07:17 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-12 17:04:52 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 17:01:40 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:11:07 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:04:20 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:05:55 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:06:08 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:00:36 | Padiyathalawa (Maduru Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:01:37 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:05:18 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:03:19 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:02:36 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-12 17:32:15 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.008 |  |
| 2025-12-12 17:10:46 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.009 |  |
| 2025-12-12 17:05:41 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2025-12-12 17:05:23 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-12 17:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-12 17:02:12 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2025-12-12 17:03:01 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-12 17:01:16 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2025-12-12 17:05:46 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.021 |  |
| 2025-12-12 17:07:12 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.022 |  |
| 2025-12-12 17:16:46 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.024 |  |
| 2025-12-12 17:07:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.20 | 🟢 Normal | -0.028 |  |
| 2025-12-12 17:05:17 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.029 |  |
| 2025-12-12 17:01:09 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.040 |  |
| 2025-12-12 17:02:26 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.041 |  |
| 2025-12-12 17:11:26 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | -0.041 |  |
| 2025-12-12 17:05:57 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.042 |  |
| 2025-12-12 17:10:18 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.058 |  |
| 2025-12-12 17:03:50 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.063 |  |
| 2025-12-12 17:05:11 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)