# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_13:22:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,050 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 13:22:20 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-27 13:21:02 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:17:20 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-27 13:15:47 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:13:34 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-05-27 13:11:47 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.053 |  |
| 2026-05-27 13:08:51 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:08:39 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-05-27 13:07:50 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 13:07:18 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-05-27 13:07:06 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:06:13 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-27 13:05:59 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-27 13:04:09 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-27 13:03:52 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 13:03:40 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:03:36 | Deraniyagala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-27 13:03:23 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:03:11 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 13:03:04 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:03:02 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:02:58 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:02:32 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:02:25 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-27 13:02:14 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:01:50 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:01:49 | Ellagawa (Kalu Ganga) | 8.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 13:01:37 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:01:14 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:00:52 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-05-27 13:00:49 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:00:49 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-27 13:00:44 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.010 |  |
| 2026-05-27 13:00:41 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:00:21 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:00:20 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 13:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-27 13:08:39 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-05-27 13:06:13 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-27 13:03:36 | Deraniyagala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-27 13:22:20 | Rathnapura (Kalu Ganga) | 3.96 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-27 13:05:59 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-27 13:00:49 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-27 13:17:20 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-27 13:01:49 | Ellagawa (Kalu Ganga) | 8.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 13:03:52 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 13:07:50 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 12:05:02 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 13:03:11 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 13:00:20 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:03:23 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:02:32 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:01:37 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:00:41 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:02:58 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:02:25 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:21:02 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:00:21 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:07:06 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:00:49 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:03:04 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:02:14 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:01:50 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:08:51 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:03:02 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:01:14 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:15:47 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:03:40 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-27 13:07:18 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-05-27 13:13:34 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-05-27 13:04:09 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-27 13:00:44 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.010 |  |
| 2026-05-27 13:00:52 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-05-27 13:11:47 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)