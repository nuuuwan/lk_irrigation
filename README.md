# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_17:15:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,835 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 17:15:07 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-09-14 17:11:32 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-14 17:10:28 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:09:49 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-14 17:09:33 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:08:54 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-09-14 17:06:45 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:06:42 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-09-14 17:06:39 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.042 |  |
| 2026-09-14 17:06:22 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:06:16 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.010 |  |
| 2026-09-14 17:06:15 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | -0.021 |  |
| 2026-09-14 17:05:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-14 17:05:41 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-09-14 17:05:32 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:05:22 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:05:01 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:04:29 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:04:26 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:04:14 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:04:04 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-09-14 17:03:56 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:03:48 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-14 17:03:37 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:03:03 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-09-14 17:02:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-09-14 17:02:53 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:02:24 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:02:19 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:02:19 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:01:57 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-14 17:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-14 17:01:18 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-09-14 17:01:17 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:01:16 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:01:15 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-14 17:01:15 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:00:44 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 17:08:54 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-09-14 17:03:03 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-09-14 17:04:04 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-09-14 17:06:42 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-09-14 17:01:15 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-14 17:05:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-14 17:03:48 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-14 17:09:49 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-14 17:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-14 17:11:32 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-14 17:01:15 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:03:37 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:04:26 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:01:17 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:04:14 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:05:32 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 17:00:44 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:02:19 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:03:56 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:01:16 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:05:01 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:06:22 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:10:28 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:02:24 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:02:53 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:09:33 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:02:19 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:06:45 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:04:29 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:05:22 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-14 17:15:07 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-09-14 17:01:57 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-14 17:06:16 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.010 |  |
| 2026-09-14 17:01:18 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-09-14 17:05:41 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-09-14 17:06:15 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | -0.021 |  |
| 2026-09-14 17:06:39 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.042 |  |
| 2026-09-14 17:02:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)