# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_07:04:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,886 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 07:04:19 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.065 |  |
| 2026-11-09 07:04:16 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.142 |  |
| 2026-11-09 07:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-09 07:03:27 | Dunamale (Aththanagalu Oya) | 4.32 | 🟡 Alert | 0.071 | 🔺 Rising |
| 2026-11-09 07:03:23 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:03:22 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-09 07:03:19 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | -0.058 |  |
| 2026-11-09 07:02:51 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.291 |  |
| 2026-11-09 07:02:47 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:02:41 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-09 07:02:22 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-09 07:02:19 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:02:17 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.032 |  |
| 2026-11-09 07:01:42 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | -0.149 |  |
| 2026-11-09 07:01:42 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-11-09 07:01:36 | Moragaswewa (Deduru Oya) | 2.90 | 🟢 Normal | -0.082 |  |
| 2026-11-09 07:01:35 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.172 |  |
| 2026-11-09 07:01:23 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.120 |  |
| 2026-11-09 07:01:16 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-09 07:01:03 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:01:00 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-11-09 07:00:43 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.022 |  |
| 2026-11-09 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.052 |  |
| 2026-11-09 06:37:51 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 07:03:27 | Dunamale (Aththanagalu Oya) | 4.32 | 🟡 Alert | 0.071 | 🔺 Rising |
| 2026-11-09 07:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.93 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-09 06:01:08 | Magura (Kalu Ganga) | 5.25 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-11-09 06:09:35 | Baddegama (Gin Ganga) | 3.56 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-11-09 07:01:16 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-09 06:03:44 | Panadugama (Nilwala Ganga) | 5.77 | 🟡 Alert | -0.041 |  |
| 2026-11-09 07:02:22 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-09 06:08:24 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:03:23 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:02:19 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:02:47 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:01:03 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-09 06:01:33 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-09 07:03:22 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-09 06:04:22 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-09 06:07:22 | Badalgama (Maha Oya) | 4.63 | 🟢 Normal | -0.010 |  |
| 2026-11-09 07:02:41 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-09 07:01:42 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-11-08 23:07:10 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-11-09 07:01:00 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-11-09 07:00:43 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | -0.022 |  |
| 2026-11-09 07:02:17 | Horowpothana (Yan Oya) | 2.99 | 🟢 Normal | -0.032 |  |
| 2026-11-09 06:04:41 | Ellagawa (Kalu Ganga) | 7.99 | 🟢 Normal | -0.038 |  |
| 2026-11-09 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.052 |  |
| 2026-11-09 06:07:01 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.054 |  |
| 2026-11-09 06:08:06 | Holombuwa (Kelani Ganga) | 1.65 | 🟢 Normal | -0.056 |  |
| 2026-11-09 07:03:19 | Putupaula (Kalu Ganga) | 2.41 | 🟢 Normal | -0.058 |  |
| 2026-11-09 07:04:19 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.065 |  |
| 2026-11-09 06:07:25 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | -0.069 |  |
| 2026-11-09 07:01:36 | Moragaswewa (Deduru Oya) | 2.90 | 🟢 Normal | -0.082 |  |
| 2026-11-09 06:02:02 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.086 |  |
| 2026-11-09 07:01:23 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.120 |  |
| 2026-11-09 07:04:16 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.142 |  |
| 2026-11-09 07:01:42 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | -0.149 |  |
| 2026-11-09 07:01:35 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.172 |  |
| 2026-11-09 06:03:56 | Glencourse (Kelani Ganga) | 12.27 | 🟢 Normal | -0.224 |  |
| 2026-11-09 06:04:20 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.271 |  |
| 2026-11-09 07:02:51 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.291 |  |
| 2026-11-09 06:04:10 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -7.714 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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