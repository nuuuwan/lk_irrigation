# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_05:24:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,760 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 05:24:29 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:20:54 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2025-12-29 05:16:49 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:08:37 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-29 05:07:52 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:07:51 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.019 |  |
| 2025-12-29 05:07:37 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2025-12-29 05:07:05 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2025-12-29 05:06:49 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -4.320 |  |
| 2025-12-29 05:05:59 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -4.320 |  |
| 2025-12-29 05:05:51 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.011 |  |
| 2025-12-29 05:04:48 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:04:44 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2025-12-29 05:04:28 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-29 05:04:11 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:04:04 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.016 |  |
| 2025-12-29 05:04:04 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-29 05:03:04 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 05:03:01 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:02:58 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:02:55 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2025-12-29 05:02:42 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:02:40 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-29 05:02:35 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:02:18 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:02:08 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:02:02 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-29 05:01:43 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:01:22 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:01:08 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:01:01 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:00:55 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 02:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-29 02:04:51 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-29 05:04:04 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-29 05:02:40 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-29 05:08:37 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-29 05:00:55 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 05:03:04 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 05:02:42 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:02:08 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:04:48 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:02:58 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:12:51 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:11:45 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:02:35 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:03:01 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:01:08 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:16:49 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:07:52 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:01:01 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:04:11 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:24:29 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:02:18 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:09:20 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:01:43 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:00:53 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:01:22 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 05:02:02 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-29 05:07:05 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2025-12-28 18:02:15 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-29 05:04:28 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-29 05:04:44 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2025-12-29 05:05:51 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.011 |  |
| 2025-12-29 05:07:37 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2025-12-29 05:04:04 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.016 |  |
| 2025-12-29 04:27:13 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.016 |  |
| 2025-12-29 05:02:55 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2025-12-29 05:07:51 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.019 |  |
| 2025-12-29 05:20:54 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2025-12-29 05:06:49 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -4.320 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)