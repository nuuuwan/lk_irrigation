# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_06:12:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,211 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 06:12:38 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-11-24 06:08:26 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 06:07:15 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-24 06:07:13 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-24 06:06:14 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.033 |  |
| 2026-11-24 06:06:13 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.035 |  |
| 2026-11-24 06:05:38 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.029 |  |
| 2026-11-24 06:05:38 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-11-24 06:05:29 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-24 06:05:26 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.114 |  |
| 2026-11-24 06:05:17 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.062 |  |
| 2026-11-24 06:04:55 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.060 |  |
| 2026-11-24 06:04:25 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.029 |  |
| 2026-11-24 06:04:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 06:03:51 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | -0.215 |  |
| 2026-11-24 06:03:50 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.110 |  |
| 2026-11-24 06:03:45 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.093 |  |
| 2026-11-24 06:03:41 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-11-24 06:03:40 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-24 06:03:27 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-24 06:03:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.146 |  |
| 2026-11-24 06:03:11 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-24 06:02:43 | Badalgama (Maha Oya) | 4.57 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-24 06:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.177 |  |
| 2026-11-24 06:02:26 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 06:02:05 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.127 |  |
| 2026-11-24 06:01:48 | Giriulla (Maha Oya) | 3.88 | 🟢 Normal | -0.322 |  |
| 2026-11-24 06:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-24 06:01:32 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.091 |  |
| 2026-11-24 06:01:23 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 9.600 | 🔺 Rising |
| 2026-11-24 06:01:21 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-24 06:01:13 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-24 06:01:08 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 9.600 | 🔺 Rising |
| 2026-11-24 06:00:13 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-24 05:49:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.31 | 🟢 Normal | -0.177 |  |
| 2026-11-24 05:49:08 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.035 |  |
| 2026-11-24 05:45:03 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 06:01:23 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 9.600 | 🔺 Rising |
| 2026-11-24 06:02:43 | Badalgama (Maha Oya) | 4.57 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-24 06:07:15 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-24 06:03:40 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-24 06:03:27 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-24 06:01:13 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-11-24 06:05:29 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-24 06:01:21 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-24 06:00:13 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-24 06:07:13 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-24 05:04:43 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-24 06:08:26 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 06:04:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 06:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-24 06:02:26 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-24 06:03:11 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:18:13 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-24 06:03:41 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-11-24 06:05:38 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-11-24 06:12:38 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 06:04:25 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.029 |  |
| 2026-11-24 06:05:38 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.029 |  |
| 2026-11-24 06:06:14 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.033 |  |
| 2026-11-24 06:06:13 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.035 |  |
| 2026-11-24 06:04:55 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.060 |  |
| 2026-11-24 06:05:17 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.062 |  |
| 2026-11-24 05:02:13 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | -0.073 |  |
| 2026-11-24 06:01:32 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.091 |  |
| 2026-11-24 06:03:45 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.093 |  |
| 2026-11-24 06:03:50 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.110 |  |
| 2026-11-24 06:05:26 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.114 |  |
| 2026-11-24 06:02:05 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.127 |  |
| 2026-11-24 06:03:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.146 |  |
| 2026-11-24 06:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.177 |  |
| 2026-11-24 06:03:51 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | -0.215 |  |
| 2026-11-24 06:01:48 | Giriulla (Maha Oya) | 3.88 | 🟢 Normal | -0.322 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)