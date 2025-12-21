# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_09:26:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,793 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 09:26:50 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.007 |  |
| 2025-12-21 09:15:28 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:10:09 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:08:46 | Weraganthota (Mahaweli Ganga) | -0.86 | 🟢 Normal | -0.189 |  |
| 2025-12-21 09:08:32 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-21 09:08:09 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:08:01 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-21 09:05:38 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | -0.029 |  |
| 2025-12-21 09:05:28 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:05:02 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 09:04:34 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-21 09:04:30 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 09:04:27 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.065 |  |
| 2025-12-21 09:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.042 |  |
| 2025-12-21 09:04:07 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2025-12-21 09:03:55 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:03:46 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:03:45 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:03:29 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:03:20 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:03:18 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-21 09:03:13 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2025-12-21 09:02:57 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:02:53 | Manampitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.019 |  |
| 2025-12-21 09:02:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2025-12-21 09:02:47 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:02:46 | Thanthirimale (Malwathu Oya) | 5.17 | 🟡 Alert | -0.022 |  |
| 2025-12-21 09:02:26 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.031 |  |
| 2025-12-21 09:02:11 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:01:58 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:01:35 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | -0.117 |  |
| 2025-12-21 09:01:34 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:01:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:01:24 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-21 09:01:19 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:00:49 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 09:02:46 | Thanthirimale (Malwathu Oya) | 5.17 | 🟡 Alert | -0.022 |  |
| 2025-12-21 09:08:01 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-21 09:08:32 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-21 09:01:24 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-21 09:04:30 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 09:05:02 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 09:08:09 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:01:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:02:11 | Nakkala (Kumbukkan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:02:57 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:03:55 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:10:09 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:03:46 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:03:29 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:03:45 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:02:47 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:05:28 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:01:58 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:03:20 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:01:34 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:01:19 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:15:28 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-21 09:26:50 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.007 |  |
| 2025-12-21 09:04:34 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-21 09:03:18 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-21 09:00:49 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-21 09:03:13 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2025-12-21 09:02:53 | Manampitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.019 |  |
| 2025-12-21 08:08:29 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.019 |  |
| 2025-12-21 09:05:38 | Panadugama (Nilwala Ganga) | 3.86 | 🟢 Normal | -0.029 |  |
| 2025-12-21 09:02:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2025-12-21 09:02:26 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.031 |  |
| 2025-12-21 09:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.042 |  |
| 2025-12-21 09:04:07 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2025-12-21 09:04:27 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.065 |  |
| 2025-12-21 09:01:35 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | -0.117 |  |
| 2025-12-21 08:59:50 | Horowpothana (Yan Oya) | 5.39 | 🟢 Normal | -0.130 |  |
| 2025-12-21 09:08:46 | Weraganthota (Mahaweli Ganga) | -0.86 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)