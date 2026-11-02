# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_08:03:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,597 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 08:03:19 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:02:57 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.154 |  |
| 2026-11-02 08:02:30 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.040 |  |
| 2026-11-02 08:02:22 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:02:17 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 08:01:50 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-11-02 08:01:42 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.111 |  |
| 2026-11-02 08:01:34 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:01:11 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 08:01:09 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-11-02 08:00:46 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-02 08:00:22 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.111 |  |
| 2026-11-02 07:39:36 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.154 |  |
| 2026-11-02 07:32:38 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 07:05:45 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-02 08:01:11 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 07:04:26 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-02 07:03:05 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-02 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 08:02:17 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 07:16:06 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-02 07:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:01:34 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:03:23 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:07:47 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:04:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:09:50 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:03:19 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:02:22 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:06:26 | Thalgahagoda (Nilwala Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:05:56 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-02 07:06:22 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-11-02 07:01:50 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-11-02 07:06:32 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-02 07:07:02 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-11-02 08:00:46 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-02 07:01:09 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-02 07:00:51 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-11-02 07:02:47 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-11-02 07:03:54 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | -0.021 |  |
| 2026-11-02 07:00:49 | Rathnapura (Kalu Ganga) | 3.03 | 🟢 Normal | -0.022 |  |
| 2026-11-02 08:01:09 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-11-02 08:01:50 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-11-02 08:02:30 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.040 |  |
| 2026-11-02 07:01:58 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.049 |  |
| 2026-11-02 07:11:56 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.059 |  |
| 2026-11-02 07:07:12 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.086 |  |
| 2026-11-02 07:08:02 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.090 |  |
| 2026-11-02 08:01:42 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.111 |  |
| 2026-11-02 08:00:22 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.111 |  |
| 2026-11-02 07:07:43 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.118 |  |
| 2026-11-02 07:09:58 | Thawalama (Gin Ganga) | 2.72 | 🟢 Normal | -0.143 |  |
| 2026-11-02 08:02:57 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)