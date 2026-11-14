# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_08:20:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,423 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 08:20:09 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:15:23 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-11-14 08:14:55 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:13:16 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 08:11:29 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:10:00 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.028 |  |
| 2026-11-14 08:09:20 | Baddegama (Gin Ganga) | 3.68 | 🟡 Alert | -0.020 |  |
| 2026-11-14 08:07:47 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:07:06 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:06:50 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:06:41 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.078 |  |
| 2026-11-14 08:06:28 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:06:17 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-14 08:05:38 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | -0.075 |  |
| 2026-11-14 08:05:32 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:05:17 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:05:14 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-14 08:04:59 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:04:49 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:04:47 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-11-14 08:04:39 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -0.031 |  |
| 2026-11-14 08:04:23 | Panadugama (Nilwala Ganga) | 5.58 | 🟡 Alert | -0.050 |  |
| 2026-11-14 08:04:23 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.023 |  |
| 2026-11-14 08:04:09 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.010 |  |
| 2026-11-14 08:04:08 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:03:36 | Hanwella (Kelani Ganga) | 2.97 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:03:35 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 08:02:56 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:02:56 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.005 |  |
| 2026-11-14 08:02:47 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:02:26 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.07 | 🟡 Alert | -0.082 |  |
| 2026-11-14 08:02:14 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:02:14 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.107 |  |
| 2026-11-14 08:02:09 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.044 |  |
| 2026-11-14 08:01:23 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.031 |  |
| 2026-11-14 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:00:27 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:00:19 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 08:13:16 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 08:09:20 | Baddegama (Gin Ganga) | 3.68 | 🟡 Alert | -0.020 |  |
| 2026-11-14 08:04:23 | Panadugama (Nilwala Ganga) | 5.58 | 🟡 Alert | -0.050 |  |
| 2026-11-14 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.07 | 🟡 Alert | -0.082 |  |
| 2026-11-14 08:05:14 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-14 08:06:17 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-14 08:03:35 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 08:00:19 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:02:56 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:06:28 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:02:47 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:11:29 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:05:17 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:04:08 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:05:32 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:04:59 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:04:49 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:06:50 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:20:09 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-14 08:02:56 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.005 |  |
| 2026-11-14 08:15:23 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-11-14 08:04:47 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.009 |  |
| 2026-11-14 08:04:09 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.010 |  |
| 2026-11-14 08:14:55 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:07:47 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:02:14 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:00:27 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:03:36 | Hanwella (Kelani Ganga) | 2.97 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:02:26 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:07:06 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.020 |  |
| 2026-11-14 08:04:23 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | -0.023 |  |
| 2026-11-14 08:10:00 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.028 |  |
| 2026-11-14 08:01:23 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.031 |  |
| 2026-11-14 08:04:39 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -0.031 |  |
| 2026-11-14 08:02:09 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | -0.044 |  |
| 2026-11-14 08:05:38 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | -0.075 |  |
| 2026-11-14 08:06:41 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.078 |  |
| 2026-11-14 08:02:14 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)