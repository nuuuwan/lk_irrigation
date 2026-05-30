# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_22:20:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,070 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 22:20:36 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | -0.016 |  |
| 2026-05-30 22:12:17 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.035 |  |
| 2026-05-30 22:11:08 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:09:34 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:09:23 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-05-30 22:06:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | -0.037 |  |
| 2026-05-30 22:06:57 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-05-30 22:06:14 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-30 22:05:17 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:05:11 | Ellagawa (Kalu Ganga) | 6.85 | 🟢 Normal | -0.106 |  |
| 2026-05-30 22:05:07 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:04:42 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-30 22:04:41 | Putupaula (Kalu Ganga) | 2.42 | 🟢 Normal | -0.021 |  |
| 2026-05-30 22:04:14 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:03:52 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-05-30 22:03:51 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.040 |  |
| 2026-05-30 22:03:51 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 22:03:44 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:03:25 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-30 22:03:23 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-05-30 22:03:08 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:02:41 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:02:33 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 22:02:24 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.060 |  |
| 2026-05-30 22:01:56 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:01:47 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-05-30 22:01:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:01:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:01:28 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:01:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 22:01:07 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:00:59 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-30 22:00:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 22:06:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | -0.037 |  |
| 2026-05-30 22:04:42 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-30 22:03:25 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-30 22:02:33 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 22:01:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 22:03:51 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 22:05:07 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:00:56 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:01:56 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:00:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:00:59 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:02:41 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:03:44 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:01:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:05:17 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:09:34 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:11:08 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:01:07 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:03:08 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:01:38 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-30 21:14:17 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:01:28 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 22:09:23 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-05-30 22:06:14 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-30 22:03:23 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-05-30 22:01:47 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-05-30 22:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-30 22:20:36 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | -0.016 |  |
| 2026-05-30 22:03:52 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-05-30 22:04:41 | Putupaula (Kalu Ganga) | 2.42 | 🟢 Normal | -0.021 |  |
| 2026-05-30 22:06:57 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.029 |  |
| 2026-05-30 22:12:17 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.035 |  |
| 2026-05-30 21:02:25 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.036 |  |
| 2026-05-30 22:03:51 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.040 |  |
| 2026-05-30 22:02:24 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.060 |  |
| 2026-05-30 22:05:11 | Ellagawa (Kalu Ganga) | 6.85 | 🟢 Normal | -0.106 |  |
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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)