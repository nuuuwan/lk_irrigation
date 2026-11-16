# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_20:08:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,681 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 20:08:15 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.028 |  |
| 2026-11-16 20:07:32 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | -0.048 |  |
| 2026-11-16 20:07:17 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-16 20:07:03 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 20:06:33 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-16 20:05:39 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-16 20:05:34 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-11-16 20:05:00 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-11-16 20:04:53 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-11-16 20:04:49 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:04:28 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:04:27 | Hanwella (Kelani Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:04:15 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -22.812 |  |
| 2026-11-16 20:03:57 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-16 20:03:49 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:03:33 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:03:31 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 20:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.019 |  |
| 2026-11-16 20:03:10 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:02:49 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:02:45 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:02:34 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | -22.812 |  |
| 2026-11-16 20:02:26 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.168 |  |
| 2026-11-16 20:02:23 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:02:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:01:55 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.031 |  |
| 2026-11-16 20:01:24 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 20:01:20 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:00:25 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:00:13 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 19:31:28 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 20:06:33 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-16 20:05:39 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-16 20:07:03 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 20:01:24 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 20:03:31 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 20:02:49 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:02:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:03:10 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:01:20 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:04:42 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-16 19:04:30 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:03:33 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:04:27 | Hanwella (Kelani Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-11-16 19:01:48 | Padiyathalawa (Maduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:03:49 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:00:13 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:00:25 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:04:28 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:03:57 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:02:45 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:00:40 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:02:23 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:04:49 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 19:31:28 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-16 20:05:34 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | -0.009 |  |
| 2026-11-16 20:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-16 20:07:17 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-16 19:02:32 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-11-16 20:05:00 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-11-16 20:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.019 |  |
| 2026-11-16 20:04:53 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-11-16 19:02:44 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.021 |  |
| 2026-11-16 20:08:15 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.028 |  |
| 2026-11-16 20:01:55 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.031 |  |
| 2026-11-16 19:11:16 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | -0.035 |  |
| 2026-11-16 18:02:17 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | -0.041 |  |
| 2026-11-16 20:07:32 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | -0.048 |  |
| 2026-11-16 20:02:26 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.168 |  |
| 2026-11-16 20:04:15 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -22.812 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)