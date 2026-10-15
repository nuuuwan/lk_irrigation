# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_14:34:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,629 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Urawa — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 14:34:05 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 74.483 | 🔺 Rising |
| 2026-10-15 14:33:36 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | 74.483 | 🔺 Rising |
| 2026-10-15 14:14:18 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.068 |  |
| 2026-10-15 14:11:03 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-15 14:09:17 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:08:07 | Thawalama (Gin Ganga) | 3.01 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-15 14:08:06 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-15 14:07:12 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 14:07:12 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 14:06:37 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:06:33 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | -0.019 |  |
| 2026-10-15 14:06:17 | Glencourse (Kelani Ganga) | 11.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 14:06:11 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | -0.091 |  |
| 2026-10-15 14:06:02 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-10-15 14:05:45 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 14:05:28 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-15 14:05:27 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-15 14:05:24 | Moragaswewa (Deduru Oya) | 1.87 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-10-15 14:05:24 | Dunamale (Aththanagalu Oya) | 3.83 | 🟡 Alert | -0.040 |  |
| 2026-10-15 14:04:58 | Rathnapura (Kalu Ganga) | 3.26 | 🟢 Normal | -0.070 |  |
| 2026-10-15 14:04:54 | Hanwella (Kelani Ganga) | 4.38 | 🟢 Normal | -0.090 |  |
| 2026-10-15 14:04:33 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-15 14:04:29 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 14:04:20 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.054 |  |
| 2026-10-15 14:04:09 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | -0.010 |  |
| 2026-10-15 14:03:57 | Urawa (Nilwala Ganga) | 3.08 | 🟡 Alert | 0.304 | 🔺 Rising |
| 2026-10-15 14:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 14:03:08 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-15 14:03:03 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:02:52 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-15 14:02:52 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-15 14:02:40 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 14:02:38 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.063 |  |
| 2026-10-15 14:02:34 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:02:14 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-15 14:02:08 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:01:20 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-10-15 14:01:18 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:00:36 | Pitabeddara (Nilwala Ganga) | 3.32 | 🟢 Normal | 0.586 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 14:05:28 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-15 14:03:57 | Urawa (Nilwala Ganga) | 3.08 | 🟡 Alert | 0.304 | 🔺 Rising |
| 2026-10-15 13:02:43 | Panadugama (Nilwala Ganga) | 5.16 | 🟡 Alert | 0.133 | 🔺 Rising |
| 2026-10-15 14:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | -0.010 |  |
| 2026-10-15 14:05:24 | Dunamale (Aththanagalu Oya) | 3.83 | 🟡 Alert | -0.040 |  |
| 2026-10-15 14:34:05 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 74.483 | 🔺 Rising |
| 2026-10-15 14:00:36 | Pitabeddara (Nilwala Ganga) | 3.32 | 🟢 Normal | 0.586 | 🔺 Rising |
| 2026-10-15 14:05:24 | Moragaswewa (Deduru Oya) | 1.87 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-10-15 14:06:02 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-10-15 14:08:07 | Thawalama (Gin Ganga) | 3.01 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-15 14:02:52 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-15 14:05:27 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-15 14:04:33 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-15 14:02:14 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-15 14:03:08 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-15 14:07:12 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 14:07:12 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 14:11:03 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-15 14:06:17 | Glencourse (Kelani Ganga) | 11.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 14:05:45 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 14:02:40 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 14:03:52 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 14:04:29 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 14:08:06 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-15 14:09:17 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:02:34 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:06:37 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:04:09 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:01:18 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:03:03 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:02:52 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-15 14:06:33 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | -0.019 |  |
| 2026-10-15 14:01:20 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-10-15 14:04:20 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.054 |  |
| 2026-10-15 14:02:38 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.063 |  |
| 2026-10-15 14:14:18 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.068 |  |
| 2026-10-15 14:04:58 | Rathnapura (Kalu Ganga) | 3.26 | 🟢 Normal | -0.070 |  |
| 2026-10-15 14:04:54 | Hanwella (Kelani Ganga) | 4.38 | 🟢 Normal | -0.090 |  |
| 2026-10-15 14:06:11 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)