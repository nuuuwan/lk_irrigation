# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_11:08:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,229 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 11:08:42 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:08:26 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 11:08:19 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-05-07 11:07:51 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.214 |  |
| 2026-05-07 11:07:37 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 11:07:16 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-05-07 11:07:00 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:06:46 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.048 |  |
| 2026-05-07 11:06:23 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.029 |  |
| 2026-05-07 11:05:44 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-07 11:05:37 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-07 11:05:20 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-07 11:04:17 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-07 11:04:10 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-05-07 11:03:55 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.030 |  |
| 2026-05-07 11:03:28 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:03:18 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.040 |  |
| 2026-05-07 11:03:17 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:03:06 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-07 11:03:02 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-07 11:02:42 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:02:42 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-07 11:02:35 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-07 11:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 11:02:32 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-05-07 11:02:31 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.242 |  |
| 2026-05-07 11:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-07 11:01:53 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:01:42 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-07 11:01:41 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | -0.194 |  |
| 2026-05-07 11:01:14 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:01:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-07 11:01:10 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:01:08 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-07 11:01:07 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:01:00 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:00:36 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:00:13 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 10:59:30 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.000 |  |
| 2026-05-07 10:21:07 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.105 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 11:02:35 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-07 11:01:08 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-07 11:05:37 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-07 11:03:06 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-07 11:04:17 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-07 11:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-07 11:02:42 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-07 11:05:44 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-07 11:03:02 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-07 11:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 11:07:37 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 11:08:26 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 11:05:20 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-07 11:01:07 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:01:10 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:02:42 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 10:02:20 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:03:17 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:01:53 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:07:00 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:03:28 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:00:36 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:01:00 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:08:42 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:00:13 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 11:01:42 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-07 11:01:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-07 11:04:10 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-05-07 11:02:32 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-05-07 11:06:23 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.029 |  |
| 2026-05-07 11:07:16 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-05-07 11:03:55 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.030 |  |
| 2026-05-07 11:08:19 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-05-07 11:03:18 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.040 |  |
| 2026-05-07 10:05:10 | Galgamuwa (Mee Oya) | 1.10 | 🟢 Normal | -0.041 |  |
| 2026-05-07 11:06:46 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.048 |  |
| 2026-05-07 11:01:41 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | -0.194 |  |
| 2026-05-07 11:07:51 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.214 |  |
| 2026-05-07 11:02:31 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.242 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)