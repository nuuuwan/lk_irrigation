# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_03:02:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,430 measurements** from **39** stations.
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
| 2026-09-02 03:02:39 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:02:00 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.030 |  |
| 2026-09-02 03:01:42 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-02 03:01:34 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 03:01:13 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:00:39 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-02 02:26:03 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-02 02:20:15 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.008 |  |
| 2026-09-02 02:18:31 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 00:20:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-09-02 01:02:06 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-02 03:00:39 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-02 03:01:42 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-02 02:03:53 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 03:01:34 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 02:12:10 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-02 02:12:35 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-02 01:02:52 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.005 |  |
| 2026-09-02 00:04:58 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-02 02:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:08:15 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-02 02:03:10 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-02 01:00:48 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-02 02:09:14 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-02 02:02:07 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 01:00:50 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 02:06:51 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:02:39 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:01:13 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 02:08:13 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-02 02:04:19 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-01 23:01:26 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:00:53 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:04:40 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-02 02:01:54 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-02 02:20:15 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.008 |  |
| 2026-09-02 02:05:02 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-09-02 02:04:04 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.010 |  |
| 2026-09-01 18:04:47 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-02 02:02:37 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-02 02:02:21 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-09-02 00:04:39 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-09-02 02:18:31 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.016 |  |
| 2026-09-02 00:17:06 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-09-02 02:02:43 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-09-02 03:02:00 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.030 |  |
| 2026-09-01 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.060 |  |
| 2026-09-02 02:01:22 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)