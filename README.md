# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_02:52:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,892 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 02:52:08 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-07 02:33:22 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-07 02:32:27 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-07 02:17:18 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | -0.286 |  |
| 2026-05-07 02:14:21 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 576.000 | 🔺 Rising |
| 2026-05-07 02:14:19 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 576.000 | 🔺 Rising |
| 2026-05-07 02:11:22 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:08:33 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-05-07 02:08:31 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-05-07 02:06:32 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 1.548 | 🔺 Rising |
| 2026-05-07 02:06:16 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-05-07 02:06:11 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:05:20 | Siyambalanduwa (Heda Oya) | 2.40 | 🟢 Normal | 67.034 | 🔺 Rising |
| 2026-05-07 02:04:48 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-07 02:04:46 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:03:44 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:03:24 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 67.034 | 🔺 Rising |
| 2026-05-07 02:03:21 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:03:19 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 02:14:21 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 576.000 | 🔺 Rising |
| 2026-05-07 02:05:20 | Siyambalanduwa (Heda Oya) | 2.40 | 🟢 Normal | 67.034 | 🔺 Rising |
| 2026-05-07 02:08:33 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-05-07 02:06:32 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 1.548 | 🔺 Rising |
| 2026-05-07 02:01:35 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.517 | 🔺 Rising |
| 2026-05-06 22:14:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-05-07 02:02:42 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-07 02:01:34 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-07 02:32:27 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-07 02:33:22 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-07 02:52:08 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-07 01:01:19 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-07 02:00:56 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-07 02:00:49 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-07 01:04:41 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-07 02:04:48 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-07 01:01:14 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 22:05:10 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 02:01:05 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-07 01:21:16 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:01:25 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:03:44 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:06:11 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:03:21 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:01:18 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:02:27 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:11:22 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:04:46 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 23:06:16 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-07 01:10:47 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-07 02:02:29 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.005 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-07 02:06:16 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-05-07 02:01:55 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-05-07 02:03:19 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.029 |  |
| 2026-05-07 02:17:18 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | -0.286 |  |
| 2026-05-07 02:01:38 | Peradeniya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -5.774 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)