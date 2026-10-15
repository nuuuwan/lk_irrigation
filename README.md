# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_12:18:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,549 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 12:18:06 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.014 |  |
| 2026-10-15 12:12:35 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 12:10:50 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:07:29 | Urawa (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.568 | 🔺 Rising |
| 2026-10-15 12:06:51 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:06:42 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | -0.052 |  |
| 2026-10-15 12:06:19 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-15 12:06:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 12:05:12 | Dunamale (Aththanagalu Oya) | 3.89 | 🟡 Alert | -0.020 |  |
| 2026-10-15 12:05:11 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | 0.296 | 🔺 Rising |
| 2026-10-15 12:05:03 | Hanwella (Kelani Ganga) | 4.59 | 🟢 Normal | -0.087 |  |
| 2026-10-15 12:04:58 | Putupaula (Kalu Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:04:58 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:04:54 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.102 |  |
| 2026-10-15 12:04:46 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 12:04:15 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-15 12:04:00 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:03:58 | Magura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.131 |  |
| 2026-10-15 12:03:53 | Badalgama (Maha Oya) | 3.79 | 🟢 Normal | -0.103 |  |
| 2026-10-15 12:03:48 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.463 | 🔺 Rising |
| 2026-10-15 12:03:44 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:03:33 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:03:20 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.031 |  |
| 2026-10-15 12:03:17 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:03:06 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 12:03:05 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.080 |  |
| 2026-10-15 12:03:02 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.019 |  |
| 2026-10-15 12:02:55 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | -0.143 |  |
| 2026-10-15 12:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -0.021 |  |
| 2026-10-15 12:02:41 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 12:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-10-15 12:02:37 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-15 12:02:34 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.024 |  |
| 2026-10-15 12:02:26 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:02:07 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.059 |  |
| 2026-10-15 12:01:48 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:01:32 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:01:24 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 12:01:10 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 12:12:35 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 12:04:15 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-15 12:05:12 | Dunamale (Aththanagalu Oya) | 3.89 | 🟡 Alert | -0.020 |  |
| 2026-10-15 12:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | -0.021 |  |
| 2026-10-15 12:07:29 | Urawa (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.568 | 🔺 Rising |
| 2026-10-15 12:03:48 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.463 | 🔺 Rising |
| 2026-10-15 12:05:11 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | 0.296 | 🔺 Rising |
| 2026-10-15 12:02:37 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-15 12:06:19 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-15 12:03:06 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 12:04:46 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 12:01:24 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 12:02:41 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 12:06:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 12:01:10 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:01:48 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:02:26 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:10:50 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:06:51 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:04:00 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-15 12:03:44 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:03:17 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:04:58 | Putupaula (Kalu Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:03:33 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:01:32 | Ellagawa (Kalu Ganga) | 8.10 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:04:58 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-15 12:18:06 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.014 |  |
| 2026-10-15 12:03:02 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.019 |  |
| 2026-10-15 12:02:34 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.024 |  |
| 2026-10-15 12:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-10-15 12:03:20 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.031 |  |
| 2026-10-15 12:06:42 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | -0.052 |  |
| 2026-10-15 12:02:07 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.059 |  |
| 2026-10-15 12:03:05 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.080 |  |
| 2026-10-15 12:05:03 | Hanwella (Kelani Ganga) | 4.59 | 🟢 Normal | -0.087 |  |
| 2026-10-15 12:04:54 | Rathnapura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.102 |  |
| 2026-10-15 12:03:53 | Badalgama (Maha Oya) | 3.79 | 🟢 Normal | -0.103 |  |
| 2026-10-15 12:03:58 | Magura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.131 |  |
| 2026-10-15 12:02:55 | Glencourse (Kelani Ganga) | 11.81 | 🟢 Normal | -0.143 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)