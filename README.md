# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_03:08:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,800 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 03:08:31 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-09 03:08:27 | Holombuwa (Kelani Ganga) | 2.03 | 🟢 Normal | -0.205 |  |
| 2026-10-09 03:07:51 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-09 03:07:40 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-09 03:07:22 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | -0.105 |  |
| 2026-10-09 03:06:55 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 03:06:23 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.018 |  |
| 2026-10-09 03:05:15 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-09 03:04:42 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-10-09 03:04:42 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-09 03:04:30 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 03:04:10 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-09 03:04:03 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.199 |  |
| 2026-10-09 03:03:51 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -18.621 |  |
| 2026-10-09 03:03:49 | Badalgama (Maha Oya) | 4.59 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-10-09 03:03:48 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-09 03:03:37 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-09 03:03:22 | Thawalama (Gin Ganga) | 3.65 | 🟢 Normal | -18.621 |  |
| 2026-10-09 03:03:20 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-09 03:03:16 | Glencourse (Kelani Ganga) | 12.60 | 🟢 Normal | -0.080 |  |
| 2026-10-09 03:03:14 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-09 03:03:07 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-09 03:03:06 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.013 |  |
| 2026-10-09 03:02:58 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-09 03:02:49 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-09 03:02:42 | Moragaswewa (Deduru Oya) | 1.65 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-10-09 03:02:33 | Giriulla (Maha Oya) | 4.57 | 🟢 Normal | -0.129 |  |
| 2026-10-09 03:02:10 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-09 03:02:09 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | -0.040 |  |
| 2026-10-09 03:01:59 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-09 03:01:55 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.049 |  |
| 2026-10-09 03:01:52 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-09 03:01:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 02:38:03 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-09 02:37:59 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-09 02:32:21 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 03:02:42 | Moragaswewa (Deduru Oya) | 1.65 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-10-09 03:03:49 | Badalgama (Maha Oya) | 4.59 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-10-09 03:03:07 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-10-09 03:04:10 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-09 03:03:20 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-09 03:03:48 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-09 03:07:51 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-09 03:02:10 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-09 02:02:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-09 03:05:15 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-09 03:04:42 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-09 03:01:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 03:03:37 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-09 03:07:40 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-09 03:04:30 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-09 02:02:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-09 03:01:59 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-09 03:06:55 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 01:06:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-09 03:03:14 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-09 03:08:31 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-09 03:02:49 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-09 03:02:58 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-09 03:03:06 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.013 |  |
| 2026-10-09 03:06:23 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.018 |  |
| 2026-10-09 03:04:42 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-10-09 02:02:58 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.030 |  |
| 2026-10-09 03:01:52 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-09 03:02:09 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | -0.040 |  |
| 2026-10-09 03:01:55 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.049 |  |
| 2026-10-09 03:03:16 | Glencourse (Kelani Ganga) | 12.60 | 🟢 Normal | -0.080 |  |
| 2026-10-09 03:07:22 | Rathnapura (Kalu Ganga) | 3.71 | 🟢 Normal | -0.105 |  |
| 2026-10-09 03:02:33 | Giriulla (Maha Oya) | 4.57 | 🟢 Normal | -0.129 |  |
| 2026-10-09 03:04:03 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | -0.199 |  |
| 2026-10-09 03:08:27 | Holombuwa (Kelani Ganga) | 2.03 | 🟢 Normal | -0.205 |  |
| 2026-10-09 03:03:51 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -18.621 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)