# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_06:26:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,506 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 06:26:34 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:21:02 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.015 |  |
| 2025-12-13 06:17:19 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2025-12-13 06:16:50 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-13 06:16:36 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:16:22 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:14:39 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-13 06:11:50 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:11:43 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | -0.055 |  |
| 2025-12-13 06:10:12 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.018 |  |
| 2025-12-13 06:09:51 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:09:07 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | -0.018 |  |
| 2025-12-13 06:08:51 | Horowpothana (Yan Oya) | 6.15 | 🟡 Alert | -0.031 |  |
| 2025-12-13 06:06:56 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.019 |  |
| 2025-12-13 06:06:33 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.009 |  |
| 2025-12-13 06:06:15 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:06:09 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:05:48 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.069 |  |
| 2025-12-13 06:05:36 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.057 |  |
| 2025-12-13 06:04:28 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:04:27 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-13 06:04:23 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.145 |  |
| 2025-12-13 06:04:20 | Yaka Wewa (Ma Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:04:06 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:04:03 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.038 |  |
| 2025-12-13 06:03:58 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:03:41 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.041 |  |
| 2025-12-13 06:03:29 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:03:28 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.049 |  |
| 2025-12-13 06:03:07 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:01:41 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:01:29 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:01:17 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2025-12-13 06:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:00:38 | Peradeniya (Mahaweli Ganga) | 2.44 | 🟢 Normal | -0.042 |  |
| 2025-12-13 06:00:22 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2025-12-13 06:00:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 06:08:51 | Horowpothana (Yan Oya) | 6.15 | 🟡 Alert | -0.031 |  |
| 2025-12-13 06:00:22 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2025-12-13 06:14:39 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-13 06:16:50 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-13 06:04:27 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-13 06:16:22 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:03:29 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:04:28 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:11:50 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:26:34 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:01:29 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:09:51 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:06:09 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:00:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | 0.000 |  |
| 2025-12-13 06:17:19 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2025-12-13 06:06:33 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.009 |  |
| 2025-12-13 06:04:06 | Padiyathalawa (Maduru Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:04:20 | Yaka Wewa (Ma Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:03:07 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:03:58 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:01:41 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:06:15 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-13 06:21:02 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.015 |  |
| 2025-12-13 06:09:07 | Moragaswewa (Deduru Oya) | 1.45 | 🟢 Normal | -0.018 |  |
| 2025-12-13 06:10:12 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.018 |  |
| 2025-12-13 06:06:56 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.019 |  |
| 2025-12-13 06:01:17 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2025-12-13 06:04:03 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.038 |  |
| 2025-12-13 06:03:41 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.041 |  |
| 2025-12-13 06:00:38 | Peradeniya (Mahaweli Ganga) | 2.44 | 🟢 Normal | -0.042 |  |
| 2025-12-13 06:03:28 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.049 |  |
| 2025-12-13 06:11:43 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | -0.055 |  |
| 2025-12-13 06:05:36 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.057 |  |
| 2025-12-13 06:05:48 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.069 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |
| 2025-12-13 06:04:23 | Magura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)