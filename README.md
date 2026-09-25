# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_15:07:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,677 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 15:07:20 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.028 |  |
| 2026-09-25 15:07:05 | Glencourse (Kelani Ganga) | 13.83 | 🟢 Normal | -0.131 |  |
| 2026-09-25 15:07:01 | Rathnapura (Kalu Ganga) | 6.10 | 🟡 Alert | -0.090 |  |
| 2026-09-25 15:06:48 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.038 |  |
| 2026-09-25 15:06:33 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 15:06:33 | Hanwella (Kelani Ganga) | 6.14 | 🟢 Normal | -0.037 |  |
| 2026-09-25 15:06:26 | Pitabeddara (Nilwala Ganga) | 2.46 | 🟢 Normal | 6.372 | 🔺 Rising |
| 2026-09-25 15:05:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:05:28 | Thawalama (Gin Ganga) | 3.74 | 🟢 Normal | -0.183 |  |
| 2026-09-25 15:05:25 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.040 |  |
| 2026-09-25 15:05:21 | Baddegama (Gin Ganga) | 4.72 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 15:05:19 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-09-25 15:04:33 | Pitabeddara (Nilwala Ganga) | 2.26 | 🟢 Normal | 6.372 | 🔺 Rising |
| 2026-09-25 15:04:33 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-25 15:04:33 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 0.000 |  |
| 2026-09-25 15:04:30 | Ellagawa (Kalu Ganga) | 8.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-25 15:04:23 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.042 |  |
| 2026-09-25 15:04:22 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:04:17 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:03:24 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-25 15:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 15:03:11 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:03:01 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.039 |  |
| 2026-09-25 15:02:44 | Putupaula (Kalu Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:02:33 | Nawalapitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.066 |  |
| 2026-09-25 15:02:26 | Panadugama (Nilwala Ganga) | 6.44 | 🟠 Minor Flood | -0.022 |  |
| 2026-09-25 15:02:21 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:02:16 | Deraniyagala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-09-25 15:02:13 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-09-25 15:01:48 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-25 15:01:40 | Nagalagam Street (Kelani Ganga) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-09-25 15:01:38 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:01:32 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:01:31 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | -18.000 |  |
| 2026-09-25 15:01:29 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | -18.000 |  |
| 2026-09-25 15:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:01:19 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:01:09 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | -0.033 |  |
| 2026-09-25 15:00:49 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:00:21 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:27:07 | Pitabeddara (Nilwala Ganga) | 2.47 | 🟢 Normal | 6.372 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 15:05:21 | Baddegama (Gin Ganga) | 4.72 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 15:06:33 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 15:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 15:02:26 | Panadugama (Nilwala Ganga) | 6.44 | 🟠 Minor Flood | -0.022 |  |
| 2026-09-25 15:04:33 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 0.000 |  |
| 2026-09-25 15:07:01 | Rathnapura (Kalu Ganga) | 6.10 | 🟡 Alert | -0.090 |  |
| 2026-09-25 15:06:26 | Pitabeddara (Nilwala Ganga) | 2.46 | 🟢 Normal | 6.372 | 🔺 Rising |
| 2026-09-25 15:05:19 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-09-25 15:02:13 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-09-25 15:01:48 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-25 15:04:33 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-25 15:04:30 | Ellagawa (Kalu Ganga) | 8.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-25 15:00:21 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:04:22 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:01:19 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:00:49 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:05:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:04:17 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:01:32 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:03:44 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:02:44 | Putupaula (Kalu Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:01:38 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:03:11 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:02:21 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 15:02:16 | Deraniyagala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-09-25 15:03:24 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-09-25 15:07:20 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.028 |  |
| 2026-09-25 15:01:40 | Nagalagam Street (Kelani Ganga) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-09-25 15:01:09 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | -0.033 |  |
| 2026-09-25 15:06:33 | Hanwella (Kelani Ganga) | 6.14 | 🟢 Normal | -0.037 |  |
| 2026-09-25 15:06:48 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.038 |  |
| 2026-09-25 15:03:01 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.039 |  |
| 2026-09-25 15:05:25 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.040 |  |
| 2026-09-25 15:04:23 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.042 |  |
| 2026-09-25 15:02:33 | Nawalapitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.066 |  |
| 2026-09-25 15:07:05 | Glencourse (Kelani Ganga) | 13.83 | 🟢 Normal | -0.131 |  |
| 2026-09-25 15:05:28 | Thawalama (Gin Ganga) | 3.74 | 🟢 Normal | -0.183 |  |
| 2026-09-25 15:01:31 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)