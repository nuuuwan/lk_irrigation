# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_12:10:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,482 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 12:10:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-25 12:10:41 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.018 |  |
| 2025-12-25 12:10:06 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.053 |  |
| 2025-12-25 12:07:31 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.024 |  |
| 2025-12-25 12:06:49 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:06:16 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2025-12-25 12:06:06 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.038 |  |
| 2025-12-25 12:05:57 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2025-12-25 12:05:22 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.051 |  |
| 2025-12-25 12:05:13 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.151 |  |
| 2025-12-25 12:05:08 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.116 |  |
| 2025-12-25 12:04:42 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:04:30 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:04:00 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:48 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:47 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.080 |  |
| 2025-12-25 12:03:41 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:41 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:28 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 12:03:28 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:13 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.138 |  |
| 2025-12-25 12:02:55 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:02:54 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:02:53 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.029 |  |
| 2025-12-25 12:02:32 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | -0.011 |  |
| 2025-12-25 12:02:15 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 12:02:14 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2025-12-25 12:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-25 12:02:08 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:01:28 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.011 |  |
| 2025-12-25 12:01:23 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.020 |  |
| 2025-12-25 12:01:16 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:01:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:01:11 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:00:34 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:00:07 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:17:27 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.151 |  |
| 2025-12-25 11:17:08 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 12:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-25 12:10:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-25 12:02:15 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 12:03:28 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 12:01:11 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:02:08 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:00:07 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:01:11 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:48 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 11:10:04 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:41 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:04:42 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:02:54 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:28 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:03:41 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:04:30 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:06:49 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:02:55 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:00:34 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:01:16 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:04:00 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 12:05:57 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2025-12-25 12:02:32 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | -0.011 |  |
| 2025-12-25 12:01:28 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.011 |  |
| 2025-12-25 12:10:41 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.018 |  |
| 2025-12-25 12:02:14 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2025-12-25 12:06:16 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2025-12-25 12:01:23 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.020 |  |
| 2025-12-25 12:07:31 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.024 |  |
| 2025-12-25 12:02:53 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.029 |  |
| 2025-12-25 12:06:06 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.038 |  |
| 2025-12-25 12:05:22 | Rathnapura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.051 |  |
| 2025-12-25 12:10:06 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.053 |  |
| 2025-12-25 11:12:43 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.064 |  |
| 2025-12-25 12:03:47 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.080 |  |
| 2025-12-25 12:05:08 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.116 |  |
| 2025-12-25 12:03:13 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.138 |  |
| 2025-12-25 12:05:13 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)