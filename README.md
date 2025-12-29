# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_16:09:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,186 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 16:09:07 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:08:08 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:07:51 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:07:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-29 16:07:24 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:07:08 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-29 16:06:47 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:06:38 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:06:28 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.103 |  |
| 2025-12-29 16:06:02 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:04:46 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:04:03 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:03:46 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:03:45 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:03:43 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.021 |  |
| 2025-12-29 16:03:37 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:03:12 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:52 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:49 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:41 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 16:02:36 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-29 16:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.050 |  |
| 2025-12-29 16:02:03 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:00 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:01:56 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2025-12-29 16:01:50 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 16:01:41 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:01:39 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:01:29 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2025-12-29 16:01:28 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 16:01:18 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:01:04 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:00:59 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:00:21 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-29 15:18:37 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 15:14:53 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 15:04:13 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2025-12-29 16:01:56 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2025-12-29 16:07:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-29 16:07:08 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-29 16:01:50 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 16:01:28 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-29 16:02:41 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 16:07:51 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:03 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:00 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:01:41 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 15:00:42 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-29 15:04:49 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:01:18 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:08:08 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:03:45 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:00:59 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:07:24 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:49 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:03:12 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:06:02 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:02:52 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:01:04 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:03:37 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:06:47 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:06:38 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:04:03 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-29 16:09:07 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:03:46 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:00:21 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:01:39 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:04:46 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-29 16:02:36 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-29 16:01:29 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2025-12-29 16:03:43 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | -0.021 |  |
| 2025-12-29 15:06:05 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.038 |  |
| 2025-12-29 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.050 |  |
| 2025-12-29 16:06:28 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)