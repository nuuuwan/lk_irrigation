# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_03:40:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,386 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 03:40:53 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.980 | 🔺 Rising |
| 2026-05-22 03:30:54 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-22 03:24:00 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:21:54 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:18:25 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-05-22 03:16:46 | Deraniyagala (Kelani Ganga) | 2.43 | 🟢 Normal | 0.856 | 🔺 Rising |
| 2026-05-22 03:14:39 | Badalgama (Maha Oya) | 3.36 | 🟢 Normal | 0.551 | 🔺 Rising |
| 2026-05-22 03:14:18 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:10:58 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-22 03:09:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-22 03:07:14 | Glencourse (Kelani Ganga) | 11.78 | 🟢 Normal | 0.850 | 🔺 Rising |
| 2026-05-22 03:07:04 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | 0.750 | 🔺 Rising |
| 2026-05-22 03:05:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:05:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:05:26 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.070 |  |
| 2026-05-22 03:05:13 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-05-22 03:05:12 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.005 |  |
| 2026-05-22 03:04:47 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 03:40:53 | Rathnapura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.980 | 🔺 Rising |
| 2026-05-22 03:16:46 | Deraniyagala (Kelani Ganga) | 2.43 | 🟢 Normal | 0.856 | 🔺 Rising |
| 2026-05-22 03:07:14 | Glencourse (Kelani Ganga) | 11.78 | 🟢 Normal | 0.850 | 🔺 Rising |
| 2026-05-22 03:07:04 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | 0.750 | 🔺 Rising |
| 2026-05-22 03:14:39 | Badalgama (Maha Oya) | 3.36 | 🟢 Normal | 0.551 | 🔺 Rising |
| 2026-05-22 03:02:38 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-05-22 03:05:13 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-05-22 02:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-05-22 03:09:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-22 03:18:25 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-05-22 01:32:15 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-22 03:03:45 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 03:30:54 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-22 03:10:58 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-21 18:16:06 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-22 02:53:00 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-22 03:03:01 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:21:54 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 02:02:48 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:27 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:24:00 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:04:17 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:05:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:01:53 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:05:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:01:09 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:02:24 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-22 03:03:29 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.003 |  |
| 2026-05-22 03:05:12 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.005 |  |
| 2026-05-22 03:02:33 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-22 03:04:47 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.019 |  |
| 2026-05-22 03:01:38 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-22 03:04:25 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.021 |  |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-22 01:08:11 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.066 |  |
| 2026-05-22 03:05:26 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.070 |  |
| 2026-05-22 03:03:15 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.166 |  |
| 2026-05-22 03:02:13 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | -0.221 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)