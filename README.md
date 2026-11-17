# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_09:11:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,150 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 09:11:45 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:09:52 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:09:44 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.009 |  |
| 2026-11-17 09:09:40 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:08:06 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-11-17 09:07:30 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:07:16 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:07:14 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:06:54 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.009 |  |
| 2026-11-17 09:06:40 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-11-17 09:06:39 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.028 |  |
| 2026-11-17 09:06:08 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.080 |  |
| 2026-11-17 09:06:01 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-11-17 09:05:49 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.019 |  |
| 2026-11-17 09:05:41 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:05:38 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-17 09:05:26 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:05:23 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:05:14 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:04:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | -0.029 |  |
| 2026-11-17 09:04:28 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.061 |  |
| 2026-11-17 09:03:43 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:03:40 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 09:02:21 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-17 09:03:06 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 09:05:38 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-17 09:02:13 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 09:00:12 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-17 08:00:03 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:05:14 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:02:20 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:05:26 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:11:45 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:07:30 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:03:03 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:03:43 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:05:41 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:02:19 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:02:31 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:07:16 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:03:18 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:09:52 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:00:44 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:05:23 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:07:14 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-17 09:09:44 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.009 |  |
| 2026-11-17 09:08:06 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-11-17 09:06:54 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.009 |  |
| 2026-11-17 09:02:40 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-11-17 09:03:01 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | -0.010 |  |
| 2026-11-17 09:06:01 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-11-17 09:03:06 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-11-17 09:05:49 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | -0.019 |  |
| 2026-11-17 09:06:40 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-11-17 09:02:57 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.027 |  |
| 2026-11-17 09:06:39 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.028 |  |
| 2026-11-17 09:04:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | -0.029 |  |
| 2026-11-17 09:00:18 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-11-17 09:03:04 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.041 |  |
| 2026-11-17 09:04:28 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.061 |  |
| 2026-11-17 09:06:08 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)