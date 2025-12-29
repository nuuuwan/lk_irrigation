# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_17:04:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,216 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 17:04:20 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2025-12-29 17:04:20 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.058 |  |
| 2025-12-29 17:04:09 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-29 17:04:08 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:03:32 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:02:59 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 17:02:53 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-29 17:02:52 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 17:02:50 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-29 17:02:48 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:02:33 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-29 17:02:33 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:02:33 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:02:22 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:02:16 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 17:02:12 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.036 |  |
| 2025-12-29 17:01:55 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 17:01:24 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:01:21 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:01:16 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:01:12 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 17:01:10 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.025 |  |
| 2025-12-29 17:01:06 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:01:03 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:00:45 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-29 16:18:33 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:13:56 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2025-12-29 16:13:39 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.025 |  |
| 2025-12-29 16:12:01 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.036 |  |
| 2025-12-29 16:09:07 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:08:08 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:07:51 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:07:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:07:24 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:07:08 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-29 16:06:47 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 16:06:38 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:06:28 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.103 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 17:02:33 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-29 17:00:45 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-29 17:02:50 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-29 17:02:16 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 17:02:59 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 17:01:12 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 17:01:55 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 17:02:52 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 16:07:51 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:01:21 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:03 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:02:48 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:04:20 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:04:08 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:02:22 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:01:24 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:02:33 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:03:32 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:01:03 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:08:08 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:01:06 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:01:16 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 17:02:33 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:52 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:01:04 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:03:37 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:06:38 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:13:56 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2025-12-29 16:09:07 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-29 17:04:09 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-29 17:02:53 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-29 17:04:20 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:04:46 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:01:29 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2025-12-29 16:03:43 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.021 |  |
| 2025-12-29 17:01:10 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.025 |  |
| 2025-12-29 17:02:12 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.036 |  |
| 2025-12-29 17:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.058 |  |
| 2025-12-29 16:06:28 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)