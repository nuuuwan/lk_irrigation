# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_09:10:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,426 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 09:10:19 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.028 |  |
| 2026-10-15 09:10:03 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.044 | 🔺 Rising |
| 2026-10-15 09:09:07 | Dunamale (Aththanagalu Oya) | 3.93 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-10-15 09:07:17 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 09:07:03 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | -0.117 |  |
| 2026-10-15 09:06:13 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 09:05:45 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-10-15 09:05:40 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-15 09:05:20 | Glencourse (Kelani Ganga) | 12.31 | 🟢 Normal | -0.194 |  |
| 2026-10-15 09:05:15 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-15 09:04:54 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.035 |  |
| 2026-10-15 09:04:49 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 09:04:41 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.005 |  |
| 2026-10-15 09:04:21 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 09:04:16 | Putupaula (Kalu Ganga) | 2.32 | 🟢 Normal | -0.039 |  |
| 2026-10-15 09:04:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-10-15 09:03:57 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.059 |  |
| 2026-10-15 09:03:55 | Panadugama (Nilwala Ganga) | 5.01 | 🟡 Alert | -0.021 |  |
| 2026-10-15 09:03:35 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-10-15 09:03:17 | Holombuwa (Kelani Ganga) | 1.70 | 🟢 Normal | -0.044 |  |
| 2026-10-15 09:03:04 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 09:03:04 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-15 09:03:04 | Hanwella (Kelani Ganga) | 4.88 | 🟢 Normal | -0.070 |  |
| 2026-10-15 09:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.00 | 🟡 Alert | -0.010 |  |
| 2026-10-15 09:02:53 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 09:02:53 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.023 |  |
| 2026-10-15 09:02:29 | Giriulla (Maha Oya) | 2.69 | 🟢 Normal | -0.122 |  |
| 2026-10-15 09:02:04 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 09:01:34 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-10-15 09:01:33 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.071 |  |
| 2026-10-15 09:01:31 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-15 09:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-15 09:00:45 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-10-15 09:00:16 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 09:10:03 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.044 | 🔺 Rising |
| 2026-10-15 09:09:07 | Dunamale (Aththanagalu Oya) | 3.93 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-10-15 09:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.00 | 🟡 Alert | -0.010 |  |
| 2026-10-15 09:03:55 | Panadugama (Nilwala Ganga) | 5.01 | 🟡 Alert | -0.021 |  |
| 2026-10-15 08:04:39 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-15 09:05:40 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-15 09:03:04 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-15 08:01:07 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 09:02:04 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 09:02:53 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 09:03:04 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 09:06:13 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 09:04:49 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:09:52 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-15 09:07:17 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 09:01:31 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-15 08:10:10 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-15 09:04:21 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 09:04:41 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.005 |  |
| 2026-10-15 09:03:35 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-10-15 09:05:15 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-15 09:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-15 09:04:13 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-10-15 09:00:45 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-10-15 09:01:34 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-10-15 09:02:53 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.023 |  |
| 2026-10-15 09:10:19 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | -0.028 |  |
| 2026-10-15 09:05:45 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-10-15 08:05:52 | Rathnapura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.033 |  |
| 2026-10-15 09:04:54 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.035 |  |
| 2026-10-15 09:04:16 | Putupaula (Kalu Ganga) | 2.32 | 🟢 Normal | -0.039 |  |
| 2026-10-15 09:00:16 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.040 |  |
| 2026-10-15 09:03:17 | Holombuwa (Kelani Ganga) | 1.70 | 🟢 Normal | -0.044 |  |
| 2026-10-15 09:03:57 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.059 |  |
| 2026-10-15 09:03:04 | Hanwella (Kelani Ganga) | 4.88 | 🟢 Normal | -0.070 |  |
| 2026-10-15 09:01:33 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.071 |  |
| 2026-10-15 09:07:03 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | -0.117 |  |
| 2026-10-15 09:02:29 | Giriulla (Maha Oya) | 2.69 | 🟢 Normal | -0.122 |  |
| 2026-10-15 09:05:20 | Glencourse (Kelani Ganga) | 12.31 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)