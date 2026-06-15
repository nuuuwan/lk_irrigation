# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_11:28:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,984 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 11:28:10 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-06-15 11:18:08 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-06-15 11:13:50 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.038 |  |
| 2026-06-15 11:11:01 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-06-15 11:10:09 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:09:15 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:08:42 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-06-15 11:08:23 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.070 |  |
| 2026-06-15 11:07:19 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-15 11:07:14 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:04:38 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:04:30 | Glencourse (Kelani Ganga) | 11.56 | 🟢 Normal | 0.919 | 🔺 Rising |
| 2026-06-15 11:04:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-15 11:03:29 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:03:26 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-15 11:03:26 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.041 |  |
| 2026-06-15 11:03:20 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-15 11:03:18 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:03:13 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-06-15 11:03:10 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-06-15 11:02:54 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | -0.089 |  |
| 2026-06-15 11:02:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:02:36 | Putupaula (Kalu Ganga) | 1.95 | 🟢 Normal | -0.031 |  |
| 2026-06-15 11:02:34 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.080 |  |
| 2026-06-15 11:02:28 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:02:28 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:02:27 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:02:18 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-06-15 11:02:06 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-06-15 11:01:58 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.020 |  |
| 2026-06-15 11:01:43 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:01:37 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:01:28 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:01:00 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:00:38 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:00:17 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.030 |  |
| 2026-06-15 11:00:08 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 11:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | -0.089 |  |
| 2026-06-15 11:04:30 | Glencourse (Kelani Ganga) | 11.56 | 🟢 Normal | 0.919 | 🔺 Rising |
| 2026-06-15 11:04:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-15 11:07:19 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-15 11:03:20 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-15 11:03:26 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-15 11:01:00 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:02:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:01:28 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:09:15 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:01:37 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:10:09 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:00:38 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:00:08 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:02:54 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:07:14 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:02:28 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-15 11:18:08 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-06-15 11:08:42 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-06-15 11:02:27 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:03:18 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:01:43 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:04:38 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:03:29 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:02:28 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-06-15 11:11:01 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-06-15 10:00:48 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.017 |  |
| 2026-06-15 11:01:58 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.020 |  |
| 2026-06-15 11:03:13 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-06-15 11:02:18 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-06-15 11:03:10 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.021 |  |
| 2026-06-15 11:28:10 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-06-15 11:00:17 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.030 |  |
| 2026-06-15 11:02:06 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-06-15 11:02:36 | Putupaula (Kalu Ganga) | 1.95 | 🟢 Normal | -0.031 |  |
| 2026-06-15 11:13:50 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.038 |  |
| 2026-06-15 11:03:26 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.041 |  |
| 2026-06-15 11:08:23 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.070 |  |
| 2026-06-15 11:02:34 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)