# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_08:18:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,763 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 08:18:12 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-30 08:16:50 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-30 08:13:34 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:11:05 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-30 08:10:34 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2025-12-30 08:07:19 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:06:05 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:05:51 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:05:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.022 |  |
| 2025-12-30 08:05:41 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.062 |  |
| 2025-12-30 08:05:30 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.024 |  |
| 2025-12-30 08:04:55 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:04:33 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-30 08:04:28 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:04:11 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 08:03:43 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-30 08:03:39 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.021 |  |
| 2025-12-30 08:03:31 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:03:27 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:03:22 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:03:03 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:03:02 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:02:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-30 08:02:54 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:02:53 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.070 |  |
| 2025-12-30 08:02:09 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:02:09 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:02:07 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.072 |  |
| 2025-12-30 08:01:49 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:47 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:39 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:32 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:27 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 08:01:16 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:16 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:09 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.034 |  |
| 2025-12-30 08:00:53 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-30 08:00:46 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-30 07:50:57 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 08:16:50 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-30 08:02:59 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-30 08:11:05 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-30 08:00:53 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-30 08:00:46 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-30 08:03:43 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-30 08:01:27 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 08:04:11 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 08:03:31 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:02:54 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:07:19 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:47 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:13:34 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:03:27 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:06:05 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:02:09 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:16 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:03:22 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:03:03 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:05:51 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:03:02 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:49 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:02:09 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:16 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:02:53 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:32 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:04:55 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:04:28 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:01:39 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-30 08:10:34 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2025-12-30 08:04:33 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-30 08:18:12 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-30 08:03:39 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.021 |  |
| 2025-12-30 08:05:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.022 |  |
| 2025-12-30 08:05:30 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.024 |  |
| 2025-12-30 08:01:09 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.034 |  |
| 2025-12-30 08:05:41 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.062 |  |
| 2025-12-30 08:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.070 |  |
| 2025-12-30 08:02:07 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)