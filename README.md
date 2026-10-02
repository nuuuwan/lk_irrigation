# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_14:11:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,923 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 14:11:00 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-02 14:09:09 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.029 |  |
| 2026-10-02 14:08:35 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.018 |  |
| 2026-10-02 14:08:16 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.030 |  |
| 2026-10-02 14:06:30 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:06:16 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.014 |  |
| 2026-10-02 14:05:45 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.059 |  |
| 2026-10-02 14:05:27 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | -0.052 |  |
| 2026-10-02 14:04:38 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-10-02 14:04:15 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:04:04 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:03:54 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-02 14:03:45 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-02 14:03:43 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.031 |  |
| 2026-10-02 14:03:40 | Hanwella (Kelani Ganga) | 2.09 | 🟢 Normal | -0.030 |  |
| 2026-10-02 14:03:37 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.372 |  |
| 2026-10-02 14:03:36 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.098 |  |
| 2026-10-02 14:03:27 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.062 |  |
| 2026-10-02 14:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-02 14:03:15 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:03:14 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-10-02 14:03:08 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:03:08 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:02:56 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.044 |  |
| 2026-10-02 14:02:53 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-02 14:02:39 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:02:38 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-02 14:02:37 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.01 | 🟢 Normal | -0.010 |  |
| 2026-10-02 14:01:44 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:01:27 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:01:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-02 14:01:10 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.040 |  |
| 2026-10-02 14:01:03 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-02 14:00:44 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:00:31 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 14:02:53 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-02 14:01:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-02 14:02:38 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-02 14:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-02 14:11:00 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-02 14:03:08 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:01:44 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:04:15 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:02:37 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:03:15 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:04:04 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:02:39 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:01:27 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:06:30 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:03:08 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-02 14:00:44 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-02 13:31:08 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.008 |  |
| 2026-10-02 14:03:45 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-02 14:03:54 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-02 14:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.01 | 🟢 Normal | -0.010 |  |
| 2026-10-02 14:04:38 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-10-02 14:01:03 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-10-02 14:06:16 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.014 |  |
| 2026-10-02 14:08:35 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.018 |  |
| 2026-10-02 14:00:31 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.020 |  |
| 2026-10-02 14:09:09 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.029 |  |
| 2026-10-02 14:08:16 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.030 |  |
| 2026-10-02 14:03:40 | Hanwella (Kelani Ganga) | 2.09 | 🟢 Normal | -0.030 |  |
| 2026-10-02 14:03:14 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-10-02 14:03:43 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.031 |  |
| 2026-10-02 14:01:10 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.040 |  |
| 2026-10-02 14:02:56 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.044 |  |
| 2026-10-02 13:06:05 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.050 |  |
| 2026-10-02 14:05:27 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | -0.052 |  |
| 2026-10-02 14:05:45 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.059 |  |
| 2026-10-02 14:03:27 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.062 |  |
| 2026-10-02 14:03:36 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.098 |  |
| 2026-10-02 14:03:37 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.372 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)