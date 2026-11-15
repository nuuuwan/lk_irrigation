# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_06:13:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,255 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 06:13:02 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:10:33 | Moraketiya (Walawe Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 06:08:11 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-11-15 06:08:07 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | -0.018 |  |
| 2026-11-15 06:06:15 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 8.877 | 🔺 Rising |
| 2026-11-15 06:05:53 | Baddegama (Gin Ganga) | 2.86 | 🟢 Normal | -0.031 |  |
| 2026-11-15 06:05:02 | Yaka Wewa (Ma Oya) | 0.35 | 🟢 Normal | 8.877 | 🔺 Rising |
| 2026-11-15 06:04:55 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 06:04:44 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:04:39 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:04:37 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:04:31 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.013 |  |
| 2026-11-15 06:04:22 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:04:20 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-11-15 06:04:08 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:03:56 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:03:36 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-15 06:03:03 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.011 |  |
| 2026-11-15 06:03:00 | Wellawaya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:03:00 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.021 |  |
| 2026-11-15 06:02:50 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.041 |  |
| 2026-11-15 06:02:45 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:02:44 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:02:39 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:02:38 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-15 06:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.043 |  |
| 2026-11-15 06:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:02:11 | Panadugama (Nilwala Ganga) | 4.89 | 🟢 Normal | -0.032 |  |
| 2026-11-15 06:02:06 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:01:42 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 06:01:40 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:01:33 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-15 06:01:31 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:01:30 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:01:30 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal | -0.057 |  |
| 2026-11-15 06:01:29 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:01:25 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:01:20 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:01:16 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:01:13 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-15 06:00:19 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-15 05:42:41 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-15 05:38:20 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-15 05:34:42 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 06:01:13 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-15 06:06:15 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 8.877 | 🔺 Rising |
| 2026-11-15 06:03:36 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-15 06:02:38 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-15 06:01:33 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-15 06:00:19 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-15 06:01:42 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 06:10:33 | Moraketiya (Walawe Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 06:04:55 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 06:01:20 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:03:56 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:01:31 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:01:25 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:01:40 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:04:39 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:13:02 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:04:22 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-15 06:02:44 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:02:39 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:01:16 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:02:06 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:04:37 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:04:44 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:04:08 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:03:00 | Wellawaya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-11-15 06:03:03 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.011 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-15 06:04:31 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.013 |  |
| 2026-11-15 06:08:07 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | -0.018 |  |
| 2026-11-15 06:04:20 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-11-15 06:03:00 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.021 |  |
| 2026-11-15 06:08:11 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-11-15 06:05:53 | Baddegama (Gin Ganga) | 2.86 | 🟢 Normal | -0.031 |  |
| 2026-11-15 06:02:11 | Panadugama (Nilwala Ganga) | 4.89 | 🟢 Normal | -0.032 |  |
| 2026-11-15 06:02:50 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.041 |  |
| 2026-11-15 06:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.043 |  |
| 2026-11-15 06:01:30 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal | -0.057 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)