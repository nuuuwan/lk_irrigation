# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_20:19:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,467 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 20:19:27 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-20 20:11:15 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-20 20:09:42 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.111 |  |
| 2026-04-20 20:08:34 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-20 20:08:28 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 20:08:12 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-20 20:08:09 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 1.117 | 🔺 Rising |
| 2026-04-20 20:07:04 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-20 20:06:37 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-20 20:06:37 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-20 20:06:19 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-20 20:06:03 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 20:05:38 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:05:36 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 20:05:24 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-20 20:04:51 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.091 |  |
| 2026-04-20 20:04:51 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.158 |  |
| 2026-04-20 20:03:57 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.386 |  |
| 2026-04-20 20:03:47 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-20 20:03:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.121 |  |
| 2026-04-20 20:03:43 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-20 20:03:28 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 20:03:23 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 20:03:04 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:02:55 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-20 20:02:51 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-04-20 20:02:49 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 20:02:42 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-20 20:01:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:01:42 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 20:01:41 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:01:29 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-20 20:01:12 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-20 20:00:52 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:00:32 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 19:58:38 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 20:08:09 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 1.117 | 🔺 Rising |
| 2026-04-20 20:07:04 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-20 20:11:15 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-20 20:02:55 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-20 20:06:37 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-20 20:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-20 20:01:12 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-20 20:05:24 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-20 20:08:34 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-20 20:06:37 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-20 20:06:19 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-04-20 20:19:27 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-20 20:03:47 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-20 20:08:12 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-20 20:06:03 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-20 20:02:49 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 20:01:42 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 20:03:28 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 20:03:43 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-20 20:03:23 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 20:05:36 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 20:08:28 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 20:01:29 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:01:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:05:38 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:01:41 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:03:04 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:00:32 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:00:52 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-20 20:02:42 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-20 20:02:51 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-04-20 20:04:51 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.091 |  |
| 2026-04-20 20:09:42 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.111 |  |
| 2026-04-20 20:03:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.121 |  |
| 2026-04-20 20:04:51 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.158 |  |
| 2026-04-20 20:03:57 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.386 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)