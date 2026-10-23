# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_06:33:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,533 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 06:33:57 | Galgamuwa (Mee Oya) | 2.63 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-23 06:14:34 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.017 |  |
| 2026-10-23 06:09:40 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:08:40 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.090 |  |
| 2026-10-23 06:08:40 | Hanwella (Kelani Ganga) | 4.45 | 🟢 Normal | -0.047 |  |
| 2026-10-23 06:08:22 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:06:26 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:06:12 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-23 06:05:39 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-23 06:05:38 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-23 06:05:09 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | -0.086 |  |
| 2026-10-23 06:04:57 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.144 |  |
| 2026-10-23 06:04:51 | Glencourse (Kelani Ganga) | 11.88 | 🟢 Normal | -0.088 |  |
| 2026-10-23 06:04:33 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:04:28 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:04:18 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | 0.062 | 🔺 Rising |
| 2026-10-23 06:04:07 | Moragaswewa (Deduru Oya) | 4.93 | 🟡 Alert | -0.117 |  |
| 2026-10-23 06:03:42 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.034 |  |
| 2026-10-23 06:03:38 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-23 06:03:37 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.013 |  |
| 2026-10-23 06:03:33 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-23 06:03:15 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | -0.052 |  |
| 2026-10-23 06:03:15 | Rathnapura (Kalu Ganga) | 4.21 | 🟢 Normal | -0.078 |  |
| 2026-10-23 06:03:14 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-10-23 06:03:00 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 06:02:48 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:02:39 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2026-10-23 06:02:39 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.048 |  |
| 2026-10-23 06:02:34 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:02:23 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 06:02:21 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.085 |  |
| 2026-10-23 06:01:57 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.056 |  |
| 2026-10-23 06:01:50 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:01:42 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | -0.022 |  |
| 2026-10-23 06:01:32 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:01:28 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-10-23 06:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 06:01:19 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-23 06:01:12 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 06:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | 0.062 | 🔺 Rising |
| 2026-10-23 06:04:07 | Moragaswewa (Deduru Oya) | 4.93 | 🟡 Alert | -0.117 |  |
| 2026-10-23 06:03:38 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-23 06:05:39 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-23 06:33:57 | Galgamuwa (Mee Oya) | 2.63 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 06:03:00 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 06:02:23 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 06:05:38 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-23 06:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 06:08:22 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:04:33 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:06:26 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:02:34 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:04:18 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:01:32 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:09:40 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:01:50 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:06:12 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-23 06:03:33 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-23 06:01:19 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-23 06:03:37 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.013 |  |
| 2026-10-23 06:14:34 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.017 |  |
| 2026-10-23 06:01:12 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-10-23 06:01:42 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | -0.022 |  |
| 2026-10-23 06:02:39 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2026-10-23 06:03:42 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.034 |  |
| 2026-10-23 06:03:14 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-10-23 06:08:40 | Hanwella (Kelani Ganga) | 4.45 | 🟢 Normal | -0.047 |  |
| 2026-10-23 06:02:39 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.048 |  |
| 2026-10-23 06:03:15 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | -0.052 |  |
| 2026-10-23 06:01:57 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.056 |  |
| 2026-10-23 06:01:28 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.056 |  |
| 2026-10-23 06:03:15 | Rathnapura (Kalu Ganga) | 4.21 | 🟢 Normal | -0.078 |  |
| 2026-10-23 06:02:21 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.085 |  |
| 2026-10-23 06:05:09 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | -0.086 |  |
| 2026-10-23 06:04:51 | Glencourse (Kelani Ganga) | 11.88 | 🟢 Normal | -0.088 |  |
| 2026-10-23 06:08:40 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.090 |  |
| 2026-10-23 06:04:57 | Panadugama (Nilwala Ganga) | 4.59 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)