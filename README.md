# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_07:00:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,819 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 07:00:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:59:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:34:56 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.001 |  |
| 2026-08-25 06:14:57 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:14:56 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:14:55 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:14:53 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:14:52 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:13:48 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 06:06:50 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-08-25 06:02:51 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-08-25 06:03:23 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-08-25 06:04:44 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-25 06:05:32 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-25 06:01:06 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-25 06:03:30 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-25 06:02:34 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 06:03:00 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 06:01:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.004 |  |
| 2026-08-25 06:34:56 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.001 |  |
| 2026-08-25 06:00:15 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:59:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:04:54 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:04:25 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:03:11 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:13:48 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:06:59 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:14:57 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:03:04 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:02:21 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:02:25 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:02:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:02:29 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:06:52 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-25 07:00:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:02:36 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 06:02:22 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-08-24 18:01:27 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-25 06:00:34 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-25 06:09:52 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | -0.019 |  |
| 2026-08-25 06:04:56 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.027 |  |
| 2026-08-25 06:06:01 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-08-25 06:08:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.042 |  |
| 2026-08-25 06:00:17 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.063 |  |
| 2026-08-25 06:00:36 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.078 |  |
| 2026-08-25 06:06:17 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)