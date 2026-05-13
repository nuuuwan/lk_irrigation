# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_02:17:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,178 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 02:17:11 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-05-14 02:15:41 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.025 |  |
| 2026-05-14 02:09:30 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.083 |  |
| 2026-05-14 02:08:26 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-14 02:07:36 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.134 |  |
| 2026-05-14 02:07:14 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-05-14 02:06:34 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-14 02:06:14 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.103 |  |
| 2026-05-14 02:05:49 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.108 |  |
| 2026-05-14 02:05:38 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-14 02:05:26 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.065 |  |
| 2026-05-14 02:05:21 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | -0.132 |  |
| 2026-05-14 02:04:59 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.340 |  |
| 2026-05-14 02:04:31 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.101 |  |
| 2026-05-14 02:04:02 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.049 |  |
| 2026-05-14 02:03:24 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.198 |  |
| 2026-05-14 02:03:10 | Ellagawa (Kalu Ganga) | 8.26 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-14 02:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.12 | 🟡 Alert | 0.081 | 🔺 Rising |
| 2026-05-14 02:02:46 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-14 02:02:38 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-14 02:02:38 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.030 |  |
| 2026-05-14 02:02:30 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-14 02:02:21 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 02:02:02 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.031 |  |
| 2026-05-14 02:02:01 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 02:01:27 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.056 |  |
| 2026-05-14 02:01:10 | Moraketiya (Walawe Ganga) | 1.81 | 🟢 Normal | -0.042 |  |
| 2026-05-14 02:00:43 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-14 02:00:19 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-05-14 01:33:13 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.340 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 02:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.12 | 🟡 Alert | 0.081 | 🔺 Rising |
| 2026-05-14 02:02:38 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.030 |  |
| 2026-05-14 02:04:31 | Magura (Kalu Ganga) | 4.95 | 🟡 Alert | -0.101 |  |
| 2026-05-14 02:07:36 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.134 |  |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-14 01:07:00 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-14 02:03:10 | Ellagawa (Kalu Ganga) | 8.26 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-14 01:04:17 | Putupaula (Kalu Ganga) | 2.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-14 02:08:26 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-14 02:06:34 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 02:00:43 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-14 02:05:38 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-14 02:02:46 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-14 02:02:21 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 02:02:01 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 01:01:36 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:06:39 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 02:02:30 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-14 02:00:19 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-05-14 02:02:38 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-05-14 01:02:54 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-14 02:07:14 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-05-14 00:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-05-14 02:15:41 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.025 |  |
| 2026-05-14 02:02:02 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.031 |  |
| 2026-05-14 02:17:11 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.040 |  |
| 2026-05-14 02:01:10 | Moraketiya (Walawe Ganga) | 1.81 | 🟢 Normal | -0.042 |  |
| 2026-05-14 02:04:02 | Hanwella (Kelani Ganga) | 2.77 | 🟢 Normal | -0.049 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-14 01:01:35 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | -0.052 |  |
| 2026-05-14 02:01:27 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.056 |  |
| 2026-05-14 02:05:26 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.065 |  |
| 2026-05-14 02:09:30 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.083 |  |
| 2026-05-14 02:06:14 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.103 |  |
| 2026-05-14 02:05:49 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.108 |  |
| 2026-05-14 02:05:21 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | -0.132 |  |
| 2026-05-14 02:03:24 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.198 |  |
| 2026-05-14 02:04:59 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.340 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)