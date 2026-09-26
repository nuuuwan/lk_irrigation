# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_06:26:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,230 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 06:26:47 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | -0.074 |  |
| 2026-09-26 06:12:42 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:12:20 | Baddegama (Gin Ganga) | 4.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 06:10:14 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:09:31 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | -0.060 |  |
| 2026-09-26 06:09:16 | Hanwella (Kelani Ganga) | 5.84 | 🟢 Normal | -0.028 |  |
| 2026-09-26 06:06:40 | Pitabeddara (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-26 06:06:26 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-26 06:06:06 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | -0.044 |  |
| 2026-09-26 06:05:49 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-26 06:05:36 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.115 |  |
| 2026-09-26 06:05:01 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.039 |  |
| 2026-09-26 06:04:57 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-09-26 06:04:52 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.000 |  |
| 2026-09-26 06:04:18 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.06 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 06:03:57 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-09-26 06:03:40 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.017 |  |
| 2026-09-26 06:03:05 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.097 |  |
| 2026-09-26 06:02:53 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:02:46 | Glencourse (Kelani Ganga) | 13.55 | 🟢 Normal | -0.111 |  |
| 2026-09-26 06:02:43 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:02:36 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:02:29 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.031 |  |
| 2026-09-26 06:02:27 | Deraniyagala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-09-26 06:02:20 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:02:09 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:01:35 | Magura (Kalu Ganga) | 4.35 | 🟡 Alert | -0.082 |  |
| 2026-09-26 06:01:30 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:01:28 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.061 |  |
| 2026-09-26 06:01:22 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:01:12 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.033 |  |
| 2026-09-26 06:01:11 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-09-26 06:00:55 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 06:00:41 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:00:28 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 06:12:20 | Baddegama (Gin Ganga) | 4.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 06:00:55 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 06:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.06 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 06:06:06 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | -0.044 |  |
| 2026-09-26 06:04:52 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.000 |  |
| 2026-09-26 06:01:35 | Magura (Kalu Ganga) | 4.35 | 🟡 Alert | -0.082 |  |
| 2026-09-26 06:06:40 | Pitabeddara (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-26 06:00:28 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 06:05:49 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-26 06:06:26 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-26 06:01:22 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:00:41 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:12:42 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:02:53 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:02:20 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:02:20 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:02:36 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:04:18 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:02:43 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:10:14 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:01:30 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:02:09 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 06:03:40 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.017 |  |
| 2026-09-26 06:02:27 | Deraniyagala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-09-26 06:03:57 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-09-26 06:01:11 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-09-26 06:09:16 | Hanwella (Kelani Ganga) | 5.84 | 🟢 Normal | -0.028 |  |
| 2026-09-26 06:04:57 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-09-26 06:02:29 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.031 |  |
| 2026-09-26 06:01:12 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.033 |  |
| 2026-09-26 06:05:01 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.039 |  |
| 2026-09-26 06:09:31 | Holombuwa (Kelani Ganga) | 1.06 | 🟢 Normal | -0.060 |  |
| 2026-09-26 06:01:28 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.061 |  |
| 2026-09-26 06:26:47 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | -0.074 |  |
| 2026-09-26 06:03:05 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.097 |  |
| 2026-09-26 06:02:46 | Glencourse (Kelani Ganga) | 13.55 | 🟢 Normal | -0.111 |  |
| 2026-09-26 06:05:36 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)