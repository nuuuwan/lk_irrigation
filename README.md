# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_03:17:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,531 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 03:17:03 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.024 |  |
| 2026-11-11 03:15:25 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -108.000 |  |
| 2026-11-11 03:15:24 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | -108.000 |  |
| 2026-11-11 03:15:23 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -108.000 |  |
| 2026-11-11 03:15:22 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -108.000 |  |
| 2026-11-11 03:14:43 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.116 |  |
| 2026-11-11 03:11:15 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.007 |  |
| 2026-11-11 03:11:08 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | -0.028 |  |
| 2026-11-11 03:10:13 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | -0.151 |  |
| 2026-11-11 03:10:10 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-11 03:09:24 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.056 |  |
| 2026-11-11 03:08:54 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.045 |  |
| 2026-11-11 03:08:01 | Badalgama (Maha Oya) | 3.50 | 🟢 Normal | 0.365 | 🔺 Rising |
| 2026-11-11 03:06:58 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-11-11 03:06:40 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.031 |  |
| 2026-11-11 03:06:05 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-11 03:05:56 | Hanwella (Kelani Ganga) | 4.94 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-11 03:05:46 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-11-11 03:05:23 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.013 |  |
| 2026-11-11 03:05:11 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-11-11 03:03:47 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.041 |  |
| 2026-11-11 03:03:28 | Glencourse (Kelani Ganga) | 12.98 | 🟢 Normal | -0.197 |  |
| 2026-11-11 03:03:14 | Giriulla (Maha Oya) | 4.16 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-11 03:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 03:02:54 | Thawalama (Gin Ganga) | 3.94 | 🟢 Normal | -0.265 |  |
| 2026-11-11 03:02:50 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.029 |  |
| 2026-11-11 03:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 03:02:48 | Dunamale (Aththanagalu Oya) | 4.33 | 🟡 Alert | -0.023 |  |
| 2026-11-11 03:02:42 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-11 03:02:34 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | -0.025 |  |
| 2026-11-11 03:02:32 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | -0.043 |  |
| 2026-11-11 03:02:27 | Pitabeddara (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-11-11 03:02:27 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 03:02:23 | Horowpothana (Yan Oya) | 2.68 | 🟢 Normal | -0.166 |  |
| 2026-11-11 03:02:21 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-11-11 03:02:13 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-11 03:02:11 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | -0.361 |  |
| 2026-11-11 03:01:27 | Moragaswewa (Deduru Oya) | 3.15 | 🟢 Normal | -0.060 |  |
| 2026-11-11 03:00:16 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.154 | 🔺 Rising |
| 2026-11-11 02:55:08 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.166 |  |
| 2026-11-11 02:54:15 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.166 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 03:00:16 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.154 | 🔺 Rising |
| 2026-11-11 03:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 03:02:42 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-11 03:02:34 | Panadugama (Nilwala Ganga) | 6.08 | 🟠 Minor Flood | -0.025 |  |
| 2026-11-11 03:02:48 | Dunamale (Aththanagalu Oya) | 4.33 | 🟡 Alert | -0.023 |  |
| 2026-11-11 03:11:08 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | -0.028 |  |
| 2026-11-11 03:14:43 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.116 |  |
| 2026-11-11 03:08:01 | Badalgama (Maha Oya) | 3.50 | 🟢 Normal | 0.365 | 🔺 Rising |
| 2026-11-11 03:03:14 | Giriulla (Maha Oya) | 4.16 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-11 03:05:56 | Hanwella (Kelani Ganga) | 4.94 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-11 03:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 03:02:27 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 03:06:05 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-11 03:02:13 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-11 03:02:21 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-11-11 03:10:10 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-11 03:11:15 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.007 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-11 03:05:23 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.013 |  |
| 2026-11-11 03:05:46 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-11-11 03:05:11 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-11-11 03:06:58 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-11-11 03:02:27 | Pitabeddara (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-11-11 03:17:03 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.024 |  |
| 2026-11-11 03:02:50 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.029 |  |
| 2026-11-11 03:06:40 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.031 |  |
| 2026-11-11 03:03:47 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.041 |  |
| 2026-11-11 03:02:32 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | -0.043 |  |
| 2026-11-11 03:08:54 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.045 |  |
| 2026-11-11 03:09:24 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.056 |  |
| 2026-11-11 03:01:27 | Moragaswewa (Deduru Oya) | 3.15 | 🟢 Normal | -0.060 |  |
| 2026-11-11 03:10:13 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | -0.151 |  |
| 2026-11-11 03:02:23 | Horowpothana (Yan Oya) | 2.68 | 🟢 Normal | -0.166 |  |
| 2026-11-11 03:03:28 | Glencourse (Kelani Ganga) | 12.98 | 🟢 Normal | -0.197 |  |
| 2026-11-11 03:02:54 | Thawalama (Gin Ganga) | 3.94 | 🟢 Normal | -0.265 |  |
| 2026-11-11 03:02:11 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | -0.361 |  |
| 2026-11-11 03:15:25 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)