# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_18:20:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,587 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 18:20:38 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:11:26 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:10:21 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2025-12-17 18:08:19 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2025-12-17 18:07:38 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 18:07:24 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 18:05:32 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:05:12 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-17 18:04:32 | Yaka Wewa (Ma Oya) | 1.66 | 🟢 Normal | -0.077 |  |
| 2025-12-17 18:04:16 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-17 18:04:10 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-17 18:04:01 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-17 18:04:00 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.063 |  |
| 2025-12-17 18:03:57 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:03:39 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2025-12-17 18:03:32 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:03:30 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:02:55 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:02:51 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.148 |  |
| 2025-12-17 18:02:45 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:02:26 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.030 |  |
| 2025-12-17 18:02:23 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-17 18:02:18 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:02:10 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.020 |  |
| 2025-12-17 18:02:07 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:02:02 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2025-12-17 18:01:56 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.071 |  |
| 2025-12-17 18:01:41 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 18:01:39 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:01:22 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:01:16 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:01:14 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 18:01:02 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-17 18:00:46 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-17 18:00:32 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 18:02:02 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2025-12-17 18:04:16 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 18:00:46 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-17 18:01:02 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-17 18:07:24 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-17 18:01:41 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 18:07:38 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 18:04:01 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-17 18:03:32 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:00:32 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:11:26 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:01:16 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:01:39 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:02:55 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:03:57 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:02:10 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:01:22 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:20:38 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:02:18 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:03:30 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:05:12 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:02:07 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:05:32 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:01:14 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 18:10:21 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2025-12-17 18:08:19 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2025-12-17 18:02:23 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-17 18:04:10 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-17 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.020 |  |
| 2025-12-17 18:03:39 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2025-12-17 18:02:26 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.030 |  |
| 2025-12-17 18:04:00 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.063 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-17 18:01:56 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.071 |  |
| 2025-12-17 18:04:32 | Yaka Wewa (Ma Oya) | 1.66 | 🟢 Normal | -0.077 |  |
| 2025-12-17 17:09:21 | Horowpothana (Yan Oya) | 5.76 | 🟢 Normal | -0.096 |  |
| 2025-12-17 18:02:51 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)