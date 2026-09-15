# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_06:30:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,303 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 06:30:32 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.002 |  |
| 2026-09-15 06:18:38 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:13:27 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-09-15 06:13:26 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-09-15 06:13:25 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-09-15 06:13:04 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-15 06:10:05 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:09:49 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:09:49 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:08:59 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.104 |  |
| 2026-09-15 06:07:01 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.066 |  |
| 2026-09-15 06:06:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.642 | 🔺 Rising |
| 2026-09-15 06:05:52 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.015 |  |
| 2026-09-15 06:05:30 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.042 |  |
| 2026-09-15 06:05:19 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-15 06:05:06 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 06:04:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-15 06:04:43 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.068 |  |
| 2026-09-15 06:04:35 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-09-15 06:04:01 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 06:03:55 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-09-15 06:03:47 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-15 06:03:38 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-15 06:03:37 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-09-15 06:03:33 | Thawalama (Gin Ganga) | 3.62 | 🟢 Normal | -0.265 |  |
| 2026-09-15 06:03:17 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.275 |  |
| 2026-09-15 06:03:16 | Manampitiya (Mahaweli Ganga) | -0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-15 06:02:52 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.303 |  |
| 2026-09-15 06:02:45 | Dunamale (Aththanagalu Oya) | 3.16 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-09-15 06:02:32 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:02:15 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-15 06:02:12 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-15 06:01:55 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.124 |  |
| 2026-09-15 06:01:48 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:01:42 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | 0.091 | 🔺 Rising |
| 2026-09-15 06:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:01:14 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:00:45 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-15 06:00:10 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 06:01:42 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | 0.091 | 🔺 Rising |
| 2026-09-15 06:13:27 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-09-15 06:06:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.642 | 🔺 Rising |
| 2026-09-15 06:02:45 | Dunamale (Aththanagalu Oya) | 3.16 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-09-15 06:03:37 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-09-15 06:04:35 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-09-15 06:03:55 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-09-15 06:03:38 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-15 06:05:19 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-09-15 06:02:15 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-15 06:04:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-15 06:13:04 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-15 06:03:47 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-15 06:04:01 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 06:05:06 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 18:10:49 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 06:30:32 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.002 |  |
| 2026-09-15 06:10:05 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:00:10 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:02:32 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:01:48 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:18:38 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:09:49 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:01:14 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:09:49 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 05:06:35 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-15 06:03:16 | Manampitiya (Mahaweli Ganga) | -0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-15 06:02:12 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-15 06:00:45 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-15 06:05:52 | Horowpothana (Yan Oya) | 2.00 | 🟢 Normal | -0.015 |  |
| 2026-09-15 06:05:30 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.042 |  |
| 2026-09-15 06:07:01 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.066 |  |
| 2026-09-15 06:04:43 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.068 |  |
| 2026-09-15 06:08:59 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.104 |  |
| 2026-09-15 06:01:55 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.124 |  |
| 2026-09-15 06:03:33 | Thawalama (Gin Ganga) | 3.62 | 🟢 Normal | -0.265 |  |
| 2026-09-15 06:03:17 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.275 |  |
| 2026-09-15 06:02:52 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.303 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)