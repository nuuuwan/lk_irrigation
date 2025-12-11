# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_17:10:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,160 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 17:10:12 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-11 17:09:25 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:09:22 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:08:56 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.018 |  |
| 2025-12-11 17:07:50 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | -0.018 |  |
| 2025-12-11 17:07:23 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:07:03 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:06:34 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 17:06:12 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.020 |  |
| 2025-12-11 17:06:10 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-11 17:06:09 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 17:05:29 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-11 17:05:02 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.015 |  |
| 2025-12-11 17:04:47 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2025-12-11 17:04:39 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-11 17:04:10 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:03:56 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-11 17:03:49 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:03:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-11 17:03:26 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 17:03:09 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:03:09 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:02:31 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-11 17:02:16 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.011 |  |
| 2025-12-11 17:02:11 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:02:09 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.040 |  |
| 2025-12-11 17:02:07 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:02:07 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2025-12-11 17:02:04 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-11 17:02:01 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-11 17:01:56 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:01:46 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-11 17:01:32 | Horowpothana (Yan Oya) | 4.35 | 🟢 Normal | -0.084 |  |
| 2025-12-11 17:00:41 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2025-12-11 16:24:18 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-11 17:04:47 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2025-12-11 17:02:07 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2025-12-11 17:02:04 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-11 17:05:29 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-11 17:03:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-11 17:02:31 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-11 17:03:56 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-11 17:04:39 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-11 15:04:23 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 17:06:09 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 17:03:26 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 17:02:01 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-11 17:06:10 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-11 17:06:34 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 17:10:12 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-11 17:01:46 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:11:23 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:02:09 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:04:10 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:07:23 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:10:34 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:09:22 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:03:09 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:09:25 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:03:09 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:01:56 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:07:03 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:03:49 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:02:07 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 17:01:36 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-11 17:02:16 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.011 |  |
| 2025-12-11 17:05:02 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.015 |  |
| 2025-12-11 17:07:50 | Thanthirimale (Malwathu Oya) | 4.23 | 🟢 Normal | -0.018 |  |
| 2025-12-11 17:08:56 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.018 |  |
| 2025-12-11 17:06:12 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.020 |  |
| 2025-12-11 17:00:41 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2025-12-11 17:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.040 |  |
| 2025-12-11 17:01:32 | Horowpothana (Yan Oya) | 4.35 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)