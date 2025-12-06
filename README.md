# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_07:15:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,554 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 07:15:23 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:10:35 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | -0.103 |  |
| 2025-12-06 07:08:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-06 07:07:12 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:06:48 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:06:46 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.046 |  |
| 2025-12-06 07:06:38 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.018 |  |
| 2025-12-06 07:06:34 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | -0.075 |  |
| 2025-12-06 07:06:20 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.074 |  |
| 2025-12-06 07:06:14 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.321 |  |
| 2025-12-06 07:06:06 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:05:31 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-06 07:05:12 | Thanthirimale (Malwathu Oya) | 6.87 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2025-12-06 07:05:12 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:05:12 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | -0.029 |  |
| 2025-12-06 07:05:07 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.055 |  |
| 2025-12-06 07:05:02 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:04:58 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.009 |  |
| 2025-12-06 07:04:37 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.020 |  |
| 2025-12-06 07:04:34 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:04:33 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.058 |  |
| 2025-12-06 07:03:16 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:02:40 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:02:37 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.010 |  |
| 2025-12-06 07:02:03 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2025-12-06 07:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2025-12-06 07:01:21 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.022 |  |
| 2025-12-06 07:01:17 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 07:00:37 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:51:29 | Weraganthota (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-06 06:28:33 | Galgamuwa (Mee Oya) | 1.56 | 🟢 Normal | 0.062 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 07:05:12 | Thanthirimale (Malwathu Oya) | 6.87 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2025-12-06 07:10:35 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | -0.103 |  |
| 2025-12-06 07:02:03 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2025-12-06 06:51:29 | Weraganthota (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-06 06:28:33 | Galgamuwa (Mee Oya) | 1.56 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-06 07:01:17 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 07:08:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-06 07:02:40 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:04:34 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:23 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:07:12 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:15:23 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-06 06:02:33 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:06:48 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:03:16 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:05:02 | Katharagama (Menik Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:00:37 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:05:12 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-06 07:04:58 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.009 |  |
| 2025-12-06 06:03:37 | Giriulla (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-06 06:04:56 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-06 07:02:37 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.010 |  |
| 2025-12-06 06:01:34 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2025-12-06 07:06:38 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.018 |  |
| 2025-12-06 07:04:37 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.020 |  |
| 2025-12-06 07:05:31 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2025-12-06 07:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2025-12-06 07:01:21 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.022 |  |
| 2025-12-06 07:05:12 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | -0.029 |  |
| 2025-12-06 07:06:46 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.046 |  |
| 2025-12-06 07:05:07 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.055 |  |
| 2025-12-06 07:04:33 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.058 |  |
| 2025-12-06 07:06:20 | Rathnapura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.074 |  |
| 2025-12-06 07:06:34 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | -0.075 |  |
| 2025-12-06 07:06:14 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.321 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)