# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_02:07:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,970 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 02:07:03 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.048 |  |
| 2026-10-17 02:06:53 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-17 02:06:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-17 02:06:07 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.081 |  |
| 2026-10-17 02:05:51 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-10-17 02:05:00 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-17 02:04:57 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-10-17 02:04:45 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-17 02:04:37 | Putupaula (Kalu Ganga) | 1.24 | 🟢 Normal | -1.040 |  |
| 2026-10-17 02:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.050 |  |
| 2026-10-17 02:04:12 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.028 |  |
| 2026-10-17 02:04:08 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-17 02:04:07 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-17 02:04:01 | Rathnapura (Kalu Ganga) | 4.16 | 🟢 Normal | -0.505 |  |
| 2026-10-17 02:03:58 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.109 |  |
| 2026-10-17 02:03:48 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-17 02:03:05 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-17 02:03:03 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-17 02:02:27 | Moragaswewa (Deduru Oya) | 1.85 | 🟢 Normal | -0.050 |  |
| 2026-10-17 02:02:15 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.031 |  |
| 2026-10-17 02:02:10 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.749 | 🔺 Rising |
| 2026-10-17 02:02:09 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-17 02:02:09 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | 1.172 | 🔺 Rising |
| 2026-10-17 02:01:54 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-10-17 02:01:48 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.037 |  |
| 2026-10-17 02:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.010 |  |
| 2026-10-17 02:01:43 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-17 02:01:35 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-17 02:00:53 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-10-17 01:56:53 | Rathnapura (Kalu Ganga) | 4.22 | 🟢 Normal | -0.505 |  |
| 2026-10-17 01:38:57 | Yaka Wewa (Ma Oya) | 0.29 | 🟢 Normal | 0.749 | 🔺 Rising |
| 2026-10-17 01:33:59 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 1.172 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 02:05:00 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-17 01:06:38 | Panadugama (Nilwala Ganga) | 6.33 | 🟠 Minor Flood | -0.024 |  |
| 2026-10-17 02:04:07 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-17 02:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.010 |  |
| 2026-10-17 02:02:09 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | 1.172 | 🔺 Rising |
| 2026-10-17 02:02:10 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.749 | 🔺 Rising |
| 2026-10-17 02:02:09 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-17 02:06:07 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-17 02:01:43 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-17 01:01:57 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-17 02:03:05 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-17 02:03:03 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-17 02:03:48 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-17 02:04:45 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-17 02:06:53 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-17 01:13:06 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-17 01:01:08 | Ellagawa (Kalu Ganga) | 7.39 | 🟢 Normal | 0.000 |  |
| 2026-10-17 02:04:08 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-17 00:03:32 | Urawa (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-17 02:01:35 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-17 02:04:57 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-10-17 02:00:53 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-10-17 02:01:54 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-10-17 02:05:51 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.019 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-17 02:04:12 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.028 |  |
| 2026-10-17 02:02:15 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.031 |  |
| 2026-10-17 02:01:48 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.037 |  |
| 2026-10-17 00:09:16 | Pitabeddara (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.044 |  |
| 2026-10-17 02:07:03 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.048 |  |
| 2026-10-17 02:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.050 |  |
| 2026-10-17 02:02:27 | Moragaswewa (Deduru Oya) | 1.85 | 🟢 Normal | -0.050 |  |
| 2026-10-17 01:05:49 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | -0.060 |  |
| 2026-10-17 02:06:07 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.081 |  |
| 2026-10-17 02:03:58 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.109 |  |
| 2026-10-17 02:04:01 | Rathnapura (Kalu Ganga) | 4.16 | 🟢 Normal | -0.505 |  |
| 2026-10-17 02:04:37 | Putupaula (Kalu Ganga) | 1.24 | 🟢 Normal | -1.040 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)