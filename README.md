# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--11--30_18:13:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,080 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-30 18:13:48 | Giriulla (Maha Oya) | 4.00 | 🟢 Normal | -0.048 |  |
| 2025-11-30 18:10:10 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2025-11-30 18:06:03 | Hanwella (Kelani Ganga) | 10.51 | 🔴 Major Flood | -0.040 |  |
| 2025-11-30 18:05:33 | Thanamalwila (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-11-30 18:05:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.78 | 🟠 Minor Flood | -0.019 |  |
| 2025-11-30 18:05:10 | Nagalagam Street (Kelani Ganga) | 2.32 | 🔴 Major Flood | 0.015 | 🔺 Rising |
| 2025-11-30 18:04:38 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | -0.072 |  |
| 2025-11-30 18:04:32 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.020 |  |
| 2025-11-30 18:04:08 | Dunamale (Aththanagalu Oya) | 4.99 | 🟠 Minor Flood | -0.010 |  |
| 2025-11-30 18:03:58 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.029 |  |
| 2025-11-30 18:03:37 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.104 |  |
| 2025-11-30 18:03:15 | Deraniyagala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-11-30 18:02:54 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2025-11-30 18:02:48 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-11-30 18:02:48 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-11-30 18:02:45 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.099 |  |
| 2025-11-30 18:02:22 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2025-11-30 18:02:19 | Katharagama (Menik Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-11-30 18:02:17 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2025-11-30 18:02:09 | Rathnapura (Kalu Ganga) | 6.57 | 🟡 Alert | -0.064 |  |
| 2025-11-30 18:01:55 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-11-30 18:01:53 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-11-30 18:01:47 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-11-30 18:01:45 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2025-11-30 18:01:36 | Glencourse (Kelani Ganga) | 16.25 | 🟡 Alert | -0.230 |  |
| 2025-11-30 18:01:31 | Siyambalanduwa (Heda Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-11-30 18:01:20 | Yaka Wewa (Ma Oya) | 1.56 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-11-30 18:00:45 | Horowpothana (Yan Oya) | 7.51 | 🟠 Minor Flood | -0.021 |  |
| 2025-11-30 18:00:34 | Thanthirimale (Malwathu Oya) | 10.86 | 🔴 Major Flood | -0.041 |  |
| 2025-11-30 18:00:16 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-11-30 18:05:10 | Nagalagam Street (Kelani Ganga) | 2.32 | 🔴 Major Flood | 0.015 | 🔺 Rising |
| 2025-11-30 18:06:03 | Hanwella (Kelani Ganga) | 10.51 | 🔴 Major Flood | -0.040 |  |
| 2025-11-30 18:00:34 | Thanthirimale (Malwathu Oya) | 10.86 | 🔴 Major Flood | -0.041 |  |
| 2025-11-30 03:16:47 | Badalgama (Maha Oya) | 11.35 | 🔴 Major Flood | -0.289 |  |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-11-27 18:42:59⌛ | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood | 0.045 | 🔺 Rising |
| 2025-11-30 14:56:34 | Ellagawa (Kalu Ganga) | 11.94 | 🟠 Minor Flood | 0.044 | 🔺 Rising |
| 2025-11-30 18:01:45 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2025-11-30 18:04:08 | Dunamale (Aththanagalu Oya) | 4.99 | 🟠 Minor Flood | -0.010 |  |
| 2025-11-30 18:05:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.78 | 🟠 Minor Flood | -0.019 |  |
| 2025-11-30 18:00:45 | Horowpothana (Yan Oya) | 7.51 | 🟠 Minor Flood | -0.021 |  |
| 2025-11-30 18:02:09 | Rathnapura (Kalu Ganga) | 6.57 | 🟡 Alert | -0.064 |  |
| 2025-11-30 18:01:36 | Glencourse (Kelani Ganga) | 16.25 | 🟡 Alert | -0.230 |  |
| 2025-11-30 18:10:10 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2025-11-30 18:01:20 | Yaka Wewa (Ma Oya) | 1.56 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-11-30 18:03:15 | Deraniyagala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-11-30 18:01:47 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-11-30 18:01:55 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-11-30 18:01:53 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-11-30 18:02:19 | Katharagama (Menik Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-11-30 18:02:48 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-11-30 18:02:22 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2025-11-30 18:01:31 | Siyambalanduwa (Heda Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-11-30 18:02:48 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-11-30 18:05:33 | Thanamalwila (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-11-30 18:04:32 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.020 |  |
| 2025-11-30 18:02:17 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2025-11-30 18:02:54 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-11-30 18:00:16 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.021 |  |
| 2025-11-30 18:03:58 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.029 |  |
| 2025-11-30 18:13:48 | Giriulla (Maha Oya) | 4.00 | 🟢 Normal | -0.048 |  |
| 2025-11-30 18:04:38 | Kithulgala (Kelani Ganga) | 2.55 | 🟢 Normal | -0.072 |  |
| 2025-11-30 18:02:45 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.099 |  |
| 2025-11-30 18:03:37 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)