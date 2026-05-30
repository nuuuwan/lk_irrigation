# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_23:28:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,102 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 23:28:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | -0.022 |  |
| 2026-05-30 23:10:26 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:10:19 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:10:10 | Ellagawa (Kalu Ganga) | 6.75 | 🟢 Normal | -0.092 |  |
| 2026-05-30 23:09:06 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-30 23:08:41 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.005 |  |
| 2026-05-30 23:08:26 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | -0.049 |  |
| 2026-05-30 23:07:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-05-30 23:05:14 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | -0.040 |  |
| 2026-05-30 23:04:52 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:04:50 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:04:23 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.041 |  |
| 2026-05-30 23:04:22 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:04:18 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-30 23:04:16 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:03:56 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-05-30 23:03:40 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.019 |  |
| 2026-05-30 23:03:23 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:03:08 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:02:44 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-05-30 23:02:40 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:02:19 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.050 |  |
| 2026-05-30 23:02:03 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 23:01:54 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:01:47 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:01:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:01:42 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:01:26 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-05-30 23:01:25 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-30 23:01:12 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-30 23:00:49 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 23:28:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | -0.022 |  |
| 2026-05-30 23:09:06 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-30 23:00:49 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-30 23:04:18 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-30 23:02:03 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 18:00:56 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:01:56 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:01:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:01:47 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:02:40 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:04:50 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:01:54 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:01:42 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:03:23 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:10:26 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:04:22 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:10:19 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:01:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:03:08 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:04:16 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:01:25 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 23:08:41 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.005 |  |
| 2026-05-30 23:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-30 23:01:12 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-30 23:01:26 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-05-30 23:02:44 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-05-30 23:03:40 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.019 |  |
| 2026-05-30 23:03:56 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-05-30 21:02:25 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.036 |  |
| 2026-05-30 23:07:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-05-30 22:03:51 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.040 |  |
| 2026-05-30 23:05:14 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | -0.040 |  |
| 2026-05-30 23:04:23 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.041 |  |
| 2026-05-30 23:08:26 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | -0.049 |  |
| 2026-05-30 23:02:19 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.050 |  |
| 2026-05-30 23:10:10 | Ellagawa (Kalu Ganga) | 6.75 | 🟢 Normal | -0.092 |  |
| 2026-05-30 18:02:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -30.857 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)