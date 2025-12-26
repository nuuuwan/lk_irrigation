# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_22:44:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,753 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 22:44:48 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.006 |  |
| 2025-12-26 22:23:17 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:22:37 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:13:35 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2025-12-26 22:12:24 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.008 |  |
| 2025-12-26 22:07:02 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.029 |  |
| 2025-12-26 22:06:19 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.009 |  |
| 2025-12-26 22:06:03 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:06:03 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-26 22:06:01 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.104 |  |
| 2025-12-26 22:05:25 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.067 |  |
| 2025-12-26 22:05:21 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.019 |  |
| 2025-12-26 22:04:32 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:04:29 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:04:27 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:04:07 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-26 22:03:44 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:03:28 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2025-12-26 22:03:25 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:03:24 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:03:12 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:03:10 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-26 22:03:00 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.011 |  |
| 2025-12-26 22:02:28 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2025-12-26 22:02:25 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 22:02:12 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:01:38 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:01:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.100 |  |
| 2025-12-26 22:01:17 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:01:11 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-26 22:01:09 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:00:58 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:00:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.022 |  |
| 2025-12-26 22:00:22 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 22:03:28 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2025-12-26 22:01:11 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-26 22:02:25 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 22:04:27 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:03:44 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:01:38 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:04:32 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 18:15:02 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:03:12 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:04:29 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:01:09 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:03:24 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:22:37 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:00:58 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:06:03 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:03:25 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:02:12 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:23:17 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:00:22 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:01:17 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 22:44:48 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | -0.006 |  |
| 2025-12-26 22:12:24 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.008 |  |
| 2025-12-26 22:06:19 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.009 |  |
| 2025-12-26 22:04:07 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-26 18:01:40 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-26 22:03:10 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-26 22:03:00 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.011 |  |
| 2025-12-26 22:05:21 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.019 |  |
| 2025-12-26 22:02:28 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2025-12-26 22:06:03 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-26 22:00:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.022 |  |
| 2025-12-26 18:05:51 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | -0.029 |  |
| 2025-12-26 22:07:02 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.029 |  |
| 2025-12-26 21:03:51 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.042 |  |
| 2025-12-26 22:13:35 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2025-12-26 22:05:25 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.067 |  |
| 2025-12-26 22:01:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.100 |  |
| 2025-12-26 22:06:01 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)