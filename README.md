# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_20:16:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,219 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 20:16:28 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.068 |  |
| 2025-12-21 20:10:09 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:09:54 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:09:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2025-12-21 20:08:52 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2025-12-21 20:08:06 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:07:43 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2025-12-21 20:07:14 | Horowpothana (Yan Oya) | 4.54 | 🟢 Normal | -0.055 |  |
| 2025-12-21 20:06:52 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:06:32 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:06:25 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-21 20:06:13 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:06:03 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:05:17 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:04:29 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:04:21 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | -0.022 |  |
| 2025-12-21 20:04:08 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | -0.031 |  |
| 2025-12-21 20:03:36 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2025-12-21 20:03:29 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 20:03:25 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:03:17 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | -0.020 |  |
| 2025-12-21 20:03:16 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:03:03 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:03:01 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-21 20:03:01 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2025-12-21 20:02:57 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-21 20:02:31 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:02:31 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:02:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2025-12-21 20:02:08 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-21 20:01:59 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.040 |  |
| 2025-12-21 20:01:27 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:01:12 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:00:07 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:27:48 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.087 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 20:03:36 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2025-12-21 20:02:08 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-21 20:03:01 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-21 20:06:25 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-21 20:03:29 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 20:00:07 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:06:03 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:04:29 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:03:25 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:02:31 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:01:27 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:06:52 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:08:06 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:01:12 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:05:17 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:02:31 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:06:32 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:03:03 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:09:54 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:10:09 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:03:16 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:06:13 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:08:52 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2025-12-21 20:07:43 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2025-12-21 20:02:57 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-21 19:00:12 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.011 |  |
| 2025-12-21 20:03:01 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2025-12-21 20:09:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2025-12-21 20:03:17 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | -0.020 |  |
| 2025-12-21 20:04:21 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | -0.022 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-21 20:02:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2025-12-21 20:04:08 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | -0.031 |  |
| 2025-12-21 20:01:59 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.040 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-21 20:07:14 | Horowpothana (Yan Oya) | 4.54 | 🟢 Normal | -0.055 |  |
| 2025-12-21 20:16:28 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)