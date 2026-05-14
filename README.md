# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_11:23:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,527 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 11:23:13 | Magura (Kalu Ganga) | 4.22 | 🟡 Alert | -0.017 |  |
| 2026-05-14 11:14:07 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:11:22 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-14 11:10:13 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-05-14 11:09:31 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:09:05 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | -0.013 |  |
| 2026-05-14 11:08:43 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:06:48 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | -0.023 |  |
| 2026-05-14 11:06:31 | Panadugama (Nilwala Ganga) | 4.12 | 🟢 Normal | -0.049 |  |
| 2026-05-14 11:06:27 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-05-14 11:05:49 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:05:35 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | -0.019 |  |
| 2026-05-14 11:05:32 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-14 11:05:13 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:05:09 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:04:57 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-14 11:04:50 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.049 |  |
| 2026-05-14 11:04:30 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | -0.060 |  |
| 2026-05-14 11:04:18 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | -0.019 |  |
| 2026-05-14 11:04:10 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.142 |  |
| 2026-05-14 11:03:58 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | -0.010 |  |
| 2026-05-14 11:03:51 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:03:47 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-14 11:03:36 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | -0.058 |  |
| 2026-05-14 11:03:27 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:03:24 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-14 11:03:04 | Galgamuwa (Mee Oya) | 2.47 | 🟢 Normal | -0.139 |  |
| 2026-05-14 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-14 11:02:17 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-05-14 11:02:09 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-14 11:02:03 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-14 11:01:58 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-05-14 11:01:45 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-05-14 11:01:44 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:01:12 | Thanthirimale (Malwathu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-14 11:00:44 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.005 |  |
| 2026-05-14 11:00:17 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:00:16 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:00:14 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 11:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.38 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-14 11:23:13 | Magura (Kalu Ganga) | 4.22 | 🟡 Alert | -0.017 |  |
| 2026-05-14 11:10:13 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-05-14 11:05:32 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-05-14 11:02:03 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-14 11:03:24 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-14 11:04:57 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-14 11:03:47 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-14 11:11:22 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-14 11:05:13 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:00:16 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:00:14 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:01:44 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:03:51 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:00:17 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:14:07 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:09:31 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:01:12 | Thanthirimale (Malwathu Oya) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:05:49 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:05:09 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:03:27 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-14 11:00:44 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.005 |  |
| 2026-05-14 11:06:27 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-05-14 11:03:58 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | -0.010 |  |
| 2026-05-14 11:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-14 11:02:09 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-14 11:01:58 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-05-14 11:09:05 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | -0.013 |  |
| 2026-05-14 11:05:35 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | -0.019 |  |
| 2026-05-14 11:04:18 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | -0.019 |  |
| 2026-05-14 11:01:45 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-05-14 11:06:48 | Moragaswewa (Deduru Oya) | 1.46 | 🟢 Normal | -0.023 |  |
| 2026-05-14 11:02:17 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-05-14 11:06:31 | Panadugama (Nilwala Ganga) | 4.12 | 🟢 Normal | -0.049 |  |
| 2026-05-14 11:04:50 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.049 |  |
| 2026-05-14 11:03:36 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | -0.058 |  |
| 2026-05-14 11:04:30 | Rathnapura (Kalu Ganga) | 4.09 | 🟢 Normal | -0.060 |  |
| 2026-05-14 11:03:04 | Galgamuwa (Mee Oya) | 2.47 | 🟢 Normal | -0.139 |  |
| 2026-05-14 11:04:10 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)