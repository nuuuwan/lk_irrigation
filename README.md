# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_09:19:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,040 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 09:19:10 | Horowpothana (Yan Oya) | 6.06 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2025-12-19 09:13:51 | Weraganthota (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.126 |  |
| 2025-12-19 09:11:35 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:10:05 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:08:47 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:08:03 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | -0.048 |  |
| 2025-12-19 09:07:53 | Galgamuwa (Mee Oya) | 1.94 | 🟢 Normal | -0.028 |  |
| 2025-12-19 09:07:25 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2025-12-19 09:06:57 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:06:32 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:06:30 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 09:05:57 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2025-12-19 09:05:53 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:05:41 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.080 |  |
| 2025-12-19 09:05:36 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.013 |  |
| 2025-12-19 09:05:26 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:04:24 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:04:18 | Manampitiya (Mahaweli Ganga) | 4.81 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-19 09:04:18 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.006 |  |
| 2025-12-19 09:04:16 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:04:14 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:03:31 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:02:51 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.081 |  |
| 2025-12-19 09:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.051 |  |
| 2025-12-19 09:02:45 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 09:02:38 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:02:38 | Nakkala (Kumbukkan Oya) | 1.72 | 🟢 Normal | -0.019 |  |
| 2025-12-19 09:02:37 | Thanthirimale (Malwathu Oya) | 5.35 | 🟡 Alert | 0.000 |  |
| 2025-12-19 09:02:30 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:01:58 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-19 09:01:58 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 09:01:53 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | -0.020 |  |
| 2025-12-19 09:01:40 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.013 |  |
| 2025-12-19 09:01:16 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:00:29 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.051 |  |
| 2025-12-19 09:00:13 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2025-12-19 09:00:08 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 09:04:18 | Manampitiya (Mahaweli Ganga) | 4.81 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-19 09:19:10 | Horowpothana (Yan Oya) | 6.06 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2025-12-19 09:02:37 | Thanthirimale (Malwathu Oya) | 5.35 | 🟡 Alert | 0.000 |  |
| 2025-12-19 09:01:58 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-19 09:06:30 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 09:01:58 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 09:02:45 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 07:02:52 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 09:11:35 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:01:16 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:00:08 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:02:38 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:10:05 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:06:57 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:05:53 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:06:32 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:08:47 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-19 09:04:18 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.006 |  |
| 2025-12-19 09:05:26 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:04:16 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:04:14 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:04:24 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:03:31 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:02:30 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-19 09:00:13 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2025-12-19 08:06:29 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2025-12-19 09:05:36 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.013 |  |
| 2025-12-19 09:01:40 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | -0.013 |  |
| 2025-12-19 09:02:38 | Nakkala (Kumbukkan Oya) | 1.72 | 🟢 Normal | -0.019 |  |
| 2025-12-19 09:01:53 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | -0.020 |  |
| 2025-12-19 09:07:53 | Galgamuwa (Mee Oya) | 1.94 | 🟢 Normal | -0.028 |  |
| 2025-12-19 09:05:57 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2025-12-19 09:07:25 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2025-12-19 09:08:03 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | -0.048 |  |
| 2025-12-19 09:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.051 |  |
| 2025-12-19 09:00:29 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.051 |  |
| 2025-12-19 09:05:41 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.080 |  |
| 2025-12-19 09:02:51 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.081 |  |
| 2025-12-19 09:13:51 | Weraganthota (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)