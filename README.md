# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_05:16:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,822 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 05:16:53 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.104 |  |
| 2026-11-09 05:16:52 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | 0.000 |  |
| 2026-11-09 05:14:22 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.192 |  |
| 2026-11-09 05:11:59 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 05:08:55 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-11-09 05:08:32 | Magura (Kalu Ganga) | 5.22 | 🟡 Alert | 0.124 | 🔺 Rising |
| 2026-11-09 05:07:05 | Baddegama (Gin Ganga) | 3.53 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-09 05:06:39 | Badalgama (Maha Oya) | 4.64 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-09 05:06:16 | Hanwella (Kelani Ganga) | 5.25 | 🟢 Normal | -0.040 |  |
| 2026-11-09 05:05:55 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | -0.373 |  |
| 2026-11-09 05:05:01 | Panadugama (Nilwala Ganga) | 5.81 | 🟡 Alert | -0.022 |  |
| 2026-11-09 05:04:54 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-09 05:04:44 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 05:04:19 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.074 |  |
| 2026-11-09 05:03:55 | Holombuwa (Kelani Ganga) | 1.71 | 🟢 Normal | -0.077 |  |
| 2026-11-09 05:03:32 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.032 |  |
| 2026-11-09 05:03:24 | Horowpothana (Yan Oya) | 3.06 | 🟢 Normal | -0.029 |  |
| 2026-11-09 05:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.077 |  |
| 2026-11-09 05:03:17 | Dunamale (Aththanagalu Oya) | 4.20 | 🟡 Alert | 0.053 | 🔺 Rising |
| 2026-11-09 05:02:50 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-11-09 05:02:16 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-09 05:02:12 | Glencourse (Kelani Ganga) | 12.50 | 🟢 Normal | -0.251 |  |
| 2026-11-09 05:02:06 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.022 |  |
| 2026-11-09 05:01:57 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.040 |  |
| 2026-11-09 05:01:47 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.099 |  |
| 2026-11-09 05:01:42 | Moragaswewa (Deduru Oya) | 3.16 | 🟢 Normal | -0.080 |  |
| 2026-11-09 05:01:37 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-11-09 05:01:34 | Ellagawa (Kalu Ganga) | 8.03 | 🟢 Normal | -0.030 |  |
| 2026-11-09 05:01:31 | Giriulla (Maha Oya) | 3.68 | 🟢 Normal | -0.194 |  |
| 2026-11-09 05:01:11 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.025 |  |
| 2026-11-09 05:01:08 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 05:08:32 | Magura (Kalu Ganga) | 5.22 | 🟡 Alert | 0.124 | 🔺 Rising |
| 2026-11-09 05:03:17 | Dunamale (Aththanagalu Oya) | 4.20 | 🟡 Alert | 0.053 | 🔺 Rising |
| 2026-11-09 05:07:05 | Baddegama (Gin Ganga) | 3.53 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-09 04:08:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.74 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2026-11-09 04:10:55 | Moraketiya (Walawe Ganga) | 3.06 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-09 05:16:52 | Thalgahagoda (Nilwala Ganga) | 1.46 | 🟡 Alert | 0.000 |  |
| 2026-11-09 05:05:01 | Panadugama (Nilwala Ganga) | 5.81 | 🟡 Alert | -0.022 |  |
| 2026-11-09 05:04:54 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-09 05:06:39 | Badalgama (Maha Oya) | 4.64 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-09 05:02:16 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-09 05:04:44 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 05:11:59 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 05:01:08 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-08 23:07:10 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-11-09 05:02:50 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-09 05:08:55 | Pitabeddara (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.021 |  |
| 2026-11-09 05:02:06 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.022 |  |
| 2026-11-09 05:01:11 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.025 |  |
| 2026-11-09 05:03:24 | Horowpothana (Yan Oya) | 3.06 | 🟢 Normal | -0.029 |  |
| 2026-11-09 05:01:34 | Ellagawa (Kalu Ganga) | 8.03 | 🟢 Normal | -0.030 |  |
| 2026-11-09 05:03:32 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.032 |  |
| 2026-11-09 05:01:37 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-11-09 05:06:16 | Hanwella (Kelani Ganga) | 5.25 | 🟢 Normal | -0.040 |  |
| 2026-11-09 05:01:57 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.040 |  |
| 2026-11-09 05:04:19 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.074 |  |
| 2026-11-09 05:03:55 | Holombuwa (Kelani Ganga) | 1.71 | 🟢 Normal | -0.077 |  |
| 2026-11-09 05:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.077 |  |
| 2026-11-09 05:01:42 | Moragaswewa (Deduru Oya) | 3.16 | 🟢 Normal | -0.080 |  |
| 2026-11-09 05:01:47 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.099 |  |
| 2026-11-09 05:16:53 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.104 |  |
| 2026-11-09 04:04:57 | Urawa (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.137 |  |
| 2026-11-09 05:14:22 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.192 |  |
| 2026-11-09 05:01:31 | Giriulla (Maha Oya) | 3.68 | 🟢 Normal | -0.194 |  |
| 2026-11-09 05:02:12 | Glencourse (Kelani Ganga) | 12.50 | 🟢 Normal | -0.251 |  |
| 2026-11-09 05:05:55 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | -0.373 |  |
| 2026-11-09 03:05:51 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -1.333 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)