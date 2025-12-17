# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_13:13:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,396 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 13:13:16 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:12:38 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-17 13:10:45 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.009 |  |
| 2025-12-17 13:07:52 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:07:50 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-17 13:07:27 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:07:17 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:07:16 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:07:04 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:06:42 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-17 13:06:29 | Yaka Wewa (Ma Oya) | 1.62 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2025-12-17 13:05:44 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:05:27 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2025-12-17 13:05:25 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:04:32 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:03:52 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-17 13:03:40 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 13:03:38 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:03:37 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:03:33 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:03:25 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:03:01 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 13:02:56 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-17 13:02:51 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 13:02:31 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 13:02:22 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:02:15 | Thanthirimale (Malwathu Oya) | 3.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 13:02:15 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:01:34 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:01:34 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-17 13:01:28 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 13:01:21 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:00:56 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 13:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:00:32 | Horowpothana (Yan Oya) | 5.75 | 🟢 Normal | -0.040 |  |
| 2025-12-17 13:00:11 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 12:56:01 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 13:06:29 | Yaka Wewa (Ma Oya) | 1.62 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2025-12-17 12:02:48 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-17 13:01:34 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-17 13:02:15 | Thanthirimale (Malwathu Oya) | 3.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 13:03:40 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 13:07:50 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-17 13:02:56 | Manampitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-17 13:00:56 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 13:06:42 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-17 13:01:28 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 13:00:11 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 13:03:01 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 13:02:31 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 13:02:51 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 13:01:34 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:05:44 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:07:16 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:13:16 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-17 12:02:04 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:03:25 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:12:38 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:03:33 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:07:52 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:03:38 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:03:37 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:02:15 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:07:04 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:02:22 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:07:27 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:07:17 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:04:32 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:05:25 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:10:45 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.009 |  |
| 2025-12-17 13:03:52 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-17 13:05:27 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2025-12-17 13:00:32 | Horowpothana (Yan Oya) | 5.75 | 🟢 Normal | -0.040 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)