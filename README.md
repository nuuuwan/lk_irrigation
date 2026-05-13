# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_01:33:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,149 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 01:33:13 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | 0.748 | 🔺 Rising |
| 2026-05-14 01:23:02 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | -0.037 |  |
| 2026-05-14 01:18:44 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.065 |  |
| 2026-05-14 01:10:46 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:10:00 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:07:39 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.039 |  |
| 2026-05-14 01:07:08 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-05-14 01:07:00 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-14 01:06:21 | Moragaswewa (Deduru Oya) | 2.38 | 🟢 Normal | -0.158 |  |
| 2026-05-14 01:05:04 | Rathnapura (Kalu Ganga) | 5.35 | 🟡 Alert | -0.142 |  |
| 2026-05-14 01:04:55 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-14 01:04:46 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | -0.088 |  |
| 2026-05-14 01:04:44 | Ellagawa (Kalu Ganga) | 8.21 | 🟢 Normal | -0.011 |  |
| 2026-05-14 01:04:40 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 01:04:17 | Putupaula (Kalu Ganga) | 2.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-14 01:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | 0.212 | 🔺 Rising |
| 2026-05-14 01:03:27 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | -0.048 |  |
| 2026-05-14 01:03:18 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-05-14 01:03:04 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | -0.052 |  |
| 2026-05-14 01:02:59 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-14 01:02:54 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-14 01:02:50 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-05-14 01:02:49 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.958 | 🔺 Rising |
| 2026-05-14 01:02:38 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | -0.060 |  |
| 2026-05-14 01:02:30 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:02:25 | Giriulla (Maha Oya) | 2.06 | 🟢 Normal | -0.118 |  |
| 2026-05-14 01:01:36 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:01:35 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | -0.052 |  |
| 2026-05-14 01:01:21 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-05-14 01:01:10 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:00:25 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 01:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | 0.212 | 🔺 Rising |
| 2026-05-14 01:23:02 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | -0.037 |  |
| 2026-05-14 01:02:38 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | -0.060 |  |
| 2026-05-14 01:05:04 | Rathnapura (Kalu Ganga) | 5.35 | 🟡 Alert | -0.142 |  |
| 2026-05-14 01:02:49 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.958 | 🔺 Rising |
| 2026-05-14 01:33:13 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | 0.748 | 🔺 Rising |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-14 01:07:00 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-14 01:00:25 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-14 01:04:17 | Putupaula (Kalu Ganga) | 2.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-14 01:04:40 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 00:00:46 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:01:10 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:01:36 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:02:30 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:06:39 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 00:01:03 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:10:00 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:10:46 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:04:55 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-14 01:07:08 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-05-14 01:02:54 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-14 01:02:59 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-14 01:04:44 | Ellagawa (Kalu Ganga) | 8.21 | 🟢 Normal | -0.011 |  |
| 2026-05-14 00:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-05-14 01:02:50 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-05-14 01:03:18 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-05-14 01:07:39 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.039 |  |
| 2026-05-14 01:01:21 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-05-14 01:03:27 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | -0.048 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-14 01:03:04 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | -0.052 |  |
| 2026-05-14 01:01:35 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | -0.052 |  |
| 2026-05-14 01:18:44 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.065 |  |
| 2026-05-14 01:04:46 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | -0.088 |  |
| 2026-05-14 01:02:25 | Giriulla (Maha Oya) | 2.06 | 🟢 Normal | -0.118 |  |
| 2026-05-14 01:06:21 | Moragaswewa (Deduru Oya) | 2.38 | 🟢 Normal | -0.158 |  |
| 2026-05-14 00:05:43 | Panadugama (Nilwala Ganga) | 4.92 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)