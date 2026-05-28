# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_09:13:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,793 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 09:13:33 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:11:13 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-28 09:10:45 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-28 09:10:11 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-05-28 09:08:07 | Magura (Kalu Ganga) | 4.59 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-05-28 09:07:56 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:05:46 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:05:39 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:05:38 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.052 |  |
| 2026-05-28 09:05:17 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.085 |  |
| 2026-05-28 09:05:07 | Rathnapura (Kalu Ganga) | 4.13 | 🟢 Normal | -0.091 |  |
| 2026-05-28 09:04:45 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2026-05-28 09:04:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:04:41 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:04:39 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:04:27 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:04:19 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 09:04:08 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:04:05 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.053 |  |
| 2026-05-28 09:03:52 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:03:44 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:03:29 | Hanwella (Kelani Ganga) | 4.36 | 🟢 Normal | -0.072 |  |
| 2026-05-28 09:03:18 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-28 09:03:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-28 09:02:50 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:02:40 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.030 |  |
| 2026-05-28 09:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.07 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 09:01:56 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:01:52 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:01:52 | Deraniyagala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-05-28 09:01:48 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-28 09:01:47 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-05-28 09:01:37 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:01:29 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 09:01:27 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:01:23 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:01:09 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:00:50 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-28 09:00:18 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 09:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.07 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 09:08:07 | Magura (Kalu Ganga) | 4.59 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-05-28 09:11:13 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-28 09:10:45 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-28 09:04:19 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 09:03:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-28 09:01:48 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-28 09:00:50 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-28 09:00:18 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 09:01:29 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 09:03:44 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:03:18 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:01:27 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:01:23 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:05:39 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:04:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:04:41 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:01:52 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:05:46 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:01:09 | Ellagawa (Kalu Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:13:33 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:07:56 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:01:37 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:02:50 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:04:27 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:01:56 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:04:39 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:03:52 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:10:11 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-05-28 09:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-28 09:04:45 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.011 |  |
| 2026-05-28 09:01:47 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-05-28 09:01:52 | Deraniyagala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-05-28 09:02:40 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.030 |  |
| 2026-05-28 09:05:38 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.052 |  |
| 2026-05-28 09:04:05 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.053 |  |
| 2026-05-28 09:03:29 | Hanwella (Kelani Ganga) | 4.36 | 🟢 Normal | -0.072 |  |
| 2026-05-28 09:05:17 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.085 |  |
| 2026-05-28 09:05:07 | Rathnapura (Kalu Ganga) | 4.13 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)