# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_04:12:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,713 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 04:12:13 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-06-15 04:11:04 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-06-15 04:09:04 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.032 |  |
| 2026-06-15 04:08:56 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2026-06-15 04:07:26 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:06:58 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -0.037 |  |
| 2026-06-15 04:06:52 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.019 |  |
| 2026-06-15 04:05:32 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-06-15 04:05:20 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-06-15 04:03:48 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-06-15 04:03:33 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:03:32 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.288 |  |
| 2026-06-15 04:03:19 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.052 |  |
| 2026-06-15 04:03:10 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:03:03 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:02:28 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.031 |  |
| 2026-06-15 04:02:27 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-15 04:02:17 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:02:13 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 04:02:02 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:01:55 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:01:46 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:01:42 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-15 04:01:20 | Ellagawa (Kalu Ganga) | 7.02 | 🟢 Normal | -0.111 |  |
| 2026-06-15 04:01:17 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.140 |  |
| 2026-06-15 04:01:16 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:01:09 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:01:01 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.058 |  |
| 2026-06-15 04:00:59 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 03:56:19 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:50:02 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:41:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -1.500 |  |
| 2026-06-15 03:40:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | -1.500 |  |
| 2026-06-15 03:40:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -1.500 |  |
| 2026-06-15 03:39:51 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.140 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 03:41:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -1.500 |  |
| 2026-06-15 04:02:27 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-15 04:01:42 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-15 04:00:59 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 04:02:13 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 03:03:19 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:01:16 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:01:46 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:02:02 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:01:55 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:03:33 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:00:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:50:02 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:03:48 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:03:03 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:07:26 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:03:10 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:01:09 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:02:17 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-15 04:12:13 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-06-14 18:04:23 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-06-15 04:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-15 04:05:20 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.010 |  |
| 2026-06-15 04:06:52 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.019 |  |
| 2026-06-15 04:11:04 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-06-15 04:05:32 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-06-14 18:03:42 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-15 03:05:01 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | -0.030 |  |
| 2026-06-15 04:02:28 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.031 |  |
| 2026-06-15 04:09:04 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.032 |  |
| 2026-06-15 04:06:58 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -0.037 |  |
| 2026-06-15 04:03:19 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.052 |  |
| 2026-06-15 04:01:01 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.058 |  |
| 2026-06-15 04:08:56 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2026-06-15 03:02:16 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.075 |  |
| 2026-06-15 04:01:20 | Ellagawa (Kalu Ganga) | 7.02 | 🟢 Normal | -0.111 |  |
| 2026-06-15 04:01:17 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.140 |  |
| 2026-06-15 04:03:32 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.288 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)