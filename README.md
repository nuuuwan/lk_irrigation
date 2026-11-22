# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_08:07:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,524 measurements** from **39** stations.
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
| 2026-11-22 08:07:37 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-11-22 08:07:31 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.028 |  |
| 2026-11-22 08:07:23 | Weraganthota (Mahaweli Ganga) | -1.01 | 🟢 Normal | 0.915 | 🔺 Rising |
| 2026-11-22 08:07:06 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.039 |  |
| 2026-11-22 08:05:20 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 08:05:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 08:05:00 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-11-22 08:04:54 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-22 08:04:42 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | 0.359 | 🔺 Rising |
| 2026-11-22 08:04:21 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.039 |  |
| 2026-11-22 08:04:21 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:04:21 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-11-22 08:04:03 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 08:04:01 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-22 08:03:45 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-22 08:03:33 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:03:32 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:03:12 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-22 08:02:22 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.022 |  |
| 2026-11-22 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.030 |  |
| 2026-11-22 08:02:11 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 08:02:05 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.053 |  |
| 2026-11-22 08:02:04 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-11-22 08:01:39 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:01:31 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-11-22 08:01:30 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-22 08:01:25 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:01:18 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:01:10 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.058 |  |
| 2026-11-22 08:00:59 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-11-22 08:00:57 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:00:45 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-11-22 08:00:27 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.023 |  |
| 2026-11-22 07:41:53 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-22 07:21:39 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-11-22 07:19:55 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | -0.058 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 08:07:23 | Weraganthota (Mahaweli Ganga) | -1.01 | 🟢 Normal | 0.915 | 🔺 Rising |
| 2026-11-22 08:04:42 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | 0.359 | 🔺 Rising |
| 2026-11-22 08:02:04 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-11-22 08:02:11 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-22 08:04:01 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-22 08:05:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 08:01:30 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-22 08:04:03 | Moraketiya (Walawe Ganga) | 2.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 07:41:53 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-22 08:03:45 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-22 08:05:20 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 08:03:32 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:01:25 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:01:18 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:00:57 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:04:21 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:01:39 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 07:04:22 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:03:33 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-11-22 08:07:37 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-11-22 08:04:54 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-22 08:03:12 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-22 07:10:54 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.012 |  |
| 2026-11-22 08:05:00 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-11-22 08:04:21 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-11-22 08:00:45 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-11-22 08:02:22 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.022 |  |
| 2026-11-22 08:00:27 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.023 |  |
| 2026-11-22 08:07:31 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.028 |  |
| 2026-11-22 08:01:31 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-11-22 08:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.030 |  |
| 2026-11-22 07:21:39 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-11-22 08:04:21 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.039 |  |
| 2026-11-22 08:07:06 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.039 |  |
| 2026-11-22 07:07:19 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.047 |  |
| 2026-11-22 08:00:59 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-11-22 08:02:05 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.053 |  |
| 2026-11-22 08:01:10 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)