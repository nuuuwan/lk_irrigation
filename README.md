# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_05:16:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,285 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 05:16:10 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -144.000 |  |
| 2025-12-15 05:16:09 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -144.000 |  |
| 2025-12-15 05:16:07 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -144.000 |  |
| 2025-12-15 05:16:05 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -144.000 |  |
| 2025-12-15 05:15:31 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -144.000 |  |
| 2025-12-15 05:15:13 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.005 |  |
| 2025-12-15 05:15:00 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -144.000 |  |
| 2025-12-15 05:14:04 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -144.000 |  |
| 2025-12-15 05:13:34 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -4.235 |  |
| 2025-12-15 05:13:17 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -4.235 |  |
| 2025-12-15 05:11:41 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:07:55 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2025-12-15 05:07:34 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.005 |  |
| 2025-12-15 05:06:52 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.036 |  |
| 2025-12-15 05:06:49 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-15 05:06:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:05:01 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.025 |  |
| 2025-12-15 05:04:53 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2025-12-15 05:04:44 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-15 05:04:38 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:04:27 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:03:46 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-15 05:03:17 | Horowpothana (Yan Oya) | 4.15 | 🟢 Normal | -0.010 |  |
| 2025-12-15 05:03:16 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-15 05:02:49 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | -0.039 |  |
| 2025-12-15 05:02:46 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.021 |  |
| 2025-12-15 05:02:46 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:02:42 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2025-12-15 05:02:20 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:02:18 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:01:36 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:01:21 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 05:01:19 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-15 05:01:10 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:00:53 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.032 |  |
| 2025-12-15 05:00:38 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:00:10 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:55:06 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:54:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:51:26 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:42:11 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.032 |  |
| 2025-12-15 04:42:09 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.032 |  |
| 2025-12-15 04:40:47 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.025 |  |
| 2025-12-15 04:20:00 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 05:04:44 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-15 05:03:16 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-15 03:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-15 05:01:21 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 05:04:27 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:02:20 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:02:26 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:01:36 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:04:38 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:06:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:02:46 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:02:18 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:01:10 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:11:41 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:00:38 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:00:10 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-15 04:51:26 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-15 05:07:34 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.005 |  |
| 2025-12-15 05:15:13 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.005 |  |
| 2025-12-15 05:06:49 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-15 05:02:42 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2025-12-15 05:03:17 | Horowpothana (Yan Oya) | 4.15 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-15 05:01:19 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-15 05:03:46 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-15 05:07:55 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2025-12-15 05:04:53 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2025-12-15 05:02:46 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.021 |  |
| 2025-12-15 05:05:01 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.025 |  |
| 2025-12-15 05:00:53 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.032 |  |
| 2025-12-15 05:06:52 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.036 |  |
| 2025-12-15 05:02:49 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | -0.039 |  |
| 2025-12-15 04:01:41 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.040 |  |
| 2025-12-15 04:08:31 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | -0.058 |  |
| 2025-12-15 05:13:34 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -4.235 |  |
| 2025-12-15 05:16:10 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)