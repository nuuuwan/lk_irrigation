# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_04:04:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,374 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 04:04:45 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:04:19 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:03:58 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.005 |  |
| 2026-09-03 04:03:30 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:02:41 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:02:38 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-09-03 04:02:31 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:02:30 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:02:20 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:02:10 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-03 04:02:08 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:02:06 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.013 |  |
| 2026-09-03 04:01:55 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.029 |  |
| 2026-09-03 04:01:47 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:00:53 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-03 03:46:56 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.006 |  |
| 2026-09-03 03:23:29 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.017 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 03:16:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-09-03 01:44:03 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-03 04:00:53 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-03 04:02:10 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-03 03:23:29 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-03 03:02:30 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-03 04:03:30 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:02:08 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-03 03:00:45 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-03 03:12:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:02:30 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 18:04:32 | Galgamuwa (Mee Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-03 02:01:35 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:02:41 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 03:05:20 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-03 03:03:28 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-09-03 02:05:26 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-09-03 03:04:32 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 02:01:51 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:02:31 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:04:45 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:04:19 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-03 03:08:30 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-02 18:03:25 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 03:15:25 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:02:20 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-03 04:03:58 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | -0.005 |  |
| 2026-09-03 03:46:56 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.006 |  |
| 2026-09-03 03:17:15 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.008 |  |
| 2026-09-03 03:02:23 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-03 04:02:38 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-09-03 03:08:43 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-09-03 04:02:06 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.013 |  |
| 2026-09-03 04:01:55 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.029 |  |
| 2026-09-03 03:05:27 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.029 |  |
| 2026-09-02 18:00:38 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-09-03 03:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.064 |  |
| 2026-09-03 03:05:06 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)