# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_07:17:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,530 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 07:17:30 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | -0.002 |  |
| 2026-10-13 07:13:38 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.078 |  |
| 2026-10-13 07:10:55 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.026 |  |
| 2026-10-13 07:10:40 | Urawa (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.236 |  |
| 2026-10-13 07:10:15 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-13 07:10:07 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.048 |  |
| 2026-10-13 07:09:05 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-13 07:08:51 | Putupaula (Kalu Ganga) | 1.88 | 🟢 Normal | -0.027 |  |
| 2026-10-13 07:08:33 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-13 07:08:31 | Panadugama (Nilwala Ganga) | 6.28 | 🟠 Minor Flood | -0.087 |  |
| 2026-10-13 07:08:28 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-13 07:08:09 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-13 07:07:26 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-10-13 07:07:22 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.037 |  |
| 2026-10-13 07:07:12 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.063 |  |
| 2026-10-13 07:06:39 | Thalgahagoda (Nilwala Ganga) | 1.47 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-10-13 07:06:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-10-13 07:06:10 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-13 07:04:50 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.029 |  |
| 2026-10-13 07:04:46 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.144 |  |
| 2026-10-13 07:04:41 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 07:04:35 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.023 |  |
| 2026-10-13 07:03:34 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.178 |  |
| 2026-10-13 07:03:15 | Hanwella (Kelani Ganga) | 3.66 | 🟢 Normal | -0.039 |  |
| 2026-10-13 07:02:52 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-13 07:02:52 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.061 |  |
| 2026-10-13 07:02:48 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-13 07:02:41 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 07:02:34 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-10-13 07:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-13 07:02:15 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-13 07:02:08 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 07:01:36 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-10-13 07:01:34 | Pitabeddara (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.234 |  |
| 2026-10-13 07:01:16 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-10-13 07:00:51 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-13 07:00:45 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 07:00:41 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-13 07:00:39 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.053 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 07:08:31 | Panadugama (Nilwala Ganga) | 6.28 | 🟠 Minor Flood | -0.087 |  |
| 2026-10-13 07:06:39 | Thalgahagoda (Nilwala Ganga) | 1.47 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-10-13 07:06:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-10-13 07:09:05 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-13 07:00:39 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-13 07:08:09 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-13 07:08:33 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-13 07:10:15 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-13 07:04:41 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 07:02:48 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-13 07:02:41 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 07:00:41 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-13 07:02:08 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 07:00:45 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 07:08:28 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-13 07:02:52 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-13 07:17:30 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | -0.002 |  |
| 2026-10-13 07:07:26 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-10-13 07:06:10 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-13 07:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-10-13 07:02:15 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-13 07:00:51 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-13 07:01:36 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-10-13 07:04:35 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.023 |  |
| 2026-10-13 07:10:55 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.026 |  |
| 2026-10-13 07:08:51 | Putupaula (Kalu Ganga) | 1.88 | 🟢 Normal | -0.027 |  |
| 2026-10-13 07:04:50 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.029 |  |
| 2026-10-13 07:02:34 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-10-13 07:07:22 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.037 |  |
| 2026-10-13 07:03:15 | Hanwella (Kelani Ganga) | 3.66 | 🟢 Normal | -0.039 |  |
| 2026-10-13 07:01:16 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-10-13 07:10:07 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.048 |  |
| 2026-10-13 07:02:52 | Dunamale (Aththanagalu Oya) | 2.50 | 🟢 Normal | -0.061 |  |
| 2026-10-13 07:07:12 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.063 |  |
| 2026-10-13 07:13:38 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.078 |  |
| 2026-10-13 07:04:46 | Rathnapura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.144 |  |
| 2026-10-13 07:03:34 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.178 |  |
| 2026-10-13 07:01:34 | Pitabeddara (Nilwala Ganga) | 2.71 | 🟢 Normal | -0.234 |  |
| 2026-10-13 07:10:40 | Urawa (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.236 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)