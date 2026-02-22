# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_17:12:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,159 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 17:12:46 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.185 |  |
| 2026-02-22 17:10:26 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-22 17:09:33 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.078 |  |
| 2026-02-22 17:09:29 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.162 |  |
| 2026-02-22 17:08:53 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:08:46 | Manampitiya (Mahaweli Ganga) | 3.76 | 🟡 Alert | -0.092 |  |
| 2026-02-22 17:08:36 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-22 17:05:46 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.047 |  |
| 2026-02-22 17:05:39 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:05:02 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.041 |  |
| 2026-02-22 17:04:40 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.037 |  |
| 2026-02-22 17:04:40 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.062 |  |
| 2026-02-22 17:04:30 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.142 |  |
| 2026-02-22 17:03:56 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-22 17:03:55 | Putupaula (Kalu Ganga) | 1.68 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-22 17:03:45 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:03:35 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.109 |  |
| 2026-02-22 17:03:34 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-22 17:03:15 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.150 |  |
| 2026-02-22 17:03:12 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-02-22 17:02:52 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-02-22 17:02:43 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.043 |  |
| 2026-02-22 17:02:42 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.167 |  |
| 2026-02-22 17:02:41 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:02:36 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-02-22 17:02:12 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-02-22 17:02:09 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.050 |  |
| 2026-02-22 17:02:07 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-02-22 17:01:58 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:01:51 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-02-22 17:01:47 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-02-22 17:01:42 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-02-22 17:01:16 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.022 |  |
| 2026-02-22 17:00:48 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-22 17:00:21 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.061 |  |
| 2026-02-22 17:00:20 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.040 |  |
| 2026-02-22 17:00:07 | Padiyathalawa (Maduru Oya) | 1.23 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 17:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | -0.022 |  |
| 2026-02-22 17:08:46 | Manampitiya (Mahaweli Ganga) | 3.76 | 🟡 Alert | -0.092 |  |
| 2026-02-22 17:03:55 | Putupaula (Kalu Ganga) | 1.68 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-22 17:03:56 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-22 17:03:34 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-22 17:08:36 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-22 17:10:26 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-22 17:02:52 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:01:58 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:08:53 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:01:16 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:03:45 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:05:39 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:02:41 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 17:03:12 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-02-22 17:00:48 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-22 17:02:07 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-02-22 17:01:51 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-02-22 17:02:12 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-02-22 17:01:47 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-02-22 17:02:36 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-02-22 17:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-02-22 17:01:42 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-02-22 17:04:40 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.037 |  |
| 2026-02-22 17:00:20 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.040 |  |
| 2026-02-22 17:00:07 | Padiyathalawa (Maduru Oya) | 1.23 | 🟢 Normal | -0.041 |  |
| 2026-02-22 17:05:02 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.041 |  |
| 2026-02-22 17:02:43 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | -0.043 |  |
| 2026-02-22 17:05:46 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.047 |  |
| 2026-02-22 17:02:09 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.050 |  |
| 2026-02-22 17:00:21 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.061 |  |
| 2026-02-22 17:04:40 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.062 |  |
| 2026-02-22 17:09:33 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.078 |  |
| 2026-02-22 17:03:35 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.109 |  |
| 2026-02-22 17:04:30 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.142 |  |
| 2026-02-22 17:03:15 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.150 |  |
| 2026-02-22 17:09:29 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.162 |  |
| 2026-02-22 17:02:42 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.167 |  |
| 2026-02-22 17:12:46 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.185 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)