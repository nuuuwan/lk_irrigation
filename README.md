# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_04:06:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,412 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 04:06:41 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.032 |  |
| 2026-10-03 04:06:15 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-03 04:05:26 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-03 04:05:08 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.030 |  |
| 2026-10-03 04:05:06 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-03 04:04:57 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-03 04:04:12 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-10-03 04:03:46 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 04:03:04 | Hanwella (Kelani Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-03 04:02:39 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-10-03 04:02:34 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-03 04:01:54 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 04:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 04:01:27 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-03 04:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-10-03 04:01:11 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-03 04:00:39 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 01:01:15 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-10-03 03:03:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-03 04:01:27 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-03 04:02:34 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-03 04:05:06 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-03 04:05:26 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-03 01:02:24 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-03 04:06:15 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-03 04:03:46 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 04:01:54 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 04:01:11 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-03 04:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-10-03 04:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:05:36 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:08:06 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-03 04:03:04 | Hanwella (Kelani Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:01:11 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:04:54 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:02:56 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:10:37 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:06:13 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:01:54 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:08:45 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:16:34 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-10-03 04:04:57 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-03 03:12:50 | Panadugama (Nilwala Ganga) | 4.70 | 🟢 Normal | -0.014 |  |
| 2026-10-03 03:06:15 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.018 |  |
| 2026-10-03 04:04:12 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-10-03 04:05:08 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.030 |  |
| 2026-10-03 04:00:39 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.030 |  |
| 2026-10-03 04:02:39 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-10-03 04:06:41 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.032 |  |
| 2026-10-03 03:09:16 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.033 |  |
| 2026-10-03 03:15:14 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.054 |  |
| 2026-10-03 03:05:54 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.087 |  |
| 2026-10-03 03:03:01 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.147 |  |
| 2026-10-03 03:04:43 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -16.941 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)