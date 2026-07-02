# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_17:13:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **195,409 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 17:13:31 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-02 17:10:32 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:08:36 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-02 17:06:25 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:05:47 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:05:46 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 17:05:43 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-07-02 17:05:31 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:05:06 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-07-02 17:04:57 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:04:26 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.062 |  |
| 2026-07-02 17:04:20 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:03:25 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 17:03:15 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:03:10 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:03:06 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-07-02 17:03:04 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:02:55 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:02:48 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-07-02 17:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.020 |  |
| 2026-07-02 17:02:31 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.012 |  |
| 2026-07-02 17:01:50 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-07-02 17:01:34 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:33 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:32 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:30 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:17 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.113 |  |
| 2026-07-02 17:01:08 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.010 |  |
| 2026-07-02 17:01:06 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:00:46 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:00:40 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:00:31 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:00:16 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 17:02:48 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-07-02 16:19:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-02 17:13:31 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-02 17:03:25 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 17:05:46 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 17:00:31 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:00:16 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:04:57 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:34 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:30 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:32 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:10:32 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:05:47 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-07-02 16:08:54 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:02:55 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:03:10 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:04:20 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-07-02 16:05:21 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:00:40 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:06:25 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:05:31 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:03:04 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:03:15 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-02 16:01:24 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:33 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:06 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:00:46 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-02 17:01:08 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.010 |  |
| 2026-07-02 17:05:06 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-07-02 17:08:36 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-02 17:01:50 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-07-02 16:02:16 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-07-02 17:02:31 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.012 |  |
| 2026-07-02 17:05:43 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-07-02 17:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.020 |  |
| 2026-07-02 17:03:06 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-07-02 17:04:26 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.062 |  |
| 2026-07-02 17:01:17 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)