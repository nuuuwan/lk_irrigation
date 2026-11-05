# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_09:22:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,375 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 09:22:00 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:20:26 | Urawa (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.070 |  |
| 2026-11-05 09:19:27 | Thanamalwila (Kirindi Oya) | 2.18 | 🟢 Normal | -0.046 |  |
| 2026-11-05 09:10:58 | Moraketiya (Walawe Ganga) | 2.22 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-05 09:09:46 | Kuda Oya (Kirindi Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:09:22 | Kuda Oya (Kirindi Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:08:31 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.094 |  |
| 2026-11-05 09:07:17 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:07:05 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-05 09:06:55 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.066 |  |
| 2026-11-05 09:06:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-05 09:06:12 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.051 |  |
| 2026-11-05 09:05:12 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:05:02 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.012 |  |
| 2026-11-05 09:04:51 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-11-05 09:04:51 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 09:04:46 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:04:24 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-05 09:04:22 | Rathnapura (Kalu Ganga) | 3.79 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-05 09:04:08 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.041 |  |
| 2026-11-05 09:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.000 |  |
| 2026-11-05 09:03:50 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-05 09:03:42 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:03:36 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-05 09:03:34 | Galgamuwa (Mee Oya) | 0.86 | 🟢 Normal | -0.083 |  |
| 2026-11-05 09:03:29 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:03:13 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 09:03:13 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.040 |  |
| 2026-11-05 09:03:07 | Dunamale (Aththanagalu Oya) | 2.89 | 🟢 Normal | -0.049 |  |
| 2026-11-05 09:02:36 | Moragaswewa (Deduru Oya) | 3.63 | 🟢 Normal | -0.043 |  |
| 2026-11-05 09:01:55 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.080 |  |
| 2026-11-05 09:01:31 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-05 09:01:23 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.090 |  |
| 2026-11-05 09:01:10 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-05 09:00:55 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.517 |  |
| 2026-11-05 09:00:22 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-05 08:56:20 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.248 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 09:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | 0.000 |  |
| 2026-11-05 09:01:10 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-05 09:06:22 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-11-05 09:04:22 | Rathnapura (Kalu Ganga) | 3.79 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-05 08:20:42 | Panadugama (Nilwala Ganga) | 4.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-05 09:07:05 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-05 09:04:24 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-05 09:04:51 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 09:10:58 | Moraketiya (Walawe Ganga) | 2.22 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-05 09:00:22 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-05 09:03:13 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 09:22:00 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:05:12 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:04:46 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:07:17 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:03:42 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:03:29 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:01:01 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-05 09:09:46 | Kuda Oya (Kirindi Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 08:15:45 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.005 |  |
| 2026-11-05 09:04:51 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-11-05 09:03:36 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-05 09:03:50 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-05 09:01:31 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-05 09:05:02 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.012 |  |
| 2026-11-05 09:03:13 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.040 |  |
| 2026-11-05 09:04:08 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.041 |  |
| 2026-11-05 09:02:36 | Moragaswewa (Deduru Oya) | 3.63 | 🟢 Normal | -0.043 |  |
| 2026-11-05 09:19:27 | Thanamalwila (Kirindi Oya) | 2.18 | 🟢 Normal | -0.046 |  |
| 2026-11-05 09:03:07 | Dunamale (Aththanagalu Oya) | 2.89 | 🟢 Normal | -0.049 |  |
| 2026-11-05 09:06:12 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.051 |  |
| 2026-11-05 09:06:55 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.066 |  |
| 2026-11-05 09:20:26 | Urawa (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.070 |  |
| 2026-11-05 09:01:55 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.080 |  |
| 2026-11-05 09:03:34 | Galgamuwa (Mee Oya) | 0.86 | 🟢 Normal | -0.083 |  |
| 2026-11-05 09:01:23 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.090 |  |
| 2026-11-05 09:08:31 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.094 |  |
| 2026-11-05 09:00:55 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.517 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)