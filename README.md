# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_06:16:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 06:16:44 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:15:44 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-30 06:11:36 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-30 06:11:07 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.084 |  |
| 2026-07-30 06:10:04 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:08:31 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-30 06:08:24 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:08:15 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:08:10 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.251 |  |
| 2026-07-30 06:06:43 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.046 |  |
| 2026-07-30 06:06:24 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:06:11 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:05:49 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-30 06:05:25 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:05:25 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-07-30 06:04:40 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-30 06:04:38 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:04:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:04:17 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-30 06:03:37 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:03:33 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.141 |  |
| 2026-07-30 06:03:26 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.205 |  |
| 2026-07-30 06:03:01 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | -0.021 |  |
| 2026-07-30 06:02:34 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.113 |  |
| 2026-07-30 06:02:19 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:02:15 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.046 |  |
| 2026-07-30 06:02:11 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.041 |  |
| 2026-07-30 06:02:04 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.004 |  |
| 2026-07-30 06:01:55 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.102 |  |
| 2026-07-30 06:01:42 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:01:10 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:00:52 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -108.000 |  |
| 2026-07-30 06:00:51 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -108.000 |  |
| 2026-07-30 06:00:26 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:00:11 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:51:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.205 |  |
| 2026-07-30 05:38:15 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.102 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 06:04:40 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-30 06:08:31 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-30 06:05:49 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-30 06:04:17 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-30 06:15:44 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-30 06:11:36 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-30 06:16:44 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:00:26 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:08:24 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:06:24 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:06:11 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:03:37 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:05:25 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:46 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:00:11 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:10:04 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:01:42 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:04:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:01:10 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:01:55 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:02:19 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:03:26 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:04:38 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:08:15 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 06:02:04 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.004 |  |
| 2026-07-29 18:01:01 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-07-30 06:05:25 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-07-30 06:03:01 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | -0.021 |  |
| 2026-07-30 04:12:00 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-07-30 06:02:11 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.041 |  |
| 2026-07-30 06:06:43 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.046 |  |
| 2026-07-30 06:02:15 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.046 |  |
| 2026-07-30 06:11:07 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.084 |  |
| 2026-07-30 06:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.102 |  |
| 2026-07-30 06:02:34 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.113 |  |
| 2026-07-30 06:03:33 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.141 |  |
| 2026-07-30 06:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -0.205 |  |
| 2026-07-30 06:08:10 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.251 |  |
| 2026-07-30 06:00:52 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)