# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_22:14:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,551 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 22:14:45 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-11-26 22:11:31 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-26 22:09:25 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.100 |  |
| 2026-11-26 22:09:06 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 22:08:36 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.018 |  |
| 2026-11-26 22:07:57 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | -0.052 |  |
| 2026-11-26 22:07:23 | Padiyathalawa (Maduru Oya) | 2.70 | 🟢 Normal | -0.991 |  |
| 2026-11-26 22:07:14 | Holombuwa (Kelani Ganga) | 2.75 | 🟢 Normal | -0.284 |  |
| 2026-11-26 22:07:11 | Giriulla (Maha Oya) | 4.10 | 🟢 Normal | 0.451 | 🔺 Rising |
| 2026-11-26 22:07:09 | Rathnapura (Kalu Ganga) | 3.59 | 🟢 Normal | -0.042 |  |
| 2026-11-26 22:07:07 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.049 |  |
| 2026-11-26 22:06:45 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-11-26 22:06:02 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-26 22:05:18 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-26 22:05:16 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.087 |  |
| 2026-11-26 22:04:46 | Moragaswewa (Deduru Oya) | 4.66 | 🟢 Normal | -0.020 |  |
| 2026-11-26 22:04:35 | Thanamalwila (Kirindi Oya) | 3.52 | 🟢 Normal | 1.134 | 🔺 Rising |
| 2026-11-26 22:04:04 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-26 22:03:58 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-26 22:03:42 | Moraketiya (Walawe Ganga) | 4.27 | 🟡 Alert | -0.197 |  |
| 2026-11-26 22:03:22 | Panadugama (Nilwala Ganga) | 3.88 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-26 22:03:13 | Kuda Oya (Kirindi Oya) | 3.92 | 🟢 Normal | -0.182 |  |
| 2026-11-26 22:02:53 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-26 22:02:47 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-26 22:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-11-26 22:02:43 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.118 |  |
| 2026-11-26 22:02:42 | Siyambalanduwa (Heda Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-11-26 22:02:34 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-26 22:02:15 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-26 22:01:44 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | 0.079 | 🔺 Rising |
| 2026-11-26 22:01:25 | Nakkala (Kumbukkan Oya) | 2.26 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-11-26 22:01:23 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.040 |  |
| 2026-11-26 22:01:12 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-26 22:01:02 | Wellawaya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 20:03:05 | Magura (Kalu Ganga) | 4.55 | 🟡 Alert | 0.271 | 🔺 Rising |
| 2026-11-26 22:01:44 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | 0.079 | 🔺 Rising |
| 2026-11-26 22:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-11-26 22:03:42 | Moraketiya (Walawe Ganga) | 4.27 | 🟡 Alert | -0.197 |  |
| 2026-11-26 22:04:35 | Thanamalwila (Kirindi Oya) | 3.52 | 🟢 Normal | 1.134 | 🔺 Rising |
| 2026-11-26 22:07:11 | Giriulla (Maha Oya) | 4.10 | 🟢 Normal | 0.451 | 🔺 Rising |
| 2026-11-26 22:06:45 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-11-26 22:03:22 | Panadugama (Nilwala Ganga) | 3.88 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-26 22:01:25 | Nakkala (Kumbukkan Oya) | 2.26 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-11-26 22:06:02 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-26 22:02:47 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-26 22:05:18 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-26 22:02:15 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-26 21:02:03 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 22:02:53 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-26 22:09:06 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 22:01:12 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-26 22:03:58 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-26 22:04:04 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 22:11:31 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-26 22:08:36 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.018 |  |
| 2026-11-26 22:04:46 | Moragaswewa (Deduru Oya) | 4.66 | 🟢 Normal | -0.020 |  |
| 2026-11-26 22:01:02 | Wellawaya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-11-26 22:02:34 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-26 22:14:45 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-11-26 22:02:42 | Siyambalanduwa (Heda Oya) | 1.65 | 🟢 Normal | -0.030 |  |
| 2026-11-26 22:01:23 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.040 |  |
| 2026-11-26 22:07:09 | Rathnapura (Kalu Ganga) | 3.59 | 🟢 Normal | -0.042 |  |
| 2026-11-26 22:07:07 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.049 |  |
| 2026-11-26 22:07:57 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | -0.052 |  |
| 2026-11-26 22:05:16 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.087 |  |
| 2026-11-26 22:09:25 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.100 |  |
| 2026-11-26 22:02:43 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.118 |  |
| 2026-11-26 22:03:13 | Kuda Oya (Kirindi Oya) | 3.92 | 🟢 Normal | -0.182 |  |
| 2026-11-26 22:07:14 | Holombuwa (Kelani Ganga) | 2.75 | 🟢 Normal | -0.284 |  |
| 2026-11-26 22:07:23 | Padiyathalawa (Maduru Oya) | 2.70 | 🟢 Normal | -0.991 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)