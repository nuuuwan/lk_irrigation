# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_23:08:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,977 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 23:08:10 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:07:37 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2025-12-15 23:07:16 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:06:40 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:06:36 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:06:33 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:06:03 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-15 23:05:44 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:05:37 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.035 |  |
| 2025-12-15 23:05:09 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:04:49 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:04:34 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:04:21 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:04:21 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.029 |  |
| 2025-12-15 23:04:09 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:03:53 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:03:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:03:07 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 23:02:35 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-15 23:02:27 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:02:27 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:02:19 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:02:05 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:01:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:01:47 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:01:40 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-15 23:01:39 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:01:31 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.041 |  |
| 2025-12-15 23:01:08 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:01:07 | Moragaswewa (Deduru Oya) | 1.21 | 🟢 Normal | -0.031 |  |
| 2025-12-15 23:00:55 | Horowpothana (Yan Oya) | 3.45 | 🟢 Normal | -0.023 |  |
| 2025-12-15 22:26:21 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 22:18:41 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-15 22:17:33 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-15 22:14:18 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.035 |  |
| 2025-12-15 22:13:58 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 22:10:47 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.066 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 23:06:03 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-15 21:16:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-15 22:05:06 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-15 23:03:07 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 23:01:40 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-15 23:02:35 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-15 23:01:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:03:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:02:19 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:04:21 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:01:39 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:02:05 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:06:36 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:01:47 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:08:10 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:05:09 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:02:27 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:04:09 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 22:05:20 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:06:40 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:02:27 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-15 21:02:48 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:04:34 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:07:16 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-15 23:03:53 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:04:49 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-15 22:03:56 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:01:08 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:05:44 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:06:33 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2025-12-15 23:07:37 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2025-12-15 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-15 23:00:55 | Horowpothana (Yan Oya) | 3.45 | 🟢 Normal | -0.023 |  |
| 2025-12-15 23:04:21 | Ellagawa (Kalu Ganga) | 5.09 | 🟢 Normal | -0.029 |  |
| 2025-12-15 23:01:07 | Moragaswewa (Deduru Oya) | 1.21 | 🟢 Normal | -0.031 |  |
| 2025-12-15 23:05:37 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.035 |  |
| 2025-12-15 23:01:31 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.041 |  |
| 2025-12-15 18:00:44 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2025-12-15 18:01:57 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)