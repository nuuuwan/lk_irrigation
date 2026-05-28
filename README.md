# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_05:22:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,632 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 05:22:53 | Rathnapura (Kalu Ganga) | 4.51 | 🟢 Normal | -0.129 |  |
| 2026-05-28 05:17:01 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.109 |  |
| 2026-05-28 05:10:11 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 05:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.60 | 🟡 Alert | 0.014 | 🔺 Rising |
| 2026-05-28 05:05:44 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:05:13 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:04:47 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-05-28 05:04:41 | Glencourse (Kelani Ganga) | 12.18 | 🟢 Normal | -0.118 |  |
| 2026-05-28 05:04:21 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:04:19 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-05-28 05:04:19 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 05:03:57 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 05:03:37 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:03:26 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:03:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:03:10 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:03:06 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:02:49 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-05-28 05:02:17 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-05-28 05:02:01 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 05:01:53 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-28 05:01:49 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | -0.294 |  |
| 2026-05-28 05:01:47 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-05-28 05:01:39 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:01:39 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.048 |  |
| 2026-05-28 05:01:22 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 05:01:18 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-28 05:01:10 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.052 |  |
| 2026-05-28 05:00:50 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 05:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.60 | 🟡 Alert | 0.014 | 🔺 Rising |
| 2026-05-28 04:11:49 | Magura (Kalu Ganga) | 4.73 | 🟡 Alert | -0.040 |  |
| 2026-05-27 18:00:23 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-28 05:01:18 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-28 04:08:39 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-28 05:03:57 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 04:04:13 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 05:10:11 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 05:02:01 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 05:01:22 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 05:04:19 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 05:05:13 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:02:49 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:01:39 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:03:37 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:03:06 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:02:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:03:26 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:03:10 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:04:21 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:00:50 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:05:44 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 04:02:47 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:03:16 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-28 05:01:47 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-05-28 04:15:34 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-05-27 18:05:39 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.009 |  |
| 2026-05-28 05:01:53 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-28 04:25:11 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | -0.014 |  |
| 2026-05-28 05:04:47 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-05-28 05:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-05-28 05:04:19 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-05-28 05:02:17 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.040 |  |
| 2026-05-28 05:01:39 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.048 |  |
| 2026-05-28 05:01:10 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.052 |  |
| 2026-05-28 05:17:01 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.109 |  |
| 2026-05-28 05:04:41 | Glencourse (Kelani Ganga) | 12.18 | 🟢 Normal | -0.118 |  |
| 2026-05-28 05:22:53 | Rathnapura (Kalu Ganga) | 4.51 | 🟢 Normal | -0.129 |  |
| 2026-05-28 05:01:49 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | -0.294 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)