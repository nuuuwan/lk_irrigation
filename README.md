# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_03:50:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,682 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 03:50:02 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:41:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -1.500 |  |
| 2026-06-15 03:40:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | -1.500 |  |
| 2026-06-15 03:40:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -1.500 |  |
| 2026-06-15 03:39:51 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.031 |  |
| 2026-06-15 03:19:28 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.026 |  |
| 2026-06-15 03:18:04 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | -0.017 |  |
| 2026-06-15 03:13:18 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.018 |  |
| 2026-06-15 03:11:58 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:08:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.172 |  |
| 2026-06-15 03:08:19 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.009 |  |
| 2026-06-15 03:06:09 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:05:35 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-06-15 03:05:16 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.148 |  |
| 2026-06-15 03:05:01 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | -0.030 |  |
| 2026-06-15 03:04:34 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.020 |  |
| 2026-06-15 03:04:14 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.031 |  |
| 2026-06-15 03:04:12 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-15 03:04:12 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.021 |  |
| 2026-06-15 03:03:57 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-06-15 03:03:41 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-15 03:03:35 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-15 03:03:32 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:03:19 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:03:16 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:03:12 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-06-15 03:02:50 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-06-15 03:02:25 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.040 |  |
| 2026-06-15 03:02:24 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-15 03:02:16 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.075 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 03:41:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -1.500 |  |
| 2026-06-15 03:03:57 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-06-15 03:03:19 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:01:09 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:11:58 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:03:20 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:03:32 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:00:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:06:09 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:50:02 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:03:16 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:01:18 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-15 03:08:19 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.009 |  |
| 2026-06-14 18:04:23 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-06-15 03:03:41 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-15 03:04:12 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-15 03:02:50 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-06-15 03:00:19 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-15 03:02:24 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-15 03:03:35 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-15 03:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.015 |  |
| 2026-06-15 03:18:04 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | -0.017 |  |
| 2026-06-15 03:13:18 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.018 |  |
| 2026-06-15 03:05:35 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-06-15 03:03:12 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-06-14 18:03:42 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-15 03:04:34 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.020 |  |
| 2026-06-15 03:04:12 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.021 |  |
| 2026-06-15 03:19:28 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.026 |  |
| 2026-06-15 03:05:01 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | -0.030 |  |
| 2026-06-15 03:39:51 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.031 |  |
| 2026-06-15 03:04:14 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.031 |  |
| 2026-06-15 03:02:25 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.040 |  |
| 2026-06-15 03:02:16 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.075 |  |
| 2026-06-15 03:01:42 | Ellagawa (Kalu Ganga) | 7.13 | 🟢 Normal | -0.120 |  |
| 2026-06-15 03:05:16 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.148 |  |
| 2026-06-15 03:08:44 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.172 |  |
| 2026-06-15 02:14:54 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)