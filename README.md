# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_01:02:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,244 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 01:02:31 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:02:16 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:01:52 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-03 01:01:48 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:01:44 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:01:20 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-03 01:01:14 | Thaldena (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.120 |  |
| 2026-11-03 01:00:40 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-03 01:00:26 | Wellawaya (Kirindi Oya) | 2.46 | 🟢 Normal | -0.389 |  |
| 2026-11-03 00:39:44 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.007 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 00:05:42 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 1.166 | 🔺 Rising |
| 2026-11-03 00:08:45 | Padiyathalawa (Maduru Oya) | 2.41 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2026-11-03 00:15:17 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-11-03 00:03:17 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-03 01:01:52 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-03 00:06:36 | Peradeniya (Mahaweli Ganga) | 4.35 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 00:00:13 | Horowpothana (Yan Oya) | 3.18 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-03 00:02:46 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 01:01:20 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-03 00:39:44 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-03 00:01:38 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:02:16 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:01:48 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 00:03:16 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-03 00:13:37 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-03 00:13:35 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:02:31 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-03 00:04:36 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:21:44 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:01:44 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-03 00:05:55 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 01:00:40 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-03 00:08:37 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-03 00:06:22 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-11-03 00:02:54 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-11-03 00:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -0.020 |  |
| 2026-11-03 00:03:32 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.021 |  |
| 2026-11-03 00:05:05 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.029 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-03 00:03:19 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.039 |  |
| 2026-11-03 00:06:42 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.039 |  |
| 2026-11-03 00:03:56 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.048 |  |
| 2026-11-03 00:03:44 | Rathnapura (Kalu Ganga) | 4.07 | 🟢 Normal | -0.081 |  |
| 2026-11-03 01:01:14 | Thaldena (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.120 |  |
| 2026-11-03 00:12:38 | Holombuwa (Kelani Ganga) | 2.57 | 🟢 Normal | -0.220 |  |
| 2026-11-03 00:03:48 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.221 |  |
| 2026-11-03 01:00:26 | Wellawaya (Kirindi Oya) | 2.46 | 🟢 Normal | -0.389 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)