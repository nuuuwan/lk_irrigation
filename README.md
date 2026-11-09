# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_06:09:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,862 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 06:09:35 | Baddegama (Gin Ganga) | 3.56 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-11-09 06:09:17 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.092 |  |
| 2026-11-09 06:08:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-09 06:08:10 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.136 |  |
| 2026-11-09 06:08:06 | Holombuwa (Kelani Ganga) | 1.65 | 🟢 Normal | -0.056 |  |
| 2026-11-09 06:07:25 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | -0.069 |  |
| 2026-11-09 06:07:22 | Badalgama (Maha Oya) | 4.63 | 🟢 Normal | -0.010 |  |
| 2026-11-09 06:07:01 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.054 |  |
| 2026-11-09 06:05:43 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.113 |  |
| 2026-11-09 06:05:40 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | -0.039 |  |
| 2026-11-09 06:05:27 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.118 |  |
| 2026-11-09 06:05:14 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 06:04:41 | Ellagawa (Kalu Ganga) | 7.99 | 🟢 Normal | -0.038 |  |
| 2026-11-09 06:04:39 | Thalgahagoda (Nilwala Ganga) | 1.48 | 🟡 Alert | 0.025 | 🔺 Rising |
| 2026-11-09 06:04:22 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-09 06:04:20 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.271 |  |
| 2026-11-09 06:04:16 | Dunamale (Aththanagalu Oya) | 4.25 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-11-09 06:04:10 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -7.714 |  |
| 2026-11-09 06:03:56 | Glencourse (Kelani Ganga) | 12.27 | 🟢 Normal | -0.224 |  |
| 2026-11-09 06:03:44 | Panadugama (Nilwala Ganga) | 5.77 | 🟡 Alert | -0.041 |  |
| 2026-11-09 06:03:42 | Yaka Wewa (Ma Oya) | 1.14 | 🟢 Normal | -7.714 |  |
| 2026-11-09 06:03:35 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-11-09 06:03:27 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.068 |  |
| 2026-11-09 06:03:14 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.019 |  |
| 2026-11-09 06:03:03 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | -0.347 |  |
| 2026-11-09 06:02:50 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | -0.177 |  |
| 2026-11-09 06:02:35 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-09 06:02:35 | Yaka Wewa (Ma Oya) | 1.14 | 🟢 Normal | -7.714 |  |
| 2026-11-09 06:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.102 |  |
| 2026-11-09 06:02:08 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 06:02:02 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.086 |  |
| 2026-11-09 06:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.89 | 🟡 Alert | 2.700 | 🔺 Rising |
| 2026-11-09 06:01:48 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | -7.714 |  |
| 2026-11-09 06:01:34 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-09 06:01:33 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-09 06:01:26 | Giriulla (Maha Oya) | 3.48 | 🟢 Normal | -0.200 |  |
| 2026-11-09 06:01:26 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-09 06:01:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.86 | 🟡 Alert | 2.700 | 🔺 Rising |
| 2026-11-09 06:01:08 | Magura (Kalu Ganga) | 5.25 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-11-09 06:01:05 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 06:01:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.89 | 🟡 Alert | 2.700 | 🔺 Rising |
| 2026-11-09 06:04:16 | Dunamale (Aththanagalu Oya) | 4.25 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-11-09 06:01:08 | Magura (Kalu Ganga) | 5.25 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-11-09 06:09:35 | Baddegama (Gin Ganga) | 3.56 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-11-09 06:04:39 | Thalgahagoda (Nilwala Ganga) | 1.48 | 🟡 Alert | 0.025 | 🔺 Rising |
| 2026-11-09 06:03:44 | Panadugama (Nilwala Ganga) | 5.77 | 🟡 Alert | -0.041 |  |
| 2026-11-09 06:01:26 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-09 06:01:34 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-09 06:08:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-09 06:05:14 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 06:02:08 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 06:02:35 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-09 06:01:33 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-09 06:04:22 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-09 06:07:22 | Badalgama (Maha Oya) | 4.63 | 🟢 Normal | -0.010 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-08 23:07:10 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-11-09 06:03:35 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-11-09 06:03:14 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | -0.019 |  |
| 2026-11-09 06:01:05 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-11-09 06:04:41 | Ellagawa (Kalu Ganga) | 7.99 | 🟢 Normal | -0.038 |  |
| 2026-11-09 06:05:40 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | -0.039 |  |
| 2026-11-09 06:07:01 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.054 |  |
| 2026-11-09 06:08:06 | Holombuwa (Kelani Ganga) | 1.65 | 🟢 Normal | -0.056 |  |
| 2026-11-09 06:03:27 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.068 |  |
| 2026-11-09 06:07:25 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | -0.069 |  |
| 2026-11-09 06:02:02 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.086 |  |
| 2026-11-09 06:09:17 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.092 |  |
| 2026-11-09 06:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.102 |  |
| 2026-11-09 06:05:43 | Peradeniya (Mahaweli Ganga) | 3.36 | 🟢 Normal | -0.113 |  |
| 2026-11-09 06:05:27 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.118 |  |
| 2026-11-09 06:08:10 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.136 |  |
| 2026-11-09 06:02:50 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | -0.177 |  |
| 2026-11-09 06:01:26 | Giriulla (Maha Oya) | 3.48 | 🟢 Normal | -0.200 |  |
| 2026-11-09 06:03:56 | Glencourse (Kelani Ganga) | 12.27 | 🟢 Normal | -0.224 |  |
| 2026-11-09 06:04:20 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.271 |  |
| 2026-11-09 06:03:03 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | -0.347 |  |
| 2026-11-09 06:04:10 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -7.714 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)